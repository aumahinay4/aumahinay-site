"""Checks the Housing Loan Calculator's math (housing_math.py) against an independent version written here, every
figure printed in the page's worked examples, and the Python the browser runs. Run:  python tests/test_housing.py"""

import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import housing_math as H  # noqa: E402

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)))
    if not ok:
        FAILS.append(name)


def ref_payment(p, yearly, n):
    """Standard amortization formula, written separately from loan_math."""
    i = yearly / 100 / 12
    return p / n if i == 0 else p * i * (1 + i) ** n / ((1 + i) ** n - 1)


def ref_balance(p, yearly, n, k):
    """Balance left after k payments (closed form, no rounding)."""
    i = yearly / 100 / 12
    a = ref_payment(p, yearly, n)
    return p * (1 + i) ** k - a * ((1 + i) ** k - 1) / i


def f(**kw):
    d = dict(H.DEFAULTS)
    d.update(kw)
    return d


def main():
    # 1. payment vs a separate formula, and a textbook figure (P1,000,000 at 6% for 30 years = P5,995.51)
    bad = 0
    for p in (500000, 2250000, 9999999):
        for rate in (3, 5.75, 6.25, 7, 9.75):
            for yrs in (5, 10, 20, 25, 30):
                o = H.compute(f(price=p * 2, down=p, ltv=100, cap=0, rate=rate, years=yrs, fixYears=30))
                if abs(o["pi"] - ref_payment(p, rate, yrs * 12)) > 0.006:
                    bad += 1
    check("monthly amortization vs separate formula (75 cases)", bad == 0, bad)
    o = H.compute(f(price=1000000, down=0, ltv=100, cap=0, rate=6, years=30))
    check("P1,000,000 at 6% for 30 years = P5,995.51", o["pi"] == 5995.51, o["pi"])

    # 2. schedules: principal adds up to the loan and ends at zero, with and without repricing
    bad = []
    for rate, after, fix, yrs in ((6.25, 0, 3, 30), (6.25, 8, 3, 30), (5.75, 9.5, 1, 15), (7, 4, 5, 20), (0, 0, 3, 10),
                                  (8, 12, 10, 25)):
        o = H.compute(f(rate=rate, rateAfter=after, fixYears=fix, years=yrs))
        rows = o["rows"]
        prin = round(sum(r["principal"] for r in rows), 2)
        if prin != o["loan"] or rows[-1]["balance"] != 0 or len(rows) != yrs * 12 \
                or abs(rows[-1]["payment"] - rows[-2]["payment"]) > 10:
            bad.append((rate, after, fix, yrs, prin, rows[-1]))
        yr = H.by_year(rows)
        if len(yr) != yrs or abs(sum(y["payment"] for y in yr) - o["totalPI"]) > 0.05:
            bad.append(("yearly", rate, after))
    check("schedules add up, end at 0, last payment within P10 of the others, yearly totals match", not bad, bad[:2])

    # 3. repricing: balance after the fixing period and the new payment match the closed form
    o = H.compute(f(rateAfter=8))
    b = ref_balance(2250000, 6.25, 360, 36)
    check("balance after 3 years ~ P2,165,706.98", abs(o["rows"][35]["balance"] - b) < 0.5 and o["rows"][35]["balance"] == 2165706.98,
          (o["rows"][35]["balance"], b))
    check("new payment at 8% for 324 months = P16,335.49",
          o["piAfter"] == 16335.49 and abs(ref_payment(o["rows"][35]["balance"], 8, 324) - 16335.49) < 0.006, o["piAfter"])

    # 4. worked example 1 (the page's default figures)
    o = H.compute(H.DEFAULTS)
    check("ex1 loan 2,250,000 (90%)", o["loan"] == 2250000 and o["gap"] == 0, o["loan"])
    check("ex1 amortization 13,853.64", o["pi"] == 13853.64 and o["monthly"] == 13853.64, o["pi"])
    check("ex1 income needed 39,582 and 27.7% of 50,000",
          o["incomeNeeded"] == 39582 and round(o["share"] * 100, 1) == 27.7 and o["fits"], o["incomeNeeded"])
    check("ex1 total interest 2,737,307.14", o["interest"] == 2737307.14, o["interest"])
    # worked example 2
    o2 = H.compute(f(rateAfter=8))
    check("ex2 +2,481.85 and income needed 46,673",
          round(o2["piAfter"] - o2["pi"], 2) == 2481.85 and o2["incomeNeededAfter"] == 46673, (o2["piAfter"], o2["incomeNeededAfter"]))
    # worked example 3
    o3 = H.compute(f(lender="bank", ltv=80, cap=0, price=3000000, down=600000, rate=7, fixYears=5, years=20,
                     income=60000, mriYear=6000, fireYear=3000))
    check("ex3 loan 2,400,000, P&I 18,607.17, insurance 750, monthly 19,357.17",
          o3["loan"] == 2400000 and o3["pi"] == 18607.17 and o3["ins"] == 750 and o3["monthly"] == 19357.17, o3["monthly"])
    check("ex3 income needed 55,307, interest 2,065,723.39",
          o3["incomeNeeded"] == 55307 and o3["interest"] == 2065723.39 and o3["fits"], (o3["incomeNeeded"], o3["interest"]))
    check("step 4 of How it works: 14,000 / 35% = 40,000", H.round_up(14000 / 0.35) == 40000)

    # 5. limits: down payment too small, peso cap, what the income can carry
    o = H.compute(f(down=100000))
    check("down too small: loan held at 90%, gap 150,000, min down 250,000",
          o["loan"] == 2250000 and o["gap"] == 150000 and o["minDown"] == 250000 and o["limitBy"] == "ltv", o)
    o = H.compute(f(price=14000000, down=1400000))
    check("P10M cap: loan 10,000,000, min down 4,000,000",
          o["loan"] == 10000000 and o["minDown"] == 4000000 and o["limitBy"] == "cap", (o["loan"], o["minDown"]))
    bad = []
    for inc in (15000, 32000, 50000, 87500, 150000):
        for rate in (3, 6.25, 9):
            for yrs in (10, 20, 30):
                for ins in (0, 9000):
                    o = H.compute(f(income=inc, rate=rate, years=yrs, mriYear=ins, cap=0, down=10 ** 7, price=2 * 10 ** 7,
                                    ltv=100))
                    m = o["maxByIncome"]
                    pay = round(ref_payment(m, rate, yrs * 12), 2) + o["ins"]
                    nxt = round(ref_payment(m + 1000, rate, yrs * 12), 2) + o["ins"]
                    if m and (pay > inc * 0.35 + 0.005 or nxt <= inc * 0.35):
                        bad.append((inc, rate, yrs, ins, m))
    check("biggest loan for an income fits 35%% and is within P1,000 of the limit (90 cases)", not bad, bad[:2])
    o = H.compute(H.DEFAULTS)
    check("defaults: income carries 2,842,000; down payment limits the house to 2,500,000",
          o["maxLoan"] == 2842000 and o["maxPrice"] == 2500000 and o["downLimits"], (o["maxLoan"], o["maxPrice"]))

    # 6. what the page shows
    v = H.view(H.DEFAULTS)
    check("default view: big figure and label", v["text"]["h-big"] == "₱13,853.64"
          and v["text"]["h-label"] == "Monthly amortization for the first 3 years", v["text"]["h-label"])
    check("default view: 30 yearly rows, fixing-period note shown",
          v["rows"].count("<tr>") == 30 and not v["hidden"]["d-reprice"] and "fixed for 3 years" in v["text"]["d-reprice"])
    vb = H.view(f(income=30000))
    check("too little income is flagged", "loan-bad" in vb["class"]["h-big"] and "₱39,582" in vb["text"]["h-note"], vb["text"]["h-note"])
    vg = H.view(f(down=100000))
    check("gap message", not vg["hidden"]["h-gap"] and "₱250,000" in vg["text"]["h-gap"] and "₱150,000" in vg["text"]["h-gap"],
          vg["text"]["h-gap"])
    v0 = H.view(f(price=0))
    check("empty price asks for the price", v0["text"]["h-label"].startswith("Type the price") and v0["hidden"]["h-details"])
    vn = H.view(f(down=3000000))
    check("down payment covers all", vn["text"]["h-label"] == "No loan needed" and vn["hidden"]["h-details"])

    # 7. housing_math.py stays MicroPython-friendly
    src = (ROOT / "housing_math.py").read_text(encoding="utf-8")
    imports = [ln.strip() for ln in src.splitlines() if ln.lstrip().startswith(("import ", "from "))]
    check("housing_math imports only math (and loan_math)",
          imports == ["import math", "from loan_math import r2, payment, principal, round_down, peso, peso0, pct"], imports)
    check("housing_math has no f-strings or format(',')", not re.search(r"(?<![\w\"'])f[\"']|\{[^}]*:,", src))

    # 8. the browser side, joined exactly as the page joins it, with a stand-in `js` page
    check_browser_python()

    print("\n%d failed" % len(FAILS) if FAILS else "\nall passed")
    sys.exit(1 if FAILS else 0)


