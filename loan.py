"""Salary Loan Calculator: /tools/loan-calculator/ (Butch 2026-11-26).

Estimates how much a person can borrow from a monthly salary or income without pushing the take-home pay
below a floor, or checks one loan amount. Two ways of charging interest are covered:
- add-on: interest = loan x monthly rate x months, all of it added up front, then split into equal payments;
- diminishing balance: each month's interest is charged only on what is still owed (standard amortization).

Rule used for government employees: the General Provisions of the yearly General Appropriations Act
(FY 2026, Sec. 62 "Authorized Deductions"; FY 2023, Sec. 56) say that in no case shall authorized deductions
reduce the employee's monthly net take home pay to an amount lower than Five Thousand Pesos (P5,000), and that
obligations due the BIR and contributions to PhilHealth, GSIS and HDMF are satisfied ahead of all other
obligations; the rest in the order they were incurred. COA applies the rule to LGU employees too (Manila
Bulletin, May 20, 2024: COA audit of a provincial government, citing Sec. 56 of the FY 2023 GAA).
Truth in Lending Act (RA 3765), Sec. 4: the lender must give a written statement of the finance charges and
the finance charge as a simple annual rate before the loan is made.

Written in Python, like the rest of the site (Butch 2026-11-26): loan_math.py does every computation. The
build runs it to fill the page with a worked example, and the browser runs the same file in MicroPython
(MicroPython's WebAssembly build, PyScript variant 1.29.0-6, loaded from the jsDelivr CDN) each time a number changes.
tests/test_loan.py checks it in CPython and in MicroPython.
"""

from pathlib import Path

import tags as t
from loan_math import DEFAULTS, view
from tags import Raw

LOAN_URL = "/tools/loan-calculator/"
LOAN_CHECKED = "November 2026"
# MicroPython for the web (MIT licence), PyScript build, pinned to one version on the jsDelivr CDN
MICROPYTHON = "https://cdn.jsdelivr.net/npm/@micropython/micropython-webassembly-pyscript@1.29.0-6/"
NTHP_FLOOR = 5000  # GAA General Provisions: minimum monthly net take-home pay of a government employee


# The browser side, also in Python. It runs in MicroPython after loan_math.py: it reads the
# form, asks loan_math.view() what to show, and puts it on the page. `js` is MicroPython's door to the page.
LOAN_UI_PY = r"""
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


last_who = [picked("who")]


def read_form():
    who = picked("who")
    if who != last_who[0]:  # switching sets a sensible floor; the person can still change it
        el("floor").value = "__FLOOR__" if who == "gov" else "0"
        last_who[0] = who
    return {"who": who, "gross": num("gross"), "deductions": num("deductions"), "floor": num("floor"),
            "renew": bool(el("renew").checked), "oldPay": num("old-pay"), "oldBal": num("old-bal"),
            "method": picked("method"), "rate": num("rate"), "rateUnit": el("rate-unit").value,
            "term": num("term"), "feePct": num("fee-pct"), "feeFixed": num("fee-fixed"),
            "mode": picked("mode"), "amount": num("amount"), "cap": num("cap")}


last = [None]


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
    a.download = "aumahinay-salary-loan-schedule.csv"
    doc.body.appendChild(a)
    a.click()
    a.remove()


FIELDS = {"gross": "gross", "deductions": "deductions", "floor": "floor", "oldPay": "old-pay", "oldBal": "old-bal",
          "rate": "rate", "rateUnit": "rate-unit", "term": "term", "feePct": "fee-pct", "feeFixed": "fee-fixed",
          "amount": "amount", "cap": "cap"}


def reset(*args):
    for k in FIELDS:
        d = DEFAULTS[k]
        el(FIELDS[k]).value = "" if (k in ("oldPay", "oldBal", "cap") and not d) else str(d)
    for name in ("who", "method", "mode"):
        doc.querySelector('input[name="' + name + '"][value="' + DEFAULTS[name] + '"]').checked = True
    el("renew").checked = DEFAULTS["renew"]
    last_who[0] = DEFAULTS["who"]
    el("sched-wrap").classList.add("short")
    calc()


form = el("loan")
form.addEventListener("input", calc)
form.addEventListener("change", calc)
el("sched-toggle").addEventListener("click", toggle_rows)
el("sched-csv").addEventListener("click", export_csv)
el("loan-reset").addEventListener("click", reset)
calc()
el("loan-status").hidden = True
for i in ("sched-csv", "loan-reset"):
    el(i).hidden = False
""".replace("__FLOOR__", str(NTHP_FLOOR))


