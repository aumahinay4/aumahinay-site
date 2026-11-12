"""Real Property Tax (RPT) calculator: /tools/rpt-calculator/ (Butch 2026-11-09).

Computes the basic RPT and the Special Education Fund (SEF) tax, the discount or the interest by
date of payment (quarter by quarter), and how the money is shared among the province, municipality
and barangay (or city and barangays) and the school boards.

National rules, Republic Act No. 7160 (Local Government Code of 1991):
- Sec. 218: assessed value = market value x assessment level (levels set by ordinance).
- Sec. 233: basic RPT rate, province up to 1%, city or Metro Manila municipality up to 2%.
- Sec. 235: additional 1% for the Special Education Fund.
- Sec. 250: may be paid in four quarterly installments, due March 31, June 30, Sept. 30, Dec. 31.
- Sec. 251: discount of up to 20% for advance or prompt payment, as set by ordinance.
- Sec. 255: interest of 2% a month on unpaid tax, for at most 36 months (72%).
- Sec. 271: basic RPT including interest: province 35%, municipality 40%, barangay 25%;
            city 70%, barangays 30% (half to the barangay where the property is, half shared
            equally by all barangays of the city).
- Sec. 272: SEF to the local school boards; in provinces, split equally between the
            provincial and municipal school boards.
RA 12001 (2024), Sec. 29: first-year increase after a new schedule of market values capped at 6%.

Quezon Province, Provincial Ordinance No. 2022-010 (Revised Revenue Code of 2022), from Butch's Drive:
- Sec. 25 assessment levels; Sec. 39 basic 1%; Sec. 40 SEF 1%; Sec. 43 four equal installments;
- Sec. 44 discounts: 10% if paid on or before the deadlines; 15% if paid in full on or before
  September 30 for one year in advance; 20% for two or more years in advance; only for properties
  without any delinquency;
- Sec. 45 sharing 35/40/25 and SEF split equally; Sec. 47 interest 2% a month "on the unpaid amount
  or a fraction thereof", at most 36 months. Quezon practice (Butch 2026-11-12): counted BY QUARTER, each quarter
  or part of a quarter after the due date = 3 months = 6%; e.g. Q3 paid any day Oct 1 - Dec 31 carries 6%.
"""

import json

import tags as t
from tags import Raw

RPT_URL = "/tools/rpt-calculator/"
RPT_CHECKED = "November 2026"
RPT_GUIDE_URL = "/blog/how-to-use-the-rpt-calculator/"  # step-by-step guide post (Butch 2026-11-11)

# Quezon Provincial Revenue Code of 2022, Sec. 25 (levels in %; building brackets: [up to market value, level])
QUEZON_LEVELS = {
    "land": {"Residential": 5, "Agricultural": 15, "Commercial": 17, "Industrial": 30},
    "building": {
        "Residential": [[175000, 0], [300000, 5], [500000, 10], [750000, 15], [1000000, 20], [2000000, 25],
                        [5000000, 30], [10000000, 35], [None, 40]],
        "Agricultural": [[300000, 20], [500000, 25], [750000, 30], [1000000, 35], [2000000, 40], [None, 45]],
        "Commercial or industrial": [[300000, 25], [500000, 30], [750000, 35], [1000000, 40], [2000000, 45],
                                     [5000000, 50], [10000000, 55], [None, 60]],
    },
    "machinery": {"Agricultural": 40, "Residential": 50, "Commercial": 80, "Industrial": 80},
    "special": {"Cultural": 15, "Scientific": 15, "Hospital": 15, "Local water district": 10,
                "Government water or power corporation": 10},
}