def check_browser_python():
    from housing import page_python
    src = page_python()
    typed = {"price": "3,000,000", "down": "600000", "ltv": "80", "cap": "", "rate": "7", "fix": "5", "rate-after": "",
             "years": "20", "mri": "6000", "fire": "3000", "income": "60000", "ratio": "35"}
    radios = {"lender": "bank"}
    els, handlers = {}, []

    class El:
        def __init__(self, i):
            self.value, self.hidden, self.textContent, self.className, self.innerHTML = typed.get(i, ""), False, "", "", ""

        def addEventListener(self, kind, fn):
            handlers.append(fn)

    def get(i):
        return els.setdefault(i, El(i))

    def query(q):
        return types.SimpleNamespace(value=radios[re.search(r'name="(\w+)"', q).group(1)])

    saved_js, saved_lm = sys.modules.get("js"), sys.modules.pop("loan_math", None)
    sys.modules["js"] = types.SimpleNamespace(document=types.SimpleNamespace(getElementById=get, querySelector=query))
    # In the browser there is no loan_math module to import: block it, so the joined script must stand on its own
    sys.modules["loan_math"] = None
    try:
        exec(compile(src, "housing-py", "exec"), {"__name__": "housing_py"})
        ok = (els["h-big"].textContent == "₱19,357.17" and els["d-income"].textContent == "₱55,307 a month"
              and els["h-status"].hidden and els["h-sched-body"].innerHTML.count("<tr>") == 20 and len(handlers) == 2)
        check("page Python fills the page (example 3, typed with a comma)", ok,
              {k: els[k].textContent for k in ("h-big", "d-income")})
        radios["lender"] = "pagibig"  # switching lender fills in Pag-IBIG's limits, then recomputes
        handlers[0](None)
        check("page Python: switching to Pag-IBIG sets 90% and P10M", els["ltv"].value == "90" and els["cap"].value == "10000000"
              and els["h-bank-note"].hidden and not els["h-pagibig-note"].hidden, (els["ltv"].value, els["cap"].value))
    finally:
        sys.modules.pop("loan_math", None)
        if saved_lm is not None:
            sys.modules["loan_math"] = saved_lm
        if saved_js is None:
            sys.modules.pop("js", None)
        else:
            sys.modules["js"] = saved_js


if __name__ == "__main__":
    main()