def _loader():
    """Starts MicroPython in the browser, then runs loan_math.py and LOAN_UI_PY. The only JavaScript on the page
    besides the site's own menu code: it loads Python and hands it the form."""
    py = (Path(__file__).parent / "loan_math.py").read_text(encoding="utf-8") + "\n" + LOAN_UI_PY
    assert "</script" not in py.lower(), "the Python source would end its <script> tag early"
    return [
        t.script(Raw(py), type="text/x-python", id="loan-py"),
        t.script(Raw(
            "document.getElementById('loan').addEventListener('submit', e => e.preventDefault());\n"
            "try {\n"
            "  const { loadMicroPython } = await import('%s');\n"
            "  const mp = await loadMicroPython({ url: '%s', stdout: () => {} });\n"
            "  mp.runPython(document.getElementById('loan-py').textContent);\n"
            "} catch (e) {\n"
            "  const s = document.getElementById('loan-status');\n"
            "  s.textContent = 'The calculator could not start. Please reload the page.';\n"
            "  console.error(e);\n"
            "}\n" % (MICROPYTHON + "micropython.mjs", MICROPYTHON + "micropython.wasm")), type="module"),
    ]


# The three loan calculators are separate pages joined by one tab row (Butch 2026-11-26 chose
# "Separate pages, linked by tabs"). A tab shows only once its page is in the site, so no tab ever leads to a 404.
LOAN_TABS = [(LOAN_URL, "Salary loan", "loan"), ("/tools/housing-loan-calculator/", "Housing loan", "housing"),
             ("/tools/car-loan-calculator/", "Car loan", "car")]


def loan_tabs(active):
    """Tab row for the top of each loan calculator page; empty while only one of the pages exists."""
    import importlib.util
    tabs = [(u, label) for u, label, module in LOAN_TABS if importlib.util.find_spec(module)]
    if len(tabs) < 2:
        return ""
    return t.nav([t.a(label, href=u, aria_current="page" if u == active else None) for u, label in tabs],
                 class_="loan-tabs", aria_label="Loan calculators")


def _field(label, control, hint=None, row_id=None, hidden=False):
    return t.div(t.label(label, control, t.small(hint, class_="hint") if hint else None),
                 class_="field", id=row_id, hidden=hidden)


def _num(id_, value="", step="any", minimum="0", maximum=None, placeholder=None):
    return t.input(type="number", id=id_, name=id_, value=value, step=step, min=minimum, max=maximum,
                   inputmode="decimal", placeholder=placeholder)


def _radio(name, value, label, checked=False):
    return t.label(t.input(type="radio", name=name, value=value, checked=checked), " ", label, class_="choice")


def _example(title, setup, lines, result):
    return t.div(t.h3(title), t.p(t.b("What you type: "), setup), t.ul([t.li(x) for x in lines], class_="rpt-steps"),
                 t.p(t.b("Result: "), result), class_="card rpt-example")


