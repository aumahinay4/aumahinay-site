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
        if abs(sum(r["payment"] for r in rows) - o["totalPI"]) > 0.05:
            bad.append(("total", rate, after))
    check("schedules add up, end at 0, last payment within P10 of the others, totals match", not bad, bad[:2])

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
    check("default view: 360 month rows, fixing-period note shown",
          v["rows"].count("<tr>") == 360 and not v["hidden"]["d-reprice"] and "fixed for 3 years" in v["text"]["d-reprice"])
    check("default view: Show all 360 months button, CSV of 361 lines",
          v["text"]["sched-toggle"] == "Show all 360 months" and not v["hidden"]["sched-toggle"]
          and v["csv"].count("\n") == 361 and v["csv"].startswith("Month,Payment,Interest,Principal,Balance\n1,13853.64,11718.75,"),
          v["csv"][:80])
    check("effective-rate pill: 6.25% with no insurance (same as the rate)",
          v["text"]["out-pill"] == "Effective rate 6.25% a year" and not v["hidden"]["out-pill"], v["text"]["out-pill"])
    vi = H.view(f(mriYear=6000, fireYear=3000))
    check("effective-rate pill counts insurance: 6.76%", vi["text"]["out-pill"] == "Effective rate 6.76% a year",
          vi["text"]["out-pill"])
    e = H.true_rate(2250000, [13853.64] * 359 + [H.compute(H.DEFAULTS)["rows"][-1]["payment"]])
    check("true_rate of the plain loan = 6.25%/12", abs(e * 12 - 0.0625) < 2e-6, e * 12)
    vs = H.view(f(years=1))
    check("1-year loan: no Show all button", vs["hidden"]["sched-toggle"] and vs["rows"].count("<tr>") == 12)
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
          imports == ["import math", "from loan_math import r2, payment, principal, round_down, peso, peso0, pct, schedule_csv"], imports)
    check("housing_math has no f-strings or format(',')", not re.search(r"(?<![\w\"'])f[\"']|\{[^}]*:,", src))

    # 8b. every schedule row against a decimal.Decimal version (ROUND_HALF_UP), with and without repricing
    check_against_decimal()

    # 8. the browser side, joined exactly as the page joins it, with a stand-in `js` page
    check_browser_python()

    print("\n%d failed" % len(FAILS) if FAILS else "\nall passed")
    sys.exit(1 if FAILS else 0)


