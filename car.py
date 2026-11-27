"""Car Loan Calculator: /tools/car-loan-calculator/ (Butch 2026-11-26).

For Philippine car buyers: the monthly payment on a car loan, the cash needed on release day (down payment,
chattel mortgage fee, first-year insurance, other fees, one month in advance), the total cost, the true
interest rate, and the monthly income a lender may look for. Add-on and diminishing-balance rates; an add-on
rate may be typed per month, per year or for the whole term, the three ways lenders quote it.

Rules and facts used (checked November 2026):
- Personal Property Security Act (RA 11057): a lender's security interest in a car is registered in the
  Personal Property Security Registry (PPSR) of the Land Registration Authority. LRA Circular No. 02-2025:
  the PPSR has operated since 3 February 2025 and the old chattel mortgage registry no longer accepts new
  security interests in movable collateral; registration of a new notice costs P380 (DOF Administrative Order
  No. 001, s. 2021). LRA Circular No. 03-2025 let the electronic chattel mortgage registry run only until
  29 August 2025. Lenders still call the charge a "chattel mortgage fee", and theirs is usually higher because
  it adds taxes and their own costs, so the calculator asks for the lender's figure.
- Truth in Lending Act (RA 3765), Sec. 4: the lender must give a written statement of the finance charges and
  the finance charge as a simple annual rate before the loan is made.
- Insurance Code (PD 612 as amended by RA 10607), Chapter VI: compulsory motor vehicle liability insurance
  (CTPL) is required to register a car with the LTO. Comprehensive insurance is a lender requirement, not a law.
No lender is named on purpose; each sets its own down payment, rates, terms and income rules.

All math is Python (car_math.py on top of loan_math.py). The browser runs both files plus CAR_UI_PY in
MicroPython, as the Salary Loan Calculator does.
"""

from pathlib import Path

import tags as t
from car_math import CAR_DEFAULTS, car_view
from loan import MICROPYTHON, _field, _num, _radio, loan_tabs
from tags import Raw

CAR_URL = "/tools/car-loan-calculator/"
CAR_CHECKED = "November 2026"
PPSR_FEE = 380  # LRA Circular 02-2025, Sec. 9: registration of a new notice in the PPSR


# The browser side, also in Python. Runs in MicroPython after loan_math.py and car_math.py.
CAR_UI_PY = r"""
import js

doc = js.document


def el(i):
    return doc.getElementById(i)


def num(i):
    try:
        v = float(str(el(i).value).replace(",", ""))
    except ValueError:
        return 0.0
    return v if 0 < v < 1e12 else 0.0


def picked(name):
    c = doc.querySelector('input[name="' + name + '"]:checked')
    return c.value if c else ""


def read_form():
    return {"price": num("price"), "dpMode": picked("dpmode"), "dpPct": num("dp-pct"), "dpAmt": num("dp-amt"),
            "method": picked("method"), "rate": num("rate"), "rateUnit": el("rate-unit").value,
            "term": num("term"), "mortgageFee": num("mortgage-fee"), "insurance": num("insurance"),
            "insFinanced": bool(el("ins-financed").checked), "otherFees": num("other-fees"),
            "advance": bool(el("advance").checked), "income": num("income"), "otherDebts": num("other-debts"),
            "share": num("share")}


def show(v):
    for k in v["hidden"]:
        el(k).hidden = v["hidden"][k]
    for k in v["text"]:
        el(k).textContent = v["text"][k]
    for k in v["class"]:
        el(k).className = v["class"][k]
    if v["rows"]:
        el("sched-body").innerHTML = v["rows"]
    if not el("sched-wrap").classList.contains("short"):
        el("sched-toggle").textContent = "Show first 12 months"
    last[0] = v


last = [None]


def calc(*args):
    show(car_view(read_form()))


def toggle_rows(*args):
    el("sched-wrap").classList.toggle("short")
    calc()


def export_csv(*args):
    if not last[0] or not last[0]["csv"]:
        return
    a = doc.createElement("a")
    a.href = "data:text/csv;charset=utf-8," + js.encodeURIComponent(last[0]["csv"])
    a.download = "aumahinay-car-loan-schedule.csv"
    doc.body.appendChild(a)
    a.click()
    a.remove()


FIELDS = {"price": "price", "dpPct": "dp-pct", "dpAmt": "dp-amt", "rate": "rate", "rateUnit": "rate-unit",
          "term": "term", "mortgageFee": "mortgage-fee", "insurance": "insurance", "otherFees": "other-fees",
          "income": "income", "otherDebts": "other-debts", "share": "share"}


def reset(*args):
    for k in FIELDS:
        d = CAR_DEFAULTS[k]
        el(FIELDS[k]).value = "" if (k in ("income", "otherDebts") and not d) else str(d)
    doc.querySelector('input[name="dpmode"][value="' + CAR_DEFAULTS["dpMode"] + '"]').checked = True
    doc.querySelector('input[name="method"][value="' + CAR_DEFAULTS["method"] + '"]').checked = True
    el("ins-financed").checked = CAR_DEFAULTS["insFinanced"]
    el("advance").checked = CAR_DEFAULTS["advance"]
    el("sched-wrap").classList.add("short")
    calc()


form = el("car")
form.addEventListener("input", calc)
form.addEventListener("change", calc)
el("sched-toggle").addEventListener("click", toggle_rows)
el("sched-csv").addEventListener("click", export_csv)
el("car-reset").addEventListener("click", reset)
calc()
el("car-status").hidden = True
for i in ("sched-csv", "car-reset"):
    el(i).hidden = False
"""