RPT_SCRIPT = r"""
(function () {
  var f = document.getElementById('rpt');
  if (!f) return;
  var LEVELS = __LEVELS__;
  var $ = function (id) { return document.getElementById(id); };
  var peso = function (n) { return (n < 0 ? '−' : '') + '₱' + Math.abs(n).toLocaleString('en-PH', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var r2 = function (n) { return Math.round((n + Number.EPSILON) * 100) / 100; };
  var num = function (id) { var v = parseFloat(String($(id).value).replace(/,/g, '')); return isFinite(v) && v > 0 ? v : 0; };
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var DUE = [[2, 31], [5, 30], [8, 30], [11, 31]];  // March 31, June 30, September 30, December 31

  // today's date in the Philippines, as the default payment date
  var ph = new Date(Date.now() + 8 * 3600 * 1000);
  var today = ph.toISOString().slice(0, 10);
  if (!$('paydate').value) $('paydate').value = today;
  $('todaydate').value = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
    'November', 'December'][ph.getUTCMonth()] + ' ' + ph.getUTCDate() + ', ' + ph.getUTCFullYear();
  if (!$('taxyear').value) $('taxyear').value = ph.getUTCFullYear();

  function fillClasses() {
    var kind = $('kind').value, sel = $('klass'), keep = sel.value;
    sel.innerHTML = '';
    Object.keys(LEVELS[kind]).forEach(function (k) { var o = document.createElement('option'); o.value = k; o.textContent = k; sel.appendChild(o); });
    if (LEVELS[kind][keep] !== undefined) sel.value = keep;
  }
  function quezonLevel(mv) {
    var v = LEVELS[$('kind').value][$('klass').value];
    if (typeof v === 'number') return v;
    for (var i = 0; i < v.length; i++) if (v[i][0] === null || mv <= v[i][0]) return v[i][1];
    return 0;
  }
  var lastLgu = null, lastLevelKey = null;

  function calc() {
    // a payment is never ₱0.00 (Butch 2026-11-12): when all four quarters of the tax year are paid, the next payment
    // is for the following year, so move to it and start its quarters as "Not paid"
    var rolled = '';
    if ([1, 2, 3, 4].every(function (q) { return $('qs' + q).value === 'paid'; })) {
      var y0 = Math.floor(num('taxyear')) || ph.getUTCFullYear();
      $('taxyear').value = y0 + 1;
      [1, 2, 3, 4].forEach(function (q) { $('qs' + q).value = 'now'; });
      rolled = 'Tax year ' + y0 + ' is fully paid, so this shows the next payment: tax year ' + (y0 + 1) + '.';
    }
    var lgu = f.lgu.value, city = lgu === 'city', qz = lgu === 'quezon';
    if (lgu !== lastLgu) { $('basic-rate').value = city ? '2' : '1'; lastLgu = lgu; }
    $('brgy-count-row').hidden = !city;
    var useMv = f.basis.value === 'mv';
    $('mv-rows').hidden = !useMv; $('av-row').hidden = useMv;
    $('qz-class').hidden = !(useMv && qz);
    var mv = num('mv');
    if (useMv && qz) {
      var key = $('kind').value + '|' + $('klass').value + '|' + mv;
      if (key !== lastLevelKey) { $('level').value = quezonLevel(mv); lastLevelKey = key; }
    }
    var av = useMv ? r2(mv * Math.min(num('level'), 100) / 100) : num('av');
    var bRate = Math.min(num('basic-rate'), city ? 2 : 1), sRate = Math.min(num('sef-rate'), 1);
    var basic = r2(av * bRate / 100), sef = r2(av * sRate / 100);

    // payment date and tax year
    $('disc-row').hidden = qz; $('qz-disc').hidden = !qz;
    var year = Math.floor(num('taxyear')) || ph.getUTCFullYear();
    var pd = ($('paydate').value || today).split('-').map(Number);  // [y, m, d]
    var payIdx = pd[0] * 12 + (pd[1] - 1);
    var payNum = pd[0] * 10000 + pd[1] * 100 + pd[2];
    // each quarter is one fourth of the year's tax; the last quarter takes any centavo left over
    var qb = r2(basic / 4), qs = r2(sef / 4);
    var priorClear = $('prior-paid').checked;
    var quarters = [], anyLate = false, unpaidLate = [], lateNow = [], fullYear = true, anyNow = false;
    for (var q = 0; q < 4; q++) {
      var dueNum = year * 10000 + (DUE[q][0] + 1) * 100 + DUE[q][1];
      var b = q < 3 ? qb : r2(basic - 3 * qb), s = q < 3 ? qs : r2(sef - 3 * qs);
      var st = $('qs' + (q + 1)).value;  // now = paying now, paid = paid already, later = not paying now
      var past = payNum > dueNum, months = 0;
      if (st === 'later') fullYear = false;
      if (st === 'now') anyNow = true;
      if (st === 'now' && past) {  // late: every month or part of a month after the due date counts, up to 36
        months = Math.max(payIdx - (year * 12 + DUE[q][0]), 1);
        if (qz) months = Math.ceil(months / 3) * 3;  // Quezon practice: by quarter, a part of a quarter counts as a whole quarter (6%)
        months = Math.min(months, 36);
        anyLate = true; lateNow.push('Q' + (q + 1));
      }
      if (st === 'later' && past) unpaidLate.push('Q' + (q + 1));
      quarters.push({ q: q + 1, due: MONTHS[DUE[q][0]] + ' ' + DUE[q][1], b: b, s: s, months: months, st: st, past: past });
    }
    // discount: only for quarters paid now on or before their due date, and only when the property has no
    // delinquency: no unpaid earlier year and no quarter of this year past due before this payment (Quezon Sec. 44)
    var delinquent = !priorClear || anyLate || unpaidLate.length > 0;
    var disc = 0, discNote = '';
    if (!delinquent) {
      if (qz) {
        var advYears = year - pd[0];
        if (advYears >= 2) { disc = 20; discNote = 'paid two or more years in advance'; }
        else if (advYears === 1 && fullYear && (pd[1] < 9 || (pd[1] === 9 && pd[2] <= 30))) { disc = 15; discNote = 'whole year paid on or before September 30, one year in advance'; }
        else { disc = 10; discNote = 'paid on or before the Sec. 43 deadlines'; }
      } else { disc = Math.min(num('disc'), 20); discNote = 'paid on time'; }
    }
    var tb = 0, ts = 0, tbAdj = 0, tsAdj = 0;
    var qbody = $('q-body'); qbody.innerHTML = '';
    quarters.forEach(function (x) {
      var cells;
      if (x.st !== 'now') {
        var lbl = x.st === 'paid' ? 'paid' : x.past ? 'unpaid, late' : 'not now';
        cells = ['Q' + x.q + ', due ' + x.due, lbl, peso(r2(x.b + x.s)), '—', '—'];
      } else {
        var bAdj, sAdj, label;
        // keep centavos unrounded until the totals, so 15% of ₱500 is exactly ₱75 (not ₱75.04 from rounding each part)
        if (x.months) { bAdj = x.b * x.months * 2 / 100; sAdj = x.s * x.months * 2 / 100; label = (qz ? (x.months / 3) + ' qtr late +' : x.months + ' mo late +') + (x.months * 2) + '%'; }
        else { bAdj = -x.b * disc / 100; sAdj = -x.s * disc / 100; label = disc ? 'on time −' + disc + '%' : 'on time, no discount'; }
        tb = r2(tb + x.b); ts = r2(ts + x.s); tbAdj += bAdj; tsAdj += sAdj;
        cells = ['Q' + x.q + ', due ' + x.due, label, peso(r2(x.b + x.s)), peso(r2(bAdj + sAdj)), peso(r2(x.b + x.s + bAdj + sAdj))];
      }
      var tr = document.createElement('tr');
      if (x.st !== 'now') tr.className = 'not-now';
      cells.forEach(function (c, i) {
        var td = document.createElement(i === 0 ? 'th' : 'td'); td.textContent = c; if (i === 0) td.scope = 'row'; tr.appendChild(td); });
      qbody.appendChild(tr);
    });
    // round the whole discount or interest once, then give the SEF what is left, so 15% of ₱375 is ₱56.25
    // exactly and the amount to pay is ₱318.75 (Butch 2026-11-12), not ₱318.76 from rounding basic and SEF apart
    var tAdj = r2(tbAdj + tsAdj); tbAdj = r2(tbAdj); tsAdj = r2(tAdj - tbAdj);
    var bDue = r2(tb + tbAdj), sDue = r2(ts + tsAdj);
    var adjLabel = anyLate ? 'Interest' : disc ? 'Discount (' + disc + '%, ' + discNote + ')' : 'Discount';
    var notes = [];
    if (rolled) notes.push(rolled);
    if (unpaidLate.length) notes.push(unpaidLate.join(', ') + ' of this year ' + (unpaidLate.length > 1 ? 'are' : 'is') + ' past due and not paid. The treasurer applies any payment to the oldest unpaid tax first (Sec. 250), so this payment would go there first.');
    if (anyLate) notes.push('Interest is added because ' + lateNow.join(', ') + (lateNow.length > 1 ? ' are' : ' is') + ' marked "Not paid" and past the due date. If you already paid ' + (lateNow.length > 1 ? 'them' : 'it') + ', set ' + (lateNow.length > 1 ? 'them' : 'it') + ' to "Paid" in step 4.');
    var onTimeNow = quarters.some(function (x) { return x.st === 'now' && !x.months; });
    if (onTimeNow && delinquent) {
      var isAre = function (l) { return l.join(', ') + (l.length > 1 ? ' are' : ' is'); };
      var why = !priorClear ? 'an earlier year is unpaid' : anyLate ? isAre(lateNow) + ' paid late' : isAre(unpaidLate) + ' unpaid';
      notes.push('No discount, because ' + why + '. The discount is only for properties without any delinquency.');
    }
    $('out-note').textContent = notes.join(' ');

    $('out-av').textContent = peso(av);
    $('t-basic').textContent = peso(tb); $('t-sef').textContent = peso(ts); $('t-tax').textContent = peso(r2(tb + ts));
    $('t-adj-label').textContent = adjLabel;
    $('t-badj').textContent = peso(tbAdj); $('t-sadj').textContent = peso(tsAdj); $('t-adj').textContent = peso(r2(tbAdj + tsAdj));
    $('t-bdue').textContent = peso(bDue); $('t-sdue').textContent = peso(sDue); $('t-due').textContent = peso(r2(bDue + sDue));
    $('out-due').textContent = peso(r2(bDue + sDue));
    $('out-when').textContent = 'Tax year ' + year + ' (whole year ' + peso(r2(basic + sef)) + '), target date of payment ' + MONTHS[pd[1] - 1] + ' ' + pd[2] + ', ' + pd[0];

    var rows = [], sum = 0;
    function add(who, base, pct, note) { var a = r2(base * pct / 100); sum = r2(sum + a); rows.push([who, pct + '%', a, note || '']); }
    if (city) {
      add('City general fund', bDue, 70);
      add('Barangay where the property is', bDue, 15, 'half of the 30% barangay share');
      var n = Math.floor(num('brgy-count'));
      var pool = r2(bDue * 15 / 100);
      add('All barangays of the city, shared equally', bDue, 15, n > 0 ? peso(r2(pool / n)) + ' each for ' + n + ' barangays' : 'enter the number of barangays to see each one');
      rows.push(['City school board', '100%', sDue, 'all of the SEF']); sum = r2(sum + sDue);
    } else {
      add('Province general fund', bDue, 35);
      add('Municipality general fund', bDue, 40);
      add('Barangay where the property is', bDue, 25);
      add('Provincial school board (SEF)', sDue, 50);
      add('Municipal school board (SEF)', sDue, 50);
    }
    // keep the total exact: put any one-centavo rounding difference on the largest share
    var total = r2(bDue + sDue), diff = r2(total - sum);
    if (diff !== 0) { var big = 0; rows.forEach(function (r, i) { if (r[2] > rows[big][2]) big = i; }); rows[big][2] = r2(rows[big][2] + diff); }
    var body = $('share-body'); body.innerHTML = '';
    rows.forEach(function (r) {
      var tr = document.createElement('tr');
      [r[0], r[1], peso(r[2])].forEach(function (c, i) { var td = document.createElement(i === 0 ? 'th' : 'td'); td.textContent = c; if (i === 0) td.scope = 'row'; tr.appendChild(td); });
      if (r[3]) { var small = document.createElement('small'); small.textContent = r[3]; tr.firstChild.appendChild(document.createElement('br')); tr.firstChild.appendChild(small); }
      body.appendChild(tr);
    });
    $('share-total').textContent = peso(total);
  }
  $('kind').addEventListener('change', function () { fillClasses(); lastLevelKey = null; });
  $('klass').addEventListener('change', function () { lastLevelKey = null; });
  f.addEventListener('input', calc);
  f.addEventListener('change', calc);
  f.addEventListener('submit', function (e) { e.preventDefault(); calc(); });
  fillClasses();
  calc();
})();
""".replace("__LEVELS__", json.dumps(QUEZON_LEVELS))