def check_browser_python():
    """Runs the exact Python the page hands to MicroPython (loan_math + housing_math + HOUSING_UI_PY, joined), in
    CPython, with a small fake `js` module standing in for the page (example 3 typed in), and checks what it writes."""
    from urllib.parse import quote, unquote
    from housing import page_python
    src = page_python()
    typed = {"price": "3,000,000", "down": "600000", "ltv": "80", "cap": "", "rate": "7", "fix": "5", "rate-after": "",
             "years": "20", "mri": "6000", "fire": "3000", "income": "60000", "ratio": "35"}
    radios = {"lender": "bank"}
    els, handlers, clicked = {}, {}, []

    class ClassList:
        def __init__(self, names):
            self.names = set(names)

        def contains(self, c):
            return c in self.names

        def toggle(self, c):
            self.names ^= {c}

        def add(self, c):
            self.names.add(c)

    class El:
        def __init__(self, i):
            self.id = i
            self.value, self.hidden, self.textContent, self.className, self.innerHTML = typed.get(i, ""), False, "", "", ""
            self.classList = ClassList(["short"] if i == "sched-wrap" else [])
            self.href = self.download = ""

        def addEventListener(self, kind, fn):
            handlers.setdefault(self.id, []).append(fn)

        def click(self):
            clicked.append((self.download, self.href))

        def remove(self):
            pass

    def get(i):
        return els.setdefault(i, El(i))

    class Radio:
        def __init__(self, name, value=None):
            self.name, self.v = name, value

        @property
        def value(self):
            return radios[self.name]

        @property
        def checked(self):
            return radios[self.name] == self.v

        @checked.setter
        def checked(self, on):
            if on:
                radios[self.name] = self.v

    def query(q):
        m = re.search(r'name="(\w+)"(?:\]\[value="(\w+)")?', q)
        return Radio(m.group(1), m.group(2))

    doc = types.SimpleNamespace(getElementById=get, querySelector=query, createElement=lambda tag: El("new-a"),
                                body=types.SimpleNamespace(appendChild=lambda e: None))
    saved_js, saved_lm = sys.modules.get("js"), sys.modules.pop("loan_math", None)
    sys.modules["js"] = types.SimpleNamespace(document=doc, encodeURIComponent=lambda x: quote(x, safe=""))
    # In the browser there is no loan_math module to import: block it, so the joined script must stand on its own
    sys.modules["loan_math"] = None
    try:
        exec(compile(src, "housing-py", "exec"), {"__name__": "housing_py"})
        ok = (els["h-big"].textContent == "₱19,357.17" and els["d-income"].textContent == "₱55,307 a month"
              and els["h-status"].hidden and els["h-sched-body"].innerHTML.count("<tr>") == 240
              and len(handlers["housing"]) == 2 and not els["h-reset"].hidden and not els["sched-csv"].hidden)
        check("page Python fills the page (example 3, typed with a comma)", ok,
              {k: els[k].textContent for k in ("h-big", "d-income")})
        check("page Python: effective-rate pill counts insurance",
              els["out-pill"].textContent == "Effective rate 7.52% a year" and not els["out-pill"].hidden, els["out-pill"].textContent)
        check("page Python: Show all 240 months button", els["sched-toggle"].textContent == "Show all 240 months")
        handlers["sched-toggle"][0](None)
        check("page Python: Show all opens the table", not els["sched-wrap"].classList.contains("short")
              and els["sched-toggle"].textContent == "Show first 12 months", els["sched-toggle"].textContent)
        handlers["sched-csv"][0](None)
        name, href = clicked[-1]
        lines = unquote(href.split(",", 1)[1]).strip().split("\n")
        check("page Python: CSV export has header + 240 rows", name == "aumahinay-housing-loan-schedule.csv"
              and lines[0] == "Month,Payment,Interest,Principal,Balance" and len(lines) == 241
              and lines[1].startswith("1,18607.17,14000.00,") and lines[-1].endswith(",0.00"), (name, lines[:2], lines[-1]))
        radios["lender"] = "pagibig"  # switching lender fills in Pag-IBIG's limits, then recomputes
        handlers["housing"][0](None)
        check("page Python: switching to Pag-IBIG sets 90% and P10M", els["ltv"].value == "90" and els["cap"].value == "10000000"
              and els["h-bank-note"].hidden and not els["h-pagibig-note"].hidden, (els["ltv"].value, els["cap"].value))
        handlers["h-reset"][0](None)
        check("page Python: Reset brings back the sample (P13,853.64)", els["h-big"].textContent == "₱13,853.64"
              and radios == {"lender": "pagibig"} and els["price"].value == "2500000" and els["mri"].value == ""
              and els["fix"].value == "3" and els["sched-wrap"].classList.contains("short")
              and els["sched-toggle"].textContent == "Show all 360 months", els["h-big"].textContent)
    finally:
        sys.modules.pop("loan_math", None)
        if saved_lm is not None:
            sys.modules["loan_math"] = saved_lm
        if saved_js is None:
            sys.modules.pop("js", None)
        else:
            sys.modules["js"] = saved_js


def check_against_decimal():
    """MicroPython has no decimal module, so housing_math uses floats rounded half-up to centavos. This rebuilds the
    schedule with decimal.Decimal and ROUND_HALF_UP (repricing included) and compares every row."""
    import random
    from decimal import ROUND_HALF_UP, Decimal as D

    def q(x):
        return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)

    def pay(p, annual, n):
        if annual == 0:
            return q(p / D(n))
        r = annual / D(1200)
        f = (1 + r) ** n
        return q(p * r * f / (f - 1))

    def dec_rows(p, a1, a2, k, n):
        bal, rows = p, []
        m, annual = pay(p, a1, n), a1
        for i in range(1, n + 1):
            if i == k + 1 and 0 < k < n and a2 != a1:
                annual = a2
                m = pay(bal, a2, n - k)
            interest = q(bal * annual / D(1200))
            pr, amt = q(m - interest), m
            if i == n or pr > bal:
                pr = bal
                amt = q(pr + interest)
            bal = q(bal - pr)
            rows.append((amt, interest, pr, max(bal, D("0.00"))))
            if bal <= 0:
                break
        return rows

    rnd = random.Random(304)
    bad, count = 0, 0
    for _ in range(600):
        p = rnd.randrange(300000, 10000000, 1000)
        yrs = rnd.choice([5, 10, 15, 20, 25, 30])
        a1 = D(rnd.choice(["3", "5.75", "6.25", "6.5", "7", "7.125", "8.5", "9.75"]))
        a2 = D(rnd.choice(["0", "6", "8", "9.5", "11"]))
        fix = rnd.choice(H.FIX_CHOICES)
        o = H.compute(f(price=p, down=0, ltv=100, cap=0, rate=float(a1), rateAfter=float(a2), fixYears=fix, years=yrs))
        want = dec_rows(D(p), a1, a2 if a2 > 0 else a1, fix * 12, yrs * 12)
        if len(want) != len(o["rows"]):
            bad += 1
            continue
        for w, r in zip(want, o["rows"]):
            count += 1
            if tuple(D("%.2f" % r[k]) for k in ("payment", "interest", "principal", "balance")) != w:
                bad += 1
                break
    check("every schedule row matches a Decimal ROUND_HALF_UP version (600 loans, %d rows)" % count, bad == 0, bad)


if __name__ == "__main__":
    main()