def _form():
    return t.form(
        t.fieldset(
            t.legend("1. Your pay each month"),
            t.div(_radio("who", "gov", "Government employee", True), _radio("who", "other", "Private employee or other income"),
                  class_="choices"),
            t.div(
                _field("Gross monthly pay (₱)", _num("gross", "30000", placeholder="e.g. 30000"),
                       "Basic salary plus regular monthly allowances, such as PERA."),
                _field("Total deductions now (₱)", _num("deductions", "9000", placeholder="e.g. 9000"),
                       "Everything taken from your pay today: tax, GSIS or SSS, PhilHealth, Pag-IBIG and loans."),
                class_="field-pair",
            ),
            _field("Lowest take-home pay to keep (₱)", _num("floor", str(NTHP_FLOOR)), None),
            t.p("For government employees the law sets ₱5,000 a month as the lowest net take-home pay after all "
                "deductions. You may type a higher amount to leave room for your family's needs.",
                id="floor-gov", class_="hint block-hint"),
            t.p("Type the least you need each month after loan payments. Many lenders also look at how much of your "
                "pay already goes to debts, so a safe amount is better than zero.",
                id="floor-other", class_="hint block-hint", hidden=True),
            t.label(t.input(type="checkbox", id="renew", name="renew"), " ",
                    "This loan will pay off an old loan (renewal)", class_="choice prior-paid"),
            t.div(
                _field("Old loan's monthly payment (₱)", _num("old-pay", "", placeholder="e.g. 3000"),
                       "This stops once the old loan is paid off, so it frees up room."),
                _field("Old loan's balance (₱)", _num("old-bal", "", placeholder="e.g. 40000"),
                       "Taken out of the new loan before you get the cash."),
                id="renew-rows", class_="field-pair", hidden=True,
            ),
        ),
        t.fieldset(
            t.legend("2. The loan"),
            t.p("How is the interest charged?", class_="field-title"),
            t.div(_radio("method", "addon", "Add-on rate", True), _radio("method", "dim", "Diminishing balance"),
                  class_="choices"),
            t.p("Look at the loan offer or disclosure statement. \"Add-on\" means interest on the full amount for the "
                "whole term; \"diminishing\" means interest only on what is still unpaid. See the explanation below.",
                class_="hint block-hint"),
            t.div(
                _field("Interest rate (%)", _num("rate", "1", maximum="100")),
                _field("Rate is per", t.select(t.option("Month", value="month"), t.option("Year", value="year"),
                                               id="rate-unit", name="rate-unit")),
                class_="field-pair",
            ),
            t.div(
                _field("Term (months)", _num("term", "36", step="1", minimum="1", maximum="360"),
                       "For example 12, 24, 36 or 60."),
                _field("Fees taken from the loan (%)", _num("fee-pct", "0", maximum="100"),
                       "Service, processing or insurance fees, if given as a percentage."),
                class_="field-pair",
            ),
            _field("Other fixed fees (₱)", _num("fee-fixed", "0"), "Such as a notarial or documentary fee, if any."),
        ),
        t.fieldset(
            t.legend("3. What do you want to know?"),
            t.div(_radio("mode", "max", "How much can I borrow?", True), _radio("mode", "check", "Can I afford this amount?"),
                  class_="choices"),
            _field("Amount you want to borrow (₱)", _num("amount", "100000", placeholder="e.g. 100000"), None,
                   row_id="amount-row", hidden=True),
            _field("Most the lender allows (₱, optional)", _num("cap", "", placeholder="e.g. 500000"),
                   "Some lenders cap the loan, for example at a number of months of your salary. Leave blank if you do not know."),
        ),
        t.div(t.button("Reset sample values", type="button", id="loan-reset", class_="loan-btn", hidden=True),
              class_="loan-btns"),
        id="loan", class_="card rpt-form", novalidate=True,
    )


