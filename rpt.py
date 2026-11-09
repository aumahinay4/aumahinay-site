"""Real Property Tax (RPT) calculator: /tools/rpt-calculator/ (Butch 2026-11-09).

Computes the basic RPT and the Special Education Fund (SEF) tax on a property's assessed value,
with the advance-payment discount or the interest on late payment, and shows how the money is
shared among the province, municipality and barangay (or city and barangays) and the school boards.

Rules (Republic Act No. 7160, the Local Government Code of 1991):
- Sec. 218: assessed value = market value x assessment level (levels set by ordinance).
- Sec. 233: basic RPT rate, province up to 1%, city or Metro Manila municipality up to 2%.
- Sec. 235: additional 1% for the Special Education Fund.
- Sec. 251: discount of up to 20% for advance or prompt payment, as set by ordinance.
- Sec. 255: interest of 2% a month on unpaid tax, for at most 36 months (72%).
- Sec. 271: basic RPT including interest: province 35%, municipality 40%, barangay 25%;
            city 70%, barangays 30% (half to the barangay where the property is, half shared
            equally by all barangays of the city).
- Sec. 272: SEF goes to the local school boards; in provinces, split equally between the
            provincial and municipal school boards.
RA 12001 (2024) caps the first-year increase after a new schedule of market values at 6%;
it does not change the rates or the sharing.
"""

import tags as t
from tags import Raw

RPT_URL = "/tools/rpt-calculator/"
RPT_CHECKED = "November 2026"

RPT_SCRIPT = r"""
(function () {
  var f = document.getElementById('rpt');
  if (!f) return;
  var $ = function (id) { return document.getElementById(id); };
  var peso = function (n) { return (n < 0 ? '−' : '') + '₱' + Math.abs(n).toLocaleString('en-PH', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var r2 = function (n) { return Math.round((n + Number.EPSILON) * 100) / 100; };
  var num = function (id) { var v = parseFloat(String($(id).value).replace(/,/g, '')); return isFinite(v) && v > 0 ? v : 0; };
  var lastLgu = null;

  function calc() {
    var lgu = f.lgu.value, city = lgu === 'city';
    if (lgu !== lastLgu) { $('basic-rate').value = city ? '2' : '1'; lastLgu = lgu; }
    $('brgy-count-row').hidden = !city;
    var useMv = f.basis.value === 'mv';
    $('mv-rows').hidden = !useMv; $('av-row').hidden = useMv;
    var av = useMv ? r2(num('mv') * Math.min(num('level'), 100) / 100) : num('av');
    var bRate = Math.min(num('basic-rate'), city ? 2 : 1), sRate = Math.min(num('sef-rate'), 1);
    var basic = r2(av * bRate / 100), sef = r2(av * sRate / 100);
    var when = f.when.value, disc = 0, months = 0;
    $('disc-row').hidden = when !== 'early'; $('late-row').hidden = when !== 'late';
    if (when === 'early') disc = Math.min(num('disc'), 20);
    if (when === 'late') months = Math.min(Math.floor(num('months')), 36);
    var bAdj = when === 'early' ? -r2(basic * disc / 100) : r2(basic * months * 2 / 100);
    var sAdj = when === 'early' ? -r2(sef * disc / 100) : r2(sef * months * 2 / 100);
    var bDue = r2(basic + bAdj), sDue = r2(sef + sAdj);
    var adjLabel = when === 'early' ? 'Discount (' + disc + '%)' : when === 'late' ? 'Interest (2% × ' + months + ' month' + (months === 1 ? '' : 's') + ' = ' + (months * 2) + '%)' : 'Discount or interest';

    $('out-av').textContent = peso(av);
    $('t-basic').textContent = peso(basic); $('t-sef').textContent = peso(sef); $('t-tax').textContent = peso(r2(basic + sef));
    $('t-adj-label').textContent = adjLabel;
    $('t-badj').textContent = peso(bAdj); $('t-sadj').textContent = peso(sAdj); $('t-adj').textContent = peso(r2(bAdj + sAdj));
    $('t-bdue').textContent = peso(bDue); $('t-sdue').textContent = peso(sDue); $('t-due').textContent = peso(r2(bDue + sDue));
    $('out-due').textContent = peso(r2(bDue + sDue));

    var rows = [], sum = 0;
    function add(who, base, pct, note) { var a = r2(base * pct / 100); sum = r2(sum + a); rows.push([who, pct + '%', a, note || '']); }
    if (city) {
      add('City general fund', bDue, 70);
      add('Barangay where the property is', bDue, 15, 'half of the 30% barangay share');
      var n = Math.floor(num('brgy-count'));
      var pool = r2(bDue * 15 / 100);
      add('All barangays of the city, shared equally', bDue, 15, n > 0 ? peso(r2(pool / n)) + ' each for ' + n + ' barangays' : 'enter the number of barangays to see each one');
      var sefRow = ['City school board', '100%', sDue, 'all of the SEF']; rows.push(sefRow); sum = r2(sum + sDue);
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
  f.addEventListener('input', calc);
  f.addEventListener('change', calc);
  f.addEventListener('submit', function (e) { e.preventDefault(); calc(); });
  calc();
})();
"""