def page_python():
    """The one Python script the browser runs: the shared loan math, the car math, then the page code."""
    here = Path(__file__).parent
    return "\n".join([(here / "loan_math.py").read_text(encoding="utf-8"), (here / "car_math.py").read_text(encoding="utf-8"),
                      CAR_UI_PY])


def _loader():
    py = page_python()
    assert "</script" not in py.lower(), "the Python source would end its <script> tag early"
    return [
        t.script(Raw(py), type="text/x-python", id="car-py"),
        t.script(Raw(
            "document.getElementById('car').addEventListener('submit', e => e.preventDefault());\n"
            "try {\n"
            "  const { loadMicroPython } = await import('%s');\n"
            "  const mp = await loadMicroPython({ url: '%s', stdout: () => {} });\n"
            "  mp.runPython(document.getElementById('car-py').textContent);\n"
            "} catch (e) {\n"
            "  const s = document.getElementById('car-status');\n"
            "  s.textContent = 'The calculator could not start. Please reload the page.';\n"
            "  console.error(e);\n"
            "}\n" % (MICROPYTHON + "micropython.mjs", MICROPYTHON + "micropython.wasm")), type="module"),
    ]


def _check(id_, label, checked=False):
    return t.label(t.input(type="checkbox", id=id_, name=id_, checked=checked), " ", label, class_="choice prior-paid")


def _example(title, setup, lines, result):
    return t.div(t.h3(title), t.p(t.b("What you type: "), setup), t.ul([t.li(x) for x in lines], class_="rpt-steps"),
                 t.p(t.b("Result: "), result), class_="card rpt-example")