def _results():
    """The results card, already filled in by loan_math (CPython, at build time) for the example values in the
    form, so the page reads complete before MicroPython starts; the browser then updates it as you type."""
    v = view(DEFAULTS)

    def tx(i):
        return v["text"].get(i, "—")

    def row(label, i, row_id=None, cls=None):
        return t.tr(t.th(label, scope="row"), t.td(tx(i), id=i), id=row_id, class_=cls,
                    hidden=v["hidden"].get(row_id, False) if row_id else False)

    return t.div(
        t.p("Take-home pay now ", t.b(tx("out-net"), id="out-net"), class_="rpt-av"),
        t.p("Room for a new loan payment ", t.b(tx("out-room"), id="out-room"), class_="rpt-av"),
        t.p(tx("out-label"), id="out-label", class_="rpt-due-label"),
        t.p(tx("out-big"), id="out-big", class_=v["class"]["out-big"]),
        t.p(v["text"].get("out-pill", ""), id="out-pill", class_="loan-pill", hidden=v["hidden"]["out-pill"]),
        t.p(tx("out-note"), id="out-note", class_="rpt-av"),
        t.p("Starting the calculator…", id="loan-status", class_="rpt-av loan-line"),
        t.div(
            t.div(
                t.table(
                    t.tbody(
                        row("Loan amount", "d-loan"),
                        row("Monthly payment", "d-pay"),
                        row("Per payday (paid twice a month)", "d-payday"),
                        row("Total you will pay back", "d-total"),
                        row("Total interest", "d-interest"),
                        row("Fees taken out", "d-fees"),
                        row("Old loan paid off", "d-old", row_id="d-old-row"),
                        row("Cash in your hand", "d-cash", cls="total"),
                    ),
                    class_="rpt-table loan-sum",
                ),
                class_="table-scroll",
            ),
            t.div(
                t.table(t.tbody(row("Take-home pay after the loan", "d-netafter", row_id="d-netafter-row",
                                    cls=v["class"].get("d-netafter-row", "total")))),
                class_="table-scroll loan-after",
            ),
            t.p(t.b("True cost (effective rate): "), t.span(tx("d-eir"), id="d-eir"), class_="rpt-av loan-line"),
            t.p(v["text"].get("d-compare", ""), id="d-compare", class_="rpt-av loan-line",
                hidden=v["hidden"].get("d-compare", True)),
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
            id="loan-details", hidden=v["hidden"]["loan-details"],
        ),
        class_="card rpt-result", aria_live="polite",
    )


