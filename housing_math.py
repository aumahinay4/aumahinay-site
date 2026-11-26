"""Housing Loan Calculator math, in plain Python (Butch 2026-11-26: "use python language, for consistency").

All the computing for /tools/housing-loan-calculator/. Like loan_math.py, it runs twice:
- build.py runs it (CPython) to fill the page with a worked example before anyone types;
- the visitor's browser runs the same file in MicroPython each time a number changes.
It reuses loan_math.py (payment, principal, rounding and peso formats). In the browser the two files are joined
into one script, so the import below finds the names already defined and is skipped.
MicroPython-friendly: only `math`, no f-strings, no format(",").

A housing loan is a diminishing-balance loan: each month's interest = what is still owed x yearly rate / 12.
The rate is fixed for a "fixing period" (for example 3 years) and then repriced; the payment is then worked out
again on the balance left, for the months left.
"""

import math

try:  # CPython (build and tests). In the browser loan_math.py is already part of the same script.
    from loan_math import r2, payment, principal, round_down, peso, peso0, pct, schedule_csv
except ImportError:
    pass

PAGIBIG_CAP = 10000000  # Pag-IBIG maximum housing loan per borrower (raised from P6 million, May 2026)
PAGIBIG_LTV = 90        # HDMF Circular 402: 90% above the Economic Housing Limit (95% up to it, 100% socialized)
BANK_LTV = 80           # example only: each bank sets its own
INCOME_RATIO = 35       # HDMF Circular 402: monthly repayment not over 35% of gross monthly income
MAX_YEARS = 30


def round_up(x):
    """Whole pesos, rounded up (income needed, down payment needed)."""
    return 0 if x <= 0 else int(math.ceil(x - 1e-7))


def schedule(p, rate1, rate2, k, n):
    """Month-by-month rows of a diminishing loan: rate1 (per month) for the first k months, then rate2 on what is
    left, with the payment worked out again for the months left. Returns (rows, first payment, payment after)."""
    rows = []
    if p <= 0 or n <= 0:
        return rows, 0, 0
    pay1 = r2(payment(p, rate1, n, "dim"))
    pay2 = pay1
    bal = p
    rate, pay = rate1, pay1
    for m in range(1, n + 1):
        if m == k + 1 and 0 < k < n:
            rate = rate2
            pay = pay2 = r2(payment(bal, rate2, n - k, "dim"))
        interest = r2(bal * rate)
        prin = r2(pay - interest)
        amt = pay
        if m == n or prin > bal:  # the last payment clears the centavos
            prin = r2(bal)
            amt = r2(prin + interest)
        bal = r2(bal - prin)
        rows.append({"month": m, "payment": amt, "interest": interest, "principal": prin, "balance": max(bal, 0)})
        if bal <= 0:
            break
    return rows, pay1, pay2


