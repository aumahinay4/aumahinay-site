"""Car Loan Calculator math, in plain Python, like the Salary Loan Calculator (Butch 2026-11-26).

It builds on loan_math.py (payment, principal, effective rate, schedule, peso formats), so both calculators
share one set of loan formulas:
- build.py runs it (CPython) to fill /tools/car-loan-calculator/ with a worked example before anyone types;
- the visitor's browser runs loan_math.py, then this file, then the page code, in MicroPython;
- tests/test_car_loan.py checks it.
In the browser both files run as one script, so the import below fails there and the names are already
defined. Keep it MicroPython-friendly: no f-strings, no format(",").

Rates are decimals per month (1% a month = 0.01).
"""

try:
    from loan_math import effective_rate, payment, pct, peso, peso0, principal, r2, round_down, schedule
except ImportError:  # in the browser, loan_math.py has already run in the same script
    pass


def car_compute(inp):
    """Every figure the page shows.
    inp: price, dpMode ('pct' or 'peso'), dpPct, dpAmt, method, rate (per month), n, mortgageFee, insurance,
    insFinanced, otherFees, advance, income, otherDebts, share (% of gross income for all loan payments)."""
    o = {}
    price = max(inp["price"], 0)
    if inp["dpMode"] == "pct":
        dp = r2(price * min(inp["dpPct"], 100) / 100)
    else:
        dp = r2(min(inp["dpAmt"], price))
    n = inp["n"]
    o["dp"] = dp
    o["dpShare"] = dp / price if price else 0
    o["carLoan"] = r2(price - dp)
    ins_in_loan = inp["insurance"] if inp["insFinanced"] else 0
    loan = r2(o["carLoan"] + ins_in_loan) if o["carLoan"] > 0 else 0
    o["loan"] = loan
    o["pay"] = r2(payment(loan, inp["rate"], n, inp["method"]))
    o["totalPaid"] = r2(o["pay"] * n)
    o["interest"] = r2(o["totalPaid"] - loan)
    fees = r2(inp["mortgageFee"] + inp["otherFees"]) if loan > 0 else 0
    o["fees"] = fees
    o["insCash"] = 0 if inp["insFinanced"] else r2(inp["insurance"])
    o["advancePay"] = o["pay"] if inp["advance"] and loan > 0 else 0
    o["cashDay"] = r2(dp + fees + o["insCash"] + o["advancePay"])
    # everything paid for the car, the loan and the first year's insurance, from the down payment to the last month
    o["totalCost"] = r2(dp + o["totalPaid"] + fees + o["insCash"])
    # true cost of the loan: the fees count as finance charges; with one month in advance, the first payment
    # is paid on release day, so the money really lent is the loan minus that payment
    if loan > 0 and n > 0:
        if inp["advance"] and n > 1:
            e = effective_rate(loan - fees - o["pay"], o["pay"], n - 1)
        else:
            e = effective_rate(loan - fees, o["pay"], n)
    else:
        e = 0.0
    o["eirMonth"] = e
    o["eirYear"] = e * 12
    o["sameAsDim"] = effective_rate(loan, o["pay"], n) if inp["method"] == "addon" else inp["rate"]
    # income: how much a lender would want to see, and what the typed income can carry
    share = inp["share"] / 100
    o["incomeNeeded"] = r2((o["pay"] + inp["otherDebts"]) / share) if share > 0 and o["pay"] > 0 else 0
    o["room"] = r2(max(inp["income"] * share - inp["otherDebts"], 0))
    o["fits"] = inp["income"] > 0 and o["pay"] + inp["otherDebts"] <= inp["income"] * share + 0.005
    exact = principal(o["room"], inp["rate"], n, inp["method"])
    max_loan = round_down(exact, 1000)
    while max_loan > 0 and r2(payment(max_loan, inp["rate"], n, inp["method"])) > o["room"]:
        max_loan -= 1000  # the rounded payment of the rounded loan must still fit
    o["maxLoan"] = max_loan
    car_part = max_loan - ins_in_loan  # the financed insurance takes part of the loan
    if car_part <= 0:
        max_price = 0
    elif inp["dpMode"] == "pct":
        max_price = round_down(car_part / (1 - inp["dpPct"] / 100), 1000) if inp["dpPct"] < 100 else 0
    else:
        max_price = round_down(car_part + inp["dpAmt"], 1000)
    o["maxPrice"] = max_price
    return o


# ---- what the page shows ----

CAR_DEFAULTS = {"price": 1200000, "dpMode": "pct", "dpPct": 20, "dpAmt": 240000, "method": "addon", "rate": 6,
                "rateUnit": "year", "term": 60, "mortgageFee": 10000, "insurance": 30000, "insFinanced": False,
                "otherFees": 0, "advance": True, "income": 0, "otherDebts": 0, "share": 30}


def monthly_rate(rate_pct, unit, n):
    """The typed rate as a decimal per month. 'term' means the rate is for the whole loan, as some
    add-on rates are quoted (for example 30% for 60 months = 0.5% a month)."""
    r = rate_pct / 100
    if unit == "year":
        return r / 12
    if unit == "term":
        return r / n if n else 0
    return r


