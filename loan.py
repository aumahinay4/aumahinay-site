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

The math lives in LOAN_MATH (plain JavaScript, no page code) so tests/test_loan.py can run it in Node and
check it against an independent Python version.
"""

import tags as t
from tags import Raw

LOAN_URL = "/tools/loan-calculator/"
LOAN_CHECKED = "November 2026"
NTHP_FLOOR = 5000  # GAA General Provisions: minimum monthly net take-home pay of a government employee

# Pure math, shared by the page and the tests. Rates are decimals per month (1% a month = 0.01).
LOAN_MATH = r"""
var LoanMath = (function () {
  function r2(n) { return Math.round((n + Number.EPSILON) * 100) / 100; }
  // equal monthly payment for a loan of p over n months
  function payment(p, rate, n, method) {
    if (p <= 0 || n <= 0) return 0;
    if (method === 'addon') return p * (1 + rate * n) / n;
    if (rate === 0) return p / n;
    return p * rate / (1 - Math.pow(1 + rate, -n));
  }
  // the largest loan whose monthly payment is at most a
  function principal(a, rate, n, method) {
    if (a <= 0 || n <= 0) return 0;
    if (method === 'addon') return a * n / (1 + rate * n);
    if (rate === 0) return a * n;
    return a * (1 - Math.pow(1 + rate, -n)) / rate;
  }
  // monthly rate that makes n payments of a worth exactly `cash` today (the real cost of the loan)
  function effectiveRate(cash, a, n) {
    if (cash <= 0 || a <= 0 || n <= 0 || a * n <= cash) return 0;
    var lo = 0, hi = 1;
    for (var k = 0; k < 200; k++) {
      var mid = (lo + hi) / 2;
      if (principal(a, mid, n, 'dim') > cash) lo = mid; else hi = mid;
    }
    return (lo + hi) / 2;
  }
  // round a loan amount down to a step (lenders lend round figures)
  function roundDown(x, step) { return x <= 0 ? 0 : Math.floor(x / step + 1e-9) * step; }
  // month-by-month table; add-on interest is spread evenly (straight line), the way most add-on loans show it
  function schedule(p, rate, n, method) {
    var a = r2(payment(p, rate, n, method)), bal = p, rows = [];
    var addonInt = method === 'addon' ? r2(p * rate) : 0;
    for (var m = 1; m <= n; m++) {
      var interest = method === 'addon' ? addonInt : r2(bal * rate);
      var prin = r2(a - interest);
      var pay = a;
      if (m === n) { prin = r2(bal); pay = r2(prin + interest); }  // last payment absorbs the centavos
      bal = r2(bal - prin);
      rows.push({ month: m, payment: pay, interest: interest, principal: prin, balance: Math.max(bal, 0) });
    }
    return rows;
  }
  // everything the page shows, from plain numbers
  // inp: {gross, deductions, floor, freed, oldBalance, method, rate (per month), n, feePct, feeFixed, mode, amount, cap}
  function compute(inp) {
    var out = {};
    out.netNow = r2(inp.gross - inp.deductions);
    out.room = r2(Math.max(out.netNow + inp.freed - inp.floor, 0));  // most the new loan's payment can be
    var exact = principal(out.room, inp.rate, inp.n, inp.method);
    out.maxExact = r2(exact);
    var step = exact >= 10000 ? 1000 : 100;
    var maxLoan = roundDown(exact, step);
    // make sure the rounded payment of the rounded loan still fits
    while (maxLoan > 0 && r2(payment(maxLoan, inp.rate, inp.n, inp.method)) > out.room) maxLoan -= step;
    out.capped = false;
    if (inp.cap > 0 && maxLoan > inp.cap) { maxLoan = inp.cap; out.capped = true; }
    out.maxLoan = maxLoan;
    var loan = inp.mode === 'check' ? inp.amount : maxLoan;
    out.loan = loan;
    out.pay = r2(payment(loan, inp.rate, inp.n, inp.method));
    out.perPayday = r2(out.pay / 2);
    out.totalPaid = r2(out.pay * inp.n);
    out.interest = r2(out.totalPaid - loan);
    out.fees = loan > 0 ? r2(loan * inp.feePct / 100 + inp.feeFixed) : 0;
    out.cash = r2(loan - out.fees - (loan > 0 ? inp.oldBalance : 0));
    out.netAfter = r2(out.netNow + (loan > 0 ? inp.freed : 0) - out.pay);
    out.fits = out.netAfter >= inp.floor - 0.005;
    out.short = out.fits ? 0 : r2(inp.floor - out.netAfter);
    var e = effectiveRate(loan - out.fees, out.pay, inp.n);
    out.eirMonth = e;
    out.eirYear = e * 12;
    out.sameAsDim = inp.method === 'addon' ? effectiveRate(loan, out.pay, inp.n) : inp.rate;
    return out;
  }
  return { r2: r2, payment: payment, principal: principal, effectiveRate: effectiveRate, roundDown: roundDown,
           schedule: schedule, compute: compute };
})();
"""

LOAN_SCRIPT = r"""
(function () {
  var f = document.getElementById('loan');
  if (!f) return;
  var $ = function (id) { return document.getElementById(id); };
  var peso = function (n) { return (n < 0 ? '−' : '') + '₱' + Math.abs(n).toLocaleString('en-PH', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var peso0 = function (n) { return '₱' + Math.round(n).toLocaleString('en-PH'); };
  var pct = function (x, d) { return (x * 100).toLocaleString('en-PH', { maximumFractionDigits: d === undefined ? 2 : d }) + '%'; };
  var num = function (id) { var v = parseFloat(String($(id).value).replace(/,/g, '')); return isFinite(v) && v > 0 ? v : 0; };
  var val = function (name) { var c = f.querySelector('input[name="' + name + '"]:checked'); return c ? c.value : ''; };
  var lastWho = val('who');

  function calc() {
    var who = val('who');
    if (who !== lastWho) {  // switching sets a sensible floor; the person can still change it
      $('floor').value = who === 'gov' ? '__FLOOR__' : '0';
      lastWho = who;
    }
    $('floor-gov').hidden = who !== 'gov';
    $('floor-other').hidden = who === 'gov';
    var mode = val('mode');
    $('amount-row').hidden = mode !== 'check';
    var renew = $('renew').checked;
    $('renew-rows').hidden = !renew;
    var method = val('method');
    var rate = num('rate') / 100;
    if ($('rate-unit').value === 'year') rate = rate / 12;
    var n = Math.round(num('term'));
    var inp = {
      gross: num('gross'), deductions: num('deductions'), floor: num('floor'),
      freed: renew ? num('old-pay') : 0, oldBalance: renew ? num('old-bal') : 0,
      method: method, rate: rate, n: n, feePct: num('fee-pct'), feeFixed: num('fee-fixed'),
      mode: mode, amount: num('amount'), cap: num('cap')
    };
    var o = LoanMath.compute(inp);
    $('out-net').textContent = peso(o.netNow);
    $('out-room').textContent = peso(o.room);
    var msg = '';
    if (!inp.gross) {
      $('out-label').textContent = 'Type your monthly pay to begin';
      $('out-big').textContent = '—';
    } else if (!n) {
      $('out-label').textContent = 'Type the number of months';
      $('out-big').textContent = '—';
    } else if (mode === 'max') {
      $('out-label').textContent = 'You may borrow up to about';
      $('out-big').textContent = peso0(o.maxLoan);
      if (o.maxLoan <= 0) msg = 'Your take-home pay is already at or below the lowest amount you set, so there is no room for a new loan payment.';
      else if (o.capped) msg = 'This is the lender\'s limit you typed. Your pay alone would allow about ' + peso0(LoanMath.roundDown(o.maxExact, 1000)) + '.';
      else msg = 'Rounded down to a round figure. The exact most is ' + peso(o.maxExact) + '.';
    } else {
      $('out-label').textContent = 'Monthly payment for ' + peso0(o.loan);
      $('out-big').textContent = peso(o.pay);
      if (!o.loan) msg = 'Type the amount you want to borrow.';
      else if (o.fits) msg = 'This loan fits: your take-home pay stays at or above ' + peso(inp.floor) + '.';
      else msg = 'This loan is too big: your take-home pay would fall ' + peso(o.short) + ' below ' + peso(inp.floor) + '. The most that fits is about ' + peso0(o.maxLoan) + '.';
    }
    $('out-note').textContent = msg;
    $('out-big').className = 'rpt-due' + (mode === 'check' && o.loan && !o.fits ? ' loan-bad' : '');
    var show = inp.gross && n && o.loan > 0;
    $('loan-details').hidden = !show;
    if (!show) return;
    $('d-loan').textContent = peso(o.loan);
    $('d-pay').textContent = peso(o.pay);
    $('d-payday').textContent = peso(o.perPayday);
    $('d-total').textContent = peso(o.totalPaid);
    $('d-interest').textContent = peso(o.interest);
    $('d-fees').textContent = o.fees ? '−' + peso(o.fees) : peso(0);
    $('d-old-row').hidden = !inp.oldBalance;
    $('d-old').textContent = '−' + peso(inp.oldBalance);
    $('d-cash').textContent = peso(o.cash);
    $('d-netafter').textContent = peso(o.netAfter);
    $('d-netafter-row').className = o.fits ? 'total' : 'total loan-bad';
    $('d-eir').textContent = o.eirMonth ? pct(o.eirMonth) + ' a month, about ' + pct(o.eirYear, 1) + ' a year' : 'none';
    var cmp = '';
    if (method === 'addon' && o.sameAsDim > rate + 1e-9)
      cmp = 'An add-on rate of ' + pct(rate) + ' a month costs the same as a diminishing rate of about ' + pct(o.sameAsDim) + ' a month (' + pct(o.sameAsDim * 12, 1) + ' a year), before fees.';
    $('d-compare').textContent = cmp;
    $('d-compare').hidden = !cmp;
    var rows = LoanMath.schedule(o.loan, rate, n, method), html = '';
    rows.forEach(function (r) {
      html += '<tr><th scope="row">' + r.month + '</th><td>' + peso(r.payment) + '</td><td>' + peso(r.interest) +
              '</td><td>' + peso(r.principal) + '</td><td>' + peso(r.balance) + '</td></tr>';
    });
    $('sched-body').innerHTML = html;
  }
  f.addEventListener('input', calc);
  f.addEventListener('change', calc);
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  calc();
})();
""".replace("__FLOOR__", str(NTHP_FLOOR))


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
        id="loan", class_="card rpt-form", novalidate=True,
    )


def _results():
    return t.div(
        t.p("Take-home pay now ", t.b("—", id="out-net"), class_="rpt-av"),
        t.p("Room for a new loan payment ", t.b("—", id="out-room"), class_="rpt-av"),
        t.p("—", id="out-label", class_="rpt-due-label"),
        t.p("—", id="out-big", class_="rpt-due"),
        t.p("", id="out-note", class_="rpt-av"),
        t.div(
            t.div(
                t.table(
                    t.tbody(
                        t.tr(t.th("Loan amount", scope="row"), t.td(id="d-loan")),
                        t.tr(t.th("Monthly payment", scope="row"), t.td(id="d-pay")),
                        t.tr(t.th("Per payday (paid twice a month)", scope="row"), t.td(id="d-payday")),
                        t.tr(t.th("Total you will pay back", scope="row"), t.td(id="d-total")),
                        t.tr(t.th("Total interest", scope="row"), t.td(id="d-interest")),
                        t.tr(t.th("Fees taken out", scope="row"), t.td(id="d-fees")),
                        t.tr(t.th("Old loan paid off", scope="row"), t.td(id="d-old"), id="d-old-row"),
                        t.tr(t.th("Cash in your hand", scope="row"), t.td(id="d-cash"), class_="total"),
                    ),
                    class_="rpt-table loan-sum",
                ),
                class_="table-scroll",
            ),
            t.div(
                t.table(t.tbody(t.tr(t.th("Take-home pay after the loan", scope="row"), t.td(id="d-netafter"),
                                     id="d-netafter-row"))),
                class_="table-scroll loan-after",
            ),
            t.p(t.b("True cost (effective rate): "), t.span("—", id="d-eir"), class_="rpt-av loan-line"),
            t.p("", id="d-compare", class_="rpt-av loan-line"),
            t.details(
                t.summary("Month-by-month payments"),
                t.div(
                    t.table(
                        t.thead(t.tr(t.th("Month"), t.th("Payment"), t.th("Interest"), t.th("Principal"), t.th("Balance"))),
                        t.tbody(id="sched-body"),
                        class_="rpt-table",
                    ),
                    class_="table-scroll",
                ),
                class_="loan-sched",
            ),
            id="loan-details",
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
            t.p("Figures are worked out in your browser and nothing you type is sent or saved.", class_="muted note"),
            t.script(Raw(LOAN_MATH + LOAN_SCRIPT)),
        ],
    }