def true_rate(cash, pays):
    """Monthly rate at which the payments made (amortization plus insurance, month by month) are worth exactly the
    loan received: the effective rate. Equals the loan's own rate when there is no insurance and no repricing."""
    if cash <= 0 or not pays or sum(pays) <= cash:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        d, f, pv = 1 / (1 + mid), 1.0, 0.0
        for p in pays:
            f *= d
            pv += p * f
        if pv > cash:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def compute(f):
    """Every figure the page shows. f: price, down, ltv (%), cap (P, 0 = none), rate (% a year), fixYears,
    rateAfter (% a year, 0 = same rate), years, mriYear, fireYear (P a year), income (gross a month), ratio (%)."""
    o = {}
    price, down = f["price"], min(f["down"], f["price"])
    ltv = min(max(f["ltv"], 0), 100) / 100
    n = int(min(f["years"], MAX_YEARS) * 12 + 0.5)
    r1 = f["rate"] / 1200
    r2_ = (f["rateAfter"] if f["rateAfter"] > 0 else f["rate"]) / 1200
    k = int(f["fixYears"] * 12 + 0.5)
    o["n"] = n
    o["downPct"] = down / price if price else 0
    wanted = max(price - down, 0)
    limits = [price * ltv]
    if f["cap"] > 0:
        limits.append(f["cap"])
    o["loan"] = r2(min([wanted] + limits))
    o["gap"] = r2(wanted - o["loan"])  # more cash needed on top of the down payment typed
    o["minDown"] = round_up(price - min(limits))
    o["limitBy"] = "" if o["gap"] <= 0 else ("cap" if f["cap"] > 0 and f["cap"] < price * ltv else "ltv")
    o["repriced"] = 0 < k < n
    # same rate after the fixing period: no new payment to work out (and no centavo drift)
    rows, pay1, pay2 = schedule(o["loan"], r1, r2_, k if r2_ != r1 else 0, n)
    o["rows"] = rows
    o["pi"] = pay1
    o["piAfter"] = pay2
    o["ins"] = r2((f["mriYear"] + f["fireYear"]) / 12)
    o["monthly"] = r2(pay1 + o["ins"])
    o["monthlyAfter"] = r2(pay2 + o["ins"])
    ratio = f["ratio"] / 100
    o["incomeNeeded"] = round_up(o["monthly"] / ratio) if ratio > 0 else 0
    o["incomeNeededAfter"] = round_up(o["monthlyAfter"] / ratio) if ratio > 0 else 0
    o["fits"] = f["income"] >= o["incomeNeeded"] if f["income"] > 0 else None
    o["share"] = o["monthly"] / f["income"] if f["income"] > 0 else 0
    o["totalPI"] = r2(sum([r["payment"] for r in rows]))
    o["interest"] = r2(sum([r["interest"] for r in rows]))
    o["insTotal"] = r2(o["ins"] * len(rows))
    o["eirMonth"] = true_rate(o["loan"], [r["payment"] + o["ins"] for r in rows])
    o["eirYear"] = o["eirMonth"] * 12
    # the other way round: what the income can carry (at the first rate)
    room = f["income"] * ratio - o["ins"]
    exact = principal(room, r1, n, "dim") if room > 0 and n > 0 else 0
    max_loan = round_down(exact, 1000)
    while max_loan > 0 and r2(payment(max_loan, r1, n, "dim")) + o["ins"] > f["income"] * ratio + 0.005:
        max_loan -= 1000
    o["maxByIncome"] = max_loan
    o["maxLoan"] = min(max_loan, f["cap"]) if f["cap"] > 0 else max_loan
    top = o["maxLoan"] + down
    o["downLimits"] = False
    if ltv < 1 and down / (1 - ltv) < top:
        top = down / (1 - ltv)
        o["downLimits"] = f["income"] > 0
    o["maxPrice"] = round_down(top, 1000) if f["income"] > 0 else 0
    return o


# ---- what the page shows ----

DEFAULTS = {"lender": "pagibig", "price": 2500000, "down": 250000, "ltv": PAGIBIG_LTV, "cap": PAGIBIG_CAP,
            "rate": 6.25, "fixYears": 3, "rateAfter": 0, "years": 30, "mriYear": 0, "fireYear": 0,
            "income": 50000, "ratio": INCOME_RATIO}

FIX_CHOICES = (1, 3, 5, 10, 15, 20, 25, 30)


def _years(n):
    y, m = n // 12, n % 12
    s = (str(y) + (" year" if y == 1 else " years")) if y else ""
    if m:
        s += (" and " if s else "") + str(m) + (" month" if m == 1 else " months")
    return s


