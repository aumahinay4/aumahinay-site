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
  or a fraction thereof", at most 36 months. Office practice, from an official receipt Butch shared 2026-11-28
  (AV 5,630, Q1-Q4 of 2026 paid Nov 3, 2026, ₱126.68): the late quarters carry 2% for each whole month from the first
  month of the earliest late quarter to the month before payment, the same rate for all (Nov 3 -> Jan-Oct = 20% on
  Q1-Q3; a second receipt, 2024 Q3-Q4 paid Mar 11, 2025 -> Jul 2024-Feb 2025 = 16%), and a quarter paid on time in the same payment still gets the 10% discount.
  (Replaces the earlier "6% per quarter late" and "no discount when a quarter is late" rules.)
"""

import json

import tags as t
from tags import Raw

RPT_URL = "/tools/rpt-calculator/"
RPT_CHECKED = "November 2026"
RPT_GUIDE_URL = "/blog/how-to-use-the-rpt-calculator/"  # step-by-step guide post (Butch 2026-11-11)

# Built-in provincial revenue code of 2022, Sec. 25 (levels in %; building brackets: [up to market value, level])
PROV_LEVELS = {
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
  function provLevel(mv) {
    var v = LEVELS[$('kind').value][$('klass').value];
    if (typeof v === 'number') return v;
    for (var i = 0; i < v.length; i++) if (v[i][0] === null || mv <= v[i][0]) return v[i][1];
    return 0;
  }
  var lastLgu = null, lastLevelKey = null;

  var rolledNote = '';
  function calc() {
    // a payment is never ₱0.00 (Butch 2026-11-12): when all four quarters of the tax year are paid, the next payment
    // is for the following year, so move to it and start its quarters as "Not paid"
    if ([1, 2, 3, 4].every(function (q) { return $('qs' + q).value === 'paid'; })) {
      var y0 = Math.floor(num('taxyear')) || ph.getUTCFullYear();
      $('taxyear').value = y0 + 1;
      [1, 2, 3, 4].forEach(function (q) { $('qs' + q).value = 'now'; });
      rolledNote = 'Tax year ' + y0 + ' is fully paid, so this shows the next payment: tax year ' + (y0 + 1) + '.';
    }
    var lgu = f.lgu.value, city = lgu === 'city', qz = lgu === 'prov';
    if (lgu !== lastLgu) { $('basic-rate').value = city ? '2' : '1'; lastLgu = lgu; }
    $('brgy-count-row').hidden = !city;
    var useMv = f.basis.value === 'mv';
    $('mv-rows').hidden = !useMv; $('av-row').hidden = useMv;
    $('prov-class').hidden = !(useMv && qz);
    var mv = num('mv');
    if (useMv && qz) {
      var key = $('kind').value + '|' + $('klass').value + '|' + mv;
      if (key !== lastLevelKey) { $('level').value = provLevel(mv); lastLevelKey = key; }
    }
    var av = useMv ? r2(mv * Math.min(num('level'), 100) / 100) : num('av');
    var bRate = Math.min(num('basic-rate'), city ? 2 : 1), sRate = Math.min(num('sef-rate'), 1);
    var basic = r2(av * bRate / 100), sef = r2(av * sRate / 100);

    // payment date and tax year
    $('disc-row').hidden = qz; $('prov-disc').hidden = !qz;
    var year = Math.floor(num('taxyear')) || ph.getUTCFullYear();
    var pd = ($('paydate').value || today).split('-').map(Number);  // [y, m, d]
    var payIdx = pd[0] * 12 + (pd[1] - 1);
    var payNum = pd[0] * 10000 + pd[1] * 100 + pd[2];
    // each quarter is one fourth of the year's tax, rounded so that any number of quarters adds up to the rounded
    // fraction of the year, as on the official receipt: ₱56.30 a year -> Q1 to Q3 ₱42.23, Q4 ₱14.07
    // (worked in whole centavos, so 5,630 × 3 / 4 = 4,222.5 rounds up to 4,223 instead of slipping to 4,222)
    var part = function (tot, q) { var c = Math.round(tot * 100); return (Math.round(c * (q + 1) / 4) - Math.round(c * q / 4)) / 100; };
    var priorClear = $('prior-paid').checked;
    var quarters = [], anyLate = false, unpaidLate = [], lateNow = [], fullYear = true, anyNow = false, amnestyNow = [];
    // built-in provincial practice (two official receipts, Butch 2026-11-28): interest on the late quarters paid now runs
    // from the first month of the earliest of them to the month before payment, the same rate for all of them
    // (Q1-Q4 2026 paid Nov 3, 2026: Jan-Oct = 20%; 2024 Q3-Q4 paid Mar 11, 2025: Jul 2024-Feb 2025 = 16%)
    // RA 12001 Sec. 30 amnesty: interest and penalties on real property tax left unpaid before the Act took effect
    // (July 5, 2024) are waived when paid within two years (to July 5, 2026); the tax itself is still paid.
    // Shown on a tax clearance: 2024 Q1-Q2 paid Mar 11, 2025 with no penalty.
    var amnestyPay = payNum >= 20240705 && payNum <= 20260705;
    var dueOf = function (k) { return year * 10000 + (DUE[k][0] + 1) * 100 + DUE[k][1]; };
    var amnestyQ = function (k) { return amnestyPay && dueOf(k) < 20240705; };
    var firstLate = -1;
    for (var k = 0; k < 4; k++) if (firstLate < 0 && $('qs' + (k + 1)).value === 'now' && payNum > dueOf(k) && !amnestyQ(k)) firstLate = k;
    for (var q = 0; q < 4; q++) {
      var dueNum = year * 10000 + (DUE[q][0] + 1) * 100 + DUE[q][1];
      var b = part(basic, q), s = part(sef, q);
      var st = $('qs' + (q + 1)).value;  // now = paying now, paid = paid already, later = not paying now
      var past = payNum > dueNum, months = 0, amnesty = false;
      if (st === 'later') fullYear = false;
      if (st === 'now') anyNow = true;
      if (st === 'now' && past && amnestyQ(q)) { amnesty = true; amnestyNow.push('Q' + (q + 1)); }
      else if (st === 'now' && past) {  // late: every month or part of a month after the due date counts, up to 36
        months = Math.max(payIdx - (year * 12 + DUE[q][0]), 1);
        if (qz) months = Math.max(payIdx - (year * 12 + firstLate * 3), 1);
        months = Math.min(months, 36);
        anyLate = true; lateNow.push('Q' + (q + 1));
      }
      if (st === 'later' && past) unpaidLate.push('Q' + (q + 1));
      quarters.push({ q: q + 1, due: MONTHS[DUE[q][0]] + ' ' + DUE[q][1], b: b, s: s, months: months, st: st, past: past, amnesty: amnesty });
    }
    // discount: only for quarters paid now on or before their due date, and only when the property has no
    // delinquency: no unpaid earlier year and no quarter of this year past due before this payment. With the built-in
    // provincial rates, late quarters settled in this same payment do not block it (official receipt, 2026-11-28)
    var delinquent = !priorClear || (anyLate && !qz) || unpaidLate.length > 0;
    var disc = 0, discNote = '';
    if (!delinquent) {
      if (qz) {
        var advYears = year - pd[0];
        if (advYears >= 2) { disc = 20; discNote = 'paid two or more years in advance'; }
        else if (advYears === 1 && fullYear && (pd[1] < 9 || (pd[1] === 9 && pd[2] <= 30))) { disc = 15; discNote = 'whole year paid on or before September 30, one year in advance'; }
        else { disc = 10; discNote = 'paid on or before the quarterly deadlines'; }
      } else { disc = Math.min(num('disc'), 20); discNote = 'paid on time'; }
    }
    var tb = 0, ts = 0, bInt = 0, sInt = 0, bDisc = 0, sDisc = 0;
    var qbody = $('q-body'); qbody.innerHTML = '';
    quarters.forEach(function (x) {
      var cells;
      if (x.st !== 'now') {
        var lbl = x.st === 'paid' ? 'paid' : x.past ? 'unpaid, late' : 'not now';
        cells = ['Q' + x.q + ', due ' + x.due, lbl, peso(r2(x.b + x.s)), '—', '—'];
      } else {
        var bAdj, sAdj, label;
        // keep centavos unrounded until the totals, so 15% of ₱500 is exactly ₱75 (not ₱75.04 from rounding each part)
        if (x.amnesty) { bAdj = 0; sAdj = 0; label = 'amnesty, no interest'; }
        else if (x.months) { bAdj = x.b * x.months * 2 / 100; sAdj = x.s * x.months * 2 / 100; label = x.months + (qz ? ' mo +' : ' mo late +') + (x.months * 2) + '%'; }
        else { bAdj = -x.b * disc / 100; sAdj = -x.s * disc / 100; label = disc ? 'on time −' + disc + '%' : 'on time, no discount'; }
        tb = r2(tb + x.b); ts = r2(ts + x.s);
        if (bAdj > 0) { bInt += bAdj; sInt += sAdj; } else { bDisc -= bAdj; sDisc -= sAdj; }
        cells = ['Q' + x.q + ', due ' + x.due, label, peso(r2(x.b + x.s)), peso(r2(bAdj + sAdj)), peso(r2(x.b + x.s + bAdj + sAdj))];
      }
      var tr = document.createElement('tr');
      if (x.st !== 'now') tr.className = 'not-now';
      cells.forEach(function (c, i) {
        var td = document.createElement(i === 0 ? 'th' : 'td'); td.textContent = c; if (i === 0) td.scope = 'row'; tr.appendChild(td); });
      qbody.appendChild(tr);
    });
    // as on official receipts (AF 56 and a tax clearance, 2026-11-28): each fund's interest and each fund's discount is
    // worked on its own and rounded once, e.g. 16% of ₱200.15 = ₱32.02 basic and ₱32.02 SEF
    var tbAdj = r2(r2(bInt) - r2(bDisc)), tsAdj = r2(r2(sInt) - r2(sDisc));
    var bDue = r2(tb + tbAdj), sDue = r2(ts + tsAdj);
    var onTimeNow = quarters.some(function (x) { return x.st === 'now' && !x.past; });
    var adjLabel = anyLate ? (disc && onTimeNow ? 'Interest less discount' : 'Interest') : disc ? 'Discount (' + disc + '%, ' + discNote + ')' : 'Discount';
    var notes = [];
    if (rolledNote) notes.push(rolledNote);
    if (unpaidLate.length) notes.push(unpaidLate.join(', ') + ' of this year ' + (unpaidLate.length > 1 ? 'are' : 'is') + ' past due and not paid. The treasurer applies any payment to the oldest unpaid tax first (Sec. 250), so this payment would go there first.');
    if (amnestyNow.length) notes.push(amnestyNow.join(', ') + ' of ' + year + (amnestyNow.length > 1 ? ' were' : ' was') + ' unpaid before RA 12001 took effect on July 5, 2024, and this payment is within the two-year amnesty, so ' + (amnestyNow.length > 1 ? 'they carry' : 'it carries') + ' no interest (Sec. 30). The tax itself is still paid.');
    if (anyLate) notes.push('Interest is added because ' + lateNow.join(', ') + (lateNow.length > 1 ? ' are' : ' is') + ' marked "Not paid" and past the due date' + (qz ? ', counted from the start of ' + lateNow[0] + '.' : '.') + ' If you already paid ' + (lateNow.length > 1 ? 'them' : 'it') + ', set ' + (lateNow.length > 1 ? 'them' : 'it') + ' to "Paid" in step 4.');
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
  function onEdit(e) {  // the "fully paid, next year" note stays until the year or a quarter is changed again
    var t = e.target;
    if (t.id === 'taxyear' || (/^qs/.test(t.id) && t.value === 'paid')) rolledNote = '';
    calc();
  }
  f.addEventListener('input', onEdit);
  f.addEventListener('change', onEdit);
  f.addEventListener('submit', function (e) { e.preventDefault(); calc(); });
  fillClasses();
  calc();
})();
""".replace("__LEVELS__", json.dumps(PROV_LEVELS))


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


