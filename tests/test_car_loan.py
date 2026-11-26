"""Checks the Car Loan Calculator's math (car_math.py) and every figure in the worked examples on the page.
Run:  python tests/test_car_loan.py"""

import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import car_math as C  # noqa: E402

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)))
    if not ok:
        FAILS.append(name)


def close(a, b, tol=0.005):
    return abs(a - b) <= tol


def py_pv(a, r, n):
    return a * n if r == 0 else a * (1 - (1 + r) ** -n) / r


def view(**kw):
    return C.car_view(dict(C.CAR_DEFAULTS, **kw))


def main():
    # 1. rate units: per year, per month and for the whole term give the same add-on loan
    a, b, c = view(), view(rate=0.5, rateUnit="month"), view(rate=30, rateUnit="term")
    check("6%/year = 0.5%/month = 30%/60 months", a["o"]["pay"] == b["o"]["pay"] == c["o"]["pay"] == 20800,
          (a["o"]["pay"], b["o"]["pay"], c["o"]["pay"]))

    # 2. example 1
    o = a["o"]
    check("ex1 down payment 240,000, loan 960,000", o["dp"] == 240000 and o["loan"] == 960000, o)
    check("ex1 interest 288,000, total 1,248,000", o["interest"] == 288000 and o["totalPaid"] == 1248000, o)
    check("ex1 cash on release day 300,800", o["cashDay"] == 300800, o["cashDay"])
    check("ex1 total cost 1,528,000", o["totalCost"] == 1528000, o["totalCost"])
    check("ex1 income needed 69,333.33", o["incomeNeeded"] == 69333.33, o["incomeNeeded"])
    check("ex1 page shows ₱20,800.00 and ₱300,800", a["text"]["out-big"] == "₱20,800.00" and "₱300,800" in a["text"]["out-note"],
          a["text"])
    check("ex1 add-on 6%/yr ~ 10.8%/yr diminishing", "10.8% a year" in a["text"]["d-compare"], a["text"]["d-compare"])

    # 3. example 2: 36 months
    o2 = view(term=36)["o"]
    check("ex2 payment 31,466.67", o2["pay"] == 31466.67, o2["pay"])
    check("ex2 saves about 115,200 interest", close(o["interest"] - o2["interest"], 115200, 0.5), o["interest"] - o2["interest"])
    check("ex2 payment 10,666.67 higher", close(o2["pay"] - o["pay"], 10666.67), o2["pay"] - o["pay"])

    # 4. example 3: income 60,000, other loans 5,000, 30%
    v3 = view(income=60000, otherDebts=5000)
    o3 = v3["o"]
    check("ex3 room 13,000, max loan 600,000, max price 750,000",
          o3["room"] == 13000 and o3["maxLoan"] == 600000 and o3["maxPrice"] == 750000, o3)
    check("ex3 says too big and ₱750,000", "too big" in v3["text"]["i-note"] and "₱750,000" in v3["text"]["i-note"]
          and "loan-bad" in v3["class"]["i-note"], v3["text"]["i-note"])
    check("income 80,000 fits", view(income=80000)["o"]["fits"])

    # 5. a published bank example (20% down on ₱1,489,000; 29.13% add-on for 60 months; ₱25,637 a month,
    #    rounded up by the bank; 9.92% for 24 months: ₱54,557)
    p60 = view(price=1489000, rate=29.13, rateUnit="term", term=60)["o"]["pay"]
    p24 = view(price=1489000, rate=9.92, rateUnit="term", term=24)["o"]["pay"]
    check("matches a bank's published 60-month example (25,637)", 25636 < p60 <= 25637, p60)
    check("matches a bank's published 24-month example (54,557)", close(p24, 54557, 1), p24)

    # 6. down payment in pesos, insurance in the loan, no advance, other fees
    v = view(dpMode="peso", dpAmt=300000, insFinanced=True, advance=False, otherFees=2500)
    o = v["o"]
    check("peso down payment: loan = 900,000 + 30,000 insurance", o["loan"] == 930000, o["loan"])
    check("insurance in loan: cash day = 300,000 + 10,000 + 2,500", o["cashDay"] == 312500, o["cashDay"])
    check("insurance row shown, cash insurance row hidden", not v["hidden"]["d-ins-row"] and v["hidden"]["c-ins-row"])
    check("total cost = down + payments + fees", o["totalCost"] == C.r2(300000 + o["totalPaid"] + 12500), o["totalCost"])

    # 7. effective rate: fees and the advance payment both raise it; a diminishing loan with no fees = its rate
    def eir(**kw):
        return view(**kw)["o"]["eirMonth"]
    e_plain = eir(mortgageFee=0, otherFees=0, advance=False)
    check("EIR no fees no advance = same as diminishing equivalent", close(e_plain, view()["o"]["sameAsDim"], 1e-9))
    check("EIR rises with fees", eir(advance=False) > e_plain)
    check("EIR rises with advance payment", eir() > eir(advance=False))
    ed = eir(method="dim", rate=10, mortgageFee=0, advance=False)
    check("diminishing 10%/yr no fees: EIR = 10%/12 (to payment rounding)", close(ed, 0.1 / 12, 1e-7), ed)
    # advance: n-1 payments are worth the loan minus fees minus the first payment
    o = view()["o"]
    check("EIR with advance solves its equation",
          close(py_pv(o["pay"], o["eirMonth"], 59), o["loan"] - o["fees"] - o["pay"], 0.01))

    # 8. max price never gives a payment above the room, across many inputs
    bad = []
    for inc in (25000, 48000, 75000, 133333):
        for debts in (0, 3500, 12000):
            for m in ("addon", "dim"):
                for r in (4, 6.5, 10):
                    for n in (24, 36, 60):
                        for dp in (10, 20, 35):
                            for fin in (False, True):
                                vv = view(income=inc, otherDebts=debts, method=m, rate=r, term=n, dpPct=dp, insFinanced=fin)
                                oo = vv["o"]
                                if oo["maxPrice"]:
                                    w = view(price=oo["maxPrice"], income=inc, otherDebts=debts, method=m, rate=r,
                                             term=n, dpPct=dp, insFinanced=fin)["o"]
                                    if not w["fits"]:
                                        bad.append((inc, debts, m, r, n, dp, fin, oo["maxPrice"], w["pay"], oo["room"]))
    check("the suggested car price always fits the income (1,296 cases)", not bad, bad[:2])

    # 9. empty and edge inputs
    check("no price asks for price", view(price=0)["text"]["out-label"].startswith("Type the price") and view(price=0)["hidden"]["car-details"])
    check("100% down = no loan", view(dpPct=100)["text"]["out-label"] == "No loan needed")
    check("no term asks for months", view(term=0)["text"]["out-label"].startswith("Type the number"))
    check("diminishing + whole term shows a warning", not view(method="dim", rateUnit="term")["hidden"]["term-dim-note"])
    check("60 schedule rows", view()["rows"].count("<tr>") == 60)
    dv = view()
    check("view: pill, Show all 60 months, CSV with 60 rows", dv["text"]["out-pill"] == "Effective rate 11.7% a year"
          and not dv["hidden"]["out-pill"] and dv["text"]["sched-toggle"] == "Show all 60 months"
          and not dv["hidden"]["sched-toggle"] and dv["csv"].count("\n") == 61, (dv["text"]["out-pill"], dv["csv"][:60]))
    check("view: 12 months hides Show all; no loan hides the pill and CSV",
          view(term=12)["hidden"]["sched-toggle"] and view(dpPct=100)["hidden"]["out-pill"] and view(dpPct=100)["csv"] == "")
    s = C.schedule(960000, 0.005, 60, "addon")
    check("schedule ends at 0, principal sums to loan", s[-1]["balance"] == 0 and close(sum(x["principal"] for x in s), 960000))

    # 10. MicroPython-friendly source
    src = (ROOT / "car_math.py").read_text(encoding="utf-8")
    top = [ln for ln in src.splitlines() if ln.startswith(("import ", "from "))]
    check("car_math has no top-level imports (loan_math comes first in the browser)", not top, top)
    check("car_math has no f-strings or format(',')", not re.search(r"(?<![\w\"'])f[\"']|\{[^}]*:,", src))

    # 11. the browser's Python, run with a stand-in page
    check_browser_python()

    print("\n%d failed" % len(FAILS) if FAILS else "\nall passed")
    sys.exit(1 if FAILS else 0)