def view(f):
    """What to show for the typed-in form values f (keys as in DEFAULTS): texts, hidden parts, classes, table rows."""
    o = compute(f)
    text, hidden, cls = {}, {}, {}
    pagibig = f["lender"] == "pagibig"
    hidden["h-pagibig-note"] = not pagibig
    hidden["h-bank-note"] = pagibig
    ok = f["price"] > 0 and o["n"] > 0 and o["loan"] > 0
    note = ""
    if not f["price"]:
        text["h-label"], text["h-big"] = "Type the price of the house to begin", "—"
    elif not o["n"]:
        text["h-label"], text["h-big"] = "Type the loan term in years", "—"
    elif o["loan"] <= 0:
        text["h-label"], text["h-big"] = "No loan needed", "—"
        note = "Your down payment already covers the whole price."
    else:
        text["h-label"] = "Monthly amortization" + (" for the first " + _years(int(f["fixYears"] * 12 + 0.5))
                                                     if o["repriced"] else "")
        text["h-big"] = peso(o["monthly"])
        if o["fits"] is None:
            note = "You need a gross monthly income of about " + peso0(o["incomeNeeded"]) + " for this."
        elif o["fits"]:
            note = ("This fits your income: the payment is " + pct(o["share"], 1) + " of your gross monthly income, "
                    "within the " + pct(f["ratio"] / 100, 0) + " limit.")
        else:
            note = ("This is more than your income allows: you need about " + peso0(o["incomeNeeded"])
                    + " a month in gross income, or a smaller loan.")
    text["h-note"] = note
    cls["h-big"] = "rpt-due" + (" loan-bad" if ok and o["fits"] is False else "")
    gap = ""
    if ok and o["gap"] > 0:
        why = ("the lender's maximum loan of " + peso0(f["cap"])) if o["limitBy"] == "cap" else (
            "a loan of at most " + pct(f["ltv"] / 100, 0) + " of the price")
        gap = ("With " + why + ", the down payment must be at least " + peso0(o["minDown"]) + ". That is "
               + peso0(o["gap"]) + " more than you typed. The figures below use the smaller loan.")
    text["h-gap"] = gap
    hidden["h-gap"] = not gap
    hidden["h-details"] = not ok
    rows = ""
    csv = ""
    hidden["out-pill"] = True
    hidden["sched-toggle"] = o["n"] <= 12
    text["sched-toggle"] = "Show all " + str(o["n"]) + " months"
    if ok:
        text["d-price"] = peso(f["price"])
        text["d-down"] = "−" + peso(f["price"] - o["loan"]) + " (" + pct(1 - o["loan"] / f["price"], 1) + ")"
        text["d-loan"] = peso(o["loan"])
        text["d-term"] = _years(o["n"]) + ", " + str(o["n"]) + " payments"
        text["d-pi"] = peso(o["pi"])
        text["d-ins"] = peso(o["ins"])
        hidden["d-ins-row"] = not o["ins"]
        text["d-monthly"] = peso(o["monthly"])
        text["d-income"] = peso0(o["incomeNeeded"]) + " a month"
        text["d-total"] = peso(o["totalPI"])
        text["d-interest"] = peso(o["interest"])
        text["d-instotal"] = peso(o["insTotal"])
        hidden["d-instotal-row"] = not o["ins"]
        rep = ""
        if o["repriced"]:
            if f["rateAfter"] > 0 and abs(f["rateAfter"] - f["rate"]) > 1e-9:
                rep = ("After the first " + _years(int(f["fixYears"] * 12 + 0.5)) + ", the rate changes to "
                       + pct(f["rateAfter"] / 100) + " a year in this example. The monthly amortization then becomes "
                       + peso(o["monthlyAfter"]) + ", and the income needed about " + peso0(o["incomeNeededAfter"])
                       + ". The totals above include this change.")
            else:
                rep = ("Your rate is fixed for " + _years(int(f["fixYears"] * 12 + 0.5)) + " only. After that the lender "
                       "sets a new rate. Type a possible new rate in \"Rate after the fixing period\" to see the new "
                       "payment. The totals above assume the rate stays the same.")
        text["d-reprice"] = rep
        hidden["d-reprice"] = not rep
        if o["eirMonth"]:
            text["out-pill"] = "Effective rate " + pct(o["eirYear"]) + " a year"
            hidden["out-pill"] = False
        csv = schedule_csv(o["rows"])
        for r in o["rows"]:
            rows += ("<tr><th scope=\"row\">" + str(r["month"]) + "</th><td>" + peso(r["payment"]) + "</td><td>"
                     + peso(r["interest"]) + "</td><td>" + peso(r["principal"]) + "</td><td>" + peso(r["balance"])
                     + "</td></tr>")
    # what the income can carry
    if f["income"] > 0 and o["n"] > 0:
        text["h-afford"] = ("With a gross income of " + peso0(f["income"]) + " a month and " + pct(f["ratio"] / 100, 0)
                            + " of it for the house, you could borrow about " + peso0(o["maxLoan"]) + " over "
                            + _years(o["n"]) + " at " + pct(f["rate"] / 100) + ". With your down payment of "
                            + peso0(min(f["down"], f["price"])) + ", that is a house of up to about "
                            + peso0(o["maxPrice"]) + ".")
        if o["downLimits"]:
            text["h-afford"] += (" Here the down payment is what holds you back: the lender lends at most "
                                 + pct(f["ltv"] / 100, 0) + " of the price, so a bigger down payment would let you "
                                 "buy a more expensive house.")
        if f["cap"] > 0 and o["maxByIncome"] > f["cap"]:
            text["h-afford"] += " The loan is held at the lender's maximum of " + peso0(f["cap"]) + "."
    else:
        text["h-afford"] = "Type your gross monthly income to see the biggest loan and house price it can carry."
    return {"text": text, "hidden": hidden, "class": cls, "rows": rows, "csv": csv, "o": o}