def _form():
    d = CAR_DEFAULTS
    return t.form(
        t.fieldset(
            t.legend("1. The car"),
            _field("Price of the car (₱)", _num("price", str(d["price"]), placeholder="e.g. 1200000"),
                   "The dealer's cash price, after any discount."),
            t.p("Down payment", class_="field-title"),
            t.div(_radio("dpmode", "pct", "As a percentage", True), _radio("dpmode", "peso", "In pesos"), class_="choices"),
            _field("Down payment (%)", _num("dp-pct", str(d["dpPct"]), maximum="100"),
                   "Lenders set their own minimum. Ask before you choose a car.", row_id="dp-pct-row"),
            _field("Down payment (₱)", _num("dp-amt", str(d["dpAmt"]), placeholder="e.g. 240000"), None,
                   row_id="dp-amt-row", hidden=True),
        ),
        t.fieldset(
            t.legend("2. The loan"),
            t.p("How is the interest charged?", class_="field-title"),
            t.div(_radio("method", "addon", "Add-on rate", True), _radio("method", "dim", "Diminishing balance"),
                  class_="choices"),
            t.p("Most car loan offers give an add-on rate. Look at the quotation or disclosure statement, and see the "
                "explanation below the calculator.", class_="hint block-hint"),
            t.div(
                _field("Interest rate (%)", _num("rate", str(d["rate"]), maximum="200")),
                _field("Rate is for", t.select(t.option("One year", value="year", selected=True),
                                               t.option("One month", value="month"),
                                               t.option("The whole term", value="term"),
                                               id="rate-unit", name="rate-unit")),
                class_="field-pair",
            ),
            t.p("Some quotations give one add-on rate for the whole term, for example 30% for 60 months. Pick "
                "\"The whole term\" for those.", class_="hint block-hint"),
            t.p("A diminishing rate is almost always given per year. Check the quotation.", id="term-dim-note",
                class_="hint block-hint loan-bad", hidden=True),
            _field("Term (months)", _num("term", str(d["term"]), step="1", minimum="1", maximum="120"),
                   "For example 12, 24, 36, 48 or 60."),
        ),
        t.fieldset(
            t.legend("3. Fees and insurance"),
            t.div(
                _field("Chattel mortgage fee (₱)", _num("mortgage-fee", str(d["mortgageFee"])),
                       "The lender's charge to register its claim on the car. Ask for the exact amount."),
                _field("Other fees (₱)", _num("other-fees", "0"),
                       "Processing or service fees, if any."),
                class_="field-pair",
            ),
            _field("First-year car insurance (₱)", _num("insurance", str(d["insurance"])),
                   "Comprehensive insurance for the first year. Ask the dealer or insurer for a quote."),
            _check("ins-financed", "Add the insurance to the loan instead of paying it in cash"),
            _check("advance", "First monthly payment is paid in advance, on release day", True),
        ),
        t.fieldset(
            t.legend("4. Your income (optional)"),
            t.div(
                _field("Gross monthly income (₱)", _num("income", "", placeholder="e.g. 80000"),
                       "Your salary or business income before deductions; add your spouse's if you apply together."),
                _field("Other loan payments each month (₱)", _num("other-debts", "", placeholder="e.g. 5000"),
                       "Salary loans, housing loan, credit card installments."),
                class_="field-pair",
            ),
            _field("Most of your income for all loan payments (%)", _num("share", str(d["share"]), maximum="100"),
                   "A careful limit you choose. Lenders use their own figure, so ask."),
        ),
        t.div(t.button("Reset sample values", type="button", id="car-reset", class_="loan-btn", hidden=True),
              class_="loan-btns"),
        id="car", class_="card rpt-form", novalidate=True,
    )