def _example(title, setup, lines, result):
    """One worked example: what was typed in, what the calculator shows, and the lesson."""
    return t.div(
        t.h3(title),
        t.p(t.b("What you type: "), setup),
        t.ul([t.li(x) for x in lines], class_="rpt-steps"),
        t.p(t.b("Result: "), result),
        class_="card rpt-example",
    )


def _explanations():
    """How the calculator works, how to read its results, and worked examples (Butch 2026-11-24: "make more
    explanations to get useful information"). The step-by-step how-to post and the Study Notes on real property
    tax are linked, not repeated. Every example below was run in the calculator before publishing."""
    return [
        t.h2("How the calculator works it out"),
        t.p("The calculator works in five steps. Knowing them helps you check your own tax bill."),
        t.ol(
            t.li(t.b("Assessed value. "), "Real property tax is charged on the assessed value, not on what the property "
                 "would sell for. Assessed value is the market value times the assessment level that the local ordinance "
                 "sets for the property's class and actual use (Sec. 218). If you know the assessed value from your tax "
                 "declaration, the calculator uses it as it is."),
            t.li(t.b("Basic tax and SEF. "), "The basic tax is the assessed value times the basic rate: up to 1% when the "
                 "province levies it (for property in a municipality), or up to 2% in a city or a Metro Manila municipality "
                 "(Sec. 233). The Special Education Fund (SEF) tax is another 1% of the assessed value (Sec. 235). So at the "
                 "highest rates, a property in a municipality pays 2% of its assessed value a year, and one in a city pays 3%."),
            t.li(t.b("Four equal quarters. "), "The year's tax may be paid without interest in four equal installments, "
                 "due on or before March 31, June 30, September 30 and December 31 (Sec. 250). The calculator divides "
                 "the basic tax and the SEF by four; if the amount does not divide evenly, the centavos are rounded "
                 "so that the quarters add up to the year's tax, as on an official receipt."),
            t.li(t.b("Discount or interest, quarter by quarter. "), "Each quarter marked \"Not paid\" is compared with the "
                 "target date of payment. Paid on or before its due date, it can earn the discount for prompt or advance "
                 "payment, which the law caps at 20% of the annual tax (Sec. 251). Paid after its due date, it earns interest of 2% "
                 "for each month or part of a month, for at most 36 months, or 72% in all (Sec. 255). With the built-in "
                 "provincial rates, interest follows the practice on official receipts: interest runs from "
                 "the first month of the earliest late quarter to the month before payment, 2% a month, and the same rate "
                 "applies to every late quarter. Paid in November with Q1 unpaid, January to October is ten months, so Q1, "
                 "Q2 and Q3 each carry 20%."),
            t.li(t.b("No discount while anything is overdue. "), "With rates you type in, the calculator gives the discount only when the property "
                 "has no delinquency: no unpaid earlier year and no quarter of this year already past due. With the built-in "
                 "provincial rates, quarters paid late in the same payment do not take away the discount on a quarter "
                 "that is still on time, as on official receipts; an unpaid earlier year still does. Other local codes "
                 "may work differently, so check yours."),
            class_="rpt-steps",
        ),
        t.p("As on official receipts, the basic tax and the SEF are worked out separately: each one's interest and each "
            "one's discount is rounded to the centavo once, and the result is then shared out as shown in \"Who gets what\"."),
        t.p(t.b("RA 12001 amnesty. "), "Interest and penalties on real property tax left unpaid before July 5, 2024, "
            "when the Real Property Valuation and Assessment Reform Act took effect, were waived if paid by July 5, 2026 "
            "(Sec. 30). The tax itself still had to be paid. If your target date falls in that window, the calculator "
            "shows those quarters with no interest, so you can check an old receipt or tax clearance. The amnesty did "
            "not cover property already sold at auction, under a compromise agreement, or in a pending court case."),
        t.h2("Reading your results"),
        t.ul(
            t.li(t.b("Amount to pay. "), "The big figure is what you would bring to the treasurer's office on the target "
                 "date: the tax for every quarter marked \"Not paid\", less any discount or plus any interest. Quarters "
                 "marked \"Paid\" are left out."),
            t.li(t.b("The line under the assessed value. "), "It shows the tax year, the tax for the whole year before any "
                 "discount or interest, and the target date, so you can see at a glance which case you are looking at."),
            t.li(t.b("Notes in the result box. "), "When a quarter is past due, a short note says which one and why there "
                 "is interest or no discount. If the note names a quarter you have already paid, set it to \"Paid\"."),
            t.li(t.b("Quarter by quarter. "), "Each row shows one installment and its status. \"On time −10%\" means it earns "
                 "a 10% discount. \"2 mo late +4%\" means the quarter is two months late (a part of a month counts as a whole "
                 "month), so 4% is added. "
                 "\"10 mo +20%\" is the same idea under the built-in provincial rates, counted from the start of the earliest late quarter. "
                 "\"On time, no discount\" means the quarter is not yet due, but another quarter is overdue."),
            t.li(t.b("Basic RPT and SEF columns. "), "The summary table keeps the two taxes apart because they go to "
                 "different funds. The basic tax and its interest go to the general funds of the local governments; the "
                 "SEF goes to the school boards."),
            t.li(t.b("Who gets what. "), "This table splits the amount you pay among the local governments and school "
                 "boards, as explained in \"How the tax is shared\" below."),
            class_="plain-list rpt-notes",
        ),
        t.h2("Worked examples"),
        t.p("These three cases use rates you type in yourself, so they work for any local government. The step-by-step "
            "guide has more examples with the built-in provincial rates."),
        _example(
            "1. A lot in a city, paid in full early",
            "A city with 20 barangays. Assessed value ₱80,000. Basic rate 2%, SEF 1%, discount 10%. Tax year 2027, "
            "target date February 15, 2027, all four quarters \"Not paid\".",
            ["Basic tax: ₱80,000 × 2% = ₱1,600. SEF: ₱80,000 × 1% = ₱800. Tax for the year: ₱2,400, or ₱600 a quarter.",
             "Every quarter is paid before its due date, so each one earns 10%: ₱60 off each, ₱240 in all.",
             "Who gets what: the basic tax after discount is ₱1,440. The city gets 70% (₱1,008), the barangay where the "
             "lot is gets 15% (₱216), and the other 15% (₱216) is shared by all 20 barangays, ₱10.80 each. The city "
             "school board gets the whole SEF after discount, ₱720."],
            "₱2,160 to pay, ₱240 less than the full tax."),
        _example(
            "2. Two quarters left, one of them late",
            "A municipality, with rates you type in. Assessed value ₱40,000. Basic rate 1%, SEF 1%, discount 10%. "
            "Tax year 2026, Q1 and Q2 \"Paid\", Q3 and Q4 \"Not paid\", target date November 5, 2026.",
            ["Tax for the year: ₱400 basic + ₱400 SEF = ₱800, or ₱200 a quarter.",
             "Q3 was due September 30. October and part of November count as two months: 2 × 2% = 4%, or ₱8 interest.",
             "Q4 is not due until December 31, but because Q3 is overdue, Q4 gets no discount. It stays at ₱200.",
             "Had the same two quarters been paid on September 25, both would have been on time: ₱180 each, or ₱360."],
            "₱408 to pay. Paying six weeks earlier would have saved ₱48."),
        _example(
            "3. An old year and the 36-month cap",
            "A municipality, with rates you type in. Assessed value ₱40,000. Basic rate 1%, SEF 1%. Tax year 2023, "
            "all four quarters \"Not paid\", target date November 24, 2026. All the other years are paid, so the box "
            "for earlier years stays ticked.",
            ["Each quarter's tax is ₱200, and all four are late.",
             "Q1, Q2 and Q3 of 2023 are 44, 41 and 38 months late, but interest stops at 36 months: 72%, or ₱144 each.",
             "Q4 was due December 31, 2023, so it is 35 months late: 70%, or ₱140.",
             "Interest: ₱144 × 3 + ₱140 = ₱572 on a tax of ₱800."],
            "₱1,372 to pay. The interest has stopped growing, but the tax itself stays a lien on the property until paid."),
    ]