def _explanations():
    return [
        t.h2("How it works"),
        t.ol(
            t.li(t.b("Your take-home pay now. "), "Gross pay minus everything already deducted. This is what reaches "
                 "your account or envelope today."),
            t.li(t.b("Room for a new payment. "), "Take-home pay minus the lowest amount you must keep. If the new "
                 "loan pays off an old one, the old loan's monthly payment is added back, because it will stop."),
            t.li(t.b("The biggest loan that fits. "), "The calculator finds the loan whose monthly payment uses up "
                 "that room and no more, for the rate, method and term you typed. It then rounds the amount down, "
                 "since lenders lend round figures."),
            t.li(t.b("Cash in your hand. "), "Fees and any old balance are taken out of the loan first, so the cash "
                 "you receive is less than the loan amount. You still pay back the full loan."),
            class_="rpt-notes loan-steps",
        ),
        t.h2("Add-on rate or diminishing balance?"),
        t.p("Two loans can both say \"1% a month\" and still cost very different amounts. The difference is what the "
            "1% is charged on."),
        t.p(t.b("Add-on rate. "), "Interest is computed on the full loan for the whole term, added on top, and the "
            "total is divided into equal payments. On a ₱100,000 loan at 1% a month for 36 months, the interest is "
            "₱100,000 × 1% × 36 = ₱36,000. You pay ₱136,000 in 36 payments of ₱3,777.78. You keep paying interest on "
            "the full ₱100,000 even in the last month, when you owe very little."),
        t.p(t.b("Diminishing balance. "), "Each month's interest is charged only on what you still owe, so the "
            "interest gets smaller as you pay. The same ₱100,000 at 1% a month for 36 months costs ₱3,321.43 a month, "
            "or ₱19,571.48 in interest, a little over half the add-on interest."),
        t.p("To compare offers fairly, look at the effective rate. The calculator shows it below the results: an add-on "
            "rate of 1% a month for 36 months works out to about 1.77% a month on a diminishing balance. When fees are taken from the "
            "loan, the effective rate goes up again, because you pay interest on money you never received."),
        t.h2("The ₱5,000 take-home pay rule"),
        t.p("The General Provisions of the national budget law, the General Appropriations Act, allow deductions from "
            "a government employee's salary for taxes, GSIS, PhilHealth and Pag-IBIG (HDMF), and for loans from "
            "authorized lenders such as government financial institutions, accredited banks and employee "
            "cooperatives. They add that in no case shall these deductions reduce the employee's monthly net "
            "take-home pay below ₱5,000."),
        t.p("The same provision sets the order of payment: the BIR, PhilHealth, GSIS and Pag-IBIG are paid first, and "
            "the other obligations in the order they were incurred. That is why a new loan is the one that gets "
            "refused when the pay is too thin: the older deductions come ahead of it. The Commission on Audit has also "
            "flagged local governments whose employees took home less than ₱5,000 because of loan payments, so the "
            "rule covers local government employees as well."),
        t.p("₱5,000 is the floor, not a target. A payslip that leaves only ₱5,000 a month is hard to live on. Many "
            "employees set their own floor higher, and the calculator lets you do that."),
        t.h2("Worked examples"),
        _example(
            "1. How much can I borrow? (add-on rate)",
            "Government employee. Gross pay ₱30,000, deductions now ₱9,000. Floor ₱5,000. Add-on 1% a month, 36 months, "
            "no fees.",
            ["Take-home pay now: ₱30,000 − ₱9,000 = ₱21,000.",
             "Room for a new payment: ₱21,000 − ₱5,000 = ₱16,000 a month.",
             "Biggest loan: ₱16,000 × 36 ÷ (1 + 1% × 36) = ₱576,000 ÷ 1.36 = ₱423,529.41, rounded down to ₱423,000.",
             "Monthly payment: ₱423,000 × 1.36 ÷ 36 = ₱15,980, which leaves ₱5,020 take-home pay."],
            "About ₱423,000, if the lender's own limit allows it. Borrowing to the last peso of the room is rarely wise."),
        _example(
            "2. The same pay with a diminishing rate",
            "Same pay and floor. Diminishing balance, 12% a year (1% a month), 36 months, no fees.",
            ["Room for a new payment is still ₱16,000.",
             "Because interest falls as you pay, the same ₱16,000 a month carries a bigger loan: ₱481,720.08, "
             "rounded down to ₱481,000.",
             "Monthly payment: ₱15,976.08."],
            "About ₱481,000, or ₱58,000 more than with the add-on rate, for almost the same monthly payment."),
        _example(
            "3. Can I afford ₱150,000 with fees and a renewal?",
            "Gross pay ₱28,000, deductions now ₱20,000 (including an old loan of ₱4,000 a month with ₱50,000 left). "
            "Renewal ticked. Add-on 1.5% a month, 24 months, fees 3%.",
            ["Take-home pay now: ₱8,000. The old ₱4,000 payment stops, so the room is ₱8,000 + ₱4,000 − ₱5,000 = ₱7,000.",
             "New payment on ₱150,000: ₱150,000 × (1 + 1.5% × 24) ÷ 24 = ₱8,500. Take-home pay after: "
             "₱12,000 − ₱8,500 = ₱3,500, which is ₱1,500 below the floor.",
             "The most that fits is about ₱123,000 (₱6,970.00 a month).",
             "Cash in hand on ₱123,000: ₱123,000 − ₱3,690 fees − ₱50,000 old balance = ₱69,310."],
            "Too big. Borrowing ₱123,000 instead keeps the take-home pay above ₱5,000, but only about ₱69,000 reaches "
            "your hand."),
        t.h2("Before you sign"),
        t.ul(
            t.li(t.b("Ask for the disclosure statement. "), "Under the Truth in Lending Act (RA 3765), the lender must "
                 "tell you in writing, before the loan is made, the finance charges and what they come to as a yearly "
                 "rate. Compare that with the effective rate here."),
            t.li(t.b("Count every fee. "), "Service fees, insurance and advance interest taken out of the loan lower "
                 "the cash you receive, but not what you pay back."),
            t.li(t.b("Watch renewals. "), "A renewal pays off the old balance first. A big new loan can leave little "
                 "cash, while the payments start over for the full term."),
            t.li(t.b("Leave room for changes. "), "Higher contributions or a tax adjustment late in the year can cut "
                 "your take-home pay. A loan sized to the last peso may push you below the floor later."),
            t.li(t.b("Your agency decides too. "), "Your office checks your take-home pay before it signs a payroll "
                 "deduction, and lenders have their own limits on age, length of service and loan size."),
            class_="plain-list rpt-notes",
        ),
        t.h2("Questions people ask"),
        t.h3("Why is the approved amount different from the calculator's?", class_="rpt-q"),
        t.p("Lenders have their own limits, such as a number of months of salary, your length of service, your age, "
            "or the years left before retirement. Some also count expected deductions differently or add insurance. "
            "The calculator shows what your take-home pay can carry; the lender's own rules may give a lower amount."),
        t.h3("My pay comes twice a month. Does the ₱5,000 apply to each payday?", class_="rpt-q"),
        t.p("The rule speaks of the monthly net take-home pay, so the calculator works by month. It also shows the "
            "payment per payday, half of the monthly payment, because most government payrolls split deductions "
            "between the two paydays."),
        t.h3("Where do I find my total deductions?", class_="rpt-q"),
        t.p("On your latest payslip. Gross pay minus total deductions is your net pay. If a loan will end soon, you may "
            "leave its payment out of the deductions, but only if it really ends before the new loan starts."),
        t.h3("Is a lower monthly payment always better?", class_="rpt-q"),
        t.p("No. A longer term lowers the payment but adds interest. Try 24 and 36 months in the calculator and compare "
            "the total interest."),
    ]


