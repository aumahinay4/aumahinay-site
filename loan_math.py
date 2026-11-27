"""Salary Loan Calculator math, in plain Python (Butch 2026-11-26: "use python language, for consistency").

This one file does all the computing for /tools/salary-loan-calculator/:
- build.py runs it (CPython) to fill the page with a worked example before anyone types;
- the visitor's browser runs the very same file in MicroPython (a small Python made for the web), every time a number changes;
- tests/test_loan.py checks it in both.
So it must stay MicroPython-friendly: only the math module, no f-string tricks, no format(",").

Rates are decimals per month (1% a month = 0.01).
"""

import math


def r2(x):
    """Round to centavos, halves away from zero (Python's round() rounds halves to even)."""
    s = -1 if x < 0 else 1
    return s * math.floor(abs(x) * 100 + 0.5 + 1e-7) / 100


def payment(p, rate, n, method):
    """Equal monthly payment on a loan of p over n months."""
    if p <= 0 or n <= 0:
        return 0.0
    if method == "addon":  # interest on the full loan for every month, added on top
        return p * (1 + rate * n) / n
    if rate == 0:
        return p / n
    return p * rate / (1 - (1 + rate) ** -n)  # diminishing balance (standard amortization)


def principal(a, rate, n, method):
    """The biggest loan whose monthly payment is at most a (the reverse of payment)."""
    if a <= 0 or n <= 0:
        return 0.0
    if method == "addon":
        return a * n / (1 + rate * n)
    if rate == 0:
        return a * n
    return a * (1 - (1 + rate) ** -n) / rate


def effective_rate(cash, a, n):
    """Monthly rate at which n payments of a are worth exactly the cash received (the true cost)."""
    if cash <= 0 or a <= 0 or n <= 0 or a * n <= cash:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if principal(a, mid, n, "dim") > cash:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def round_down(x, step):
    """Lenders lend round figures: round a loan amount down to a step."""
    return 0 if x <= 0 else int(math.floor(x / step + 1e-9)) * step


def schedule(p, rate, n, method):
    """Month-by-month table: each month's interest is charged on the balance still owed.

    For an add-on loan the monthly payment stays the add-on payment, but the interest inside it is worked out at
    the diminishing rate that gives the very same payment (see effective_rate). BSP Circular 730 (Manual of
    Regulations for Banks, Sec. X305.5) says banks may charge interest only on the outstanding balance, so a
    bank's own table shows interest getting smaller each month. The total interest is the same either way."""
    a = r2(payment(p, rate, n, method))
    bal = p
    rows = []
    if method == "addon":
        rate = effective_rate(p, a, n)  # the diminishing rate that gives the same payment
    for m in range(1, n + 1):
        interest = r2(bal * rate)
        prin = r2(a - interest)
        pay = a
        if m == n:  # the last payment absorbs the centavos
            prin = r2(bal)
            if method == "addon":  # an add-on loan keeps the same payment to the end; the interest takes the centavos
                interest = r2(a - prin)
            pay = r2(prin + interest)
        bal = r2(bal - prin)
        rows.append({"month": m, "payment": pay, "interest": interest, "principal": prin, "balance": max(bal, 0)})
    return rows