def _results():
    """The results card, filled in by car_math (CPython, at build time) for the example values in the form."""
    v = car_view(CAR_DEFAULTS)

    def tx(i):
        return v["text"].get(i, "—")

    def row(label, i, row_id=None, cls=None):
        return t.tr(t.th(label, scope="row"), t.td(tx(i), id=i), id=row_id, class_=cls,
                    hidden=v["hidden"].get(row_id, False) if row_id else False)

    def table(*rows, extra=""):
        return t.div(t.table(t.tbody(*rows), class_="rpt-table loan-sum"), class_="table-scroll" + extra)

    return t.div(
        t.p(tx("out-label"), id="out-label", class_="rpt-due-label"),
        t.p(tx("out-big"), id="out-big", class_=v["class"]["out-big"]),
        t.p(v["text"].get("out-pill", ""), id="out-pill", class_="loan-pill", hidden=v["hidden"]["out-pill"]),
        t.p(tx("out-note"), id="out-note", class_="rpt-av"),
        t.p("Starting the calculator…", id="car-status", class_="rpt-av loan-line"),
        t.div(
            t.h3("The loan", class_="car-h"),
            table(
                row("Price of the car", "d-price"),
                row("Down payment", "d-dp"),
                row("Insurance added to the loan", "d-ins", row_id="d-ins-row"),
                row("Amount borrowed", "d-loan", cls="total"),
                row("Monthly payment", "d-pay"),
                row("Total of all payments", "d-total"),
                row("Total interest", "d-interest"),
            ),
            t.h3("Cash needed on release day", class_="car-h"),
            table(
                row("Down payment", "c-dp"),
                row("Chattel mortgage fee", "c-fee"),
                row("Other fees", "c-other", row_id="c-other-row"),
                row("First-year insurance", "c-ins", row_id="c-ins-row"),
                row("First monthly payment, in advance", "c-adv", row_id="c-adv-row"),
                row("Total cash on release day", "c-total", cls="total"),
            ),
            table(row("Total cost of the car, all in", "d-cost", cls="total"), extra=" loan-after"),
            t.p(t.b("True cost (effective rate): "), t.span(tx("d-eir"), id="d-eir"), class_="rpt-av loan-line"),
            t.p(v["text"].get("d-compare", ""), id="d-compare", class_="rpt-av loan-line",
                hidden=v["hidden"].get("d-compare", True)),
            t.h3("Income a lender may look for", class_="car-h"),
            t.p("Monthly income for this payment: ", t.b(tx("i-needed"), id="i-needed"), class_="rpt-av loan-line"),
            t.p(tx("i-note"), id="i-note", class_=v["class"].get("i-note", "rpt-av loan-line")),
            t.h3("Month-by-month payments", class_="loan-sched-title"),
            t.div(
                t.table(
                    t.thead(t.tr(t.th("Month"), t.th("Payment"), t.th("Interest"), t.th("Principal"), t.th("Balance"))),
                    t.tbody(Raw(v["rows"]), id="sched-body"),
                    class_="rpt-table",
                ),
                id="sched-wrap", class_="table-scroll loan-sched-wrap short",
            ),
            t.div(
                t.button(v["text"]["sched-toggle"], type="button", id="sched-toggle", class_="loan-btn",
                         hidden=v["hidden"]["sched-toggle"]),
                t.button("Export CSV", type="button", id="sched-csv", class_="loan-btn", hidden=True),
                class_="loan-btns",
            ),
            id="car-details", hidden=v["hidden"]["car-details"],
        ),
        class_="card rpt-result", aria_live="polite",
    )


