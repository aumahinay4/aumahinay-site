"""Housing Loan Calculator: /tools/housing-loan-calculator/ (Butch 2026-11-26).

Monthly amortization of a Pag-IBIG or bank housing loan in the Philippines: house price, down payment, term,
rate fixed for a period and then repriced, MRI and fire insurance, the income needed, and what an income can
carry. All the math is in housing_math.py (which reuses loan_math.py from the Salary Loan Calculator), run by the
build in CPython and in the visitor's browser in MicroPython, the same way as loan.py.

Rules used (checked November 2026; pagibigfund.gov.ph could not be read by our tools, so its circulars were read
on the Supreme Court E-Library and the 2026 changes in the news):
- HDMF Circular No. 402 (2018): monthly repayment not over 35% of gross monthly income; loan-to-appraised value
  95% up to the Economic Housing Limit, 90% above it up to P6,000,000, 100% for socialized developer-assisted loans.
- HDMF Circular No. 403 (2018, Affordable Housing Program): MRI and fire insurance required, premiums included in
  the equal monthly amortization; at least 24 monthly savings; at most 65 at application and 70 at maturity; term
  up to 30 years; rate repriced at the end of the fixing period.
- Daily Tribune (May 28, 2026) and Philstar (May 29, 2026): maximum Pag-IBIG housing loan raised to P10 million
  (from P6 million), up to 30 years, rates "as low as 5.75 percent per year, depending on the chosen fixing period",
  3% subsidized rate for socialized housing under the Expanded 4PH Program.
"""

from pathlib import Path

import tags as t
from housing_math import BANK_LTV, DEFAULTS, FIX_CHOICES, INCOME_RATIO, PAGIBIG_CAP, PAGIBIG_LTV, view
from loan import MICROPYTHON, _example, _field, _num, _radio, loan_tabs
from tags import Raw

HOUSING_URL = "/tools/housing-loan-calculator/"
HOUSING_CHECKED = "November 2026"

# The browser side, in Python. It runs in MicroPython after loan_math.py and housing_math.py.
HOUSING_UI_PY = r"""
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


last_lender = [picked("lender")]


def read_form():
    lender = picked("lender")
    if lender != last_lender[0]:  # switching fills in that lender's usual limits; the person can still change them
        el("ltv").value = "__PLTV__" if lender == "pagibig" else "__BLTV__"
        el("cap").value = "__PCAP__" if lender == "pagibig" else ""
        last_lender[0] = lender
    return {"lender": lender, "price": num("price"), "down": num("down"), "ltv": num("ltv"), "cap": num("cap"),
            "rate": num("rate"), "fixYears": num("fix"), "rateAfter": num("rate-after"), "years": num("years"),
            "mriYear": num("mri"), "fireYear": num("fire"), "income": num("income"), "ratio": num("ratio")}


def show(v):
    for k in v["hidden"]:
        el(k).hidden = v["hidden"][k]
    for k in v["text"]:
        el(k).textContent = v["text"][k]
    for k in v["class"]:
        el(k).className = v["class"][k]
    if v["rows"]:
        el("h-sched-body").innerHTML = v["rows"]
    if not el("sched-wrap").classList.contains("short"):
        el("sched-toggle").textContent = "Show first 12 months"
    last[0] = v


last = [None]


def calc(*args):
    show(view(read_form()))


def toggle_rows(*args):
    el("sched-wrap").classList.toggle("short")
    calc()


def export_csv(*args):
    if not last[0] or not last[0]["csv"]:
        return
    a = doc.createElement("a")
    a.href = "data:text/csv;charset=utf-8," + js.encodeURIComponent(last[0]["csv"])
    a.download = "aumahinay-housing-loan-schedule.csv"
    doc.body.appendChild(a)
    a.click()
    a.remove()


FIELDS = {"price": "price", "down": "down", "ltv": "ltv", "cap": "cap", "rate": "rate", "fixYears": "fix",
          "rateAfter": "rate-after", "years": "years", "mriYear": "mri", "fireYear": "fire", "income": "income",
          "ratio": "ratio"}


def reset(*args):
    for k in FIELDS:
        d = DEFAULTS[k]
        el(FIELDS[k]).value = str(d) if d else ""
    doc.querySelector('input[name="lender"][value="' + DEFAULTS["lender"] + '"]').checked = True
    last_lender[0] = DEFAULTS["lender"]
    el("sched-wrap").classList.add("short")
    calc()


form = el("housing")
form.addEventListener("input", calc)
form.addEventListener("change", calc)
el("sched-toggle").addEventListener("click", toggle_rows)
el("sched-csv").addEventListener("click", export_csv)
el("h-reset").addEventListener("click", reset)
calc()
el("h-status").hidden = True
for i in ("sched-csv", "h-reset"):
    el(i).hidden = False
""".replace("__PLTV__", str(PAGIBIG_LTV)).replace("__BLTV__", str(BANK_LTV)).replace("__PCAP__", str(PAGIBIG_CAP))