def _field(label, control, hint=None, row_id=None, hidden=False):
    return t.div(t.label(label, control, t.small(hint, class_="hint") if hint else None),
                 class_="field", id=row_id, hidden=hidden)


def _num(id_, value="", step="any", minimum="0", maximum=None, placeholder=None):
    return t.input(type="number", id=id_, name=id_, value=value, step=step, min=minimum, max=maximum,
                   inputmode="decimal", placeholder=placeholder)


def _radio(name, value, label, checked=False):
    return t.label(t.input(type="radio", name=name, value=value, checked=checked), " ", label, class_="choice")


def _quarter_select(q):
    return t.select(t.option("Not paid", value="now"), t.option("Paid", value="paid"), id="qs%d" % q, name="qs%d" % q)


def _guide_link():
    """Box under the intro pointing to the how-to post; shown only once that post is live."""
    from pages import post_is_live  # imported here: pages.py imports this module
    if not post_is_live(RPT_GUIDE_URL):
        return ""
    return t.p(t.b("New to the calculator? "), "Read the step-by-step guide with worked examples: ",
               t.a("How to Use the RPT Calculator", href=RPT_GUIDE_URL), ".", class_="rpt-guide")


def rpt_page():
    law = "https://lawphil.net/statutes/repacts/ra1991/ra_7160_1991.html"
    return {
        "title": "RPT Calculator", "active": RPT_URL, "url": RPT_URL, "og_type": "website",
        "seo_title": "Real Property Tax (Amilyar) Calculator, Philippines · Butch Mahinay",
        "description": "Free real property tax (amilyar) calculator for the Philippines: basic tax, SEF, discount or "
                       "interest by date of payment, and each share for the province, town and barangay.",
        "body": [
            t.p("Free tool", class_="eyebrow"),
            t.h1("Real Property Tax Calculator"),
            t.p("Work out the yearly real property tax (amilyar) on a piece of land or a building, then see where "
                "every peso goes: the province, the municipality, the barangay and the school boards. "
                "Based on the Local Government Code of 1991 (RA 7160), with the rules of the Quezon Provincial "
                "Revenue Code built in.", class_="lead"),
            _guide_link(),
            t.form(
                t.fieldset(
                    t.legend("1. Where is the property?"),
                    t.div(_radio("lgu", "quezon", "In a municipality of Quezon Province", True),
                          _radio("lgu", "mun", "In a municipality of another province"),
                          _radio("lgu", "city", "In a city"), class_="choices"),
                    _field("Number of barangays in the city (optional)", _num("brgy-count", step="1", placeholder="e.g. 33"),
                           "Used to show each barangay's equal share.", row_id="brgy-count-row", hidden=True),
                ),
                t.fieldset(
                    t.legend("2. Assessed value"),
                    t.div(_radio("basis", "av", "I know the assessed value", True),
                          _radio("basis", "mv", "Compute it from the market value"), class_="choices"),
                    _field("Assessed value (₱)", _num("av", "100000", placeholder="e.g. 100000"),
                           "Shown on the tax declaration.", row_id="av-row"),
                    t.div(
                        t.div(
                            _field("Property", t.select(t.option("Land", value="land"), t.option("Building", value="building"),
                                                        t.option("Machinery", value="machinery"),
                                                        t.option("Special class", value="special"), id="kind", name="kind")),
                            _field("Class or use", t.select(id="klass", name="klass"),
                                   "Fills in the assessment level from the Quezon Provincial Revenue Code (Sec. 25)."),
                            id="qz-class", class_="field-pair",
                        ),
                        t.div(
                            _field("Market value (₱)", _num("mv", "500000")),
                            _field("Assessment level (%)", _num("level", "5", maximum="100"),
                                   "Set by ordinance for each class of property; you can change it."),
                            class_="field-pair",
                        ),
                        id="mv-rows", hidden=True,
                    ),
                ),
                t.fieldset(
                    t.legend("3. Tax rates"),
                    t.div(
                        _field("Basic RPT rate (%)", _num("basic-rate", "1", maximum="2"),
                               "Up to 1% in a province, up to 2% in a city."),
                        _field("SEF rate (%)", _num("sef-rate", "1", maximum="1"),
                               "Special Education Fund, 1%."),
                        class_="field-pair",
                    ),
                ),
                t.fieldset(
                    t.legend("4. When is it paid?"),
                    t.div(
                        _field("Today's date", t.input(type="text", id="todaydate", readonly=True, tabindex="-1"),
                               "Fixed: today in the Philippines."),
                        _field("Tax year", _num("taxyear", step="1", minimum="1992", maximum="2100")),
                        class_="field-pair",
                    ),
                    _field("Target date of payment", t.input(type="date", id="paydate", name="paydate"),
                           "Starts as today. Change it to see what you would pay on another day."),
                    t.p("Which quarters of this tax year are already paid?", class_="field-title"),
                    t.div(*[_field("Q%d, due %s" % (i + 1, d), _quarter_select(i + 1))
                            for i, d in enumerate(["Mar 31", "Jun 30", "Sep 30", "Dec 31"])],
                          class_="quarter-grid"),
                    t.label(t.input(type="checkbox", id="prior-paid", name="prior-paid", checked=True), " ",
                            "Taxes of earlier years are fully paid", class_="choice prior-paid"),
                    _field("Discount for paying on time (%)", _num("disc", "10", maximum="20"),
                           "Set by your local ordinance, up to 20%.", row_id="disc-row", hidden=True),
                    t.p("Quezon Province discount (Sec. 44), worked out from the date: 10% if paid on or before the "
                        "installment deadlines of Sec. 43, 15% if the whole year is paid on or before September 30 of the year before, and 20% "
                        "if paid two or more years in advance. The discount is only for quarters paid now on or before their due "
                        "date, and only when the property has no delinquency: no unpaid earlier year and no quarter "
                        "of this year past due and unpaid.",
                        id="qz-disc", class_="hint block-hint"),
                    t.p("The year's tax is split into four equal quarters, due March 31, June 30, September 30 and "
                        "December 31. A quarter paid after its due date earns interest of 2% for each month or part of "
                        "a month, up to 36 months; in Quezon Province it is counted by quarter, so each quarter or part of a quarter late adds 6%. Mark the quarters already paid as \"Paid\"; every quarter "
                        "marked \"Not paid\" is added to the amount to pay: 10% off if paid on time, 6% more for each quarter late.", class_="hint block-hint"),
                ),
                id="rpt", class_="card rpt-form", novalidate=True,
            ),
            t.div(
                t.p("Assessed value ", t.b("—", id="out-av"), class_="rpt-av"),
                t.p("—", id="out-when", class_="rpt-av"),
                t.p("Amount to pay", class_="rpt-due-label"),
                t.p("—", id="out-due", class_="rpt-due"),
                t.p("", id="out-note", class_="rpt-av"),
                t.div(
                    t.table(
                        t.thead(t.tr(t.th(""), t.th("Basic RPT"), t.th("SEF"), t.th("Total"))),
                        t.tbody(
                            t.tr(t.th("Tax for the unpaid quarters", scope="row"), t.td(id="t-basic"), t.td(id="t-sef"), t.td(id="t-tax")),
                            t.tr(t.th("Discount or interest", scope="row", id="t-adj-label"), t.td(id="t-badj"), t.td(id="t-sadj"), t.td(id="t-adj")),
                            t.tr(t.th("To pay", scope="row"), t.td(id="t-bdue"), t.td(id="t-sdue"), t.td(id="t-due"), class_="total"),
                        ),
                        class_="rpt-table",
                    ),
                    class_="table-scroll",
                ),
                t.h3("Quarter by quarter"),
                t.div(
                    t.table(
                        t.thead(t.tr(t.th("Quarter"), t.th("Status"), t.th("Tax"), t.th("+/−"), t.th("To pay"))),
                        t.tbody(id="q-body"),
                        class_="rpt-table quarters",
                    ),
                    class_="table-scroll",
                ),
                t.h3("Who gets what"),
                t.div(
                    t.table(
                        t.thead(t.tr(t.th("Share"), t.th("Rate"), t.th("Amount"))),
                        t.tbody(id="share-body"),
                        t.tfoot(t.tr(t.th("Total", scope="row"), t.td(""), t.td(id="share-total"), class_="total")),
                        class_="rpt-table share",
                    ),
                    class_="table-scroll",
                ),
                class_="card rpt-result", aria_live="polite",
            ),
            t.h2("How the tax is shared"),
            t.p("The basic real property tax, including any interest, is divided by law. In a municipality, the "
                "province gets 35%, the municipality 40% and the barangay where the property is 25%. In a city, the "
                "city gets 70% and the barangays 30%: half of that goes to the barangay where the property is, and the "
                "other half is shared equally by all the barangays of the city (Sec. 271)."),
            t.p("The Special Education Fund tax goes to the local school boards. In a province, it is split equally "
                "between the provincial and municipal school boards; in a city, the city school board keeps all of it "
                "(Sec. 272)."),
            t.h2("Good to know"),
            t.ul(
                t.li(t.b("Assessed value. "), "Tax is charged on the assessed value, not the market value. Assessed value "
                     "is the market value times the assessment level set by ordinance for the property's class and use "
                     "(Sec. 218). For buildings in Quezon Province, the level depends on the market value bracket."),
                t.li(t.b("Installments. "), "The tax may be paid in four equal quarterly installments, due on or before "
                     "March 31, June 30, September 30 and December 31 (Sec. 250)."),
                t.li(t.b("Discount. "), "A province or city may give a discount of up to 20% for paying in advance "
                     "or on time; the rates are in the local ordinance (Sec. 251). Each quarter paid on or before its due date "
                     "earns the discount, so a taxpayer who pays quarter by quarter on time gets it on every quarter."),
                t.li(t.b("Interest. "), "Unpaid tax earns interest of 2% a month, up to 36 months, until it is paid in full "
                     "(Sec. 255). In Quezon Province, interest is counted by quarter: each quarter or part of a quarter after "
                     "the due date counts as three months, or 6%."),
                t.li(t.b("Older unpaid taxes first. "), "Payments are applied first to unpaid taxes, interest and penalties of "
                     "earlier years, and only then to the current year (Sec. 250). This calculator works out one tax year at a time."),
                t.li(t.b("Not included. "), "The idle land tax (3% in Quezon Province), special levies, and the lower SEF rate for "
                     "renewable energy property (0.5% in Quezon Province, under RA 9513) are not covered here."),
                t.li(t.b("New property values. "), "Under the Real Property Valuation and Assessment Reform Act (RA 12001, 2024), "
                     "the increase in real property tax in the first year of a new schedule of market values is capped at 6%."),
                t.li(t.b("Metro Manila. "), "Municipalities in Metro Manila follow a different sharing rule, so this "
                     "calculator does not cover them."),
                class_="plain-list rpt-notes",
            ),
            t.p("Sources: ", t.a("Local Government Code of 1991 (RA 7160)", href=law, rel="noopener"), ", Secs. 218, 233, 235, "
                "250, 251, 255, 271 and 272; ",
                t.a("RA 12001", href="https://lawphil.net/statutes/repacts/ra2024/ra_12001_2024.html", rel="noopener"),
                ", Sec. 29; Province of Quezon, Provincial Ordinance No. 2022-010 (Revised Revenue Code of 2022), "
                "Secs. 25, 39, 40, 41, 43, 44, 45, 47 and 52. Last checked " + RPT_CHECKED + ".", class_="muted note sources-line"),
            t.p("This calculator is a study aid, not an official assessment. Your actual tax depends on your local "
                "ordinances and the tax declaration; your municipal, city or provincial treasurer's office has the final "
                "figures. Figures are worked out in your browser and nothing you type is sent or saved.",
                class_="disclaimer"),
            t.script(Raw(RPT_SCRIPT)),
        ],
    }