def compute(inp):
    """Every figure the page shows.
    inp: gross, deductions, floor, freed, oldBalance, method, rate (per month), n, feePct, feeFixed, mode, amount, cap."""
    o = {}
    o["netNow"] = r2(inp["gross"] - inp["deductions"])
    o["room"] = r2(max(o["netNow"] + inp["freed"] - inp["floor"], 0))  # most the new payment can be
    exact = principal(o["room"], inp["rate"], inp["n"], inp["method"])
    o["maxExact"] = r2(exact)
    step = 1000 if exact >= 10000 else 100
    max_loan = round_down(exact, step)
    while max_loan > 0 and r2(payment(max_loan, inp["rate"], inp["n"], inp["method"])) > o["room"]:
        max_loan -= step  # the rounded payment of the rounded loan must still fit
    o["capped"] = False
    if inp["cap"] > 0 and max_loan > inp["cap"]:
        max_loan = inp["cap"]
        o["capped"] = True
    o["maxLoan"] = max_loan
    loan = inp["amount"] if inp["mode"] == "check" else max_loan
    o["loan"] = loan
    o["pay"] = r2(payment(loan, inp["rate"], inp["n"], inp["method"]))
    o["perPayday"] = r2(o["pay"] / 2)
    o["totalPaid"] = r2(o["pay"] * inp["n"])
    o["interest"] = r2(o["totalPaid"] - loan)
    o["fees"] = r2(loan * inp["feePct"] / 100 + inp["feeFixed"]) if loan > 0 else 0
    o["cash"] = r2(loan - o["fees"] - (inp["oldBalance"] if loan > 0 else 0))
    o["netAfter"] = r2(o["netNow"] + (inp["freed"] if loan > 0 else 0) - o["pay"])
    o["fits"] = o["netAfter"] >= inp["floor"] - 0.005
    o["short"] = 0 if o["fits"] else r2(inp["floor"] - o["netAfter"])
    e = effective_rate(loan - o["fees"], o["pay"], inp["n"])
    o["eirMonth"] = e
    o["eirYear"] = e * 12
    o["sameAsDim"] = effective_rate(loan, o["pay"], inp["n"]) if inp["method"] == "addon" else inp["rate"]
    return o


# ---- words and numbers as the page shows them ----

def _group(n):
    s = str(int(n))
    out = ""
    while len(s) > 3:
        out = "," + s[-3:] + out
        s = s[:-3]
    return s + out