def _faq():
    """Short answers to questions taxpayers ask about the calculator's figures."""
    qa = [
        ("Why is the calculator's amount different from my official receipt?",
         "Usually for one of four reasons: your local ordinance uses a different rate, discount or assessment level; the "
         "assessed value on your tax declaration has changed; part of your payment went to an older unpaid year first; "
         "or your bill includes something the calculator leaves out, such as an idle land tax or a special levy. Your "
         "treasurer's office can show you how its figure was computed."),
        ("I am paying before the deadline. Why is there no discount?",
         "Check the quarters in step 4 and the box for earlier years. If an earlier year is unpaid, the calculator "
         "treats the property as delinquent and gives no discount. With rates you type in, a past-due quarter of the "
         "year does the same; with the built-in provincial rates, it does not, as on official receipts. "
         "Mark the quarters you have paid as \"Paid\" and tick the box if earlier years are settled."),
        ("I paid last year's tax late. Do I lose this year's discount?",
         "In the calculator, not by itself. Once last year is fully paid, including its interest, the property has no unpaid "
         "earlier year, so leave the box for earlier years ticked."),
        ("Does interest keep growing forever?",
         "No. The law stops it at 36 months, so the most interest on any unpaid amount is 72% (Sec. 255). The unpaid tax "
         "itself remains a lien on the property until paid (Sec. 257), and the local government may collect it through the remedies the law allows."),
        ("Can I pay only one quarter at a time?",
         "Yes. The law allows four equal installments (Sec. 250). The \"Quarter by quarter\" table shows what each "
         "quarter costs on your target date, so you can read off the one you are paying now."),
        ("Where do I find the rates for my local government?",
         "In the revenue code of the province (for a municipality) or of the city, passed by its sanggunian. The "
         "treasurer's or assessor's office can tell you the current assessment levels, basic rate and discount."),
    ]
    out = [t.h2("Questions people ask")]
    for q, a in qa:
        out += [t.h3(q, class_="rpt-q"), t.p(a)]
    return out