def _explanations():
    return [
        t.h2("How it works"),
        t.ol(
            t.li(t.b("The amount borrowed. "), "The price of the car minus your down payment. If you add the first "
                 "year's insurance to the loan, it is borrowed too, and you pay interest on it."),
            t.li(t.b("The monthly payment. "), "Worked out from the amount borrowed, the rate and the term. With an "
                 "add-on rate, the interest for the whole term is added at the start and the total is split into "
                 "equal payments."),
            t.li(t.b("Cash on release day. "), "What you pay before you drive the car home: the down payment, the "
                 "chattel mortgage fee and other fees, the insurance if you pay it in cash, and the first monthly "
                 "payment if the lender asks for it in advance."),
            t.li(t.b("Income. "), "The calculator divides your loan payments by the share of income you chose, to "
                 "show the monthly income that keeps them within that limit."),
            class_="rpt-notes loan-steps",
        ),
        t.h2("Add-on rate or diminishing balance?"),
        t.p("Car loan quotations in the Philippines usually give an add-on rate. With an add-on rate, interest is "
            "charged on the full amount borrowed for the whole term, even in the last months when you owe very "
            "little. With a diminishing balance, each month's interest is charged only on what you still owe."),
        t.p("An add-on rate can be quoted three ways, and the calculator takes all three. A rate per year: 6% a year "
            "on ₱960,000 for 60 months is ₱960,000 × 6% × 5 years = ₱288,000 interest. A rate for the whole term: the "
            "same loan may be quoted as 30% for 60 months, which is the same ₱288,000. A rate per month: 0.5% a month "
            "for 60 months, again ₱288,000. Always ask which one the quotation means."),
        t.p("Because you keep paying interest on money you have already paid back, an add-on rate costs more than it "
            "looks. The calculator shows the effective rate: 6% a year add-on for 60 months works out to about 10.8% a "
            "year on a diminishing balance, and higher still once the fees and the advance payment are counted."),
        t.h2("What is the chattel mortgage fee?"),
        t.p("When a lender pays for your car, it keeps a claim on the car until the loan is paid. People still call "
            "this a chattel mortgage. Under the Personal Property Security Act (Republic Act No. 11057), the claim is "
            "now registered in the Personal Property Security Registry of the Land Registration Authority, which has "
            "run since February 3, 2025. The registry's own fee for a new notice is ₱" + format(PPSR_FEE, ",") + "."),
        t.p("The chattel mortgage fee on a car loan quotation is usually much higher, because it also covers "
            "documentary stamp tax and the lender's or dealer's own processing. It is a cost of borrowing, so the "
            "calculator counts it in the effective rate. Ask for the exact amount in writing."),
        t.h2("Insurance"),
        t.p("Every car needs compulsory third party liability (CTPL) insurance to be registered with the LTO; the "
            "Insurance Code requires it. Lenders also ask for comprehensive insurance, which covers damage to the car "
            "and theft, for as long as the loan runs, with the lender named in the policy. The first year is often "
            "paid on release day or added to the loan. From the second year you renew it yourself, so set money aside "
            "each year. The calculator counts only the first year."),
        t.h2("Worked examples"),
        _example(
            "1. A ₱1.2 million car over 60 months",
            "Price ₱1,200,000, down payment 20%. Add-on rate 6% a year, 60 months. Chattel mortgage fee ₱10,000, "
            "insurance ₱30,000 paid in cash, first payment in advance.",
            ["Down payment: ₱1,200,000 × 20% = ₱240,000. Amount borrowed: ₱960,000.",
             "Interest: ₱960,000 × 6% × 5 years = ₱288,000. Monthly payment: (₱960,000 + ₱288,000) ÷ 60 = ₱20,800.",
             "Cash on release day: ₱240,000 + ₱10,000 + ₱30,000 + ₱20,800 = ₱300,800.",
             "Income for a 30% limit: ₱20,800 ÷ 30% = about ₱69,333 a month."],
            "₱20,800 a month, about ₱300,800 cash on release day, and ₱1,528,000 in all for a ₱1.2 million car."),
        _example(
            "2. The same car over 36 months",
            "Everything as in example 1, but 36 months.",
            ["Interest: ₱960,000 × 6% × 3 years = ₱172,800.",
             "Monthly payment: (₱960,000 + ₱172,800) ÷ 36 = ₱31,466.67."],
            "The payment is ₱10,666.67 higher each month, but you save about ₱115,200 in interest."),
        _example(
            "3. What car can my income carry?",
            "As in example 1, plus gross income ₱60,000 a month and ₱5,000 of other loan payments, with a 30% limit.",
            ["Room for a car payment: ₱60,000 × 30% − ₱5,000 = ₱13,000 a month.",
             "Biggest loan for ₱13,000 a month: ₱13,000 × 60 ÷ (1 + 0.5% × 60) = ₱780,000 ÷ 1.3 = ₱600,000.",
             "With 20% down, the loan is 80% of the price: ₱600,000 ÷ 80% = ₱750,000."],
            "The ₱1.2 million car is too much for this income, but a car of about ₱750,000 fits."),
        t.h2("Before you sign"),
        t.ul(
            t.li(t.b("Ask for the disclosure statement. "), "Under the Truth in Lending Act (RA 3765), the lender must "
                 "tell you in writing, before the loan is made, all the finance charges and what they come to as a "
                 "yearly rate. Compare it with the effective rate here."),
            t.li(t.b("Get the all-in figure. "), "Ask the dealer and the lender for every amount due on release day: "
                 "down payment, chattel mortgage fee, insurance, advance payment and any other charge."),
            t.li(t.b("Compare more than one offer. "), "Type each quotation into the calculator and compare the total "
                 "cost and the effective rate, not only the monthly payment."),
            t.li(t.b("Count the running costs. "), "Fuel, parking, toll, maintenance, yearly LTO registration and "
                 "insurance renewal come on top of the loan payment."),
            t.li(t.b("Ask about paying early. "), "Some loans charge a fee if you pay the balance before the term ends."),
            class_="plain-list rpt-notes",
        ),
        t.h2("Questions people ask"),
        t.h3("Is a bigger down payment better?", class_="rpt-q"),
        t.p("Usually, yes. You borrow less, so you pay less interest, and lenders sometimes give a lower rate. Keep "
            "enough cash for the release-day costs and for emergencies, though."),
        t.h3("Why does the lender's monthly payment differ from the calculator's?", class_="rpt-q"),
        t.p("Lenders round payments their own way, may add insurance or fees to the loan, and set rates by term and "
            "down payment. The calculator uses only what you type, so use the figures in your quotation."),
        t.h3("What does \"one month advance\" mean?", class_="rpt-q"),
        t.p("Some lenders ask for the first monthly payment on release day. It is part of the loan's payments, not "
            "an extra charge, but it raises the cash you need that day and makes the loan cost a little more."),
        t.h3("Is a longer term better?", class_="rpt-q"),
        t.p("A longer term lowers the monthly payment but adds interest, as example 2 shows. Choose the shortest term "
            "your income can carry with room to spare."),
    ]