def page_python():
    """The whole Python program the browser runs: the shared loan math, the housing math, then the page code."""
    here = Path(__file__).parent
    return (here / "loan_math.py").read_text(encoding="utf-8") + "\n" + \
        (here / "housing_math.py").read_text(encoding="utf-8") + "\n" + HOUSING_UI_PY


def _loader():
    py = page_python()
    assert "</script" not in py.lower(), "the Python source would end its <script> tag early"
    return [
        t.script(Raw(py), type="text/x-python", id="housing-py"),
        t.script(Raw(
            "document.getElementById('housing').addEventListener('submit', e => e.preventDefault());\n"
            "try {\n"
            "  const { loadMicroPython } = await import('%s');\n"
            "  const mp = await loadMicroPython({ url: '%s', stdout: () => {} });\n"
            "  mp.runPython(document.getElementById('housing-py').textContent);\n"
            "} catch (e) {\n"
            "  const s = document.getElementById('h-status');\n"
            "  s.textContent = 'The calculator could not start. Please reload the page.';\n"
            "  console.error(e);\n"
            "}\n" % (MICROPYTHON + "micropython.mjs", MICROPYTHON + "micropython.wasm")), type="module"),
    ]


def _form():
    d = DEFAULTS
    return t.form(
        t.fieldset(
            t.legend("1. The house and the lender"),
            t.div(_radio("lender", "pagibig", "Pag-IBIG Fund", True), _radio("lender", "bank", "Bank"), class_="choices"),
            t.p("Pag-IBIG lends up to ₱10 million per borrower. The two boxes below are filled in with Pag-IBIG's "
                "limits; change them if your loan officer gives other figures.", id="h-pagibig-note",
                class_="hint block-hint"),
            t.p("Each bank sets its own limits. The 80% below is only an example: type the figures from the bank's "
                "offer.", id="h-bank-note", class_="hint block-hint", hidden=True),
            t.div(
                _field("Price of the house (₱)", _num("price", str(d["price"]), placeholder="e.g. 2500000"),
                       "The selling price, or the appraised value if it is lower."),
                _field("Down payment (₱)", _num("down", str(d["down"]), placeholder="e.g. 250000"),
                       "The part of the price you pay yourself (equity)."),
                class_="field-pair",
            ),
            t.div(
                _field("Most the lender lends (% of price)", _num("ltv", str(d["ltv"]), maximum="100"),
                       "Called the loan-to-value ratio."),
                _field("Biggest loan allowed (₱, optional)", _num("cap", str(d["cap"]), placeholder="e.g. 10000000"),
                       "Leave blank if there is none."),
                class_="field-pair",
            ),
        ),
        t.fieldset(
            t.legend("2. The loan"),
            t.div(
                _field("Interest rate (% a year)", _num("rate", str(d["rate"]), maximum="50"),
                       "From the lender's offer. The rate here is only an example."),
                _field("Term (years)", _num("years", str(d["years"]), step="1", minimum="1", maximum="30"),
                       "Up to 30 years."),
                class_="field-pair",
            ),
            t.div(
                _field("Rate is fixed for", t.select([t.option(str(y) + (" year" if y == 1 else " years"), value=str(y),
                                                               selected=y == d["fixYears"]) for y in FIX_CHOICES],
                                                     id="fix", name="fix"),
                       "The fixing (repricing) period you choose."),
                _field("Rate after the fixing period (% a year, optional)", _num("rate-after", "", maximum="50",
                                                                                placeholder="e.g. 8"),
                       "No one knows it in advance. Try a higher rate to be safe."),
                class_="field-pair",
            ),
            t.div(
                _field("Mortgage redemption insurance (₱ a year)", _num("mri", "", placeholder="e.g. 6000"),
                       "MRI pays off the loan if the borrower dies. Ask the lender for the premium."),
                _field("Fire insurance (₱ a year)", _num("fire", "", placeholder="e.g. 3000"),
                       "Covers the house. Ask the lender for the premium."),
                class_="field-pair",
            ),
        ),
        t.fieldset(
            t.legend("3. Your income"),
            t.div(
                _field("Gross monthly income (₱)", _num("income", str(d["income"]), placeholder="e.g. 50000"),
                       "Before deductions. Pag-IBIG may add the income of up to three co-borrowers."),
                _field("Most of income for the house (%)", _num("ratio", str(d["ratio"]), maximum="100"),
                       "Pag-IBIG uses 35%. Ask your bank for its own figure."),
                class_="field-pair",
            ),
        ),
        t.div(t.button("Reset sample values", type="button", id="h-reset", class_="loan-btn", hidden=True),
              class_="loan-btns"),
        id="housing", class_="card rpt-form", novalidate=True,
    )