def _field(label, control, hint=None, row_id=None, hidden=False):
    return t.div(t.label(label, control, t.small(hint, class_="hint") if hint else None),
                 class_="field", id=row_id, hidden=hidden)


def _num(id_, value="", step="any", minimum="0", maximum=None, placeholder=None):
    return t.input(type="number", id=id_, name=id_, value=value, step=step, min=minimum, max=maximum,
                   inputmode="decimal", placeholder=placeholder)


def _radio(name, value, label, checked=False):
    return t.label(t.input(type="radio", name=name, value=value, checked=checked), " ", label, class_="choice")


def rpt_page():
    law = "https://lawphil.net/statutes/repacts/ra1991/ra_7160_1991.html"
    return {
        "title": "RPT Calculator", "active": RPT_URL, "url": RPT_URL, "og_type": "website",
        "description": "Free real property tax (RPT) calculator for the Philippines: basic tax, SEF, discount or "
                       "interest, and how the tax is shared among the province, municipality, barangay and school boards.",
        "body": [
            t.p("Free tool", class_="eyebrow"),
            t.h1("Real Property Tax Calculator"),
            t.p("Work out the yearly real property tax (amilyar) on a piece of land or a building, then see where "
                "every peso goes: the province, the municipality, the barangay and the school boards. "
                "Based on the Local Government Code of 1991 (RA 7160).", class_="lead"),
            t.form(
                t.fieldset(
                    t.legend("1. Where is the property?"),
                    t.div(_radio("lgu", "mun", "In a municipality of a province", True),
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
                        _field("Market value (₱)", _num("mv", "500000")),
                        _field("Assessment level (%)", _num("level", "20", maximum="100"),
                               "Set by ordinance for each class of property, e.g. 20% for residential land.",
                               ),
                        id="mv-rows", hidden=True, class_="field-pair",
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
                    t.div(_radio("when", "early", "In advance, with discount", True),
                          _radio("when", "due", "On time, no discount"),
                          _radio("when", "late", "Late, with interest"), class_="choices"),
                    _field("Discount (%)", _num("disc", "10", maximum="20"),
                           "Set by your local ordinance, up to 20%.", row_id="disc-row"),
                    _field("Months late", _num("months", "3", step="1", maximum="36"),
                           "Interest is 2% a month, up to 36 months (72%).", row_id="late-row", hidden=True),
                ),
                id="rpt", class_="card rpt-form", novalidate=True,
            ),
            t.div(
                t.p("Assessed value ", t.b("—", id="out-av"), class_="rpt-av"),
                t.p("Amount to pay", class_="rpt-due-label"),
                t.p("—", id="out-due", class_="rpt-due"),
                t.div(
                    t.table(
                        t.thead(t.tr(t.th(""), t.th("Basic RPT"), t.th("SEF"), t.th("Total"))),
                        t.tbody(
                            t.tr(t.th("Tax for the year", scope="row"), t.td(id="t-basic"), t.td(id="t-sef"), t.td(id="t-tax")),
                            t.tr(t.th("Discount or interest", scope="row", id="t-adj-label"), t.td(id="t-badj"), t.td(id="t-sadj"), t.td(id="t-adj")),
                            t.tr(t.th("To pay", scope="row"), t.td(id="t-bdue"), t.td(id="t-sdue"), t.td(id="t-due"), class_="total"),
                        ),
                        class_="rpt-table",
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
                     "is the market value times the assessment level set by ordinance for the property's class and use (Sec. 218)."),
                t.li(t.b("Discount. "), "Your province or city may give a discount of up to 20% for paying in advance "
                     "or on time; the rate and deadline are in the local ordinance (Sec. 251)."),
                t.li(t.b("Interest. "), "Unpaid tax earns interest of 2% a month, up to 36 months, until it is paid in full (Sec. 255)."),
                t.li(t.b("Installments. "), "The tax may be paid in four quarterly installments, due on or before "
                     "March 31, June 30, September 30 and December 31 (Sec. 250)."),
                t.li(t.b("New property values. "), "Under the Real Property Valuation and Assessment Reform Act (RA 12001, 2024), "
                     "the increase in real property tax in the first year of a new schedule of market values is capped at 6%."),
                t.li(t.b("Metro Manila. "), "Municipalities in Metro Manila follow a different sharing rule, so this "
                     "calculator does not cover them."),
                class_="plain-list rpt-notes",
            ),
            t.p("Sources: ", t.a("Local Government Code of 1991 (RA 7160)", href=law, rel="noopener"), ", Secs. 218, 233, 235, "
                "250, 251, 255, 271 and 272; ",
                t.a("RA 12001", href="https://lawphil.net/statutes/repacts/ra2024/ra_12001_2024.html", rel="noopener"),
                ", Sec. 29. Last checked " + RPT_CHECKED + ".", class_="muted note sources-line"),
            t.p("This calculator is a study aid, not an official assessment. Your actual tax depends on your local "
                "ordinances and the tax declaration; your municipal, city or provincial treasurer's office has the final "
                "figures. Figures are worked out in your browser and nothing you type is sent or saved.",
                class_="disclaimer"),
            t.script(Raw(RPT_SCRIPT)),
        ],
    }