def car_page():
    return {
        "title": "Car Loan Calculator", "active": CAR_URL, "url": CAR_URL, "og_type": "website",
        "seo_title": "Car Loan Calculator, Philippines: Monthly Payment and Cash Out · Butch Mahinay",
        "description": "Free car loan calculator for the Philippines: monthly payment, cash needed on release day, "
                       "chattel mortgage fee, insurance, total cost, true interest rate and the income you need.",
        "body": [
            loan_tabs(CAR_URL),
            t.p("Free tool", class_="eyebrow"),
            t.h1("Car Loan Calculator"),
            t.p("Planning to buy a car on loan? Find out the monthly payment, the cash you need on release day, what "
                "the car will cost you in all, and the income that can carry it, before you visit the dealer.",
                class_="lead"),
            _form(),
            _results(),
            t.div(
                t.h3("Estimate only"),
                t.p("This calculator is for learning and planning only. Its figures are estimates based on what you "
                    "type. They are not a loan offer, an approval, or financial or legal advice. Each lender sets its "
                    "own down payment, rates, fees, insurance requirements, rounding and income rules."),
                t.p("Always read the lender's disclosure statement and the dealer's quotation before you sign. This "
                    "site is not connected with any bank, lender, car dealer, insurer or government office."),
                class_="disclaimer rpt-disclaimer",
            ),
            *_explanations(),
            t.p("Sources: ",
                t.a("Personal Property Security Act (RA 11057)", href="https://ldr.senate.gov.ph/legislative-issuance/republic-act-no-11057", rel="noopener"),
                "; ",
                t.a("LRA Circular No. 02-2025, operation of the Personal Property Security Registry", href="https://lra.gov.ph/wp-content/uploads/2025/07/02-2025-OPERATIONALIZATION-OF-THE-PERSONAL-PROPERTY-SECURITY-REGISTRY.pdf", rel="noopener"),
                "; ",
                t.a("Truth in Lending Act (RA 3765)", href="https://lawphil.net/statutes/repacts/ra1963/ra_3765_1963.html", rel="noopener"),
                ", Sec. 4. Last checked " + CAR_CHECKED + ".", class_="muted note sources-line"),
            t.p("The figures are worked out in Python, right in your browser. Nothing you type is sent or saved.", class_="muted note"),
            *_loader(),
        ],
    }