def peso(x):
    """₱1,234.56 (and −₱ for a negative)."""
    cents = int(math.floor(abs(x) * 100 + 0.5 + 1e-7))
    return ("−" if x < 0 else "") + "₱" + _group(cents // 100) + "." + ("%02d" % (cents % 100))


def peso0(x):
    """₱1,235: whole pesos."""
    return "₱" + _group(math.floor(abs(x) + 0.5))


def pct(x, d=2):
    """0.0177 -> '1.77%', with no trailing zeros."""
    s = ("%." + str(d) + "f") % (x * 100)
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s + "%"


def schedule_csv(rows):
    """The payment table as CSV text, plain numbers, for the Export CSV button."""
    out = "Month,Payment,Interest,Principal,Balance\n"
    for r in rows:
        out += ",".join([str(r["month"])] + ["%.2f" % r[k] for k in ("payment", "interest", "principal", "balance")]) + "\n"
    return out


DEFAULTS = {"who": "gov", "gross": 30000, "deductions": 9000, "floor": 5000, "renew": False, "oldPay": 0,
            "oldBal": 0, "method": "addon", "rate": 1, "rateUnit": "month", "term": 36, "feePct": 0, "feeFixed": 0,
            "mode": "max", "amount": 100000, "cap": 0}


def view(f):
    """What to show for the typed-in form values f (keys as in DEFAULTS): texts, hidden parts, classes, table rows."""
    rate = f["rate"] / 100
    if f["rateUnit"] == "year":
        rate = rate / 12
    n = int(f["term"] + 0.5)
    renew = f["renew"]
    inp = {"gross": f["gross"], "deductions": f["deductions"], "floor": f["floor"],
           "freed": f["oldPay"] if renew else 0, "oldBalance": f["oldBal"] if renew else 0,
           "method": f["method"], "rate": rate, "n": n, "feePct": f["feePct"], "feeFixed": f["feeFixed"],
           "mode": f["mode"], "amount": f["amount"], "cap": f["cap"]}
    o = compute(inp)
    text, hidden, cls = {}, {}, {}
    hidden["floor-gov"] = f["who"] != "gov"
    hidden["floor-other"] = f["who"] == "gov"
    hidden["amount-row"] = f["mode"] != "check"
    hidden["renew-rows"] = not renew
    text["out-net"] = peso(o["netNow"])
    text["out-room"] = peso(o["room"])
    note = ""
    if not f["gross"]:
        text["out-label"], text["out-big"] = "Type your monthly pay to begin", "—"
    elif not n:
        text["out-label"], text["out-big"] = "Type the number of months", "—"
    elif f["mode"] == "max":
        text["out-label"] = "You may borrow up to about"
        text["out-big"] = peso0(o["maxLoan"])
        if o["maxLoan"] <= 0:
            note = ("Your take-home pay is already at or below the lowest amount you set, so there is no room "
                    "for a new loan payment.")
        elif o["capped"]:
            note = ("This is the lender's limit you typed. Your pay alone would allow about "
                    + peso0(round_down(o["maxExact"], 1000)) + ".")
        else:
            note = "Rounded down to a round figure. The exact most is " + peso(o["maxExact"]) + "."
    else:
        text["out-label"] = "Monthly payment for " + peso0(o["loan"])
        text["out-big"] = peso(o["pay"])
        if not o["loan"]:
            note = "Type the amount you want to borrow."
        elif o["fits"]:
            note = "This loan fits: your take-home pay stays at or above " + peso(f["floor"]) + "."
        else:
            note = ("This loan is too big: your take-home pay would fall " + peso(o["short"]) + " below "
                    + peso(f["floor"]) + ". The most that fits is about " + peso0(o["maxLoan"]) + ".")
    text["out-note"] = note
    cls["out-big"] = "rpt-due" + (" loan-bad" if f["mode"] == "check" and o["loan"] and not o["fits"] else "")
    show = bool(f["gross"] and n and o["loan"] > 0)
    hidden["loan-details"] = not show
    rows = ""
    csv = ""
    hidden["out-pill"] = True
    hidden["sched-toggle"] = n <= 12
    text["sched-toggle"] = "Show all " + str(n) + " months"
    if show:
        text["d-loan"] = peso(o["loan"])
        text["d-pay"] = peso(o["pay"])
        text["d-payday"] = peso(o["perPayday"])
        text["d-total"] = peso(o["totalPaid"])
        text["d-interest"] = peso(o["interest"])
        text["d-fees"] = ("−" + peso(o["fees"])) if o["fees"] else peso(0)
        hidden["d-old-row"] = not inp["oldBalance"]
        text["d-old"] = "−" + peso(inp["oldBalance"])
        text["d-cash"] = peso(o["cash"])
        text["d-netafter"] = peso(o["netAfter"])
        cls["d-netafter-row"] = "total" if o["fits"] else "total loan-bad"
        text["d-eir"] = (pct(o["eirMonth"]) + " a month, about " + pct(o["eirYear"], 1) + " a year") if o["eirMonth"] else "none"
        cmp = ""
        if f["method"] == "addon" and o["sameAsDim"] > rate + 1e-9:
            cmp = ("An add-on rate of " + pct(rate) + " a month costs the same as a diminishing rate of about "
                   + pct(o["sameAsDim"]) + " a month (" + pct(o["sameAsDim"] * 12, 1) + " a year), before fees.")
        text["d-compare"] = cmp
        hidden["d-compare"] = not cmp
        if o["eirMonth"]:
            text["out-pill"] = "Effective rate " + pct(o["eirYear"], 1) + " a year"
            hidden["out-pill"] = False
        table = schedule(o["loan"], rate, n, f["method"])
        csv = schedule_csv(table)
        for r in table:
            rows += ("<tr><th scope=\"row\">" + str(r["month"]) + "</th><td>" + peso(r["payment"]) + "</td><td>"
                     + peso(r["interest"]) + "</td><td>" + peso(r["principal"]) + "</td><td>" + peso(r["balance"])
                     + "</td></tr>")
    return {"text": text, "hidden": hidden, "class": cls, "rows": rows, "csv": csv, "o": o}
