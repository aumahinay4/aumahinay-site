"""Checks the Salary Loan Calculator's math (loan_math.py) against an independent reference version written
here, and every figure in the worked examples printed on the page. Run:  python tests/test_loan.py"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import loan_math as LM  # noqa: E402


class _LoanMath:
    """Lets the checks below call loan_math with the same names the page uses."""
    r2 = staticmethod(LM.r2)
    payment = staticmethod(lambda p, r, n, m: LM.payment(p, r, n, m))
    principal = staticmethod(lambda a, r, n, m: LM.principal(a, r, n, m))
    effectiveRate = staticmethod(LM.effective_rate)
    schedule = staticmethod(LM.schedule)
    compute = staticmethod(LM.compute)


def js(expr_list):
    """Evaluate each check expression against loan_math (they were first written for the JavaScript version)."""
    env = {"LoanMath": _LoanMath, "true": True, "false": False, "null": None}
    return [eval(e, env) for e in expr_list]


# ---- independent Python reference ----
def py_payment(p, r, n, method):
    if method == "addon":
        return p * (1 + r * n) / n
    return p / n if r == 0 else p * r / (1 - (1 + r) ** -n)


def py_pv(a, r, n):
    return a * n if r == 0 else a * (1 - (1 + r) ** -n) / r


def py_irr(cash, a, n):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if py_pv(a, mid, n) > cash else (lo, mid)
    return (lo + hi) / 2


def close(a, b, tol=0.005):
    return abs(a - b) <= tol


def base(**kw):
    d = dict(gross=30000, deductions=9000, floor=5000, freed=0, oldBalance=0, method="addon", rate=0.01, n=36,
             feePct=0, feeFixed=0, mode="max", amount=0, cap=0)
    d.update(kw)
    return d


FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)))
    if not ok:
        FAILS.append(name)


def main():
    # 1. payment and principal against Python, many combinations
    cases = [(p, r, n, m) for p in (5000, 100000, 423000) for r in (0, 0.005, 0.01, 0.0175, 0.03)
             for n in (1, 6, 12, 36, 60) for m in ("addon", "dim")]
    exprs = []
    for p, r, n, m in cases:
        exprs += ["LoanMath.payment(%r,%r,%r,'%s')" % (p, r, n, m), "LoanMath.principal(%r,%r,%r,'%s')" % (1000, r, n, m)]
    got = js(exprs)
    bad = 0
    for i, (p, r, n, m) in enumerate(cases):
        pay, prin = got[2 * i], got[2 * i + 1]
        if not close(pay, py_payment(p, r, n, m), 1e-6):
            bad += 1
        if not close(py_payment(prin, r, n, m), 1000, 1e-6):  # principal is the inverse of payment
            bad += 1
    check("payment/principal vs Python, %d cases" % len(cases), bad == 0, bad)

    # 2. effective rate: a diminishing loan with no fees has effective rate = its own rate; add-on 1%/36 = ~1.8%
    e1, e2, e3 = js(["LoanMath.effectiveRate(100000, LoanMath.payment(100000,0.01,36,'dim'), 36)",
                     "LoanMath.effectiveRate(100000, 100000*1.36/36, 36)",
                     "LoanMath.effectiveRate(97000, 8500, 24)"])
    check("EIR of 1%/month diminishing = 1%", close(e1, 0.01, 1e-9), e1)
    check("EIR add-on 1%/36 ~ 1.77%/month", close(e2, py_irr(100000, 100000 * 1.36 / 36, 36), 1e-9) and 0.0176 < e2 < 0.0178, e2)
    check("EIR with fees matches Python", close(e3, py_irr(97000, 8500, 24), 1e-9), e3)

    # 3. schedule: principal sums to the loan, balance ends at 0, diminishing interest sums to total interest
    s_dim, s_add = js(["LoanMath.schedule(100000,0.01,36,'dim')", "LoanMath.schedule(100000,0.01,36,'addon')"])
    check("dim schedule principal sums to loan", close(sum(r["principal"] for r in s_dim), 100000), sum(r["principal"] for r in s_dim))
    check("dim schedule ends at 0", s_dim[-1]["balance"] == 0, s_dim[-1])
    check("dim schedule total interest ~ 19,571.48", close(sum(r["interest"] for r in s_dim), 19571.48, 0.05),
          sum(r["interest"] for r in s_dim))
    check("add-on schedule interest = 36,000", close(sum(r["interest"] for r in s_add), 36000), sum(r["interest"] for r in s_add))
    check("add-on schedule principal sums to loan", close(sum(r["principal"] for r in s_add), 100000))
    check("add-on schedule ends at 0", s_add[-1]["balance"] == 0, s_add[-1])

    # 4. the page's explanation figures
    p_add, p_dim = js(["LoanMath.r2(LoanMath.payment(100000,0.01,36,'addon'))", "LoanMath.r2(LoanMath.payment(100000,0.01,36,'dim'))"])
    check("₱100,000 add-on 1%/36 = ₱3,777.78", p_add == 3777.78, p_add)
    check("₱100,000 diminishing 1%/36 = ₱3,321.43", p_dim == 3321.43, p_dim)
    check("diminishing interest = ₱19,571.48", close(p_dim * 36 - 100000, 19571.48), p_dim * 36 - 100000)

    # 5. worked examples
    ex1, ex2, ex3, ex3max = js([
        "LoanMath.compute(%s)" % json.dumps(base()),
        "LoanMath.compute(%s)" % json.dumps(base(method="dim")),
        "LoanMath.compute(%s)" % json.dumps(base(gross=28000, deductions=20000, freed=4000, oldBalance=50000,
                                                 rate=0.015, n=24, feePct=3, mode="check", amount=150000)),
        "LoanMath.compute(%s)" % json.dumps(base(gross=28000, deductions=20000, freed=4000, oldBalance=50000,
                                                 rate=0.015, n=24, feePct=3, mode="check", amount=123000)),
    ])
    check("ex1 net now 21,000 / room 16,000", ex1["netNow"] == 21000 and ex1["room"] == 16000, ex1)
    check("ex1 exact max 423,529.41", ex1["maxExact"] == 423529.41, ex1["maxExact"])
    check("ex1 max loan 423,000", ex1["maxLoan"] == 423000, ex1["maxLoan"])
    check("ex1 payment 15,980 and net after 5,020", ex1["pay"] == 15980 and ex1["netAfter"] == 5020, ex1)
    check("ex2 exact 481,720.08, max 481,000", ex2["maxExact"] == 481720.08 and ex2["maxLoan"] == 481000, ex2)
    check("ex2 payment 15,976.08", ex2["pay"] == 15976.08, ex2["pay"])
    check("ex3 room 7,000", ex3["room"] == 7000, ex3["room"])
    check("ex3 ₱150,000 pays 8,500, net after 3,500, short 1,500, not fit",
          ex3["pay"] == 8500 and ex3["netAfter"] == 3500 and ex3["short"] == 1500 and not ex3["fits"], ex3)
    check("ex3 max that fits 123,000", ex3["maxLoan"] == 123000, ex3["maxLoan"])
    check("ex3 ₱123,000 pays 6,970, fits", ex3max["pay"] == 6970 and ex3max["fits"], ex3max)
    check("ex3 ₱123,000 cash 69,310 (fees 3,690)", ex3max["cash"] == 69310 and ex3max["fees"] == 3690, ex3max)

    # 6. edge cases and the floor guarantee
    edge = js([
        "LoanMath.compute(%s)" % json.dumps(base(deductions=26000)),           # net 4,000: below floor
        "LoanMath.compute(%s)" % json.dumps(base(cap=200000)),                 # lender cap
        "LoanMath.compute(%s)" % json.dumps(base(rate=0, method="dim", n=10, gross=10000, deductions=0)),  # zero rate
        "LoanMath.compute(%s)" % json.dumps(base(gross=7000, deductions=1500, n=12)),  # small room -> ₱100 steps
    ])
    check("no room -> max 0", edge[0]["maxLoan"] == 0 and edge[0]["room"] == 0, edge[0])
    check("cap applied", edge[1]["maxLoan"] == 200000 and edge[1]["capped"], edge[1])
    check("zero rate: 5,000 x 10 = 50,000", edge[2]["maxLoan"] == 50000 and edge[2]["pay"] == 5000, edge[2])
    check("small room rounds to ₱100", edge[3]["maxLoan"] % 100 == 0 and edge[3]["maxLoan"] < 10000 and edge[3]["fits"], edge[3])

    # every rounded max loan keeps take-home pay at or above the floor, across many inputs
    grid = [base(gross=g, deductions=d, method=m, rate=r, n=n, feePct=3)
            for g in (12000, 18500, 25000, 40000, 73210) for d in (2000, 6500, 9999)
            for m in ("addon", "dim") for r in (0.005, 0.01, 0.0125, 0.02) for n in (6, 12, 24, 36, 48, 60)]
    res = js(["LoanMath.compute(%s)" % json.dumps(x) for x in grid])
    broke = [(x, o) for x, o in zip(grid, res) if o["maxLoan"] and (not o["fits"] or o["netAfter"] < 5000)]
    check("floor kept for every max loan (%d cases)" % len(grid), not broke, broke[:1])
    tight = [o for x, o in zip(grid, res) if o["maxLoan"] and o["room"] - o["pay"] > py_payment(
        1000 if o["maxExact"] >= 10000 else 100, x["rate"], x["n"], x["method"]) + 0.01]
    check("max loan is within one rounding step of the limit", not tight, tight[:1])

    # 7. what the page shows (loan_math.view), and the number formats
    check("peso format", LM.peso(1234567.005) == "₱1,234,567.01" and LM.peso(-5) == "−₱5.00" and LM.peso(0) == "₱0.00",
          (LM.peso(1234567.005), LM.peso(-5)))
    check("peso0 / pct formats", LM.peso0(423000) == "₱423,000" and LM.pct(0.0177) == "1.77%" and LM.pct(0.212, 1) == "21.2%"
          and LM.pct(0.01) == "1%", (LM.peso0(423000), LM.pct(0.0177)))
    v = LM.view(LM.DEFAULTS)
    check("default view: ₱423,000 and ₱5,020.00 after",
          v["text"]["out-big"] == "₱423,000" and v["text"]["d-netafter"] == "₱5,020.00" and not v["hidden"]["loan-details"], v["text"])
    check("default view: add-on vs diminishing line says 1.77%", "1.77% a month" in v["text"]["d-compare"], v["text"]["d-compare"])
    check("default view: 36 schedule rows", v["rows"].count("<tr>") == 36, v["rows"].count("<tr>"))
    f = dict(LM.DEFAULTS, gross=28000, deductions=20000, renew=True, oldPay=4000, oldBal=50000, rate=1.5, term=24,
             feePct=3, mode="check", amount=150000)
    v3 = LM.view(f)
    check("example 3 view: too big, short ₱1,500", v3["text"]["out-big"] == "₱8,500.00" and "₱1,500.00 below" in v3["text"]["out-note"]
          and "loan-bad" in v3["class"]["out-big"], v3["text"]["out-note"])
    vy = LM.view(dict(LM.DEFAULTS, method="dim", rate=12, rateUnit="year"))
    check("yearly rate 12% = 1% a month diminishing: ₱481,000", vy["text"]["out-big"] == "₱481,000", vy["text"]["out-big"])
    v0 = LM.view(dict(LM.DEFAULTS, gross=0))
    check("empty pay asks for pay", v0["text"]["out-label"].startswith("Type your monthly pay") and v0["hidden"]["loan-details"])

    # 8. loan_math.py must stay simple enough for MicroPython in the browser
    src = (Path(__file__).resolve().parent.parent / "loan_math.py").read_text(encoding="utf-8")
    imports = [ln.strip() for ln in src.splitlines() if ln.startswith(("import ", "from "))]
    check("loan_math imports only math", imports == ["import math"], imports)
    check("loan_math has no f-strings or format(',')", not re.search(r"(?<![\w\"'])f[\"']|\{[^}]*:,", src))

    # 9. the browser side: run the page's own Python (loan_math.py + LOAN_UI_PY) against a stand-in page
    check_browser_python()

    # 10. same answers as Butch's own Decimal code (his Google Doc "Philippine Loan Calculators", 2026-11-26)
    check_against_decimal()

    print("\n%d failed" % len(FAILS) if FAILS else "\nall passed")
    sys.exit(1 if FAILS else 0)


def check_browser_python():
    """Runs the exact Python the page hands to MicroPython, in CPython, with a small fake `js` module standing in
    for the browser page (example 3 typed in), and checks what it writes on the page."""
    import types
    from loan import LOAN_UI_PY
    src = (Path(__file__).resolve().parent.parent / "loan_math.py").read_text(encoding="utf-8") + "\n" + LOAN_UI_PY
    typed = {"gross": "28,000", "deductions": "20000", "floor": "5000", "old-pay": "4000", "old-bal": "50000",
             "rate": "1.5", "rate-unit": "month", "term": "24", "fee-pct": "3", "fee-fixed": "", "amount": "150000",
             "cap": "abc"}
    radios = {"who": "gov", "method": "addon", "mode": "check"}
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
            self.checked = i == "renew"
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

    from urllib.parse import quote
    doc = types.SimpleNamespace(getElementById=get, querySelector=query, createElement=lambda tag: El("new-a"),
                                body=types.SimpleNamespace(appendChild=lambda e: None))
    saved = sys.modules.get("js")
    sys.modules["js"] = types.SimpleNamespace(document=doc, encodeURIComponent=lambda x: quote(x, safe=""))
    try:
        exec(compile(src, "loan-py", "exec"), {"__name__": "loan_py"})
        ok1 = (els["out-big"].textContent == "₱8,500.00" and els["d-cash"].textContent == "₱95,500.00"
               and els["loan-status"].hidden and els["sched-body"].innerHTML.count("<tr>") == 24
               and len(handlers["loan"]) == 2 and not els["loan-reset"].hidden)
        check("page Python fills the page (example 3)", ok1, {k: els[k].textContent for k in ("out-big", "d-cash")})
        check("page Python: effective-rate pill", els["out-pill"].textContent.startswith("Effective rate ") and not els["out-pill"].hidden,
              els["out-pill"].textContent)
        check("page Python: Show all 24 months button", els["sched-toggle"].textContent == "Show all 24 months")
        handlers["sched-toggle"][0](None)
        check("page Python: Show all opens the table", not els["sched-wrap"].classList.contains("short")
              and els["sched-toggle"].textContent == "Show first 12 months", els["sched-toggle"].textContent)
        handlers["sched-csv"][0](None)
        name, href = clicked[-1]
        body = href.split(",", 1)[1]
        from urllib.parse import unquote
        lines = unquote(body).strip().split("\n")
        check("page Python: CSV export has header + 24 rows", name == "aumahinay-salary-loan-schedule.csv"
              and lines[0] == "Month,Payment,Interest,Principal,Balance" and len(lines) == 25
              and lines[-1].endswith(",0.00"), (name, lines[:2], lines[-1]))
        radios["who"] = "other"  # switching to private sets the floor to 0, then recomputes
        handlers["loan"][0](None)
        check("page Python: switching to private sets floor 0", els["floor"].value == "0" and not els["floor-other"].hidden
              and els["out-note"].textContent.startswith("This loan fits"), els["out-note"].textContent)
        handlers["loan-reset"][0](None)
        check("page Python: Reset brings back the sample (₱423,000)", els["out-big"].textContent == "₱423,000"
              and radios == {"who": "gov", "method": "addon", "mode": "max"} and els["floor"].value == "5000"
              and els["sched-wrap"].classList.contains("short") and not els["renew"].checked, els["out-big"].textContent)
    finally:
        if saved is None:
            sys.modules.pop("js", None)
        else:
            sys.modules["js"] = saved


def check_against_decimal():
    """Butch's spec asks for decimal.Decimal with ROUND_HALF_UP. MicroPython (the browser's Python) has no decimal
    module, so loan_math uses floats rounded half-up to centavos. This checks the two agree on thousands of loans:
    the monthly payment, and for diminishing loans every row of the schedule."""
    import random
    from decimal import ROUND_HALF_UP, Decimal as D

    def q(x):
        return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)

    def dec_dim(p, annual, n):  # from Butch's compute_diminishing_balance_loan
        r = annual / D(100) / D(12)
        if r == 0:
            m = q(p / D(n))
        else:
            f = (1 + r) ** n
            m = q(p * (r * f) / (f - 1))
        bal, rows = p, []
        for k in range(1, n + 1):
            # bal * annual / 1200 instead of bal * r: r = annual/1200 is cut to 28 digits, which turns an exact
            # half-centavo (e.g. 9,697.675) into 9,697.67499... and rounds it the wrong way (14 rows in 277,023)
            i = q(bal * annual / D(1200))
            if k == n:
                pr = bal
                pay = q(pr + i)
            else:
                pay = m
                pr = q(pay - i)
            bal = q(bal - pr)
            rows.append((pay, i, pr, max(D("0.00"), bal)))
        return m, rows

    def dec_addon(p, monthly_pct, n):  # from Butch's compute_addon_rate_loan
        ti = q(p * (monthly_pct / D(100)) * D(n))
        return q((p + ti) / D(n)), ti

    rnd = random.Random(2026)
    bad_dim = bad_add = rows_checked = 0
    for _ in range(3000):
        p = rnd.randrange(5000, 5000000, 100)
        n = rnd.choice([6, 12, 18, 24, 36, 48, 60, 120, 240, 360])
        annual = D(rnd.choice(["0", "5.75", "6.25", "6.5", "8", "10", "12", "18", "24"]))
        m, rows = dec_dim(D(p), annual, n)
        ours = LM.schedule(p, float(annual) / 1200, n, "dim")
        if D("%.2f" % LM.r2(LM.payment(p, float(annual) / 1200, n, "dim"))) != m:
            bad_dim += 1
        for (pay, i, pr, b), r in zip(rows, ours):
            rows_checked += 1
            if (D("%.2f" % r["payment"]), D("%.2f" % r["interest"]), D("%.2f" % r["principal"]), D("%.2f" % r["balance"])) != (pay, i, pr, b):
                bad_dim += 1
                break
        mp = D(rnd.choice(["0.5", "0.75", "1", "1.25", "1.5", "2"]))
        am, ti = dec_addon(D(p), mp, n)
        if D("%.2f" % LM.r2(LM.payment(p, float(mp) / 100, n, "addon"))) != am:
            bad_add += 1
    check("diminishing: payment + every schedule row match Butch's Decimal code (3,000 loans, %d rows)" % rows_checked,
          bad_dim == 0, bad_dim)
    check("add-on: monthly payment matches Butch's Decimal code (3,000 loans)", bad_add == 0, bad_add)
    # his three sample loans
    check("Butch's samples: ₱4,614.49 / ₱14,618.56 / ₱18,700.00",
          LM.r2(LM.payment(100000, 0.10 / 12, 24, "dim")) == 4614.49
          and LM.r2(LM.payment(2000000, 0.0625 / 12, 240, "dim")) == 14618.56
          and LM.r2(LM.payment(880000, 0.055 / 12, 60, "addon")) == 18700.0)


if __name__ == "__main__":
    main()