def _read_more():
    """Links to the site's longer pieces on real property tax, shown only once each is live, so this page does not
    repeat them."""
    from pages import post_is_live, live_notes  # imported here: pages.py imports this module
    links = []
    if post_is_live(RPT_GUIDE_URL):
        links.append(t.li(t.a("How to Use the RPT Calculator", href=RPT_GUIDE_URL),
                          " walks through the calculator step by step, using the built-in provincial rates."))
    notes = {n["slug"]: n for n in live_notes()}
    for slug, what in [("real-property-tax-basics", " explains valuation, assessment levels, exemptions and appeals."),
                       ("paying-real-property-tax", " explains due dates, discounts, interest, and what happens when the tax stays unpaid.")]:
        if slug in notes:
            links.append(t.li(t.a("Study Note: " + notes[slug]["title"], href="/study-notes/%s/" % slug), what))
    try:
        import altos_guide  # noqa: F401  the ALTOS Demo Guide page, once it is added
        links.append(t.li(t.a("ALTOS Demo Guide", href="/tools/altos-demo-guide/"),
                          " shows how a treasury system computes the same tax at the counter."))
    except ImportError:
        pass
    if not links:
        return ""
    return t.div(t.h2("Read more"), t.ul(links, class_="plain-list rpt-notes"))