def car_view(f):
    """What to show for the typed-in form values f (keys as in CAR_DEFAULTS): texts, hidden parts, classes, rows."""
    n = int(f["term"] + 0.5)
    rate = monthly_rate(f["rate"], f["rateUnit"], n)
    inp = {"price": f["price"], "dpMode": f["dpMode"], "dpPct": f["dpPct"], "dpAmt": f["dpAmt"],
           "method": f["method"], "rate": rate, "n": n, "mortgageFee": f["mortgageFee"],
           "insurance": f["insurance"], "insFinanced": f["insFinanced"], "otherFees": f["otherFees"],
           "advance": f["advance"], "income": f["income"], "otherDebts": f["otherDebts"], "share": f["share"]}
    o = car_compute(inp)
    text, hidden, cls = {}, {}, {}
    hidden["dp-pct-row"] = f["dpMode"] != "pct"
    hidden["dp-amt-row"] = f["dpMode"] == "pct"
    hidden["term-dim-note"] = not (f["method"] == "dim" and f["rateUnit"] == "term")
    note = ""
    show = False
    if not f["price"]:
        text["out-label"], text["out-big"] = "Type the price of the car to begin", "—"
    elif not n:
        text["out-label"], text["out-big"] = "Type the number of months", "—"
    elif o["loan"] <= 0:
        text["out-label"], text["out-big"] = "No loan needed", "—"
        note = "Your down payment covers the whole price, so there is nothing to borrow."
    else:
        show = True
        text["out-label"] = "Monthly payment for " + str(n) + " months"
        text["out-big"] = peso(o["pay"])
        note = ("Cash needed on release day: " + peso0(o["cashDay"]) + ". You will pay " + peso0(o["totalPaid"])
                + " in all for a loan of " + peso0(o["loan"]) + ".")
    text["out-note"] = note
    hidden["car-details"] = not show
    rows = ""
    if show:
        text["d-price"] = peso(f["price"])
        text["d-dp"] = "−" + peso(o["dp"]) + " (" + pct(o["dpShare"], 1) + ")"
        hidden["d-ins-row"] = not f["insFinanced"] or not f["insurance"]
        text["d-ins"] = "+" + peso(f["insurance"])
        text["d-loan"] = peso(o["loan"])
        text["d-pay"] = peso(o["pay"])
        text["d-total"] = peso(o["totalPaid"])
        text["d-interest"] = peso(o["interest"])
        text["c-dp"] = peso(o["dp"])
        text["c-fee"] = peso(f["mortgageFee"])
        hidden["c-other-row"] = not f["otherFees"]
        text["c-other"] = peso(f["otherFees"])
        hidden["c-ins-row"] = not o["insCash"]
        text["c-ins"] = peso(o["insCash"])
        hidden["c-adv-row"] = not o["advancePay"]
        text["c-adv"] = peso(o["advancePay"])
        text["c-total"] = peso(o["cashDay"])
        text["d-cost"] = peso(o["totalCost"])
        text["d-eir"] = (pct(o["eirMonth"]) + " a month, about " + pct(o["eirYear"], 1) + " a year") if o["eirMonth"] else "none"
        cmp = ""
        if f["method"] == "addon" and o["sameAsDim"] > rate + 1e-9:
            cmp = ("This add-on rate (" + pct(rate) + " a month) costs the same as a diminishing rate of about "
                   + pct(o["sameAsDim"]) + " a month (" + pct(o["sameAsDim"] * 12, 1) + " a year), before fees.")
        text["d-compare"] = cmp
        hidden["d-compare"] = not cmp
        # income
        text["i-needed"] = peso0(o["incomeNeeded"])
        share_txt = pct(f["share"] / 100, 1)
        if f["income"] > 0:
            if o["fits"]:
                inote = ("Your income of " + peso0(f["income"]) + " carries this payment: your loan payments stay "
                         "within " + share_txt + " of it.")
                cls["i-note"] = "rpt-av loan-line"
            else:
                inote = ("This payment is too big for an income of " + peso0(f["income"]) + " if loan payments "
                         "should stay within " + share_txt + " of it.")
                cls["i-note"] = "rpt-av loan-line loan-bad"
            if o["maxPrice"] > 0:
                inote += (" With the same down payment, rate and term, it can carry a car of about "
                          + peso0(o["maxPrice"]) + " (a loan of about " + peso0(o["maxLoan"]) + ").")
            else:
                inote += " Your other loan payments already use up that share."
        else:
            inote = "Type your monthly income below to see if it carries this payment."
            cls["i-note"] = "rpt-av loan-line"
        text["i-note"] = inote
        for r in schedule(o["loan"], rate, n, f["method"]):
            rows += ("<tr><th scope=\"row\">" + str(r["month"]) + "</th><td>" + peso(r["payment"]) + "</td><td>"
                     + peso(r["interest"]) + "</td><td>" + peso(r["principal"]) + "</td><td>" + peso(r["balance"])
                     + "</td></tr>")
    cls["out-big"] = "rpt-due"
    return {"text": text, "hidden": hidden, "class": cls, "rows": rows, "o": o}