def _results():
    v = view(DEFAULTS)

    def tx(i):
        return v["text"].get(i, "—")

    def row(label, i, row_id=None, cls=None):
        return t.tr(t.th(label, scope="row"), t.td(tx(i), id=i), id=row_id, class_=cls,
                    hidden=v["hidden"].get(row_id, False) if row_id else False)

    return t.div(
        t.p(tx("h-label"), id="h-label", class_="rpt-due-label"),
        t.p(tx("h-big"), id="h-big", class_=v["class"]["h-big"]),
        t.p(v["text"].get("out-pill", ""), id="out-pill", class_="loan-pill", hidden=v["hidden"]["out-pill"]),
        t.p(tx("h-note"), id="h-note", class_="rpt-av"),
        t.p(tx("h-gap"), id="h-gap", class_="rpt-av loan-line loan-warn", hidden=v["hidden"]["h-gap"]),
        t.p("Starting the calculator…", id="h-status", class_="rpt-av loan-line"),
        t.div(
            t.div(
                t.table(
                    t.tbody(
                        row("Price of the house", "d-price"),
                        row("Down payment", "d-down"),
                        row("Loan amount", "d-loan", cls="total"),
                        row("Term", "d-term"),
                        row("Principal and interest a month", "d-pi"),
                        row("Insurance a month", "d-ins", row_id="d-ins-row"),
                        row("Monthly amortization", "d-monthly", cls="total"),
                        row("Gross income needed", "d-income"),
                        row("Total principal and interest paid", "d-total"),
                        row("Total interest", "d-interest"),
                        row("Total insurance", "d-instotal", row_id="d-instotal-row"),
                    ),
                    class_="rpt-table loan-sum",
                ),
                class_="table-scroll",
            ),
            t.p(v["text"].get("d-reprice", ""), id="d-reprice", class_="rpt-av h-para",
                hidden=v["hidden"].get("d-reprice", True)),
            t.h3("Month-by-month payments", class_="loan-sched-title"),
            t.div(
                t.table(
                    t.thead(t.tr(t.th("Month"), t.th("Payment"), t.th("Interest"), t.th("Principal"), t.th("Balance"))),
                    t.tbody(Raw(v["rows"]), id="h-sched-body"),
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
            id="h-details", hidden=v["hidden"]["h-details"],
        ),
        t.h3("What can my income carry?", class_="h-afford-title"),
        t.p(tx("h-afford"), id="h-afford", class_="rpt-av h-para"),
        class_="card rpt-result", aria_live="polite",
    )


def _explanations():
    return [
        t.h2("How it works"),
        t.ol(
            t.li(t.b("The loan. "), "Price minus down payment. If that is more than the lender lends (a share of the "
                 "price, or a peso limit), the calculator uses the smaller loan and tells you how much more down "
                 "payment you need."),
            t.li(t.b("The monthly amortization. "), "Housing loans charge interest on the balance still unpaid "
                 "(diminishing balance). Each month the interest is the balance × the yearly rate ÷ 12, and the rest "
                 "of the payment lowers the balance. Insurance premiums, if you type them, are added in twelfths."),
            t.li(t.b("The fixing period. "), "The rate stays the same only for the period you choose. After it, the "
                 "lender sets a new rate and works out a new payment on the balance left for the years left."),
            t.li(t.b("The income needed. "), "The monthly amortization ÷ the share of income allowed. At 35%, a "
                 "₱14,000 payment needs ₱40,000 gross income a month."),
            t.li(t.b("The effective rate. "), "The small label under the monthly amortization is the yearly rate "
                 "that the loan really costs you once the insurance premiums and any new rate after the fixing "
                 "period are counted. With no insurance and no change of rate, it equals the rate you typed."),
            class_="rpt-notes loan-steps",
        ),
        t.h2("Pag-IBIG housing loan rules to know"),
        t.ul(
            t.li(t.b("Loan limit. "), "Pag-IBIG raised its maximum housing loan to ₱10 million per borrower in May 2026, "
                 "from ₱6 million, payable in up to 30 years."),
            t.li(t.b("Rates. "), "The rate depends on the fixing period you choose. In May 2026 Pag-IBIG said its rates "
                 "start at 5.75% a year, and that socialized housing borrowers keep a 3% subsidized rate under the "
                 "Expanded 4PH Program. Rates change, so type the rate from your own loan offer."),
            t.li(t.b("Income. "), "Pag-IBIG's rule is that the monthly payment must not be more than 35% of the "
                 "borrower's gross monthly income (HDMF Circular No. 402). The incomes of up to three "
                 "borrowers may be added together."),
            t.li(t.b("Down payment. "), "The same circular lends up to 95% of the appraised value up to the Economic "
                 "Housing Limit, 90% above it, and 100% for socialized housing bought from a developer. The "
                 "calculator starts at 90% to be safe; ask Pag-IBIG which share applies to you."),
            t.li(t.b("Insurance. "), "Pag-IBIG's Affordable Housing Program guidelines (HDMF Circular No. 403) require "
                 "Mortgage Redemption Insurance and fire insurance, and the premiums are part of the monthly "
                 "amortization. Ask for the yearly premiums and type them in."),
            t.li(t.b("Age and savings. "), "Under the same guidelines, a borrower must have at least 24 monthly "
                 "savings, be at most 65 years old when applying and at most 70 when the loan ends."),
            class_="plain-list rpt-notes",
        ),
        t.h2("Pag-IBIG or a bank?"),
        t.p("Both lend for a house on a diminishing balance, so the calculator works the same way for both. What "
            "changes are the figures: the rate and fixing periods offered, the share of the price the lender will "
            "lend, the longest term, and how much of your income may go to the payment. Banks set these themselves "
            "and may change them, so type the figures from the bank's written offer, then compare it with a Pag-IBIG "
            "loan for the same house, term and down payment."),
        t.p("Compare the monthly amortization, the total interest, and what happens after the fixing period. A "
            "lower first rate with a short fixing period can turn into a higher payment once the rate is repriced."),
        t.h2("Worked examples"),
        t.p("The rates in these examples are for practice only. They are not any lender's offer.", class_="muted note"),
        _example(
            "1. A Pag-IBIG loan for a ₱2.5 million house",
            "Price ₱2,500,000, down payment ₱250,000 (10%), 6.25% a year fixed for 3 years, 30 years, income ₱50,000.",
            ["Loan: ₱2,500,000 − ₱250,000 = ₱2,250,000, which is 90% of the price.",
             "Monthly rate: 6.25% ÷ 12. Over 360 payments, the monthly amortization is ₱13,853.64.",
             "Income needed: ₱13,853.64 ÷ 35% = about ₱39,582 a month. ₱50,000 is enough: the payment is 27.7% of it.",
             "If the rate never changed, the total interest over 30 years would be ₱2,737,307.14."],
            "₱13,853.64 a month for the first 3 years, plus insurance."),
        _example(
            "2. What if the rate goes up after 3 years?",
            "Same loan. Rate after the fixing period: 8% a year.",
            ["After 36 payments the balance is ₱2,165,706.98.",
             "That balance is paid over the 324 months left at 8% ÷ 12 a month.",
             "New monthly amortization: ₱16,335.49, or ₱2,481.85 more. Income needed: about ₱46,673."],
            "Plan for a higher payment. A longer fixing period costs more at first but protects you from this jump."),
        _example(
            "3. A bank loan with insurance",
            "Price ₱3,000,000, down payment ₱600,000 (20%), bank lends up to 80%, 7% a year fixed for 5 years, 20 years, "
            "MRI ₱6,000 and fire insurance ₱3,000 a year, income ₱60,000.",
            ["Loan: ₱2,400,000, exactly 80% of the price.",
             "Principal and interest: ₱18,607.17 a month over 240 payments.",
             "Insurance: (₱6,000 + ₱3,000) ÷ 12 = ₱750 a month. Monthly amortization: ₱19,357.17.",
             "Income needed at 35%: about ₱55,307. ₱60,000 is enough."],
            "₱19,357.17 a month. The total interest over 20 years is ₱2,065,723.39 if the rate stays at 7%."),
        t.h2("Before you sign"),
        t.ul(
            t.li(t.b("Ask for the disclosure statement. "), "Under the Truth in Lending Act (RA 3765), the lender must "
                 "tell you in writing, before the loan is made, the finance charges and what they come to as a "
                 "yearly rate."),
            t.li(t.b("Know your fixing period. "), "Ask what rate applies after it and how the new rate is set."),
            t.li(t.b("Count the cash you need. "), "Besides the down payment there are fees and taxes for the title "
                 "and the mortgage. Ask the seller and the lender for the full list."),
            t.li(t.b("Leave room. "), "The income limit is the most a lender allows, not a target. Food, school, "
                 "transport and savings come out of the same pay."),
            class_="plain-list rpt-notes",
        ),
        t.h2("Questions people ask"),
        t.h3("Why does the calculator ask for a gross income, not my take-home pay?", class_="rpt-q"),
        t.p("Pag-IBIG's 35% rule is based on gross monthly income, the pay before deductions. Government employees "
            "who pay by salary deduction must also keep the minimum take-home pay set in the General Appropriations "
            "Act, which is ₱5,000 a month."),
        t.h3("Is a 30-year term better than 20 years?", class_="rpt-q"),
        t.p("It lowers the monthly payment but adds interest, because you owe the money longer. Try both terms here "
            "and compare the total interest."),
        t.h3("Why is my approved loan different?", class_="rpt-q"),
        t.p("The lender appraises the house, checks your papers and credit, and may lend on the appraised value "
            "instead of the price. Its own figures decide the loan; this calculator helps you plan before you apply."),
    ]


def housing_page():
    return {
        "title": "Housing Loan Calculator", "active": HOUSING_URL, "url": HOUSING_URL, "og_type": "website",
        "seo_title": "Housing Loan Calculator, Philippines: Pag-IBIG or Bank Amortization · Butch Mahinay",
        "description": "Free housing loan calculator for the Philippines: monthly amortization for a Pag-IBIG or bank "
                       "loan, down payment, fixing period and repricing, insurance, and the income you need.",
        "body": [
            loan_tabs(HOUSING_URL),
            t.p("Free tool", class_="eyebrow"),
            t.h1("Housing Loan Calculator"),
            t.p("See the monthly amortization of a Pag-IBIG or bank housing loan before you apply: how much down "
                "payment you need, what happens when the rate is repriced, and how much income the lender will look "
                "for.", class_="lead"),
            _form(),
            _results(),
            t.div(
                t.h3("Estimate only"),
                t.p("This calculator is for learning and planning only. Its figures are estimates based on what you "
                    "type. They are not a loan offer, an approval, or financial or legal advice. Pag-IBIG and each bank "
                    "set their own rates, fees, insurance premiums, rounding and loan limits, and these change."),
                t.p("Always read the lender's disclosure statement and loan documents before you sign. This site is not "
                    "connected with Pag-IBIG Fund or any bank, developer or government office."),
                class_="disclaimer rpt-disclaimer",
            ),
            *_explanations(),
            t.p("Sources: ",
                t.a("HDMF Circular No. 402 (loanable amount, capacity to pay, loan-to-value)",
                    href="https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90470", rel="noopener"),
                "; ",
                t.a("HDMF Circular No. 403 (Affordable Housing Program)",
                    href="https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90472", rel="noopener"),
                "; ",
                t.a("₱10 million loan limit and rates (Daily Tribune, May 2026)",
                    href="https://tribune.net.ph/2026/05/27/pag-ibig-sets-p10-m-housing-loan-cap", rel="noopener"),
                "; ",
                t.a("Philstar, May 29, 2026",
                    href="https://www.philstar.com/business/2026/05/29/2531214/pag-ibig-fund-raises-limit-housing-loans-p10-million",
                    rel="noopener"),
                "; General Provisions of the ",
                t.a("General Appropriations Act, FY 2026", href="https://www.dbm.gov.ph/wp-content/uploads/GAA/GAA2026/VolumeIB/GENPRO.pdf",
                    rel="noopener"),
                " (₱5,000 take-home pay); ",
                t.a("Truth in Lending Act (RA 3765)", href="https://lawphil.net/statutes/repacts/ra1963/ra_3765_1963.html",
                    rel="noopener"),
                ". Last checked " + HOUSING_CHECKED + ".", class_="muted note sources-line"),
            t.p("The figures are worked out in Python, right in your browser. Nothing you type is sent or saved.",
                class_="muted note"),
            *_loader(),
        ],
    }