def rpt_page():
    law = "https://lawphil.net/statutes/repacts/ra1991/ra_7160_1991.html"
    return {
        "title": "RPT Calculator", "active": RPT_URL, "url": RPT_URL, "og_type": "website",
        "seo_title": "Real Property Tax (Amilyar) Calculator, Philippines · Butch Mahinay",
        "description": "Free real property tax (amilyar) calculator for the Philippines: basic tax, SEF, discount or "
                       "interest by date of payment, and each share for the province, municipality and barangay.",
        "body": [
            t.p("Free tool", class_="eyebrow"),
            t.h1("Real Property Tax Calculator"),
            t.p("Work out the yearly real property tax (amilyar) on a piece of land or a building, then see where "
                "every peso goes: the province, the municipality, the barangay and the school boards. "
                "Based on the Local Government Code of 1991 (RA 7160), with the rules of a provincial "
                "revenue code built in.", class_="lead"),
            _guide_link(),
            t.form(
                t.fieldset(
                    t.legend("1. Where is the property?"),
                    t.div(_radio("lgu", "prov", "In a municipality (built-in provincial rates)", True),
                          _radio("lgu", "mun", "In a municipality (type your own rates)"),
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
                                   "Fills in the assessment level from the built-in provincial revenue code."),
                            id="prov-class", class_="field-pair",
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
                            "Taxes of earlier years are fully paid, or paid in this same payment", class_="choice prior-paid"),
                    _field("Discount for paying on time (%)", _num("disc", "10", maximum="20"),
                           "Set by your local ordinance, up to 20%.", row_id="disc-row", hidden=True),
                    t.p("Built-in provincial discount, worked out from the date: 10% if paid on or before the "
                        "installment deadlines, 15% if the whole year is paid on or before September 30 of the year before, and 20% "
                        "if paid two or more years in advance. The discount is for quarters paid now on or before their due "
                        "date, even when late quarters are settled in the same payment, but not when an earlier "
                        "year is unpaid.",
                        id="prov-disc", class_="hint block-hint"),
                    t.p("The year's tax is split into four equal quarters, due March 31, June 30, September 30 and "
                        "December 31. A quarter paid after its due date earns interest of 2% for each month or part of "
                        "a month, up to 36 months; with the built-in provincial rates it is counted from the start of the earliest late quarter, 2% for each whole month before the month of payment. Mark the quarters already paid as \"Paid\"; every quarter "
                        "marked \"Not paid\" is added to the amount to pay: 10% off if paid on time, interest if late.", class_="hint block-hint"),
                ),
                id="rpt", class_="card rpt-form", novalidate=True, autocomplete="off",  # no restored choices from an earlier visit (Butch 2026-11-28)
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
            # Butch's wording, from his Google Doc "aumahinay.dev Educational & Tax Disclaimers", part 1 (2026-11-20):
            # right under the calculator, in a callout box
            t.div(
                t.h3("Educational & Estimation Disclaimer"),
                t.p("The Real Property Tax (RPT) Calculator on aumahinay.dev is provided strictly for educational, informational, "
                    "and general estimation purposes only. While the computation logic reflects standard principles under the "
                    "Local Government Code of 1991 (Republic Act No. 7160) and the Real Property Valuation and Assessment Reform "
                    "Act (Republic Act No. 12001), actual tax liabilities vary based on your local government unit's (LGU) "
                    "prevailing Revenue Code, Schedule of Fair Market Values (SMV), assessment levels, Special Education Fund "
                    "(SEF) rates, idle land levies, prompt-payment discounts, and accrued delinquency penalties."),
                t.p("Output generated by this tool does not constitute an official tax assessment, billing statement, or legal "
                    "opinion. Always verify your exact real property tax dues directly with your local Municipal, City, or "
                    "Provincial Treasurer's Office and Assessor's Office before making any payment or financial decision."),
                class_="disclaimer rpt-disclaimer",
            ),
            *_explanations(),
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
                t.li(t.b("Older unpaid taxes first. "), "Payments are applied first to unpaid taxes, interest and penalties of "
                     "earlier years, and only then to the current year (Sec. 250). This calculator works out one tax year at a time, "
                     "so if you owe more than one year, run it once for each year, oldest first."),
                t.li(t.b("Not included. "), "The idle land tax (3% under the built-in provincial rates), special levies, and the lower SEF rate for "
                     "renewable energy property (0.5% under the built-in provincial rates, under RA 9513) are not covered here."),
                t.li(t.b("New property values. "), "Under the Real Property Valuation and Assessment Reform Act (RA 12001, 2024), "
                     "the increase in real property tax in the first year of a new schedule of market values is capped at 6%."),
                t.li(t.b("Metro Manila. "), "Municipalities in Metro Manila follow a different sharing rule, so this "
                     "calculator does not cover them."),
                class_="plain-list rpt-notes",
            ),
            *_faq(),
            _read_more(),
            t.p("Sources: ", t.a("Local Government Code of 1991 (RA 7160)", href=law, rel="noopener"), ", Secs. 218, 233, 235, "
                "250, 251, 255, 257, 271 and 272; ",
                t.a("RA 12001", href="https://lawphil.net/statutes/repacts/ra2024/ra_12001_2024.html", rel="noopener"),
                ", Sec. 29; built-in provincial rates from a provincial Revised Revenue Code of 2022, "
                "Secs. 25, 39, 40, 41, 43, 44, 45, 47 and 52. Last checked " + RPT_CHECKED + ".", class_="muted note sources-line"),
            t.p("Figures are worked out in your browser and nothing you type is sent or saved.", class_="muted note"),
            t.script(Raw(RPT_SCRIPT)),
        ],
    }