def check_browser_python():
    """Runs the exact Python the page hands to MicroPython (loan_math + car_math + CAR_UI_PY), in CPython, with a
    small fake `js` module standing in for the page, and checks what it writes and what the buttons do."""
    from urllib.parse import quote, unquote
    from car import page_python
    src = page_python()
    typed = {"price": "1,200,000", "dp-pct": "20", "dp-amt": "", "rate": "6", "rate-unit": "year", "term": "60",
             "mortgage-fee": "10000", "insurance": "30000", "other-fees": "", "income": "60000", "other-debts": "5000",
             "share": "30"}
    radios = {"dpmode": "pct", "method": "addon"}
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
            self.checked = i == "advance"
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
    sys.modules["loan_math"] = None  # as in the browser: there is no loan_math module, only the code above
    try:
        exec(compile(src, "car-py", "exec"), {"__name__": "car_py"})
        ok = (els["out-big"].textContent == "₱20,800.00" and els["c-total"].textContent == "₱300,800.00"
              and "₱750,000" in els["i-note"].textContent and els["car-status"].hidden
              and els["sched-body"].innerHTML.count("<tr>") == 60 and len(handlers["car"]) == 2
              and not els["car-reset"].hidden and not els["sched-csv"].hidden)
        check("page Python fills the page", ok, {k: els[k].textContent for k in ("out-big", "c-total", "i-note")})
        check("page Python: effective-rate pill 11.7% a year", els["out-pill"].textContent == "Effective rate 11.7% a year"
              and not els["out-pill"].hidden, els["out-pill"].textContent)
        check("page Python: Show all 60 months button", els["sched-toggle"].textContent == "Show all 60 months"
              and not els["sched-toggle"].hidden, els["sched-toggle"].textContent)
        handlers["sched-toggle"][0](None)
        check("page Python: Show all opens the table", not els["sched-wrap"].classList.contains("short")
              and els["sched-toggle"].textContent == "Show first 12 months", els["sched-toggle"].textContent)
        handlers["sched-toggle"][0](None)
        check("page Python: Show first 12 closes it", els["sched-wrap"].classList.contains("short")
              and els["sched-toggle"].textContent == "Show all 60 months", els["sched-toggle"].textContent)
        handlers["sched-csv"][0](None)
        name, href = clicked[-1]
        lines = unquote(href.split(",", 1)[1]).strip().split("\n")
        check("page Python: CSV export, header + 60 rows", name == "aumahinay-car-loan-schedule.csv"
              and href.startswith("data:text/csv") and lines[0] == "Month,Payment,Interest,Principal,Balance"
              and len(lines) == 61 and lines[1] == "1,20800.00,4800.00,16000.00,944000.00" and lines[-1].endswith(",0.00"),
              (name, lines[:2], lines[-1]))
        radios["dpmode"] = "peso"
        els["dp-amt"].value = "600000"
        els["term"].value = "12"
        handlers["car"][0](None)
        check("page Python: peso down payment, 12 months hides Show all", els["d-loan"].textContent == "₱600,000.00"
              and els["dp-pct-row"].hidden and not els["dp-amt-row"].hidden and els["sched-toggle"].hidden,
              els["d-loan"].textContent)
        els["ins-financed"].checked = True
        els["sched-wrap"].classList.toggle("short")
        handlers["car-reset"][0](None)
        check("page Python: Reset brings back the sample", els["out-big"].textContent == "₱20,800.00"
              and radios == {"dpmode": "pct", "method": "addon"} and els["price"].value == "1200000"
              and els["dp-amt"].value == "240000" and els["income"].value == "" and els["term"].value == "60"
              and not els["ins-financed"].checked and els["advance"].checked
              and els["sched-wrap"].classList.contains("short") and els["c-total"].textContent == "₱300,800.00",
              (els["out-big"].textContent, radios, els["price"].value))
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