def loan_page():
    return {
        "title": "Salary Loan Calculator", "active": LOAN_URL, "url": LOAN_URL, "og_type": "website",
        "seo_title": "Salary Loan Calculator, Philippines: How Much Can I Borrow? · Butch Mahinay",
        "description": "Free salary loan calculator for the Philippines: how much you can borrow from your pay while "
                       "keeping the ₱5,000 minimum take-home pay, with add-on and diminishing rates, fees and renewals.",
        "body": [
            loan_tabs(LOAN_URL),
            t.p("Free tool", class_="eyebrow"),
            t.h1("Salary Loan Calculator"),
            t.p("Find out how much you can borrow from your salary before you go to the bank, and what the loan will "
                "really cost. Made for government employees, who must keep at least ₱5,000 take-home pay a month, "
                "and useful for anyone with a regular income.", class_="lead"),
            _form(),
            _results(),
            t.div(
                t.h3("Estimate only"),
                t.p("This calculator is for learning and planning only. Its figures are estimates based on what you "
                    "type. They are not a loan offer, an approval, or financial or legal advice. Each lender sets its "
                    "own rates, fees, rounding and loan limits, and your agency's payroll office applies the deduction "
                    "rules to your actual payslip."),
                t.p("Always read the lender's disclosure statement and ask your payroll or human resource office "
                    "before you sign. This site is not connected with any bank, lender or government office."),
                class_="disclaimer rpt-disclaimer",
            ),
            *_explanations(),
            t.p("Sources: General Provisions of the ",
                t.a("General Appropriations Act, FY 2026", href="https://www.dbm.gov.ph/wp-content/uploads/GAA/GAA2026/VolumeIB/GENPRO.pdf", rel="noopener"),
                ", Authorized Deductions; ",
                t.a("COA report on take-home pay below ₱5,000 (Manila Bulletin)", href="https://mb.com.ph/2024/5/20/coa-warns-lg-us-vs-paying-employees-less-than-p5-000-net-monthly-take-home-salary", rel="noopener"),
                "; ",
                t.a("Truth in Lending Act (RA 3765)", href="https://lawphil.net/statutes/repacts/ra1963/ra_3765_1963.html", rel="noopener"),
                ", Sec. 4. Last checked " + LOAN_CHECKED + ".", class_="muted note sources-line"),
            t.p("The figures are worked out in Python, right in your browser. Nothing you type is sent or saved.", class_="muted note"),
            *_loader(),
        ],
    }
