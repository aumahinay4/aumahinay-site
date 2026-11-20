/* ALTOS demo (aumahinay.dev/projects/altos-demo/). Everything here is made up and lives only in this browser tab:
   no server, no database, nothing is saved. Reloading the page starts the demo fresh.
   The screens copy the look and the steps of ALTOS, the Automated Local Treasury Operations System. */
(function () {
  'use strict';
  var root = document.getElementById('altos-demo');
  if (!root) return;

  // ------------------------------------------------------------------ helpers
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function r2(n) { return Math.round((n + Number.EPSILON) * 100) / 100; }
  function money(n) {
    return (n < 0 ? '−' : '') + Math.abs(n).toLocaleString('en-PH', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }
  function peso(n) { return '₱' + money(n); }
  function num(v) { var x = parseFloat(String(v == null ? '' : v).replace(/,/g, '')); return isFinite(x) ? x : 0; }
  function blend(c1, c2, t) {
    var a = [1, 3, 5].map(function (i) { return parseInt(c1.substr(i, 2), 16); });
    var b = [1, 3, 5].map(function (i) { return parseInt(c2.substr(i, 2), 16); });
    return '#' + a.map(function (x, i) { var v = Math.round(x + (b[i] - x) * t); return (v < 16 ? '0' : '') + v.toString(16); }).join('');
  }
  var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  var DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

  // today and the time in the Philippines (UTC+8), whatever the visitor's own time zone
  function phNow() { return new Date(Date.now() + 8 * 3600 * 1000); }
  var NOW = phNow();
  var YEAR = NOW.getUTCFullYear(), MONTH = NOW.getUTCMonth(), DAY = NOW.getUTCDate();
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  var TODAY = YEAR + '-' + pad(MONTH + 1) + '-' + pad(DAY);
  function longDate(iso) {
    var p = iso.split('-');
    return MONTHS[+p[1] - 1] + ' ' + (+p[2]) + ', ' + p[0];
  }
  function shortDate(iso) { var p = iso.split('-'); return MONTHS[+p[1] - 1].slice(0, 3) + ' ' + (+p[2]); }
  function clock(d) {
    var h = d.getUTCHours(), m = d.getUTCMinutes();
    return ((h % 12) || 12) + ':' + pad(m) + (h < 12 ? ' AM' : ' PM');
  }
  function timeNow() { return clock(phNow()); }
  // an earlier day of this month for the sample records (never later than today)
  function dayOfMonth(d) { return YEAR + '-' + pad(MONTH + 1) + '-' + pad(Math.max(1, Math.min(d, DAY))); }

  // ------------------------------------------------------------------ the made-up LGU
  var LGU = { province: 'Sample Province', name: 'Sample Municipality', office: 'Office of the Municipal Treasurer',
    short: 'SAMPLE MUNICIPALITY, SAMPLE PROVINCE', treasurer: 'Elena Torres', treasurerTitle: 'Municipal Treasurer', bank: 'Sample Bank' };
  var ACCOUNTS = {
    GF: { name: 'General Fund', bank: 'Current Account ending 0001', line: 'GENERAL FUND SAMPLE BANK CA#0000-0000-01' },
    SEF: { name: 'Special Education Fund', bank: 'Current Account ending 0002', line: 'SPECIAL EDUCATION FUND SAMPLE BANK CA#0000-0000-02' }
  };
  var ROLES = {
    col: { label: 'Collecting Officer', page: 'COLLECTING OFFICER PAGE', a: '#1f6fd1', sel: '#3d8cf0', tint: '#7cc2ff', key: '#2f80d8', user: 'Maria Santos' },
    lo: { label: 'Liquidating Officer', page: 'LIQUIDATING OFFICER PAGE', a: '#0f8a6a', sel: '#16ad86', tint: '#4be3a8', key: '#22a06b', user: 'Ana Cruz' },
    do: { label: 'Disbursing Officer', page: 'DISBURSING OFFICER PAGE', a: '#c23a4f', sel: '#e05568', tint: '#ff8a8a', key: '#bf4040', user: 'Ramon Garcia' },
    sys: { label: 'System Administrator', page: 'SYSADMIN PAGE', a: '#6a3fc8', sel: '#8a63e6', tint: '#d1b6ff', key: '#7d58d6', user: 'Leo Mercado' }
  };
  // the menus as in ALTOS's web pages (same labels and order; the demo shows only some of each)
  var MENUS = {
    col: [['home', 'Home'], ['issue', 'Issue Official Receipt'], ['rptcalc', 'RPT Tax Calculator'], ['collections', 'My Collections'], ['rcd', 'My RCD'], ['raaf', 'My RAAF'], ['cashbook', 'My Cash Book']],
    lo: [['home', 'Home'], ['crcd', 'Consolidated RCD'], ['refused', 'Refused Reports'], ['craaf', 'RAAF & CRAAF'], ['register', 'Collections Register'], ['locash', 'My Cash Book'], ['cashbook', 'Cash Book']],
    do: [['home', 'Home'], ['prepare', 'Prepare Check'], ['checks', 'Check Issuance'], ['cashbook', 'Cash Book']],
    sys: [['home', 'Home'], ['#', 'CONTROL & SECURITY'], ['log', 'Activity Log'], ['#', 'COLLECTIONS'], ['dashboard', 'Collections Dashboard'],
      ['register', 'Collections Register'], ['#', 'REPORTING'], ['cashbook', 'Cash Book']]
  };
  // Revenue Code schedule (sample fees; a real LGU's amounts are in its own Revenue Code)
  var FEES = [
    { name: "Mayor's Permit Fee", amount: 500, fund: 'GF' },
    { name: 'Business Tax (Retailers)', amount: 0, fund: 'GF' },
    { name: 'Sanitary Inspection Fee', amount: 200, fund: 'GF' },
    { name: 'Garbage Fee', amount: 300, fund: 'GF' },
    { name: 'Market Stall Rental (1 month)', amount: 1500, fund: 'GF' },
    { name: 'Slaughter Fee (per head)', amount: 150, fund: 'GF' },
    { name: 'Building Permit Fee', amount: 0, fund: 'GF' },
    { name: 'Certification Fee', amount: 100, fund: 'GF' },
    { name: 'Burial Permit Fee', amount: 100, fund: 'GF' }
  ];
  // RPT settings of the demo: basic tax 1%, SEF 1%, 10% discount for paying on time, 2% interest a month up to 36 months
  var RPT = { basic: 0.01, sef: 0.01, disc: 0.10, interest: 0.02, maxMonths: 36 };

  // ------------------------------------------------------------------ the demo's records (fresh on every load)
  var S;
  function fresh() {
    S = {
      role: null, page: 'home',
      ors: [], rcds: [], crcds: [], raaf: {}, seen: {}, checks: [], log: [], flash: null,
      next: { or51: 1234504, or56: 5670012, rcd: 43, crcd: 1, check: { GF: 4507, SEF: 1203 }, dv: 87 },
      props: [
        { pin: '001-01-001-01-015', td: 'TD 2026-01-00215', owner: 'Juan dela Cruz', brgy: 'Poblacion', kind: 'Residential land', av: 120000, paid: [YEAR, 2] },
        { pin: '001-01-001-02-044', td: 'TD 2026-01-00344', owner: 'Rosa Mendoza', brgy: 'Poblacion', kind: 'Commercial building', av: 850000, paid: [YEAR, 4] },
        { pin: '001-01-007-03-102', td: 'TD 2026-07-00102', owner: 'Andres Villanueva', brgy: 'Malinis', kind: 'Agricultural land', av: 45000, paid: [YEAR - 2, 4] },
        { pin: '001-01-004-01-021', td: 'TD 2026-04-00021', owner: 'Teresa Bautista', brgy: 'Bagong Silang', kind: 'Residential building', av: 210000, paid: [YEAR, 3] },
        { pin: '001-01-002-05-009', td: 'TD 2026-02-00009', owner: 'Carlos Navarro', brgy: 'San Roque', kind: 'Commercial land', av: 600000, paid: [YEAR - 3, 4] }
      ],
      cash: { GF: [], SEF: [] }
    };
    var t8 = function (h, m) { return (h % 12 || 12) + ':' + pad(m) + (h < 12 ? ' AM' : ' PM'); };
    // Maria Santos (the visitor, as Collecting Officer): four ORs today, not yet reported
    addOr('col', 'Maria Santos', '51', 1234501, 'Liza Fernandez', [["Mayor's Permit Fee", 500, 'GF'], ['Sanitary Inspection Fee', 200, 'GF'], ['Garbage Fee', 300, 'GF']], t8(8, 14));
    addOr('col', 'Maria Santos', '51', 1234502, 'Pedro Aquino', [['Certification Fee', 100, 'GF']], t8(8, 41));
    addOr('col', 'Maria Santos', '51', 1234503, "Nena's Sari-Sari Store", [['Business Tax (Retailers)', 2350, 'GF'], ["Mayor's Permit Fee", 500, 'GF']], t8(9, 5)).check = '0012345';
    addOr('col', 'Maria Santos', '56', 5670011, 'Rosa Mendoza', [['Real Property Tax – Basic (2026 Q4)', 1912.5, 'GF'], ['Real Property Tax – SEF (2026 Q4)', 1912.5, 'SEF']], t8(9, 32), '001-01-001-02-044');
    // Jose Reyes: today's RCD already remitted to the Liquidating Officer, money complete
    var j = [
      addOr('col2', 'Jose Reyes', '51', 1234551, 'Ramon Dizon', [['Building Permit Fee', 3250, 'GF']], t8(8, 20)),
      addOr('col2', 'Jose Reyes', '51', 1234552, 'Gloria Lim', [["Mayor's Permit Fee", 500, 'GF'], ['Business Tax (Retailers)', 1800, 'GF']], t8(8, 55)),
      addOr('col2', 'Jose Reyes', '51', 1234553, 'Felix Torres', [['Slaughter Fee (per head)', 300, 'GF']], t8(9, 40)),
      addOr('col2', 'Jose Reyes', '51', 1234554, 'Cora Valdez', [['Burial Permit Fee', 100, 'GF']], t8(10, 12)),
      addOr('col2', 'Jose Reyes', '51', 1234555, 'Daniel Ocampo', [['Certification Fee', 100, 'GF'], ['Garbage Fee', 300, 'GF']], t8(10, 47)),
      addOr('col2', 'Jose Reyes', '51', 1234556, 'Alma Pascual', [['Sanitary Inspection Fee', 200, 'GF'], ['Market Stall Rental (1 month)', 1500, 'GF']], t8(11, 3))
    ];
    S.rcds.push({ no: 'RCD ' + YEAR + '-' + pad(MONTH + 1) + '-041', officer: 'Jose Reyes', account: 'GF', date: TODAY, ors: j,
      total: sumOrs(j, 'GF'), cash: sumOrs(j, 'GF'), status: 'Submitted', time: t8(11, 30) });
    // Luz Ramos (market collector): remitted ₱50.00 less than her report
    var l = [
      addOr('col3', 'Luz Ramos', '51', 1234601, 'Stall 12, Public Market', [['Market Stall Rental (1 month)', 1500, 'GF']], t8(7, 50)),
      addOr('col3', 'Luz Ramos', '51', 1234602, 'Stall 27, Public Market', [['Market Stall Rental (1 month)', 1500, 'GF']], t8(8, 6)),
      addOr('col3', 'Luz Ramos', '51', 1234603, 'Fish Section, Vendor 4', [['Garbage Fee', 250, 'GF']], t8(8, 30))
    ];
    S.rcds.push({ no: 'RCD ' + YEAR + '-' + pad(MONTH + 1) + '-042', officer: 'Luz Ramos', account: 'GF', date: TODAY, ors: l,
      total: sumOrs(l, 'GF'), cash: r2(sumOrs(l, 'GF') - 50), status: 'Submitted', time: t8(11, 45) });
    l.concat(j).forEach(function (o) { o.reported = true; });
    // the Cash Book this month
    var ob = { GF: 2450000, SEF: 380000 };
    ['GF', 'SEF'].forEach(function (k) {
      S.cash[k].push({ date: dayOfMonth(1), ref: '', what: 'Balance brought forward', dr: 0, cr: 0, bal: ob[k] });
    });
    cashIn('GF', dayOfMonth(3), 'CRCD ' + MO + '004 / DS 70211', 'Deposit of collections', 186420.5);
    cashOut('GF', dayOfMonth(4), 'Check 0004503', 'Sample Office Supply Co. – office supplies (DV ' + MO + '071)', 48500);
    cashIn('SEF', dayOfMonth(5), 'CRCD ' + MO + '006 / DS 70218', 'Deposit of collections (SEF share of RPT)', 23880);
    cashOut('GF', dayOfMonth(6), 'Check 0004504', 'Sample Electric Cooperative – electricity, October (DV ' + MO + '076)', 32180.55);
    cashIn('GF', dayOfMonth(10), 'CRCD ' + MO + '011 / DS 70240', 'Deposit of collections', 142310);
    cashOut('SEF', dayOfMonth(11), 'Check 0001202', 'Sample Printing Press – school forms (DV ' + MO + '080)', 18750);
    cashOut('GF', dayOfMonth(12), 'Check 0004505', 'Sample Fuel Station – fuel for service vehicles (DV ' + MO + '082)', 15600);
    cashOut('GF', dayOfMonth(14), 'Check 0004506', 'Sample Hardware – repair of the public market roof (DV ' + MO + '085)', 96375);
    S.checks.push(
      { no: '0004503', account: 'GF', date: dayOfMonth(4), payee: 'Sample Office Supply Co.', what: 'Office supplies', dv: 'DV ' + MO + '071', amount: 48500, status: 'Released', to: 'Sample Office Supply Co.' },
      { no: '0004504', account: 'GF', date: dayOfMonth(6), payee: 'Sample Electric Cooperative', what: 'Electricity, October', dv: 'DV ' + MO + '076', amount: 32180.55, status: 'Released', to: 'Sample Electric Cooperative' },
      { no: '0001202', account: 'SEF', date: dayOfMonth(11), payee: 'Sample Printing Press', what: 'School forms', dv: 'DV ' + MO + '080', amount: 18750, status: 'Released', to: 'Sample Printing Press' },
      { no: '0004505', account: 'GF', date: dayOfMonth(12), payee: 'Sample Fuel Station', what: 'Fuel for service vehicles', dv: 'DV ' + MO + '082', amount: 15600, status: 'Released', to: 'Sample Fuel Station' },
      { no: '0004506', account: 'GF', date: dayOfMonth(14), payee: 'Sample Hardware', what: 'Repair of the public market roof', dv: 'DV ' + MO + '085', amount: 96375, status: 'Prepared', to: '' }
    );
    S.log = [
      { time: t8(7, 46), user: 'Luz Ramos', role: 'Collecting Officer', what: 'Signed in' },
      { time: t8(7, 50), user: 'Luz Ramos', role: 'Collecting Officer', what: 'Issued OR No. 1234601 (AF 51) for ₱1,500.00' },
      { time: t8(8, 2), user: 'Maria Santos', role: 'Collecting Officer', what: 'Signed in' },
      { time: t8(8, 14), user: 'Maria Santos', role: 'Collecting Officer', what: 'Issued OR No. 1234501 (AF 51) for ₱1,000.00' },
      { time: t8(8, 20), user: 'Jose Reyes', role: 'Collecting Officer', what: 'Issued OR No. 1234551 (AF 51) for ₱3,250.00' },
      { time: t8(9, 32), user: 'Maria Santos', role: 'Collecting Officer', what: 'Issued OR No. 5670011 (AF 56) for ₱3,825.00' },
      { time: t8(11, 30), user: 'Jose Reyes', role: 'Collecting Officer', what: 'Remitted RCD ' + YEAR + '-' + pad(MONTH + 1) + '-041 (General Fund) for ' + peso(sumOrs(j, 'GF')) },
      { time: t8(11, 45), user: 'Luz Ramos', role: 'Collecting Officer', what: 'Remitted RCD ' + YEAR + '-' + pad(MONTH + 1) + '-042 (General Fund) for ' + peso(sumOrs(l, 'GF')) }
    ];
  }
  function addOr(officer, name, form, no, payor, lines, time, pin) {
    var o = { no: String(no), form: form, officer: officer, name: name, payor: payor, date: TODAY, time: time || timeNow(), pin: pin || '',
      lines: lines.map(function (x) { return { nature: x[0], amount: x[1], fund: x[2] }; }), reported: false };
    o.total = r2(o.lines.reduce(function (s, x) { return s + x.amount; }, 0));
    S.ors.push(o);
    return o;
  }
  function sumOrs(ors, fund) {
    return r2(ors.reduce(function (s, o) {
      return s + o.lines.reduce(function (t, x) { return t + (!fund || x.fund === fund ? x.amount : 0); }, 0);
    }, 0));
  }
  function balance(acct) { var c = S.cash[acct]; return c[c.length - 1].bal; }
  function cashIn(acct, date, ref, what, amt) { S.cash[acct].push({ date: date, ref: ref, what: what, dr: amt, cr: 0, bal: r2(balance(acct) + amt) }); }
  function cashOut(acct, date, ref, what, amt) { S.cash[acct].push({ date: date, ref: ref, what: what, dr: 0, cr: amt, bal: r2(balance(acct) - amt) }); }
  function log(what) { S.log.push({ time: timeNow(), user: ROLES[S.role].user, role: ROLES[S.role].label, what: what }); }

  // ------------------------------------------------------------------ real property tax, quarter by quarter
  // Each quarter is a fourth of the year's tax, due on the last day of March, June, September and December.
  // Paid on or before the due date (and nothing earlier unpaid): 10% discount. Late: 2% for each month or part of a month, up to 36 months.
  function rptDue(p, payIso, wholeYear) {
    var py = +payIso.slice(0, 4), pm = +payIso.slice(5, 7) - 1;
    var lastQ = wholeYear ? 4 : Math.floor(pm / 3) + 1;
    var y = p.paid[0], q = p.paid[1], rows = [], late = false;
    var qBasic = r2(p.av * RPT.basic / 4), qSef = r2(p.av * RPT.sef / 4);
    while (true) {
      q += 1; if (q > 4) { q = 1; y += 1; }
      if (y > py || (y === py && q > lastQ)) break;
      var dueM = q * 3 - 1;  // the month index of the due date (end of the month)
      var months = (py - y) * 12 + (pm - dueM);
      var row = { year: y, q: q, basic: qBasic, sef: qSef, months: 0, rate: 0, kind: '' };
      if (months > 0) {
        row.months = Math.min(months, RPT.maxMonths);
        row.rate = row.months * RPT.interest; row.kind = 'interest'; late = true;
      }
      rows.push(row);
    }
    rows.forEach(function (row) {
      if (!row.kind && !late) { row.rate = -RPT.disc; row.kind = 'discount'; }
      row.badj = r2(row.basic * row.rate); row.sadj = r2(row.sef * row.rate);
      row.bdue = r2(row.basic + row.badj); row.sdue = r2(row.sef + row.sadj);
      row.due = r2(row.bdue + row.sdue);
    });
    return rows;
  }
  function rptTable(rows) {
    if (!rows.length) return '<div class="msg ok">Nothing is due on this date: the tax is paid up to this quarter.</div>';
    var tt = 0, td = 0;
    var body = rows.map(function (r) {
      var tax = r2(r.basic + r.sef);
      tt += tax; td += r.due;
      var adj = r.kind === 'interest' ? '<span class="chip r">+' + Math.round(r.rate * 100) + '%</span><div class="muted nw">' + r.months + (r.months > 1 ? ' months' : ' month') + ' late</div>'
        : r.kind === 'discount' ? '<span class="chip g">−10%</span><div class="muted nw">on time</div>' : '<span class="chip">no discount</span><div class="muted nw">earlier quarter unpaid</div>';
      return '<tr><td class="nw">' + r.year + ' Q' + r.q + '</td><td class="r">' + money(tax) + '</td><td>' + adj + '</td><td class="r"><b>' + money(r.due) + '</b></td></tr>';
    }).join('');
    return '<div class="tbl"><table><thead><tr><th>Quarter</th><th class="r">Tax</th><th>+/−</th><th class="r">To pay</th></tr></thead><tbody>' + body +
      '<tr class="sum"><td>Total</td><td class="r">' + money(r2(tt)) + '</td><td></td><td class="r">' + money(r2(td)) + '</td></tr></tbody></table></div>' +
      '<p class="muted">Tax: the basic tax and the SEF, each 1% of the assessed value a year, a fourth of it each quarter. +/−: the discount or the interest.</p>';
  }
  function propLabel(p) { return p.pin + ' · ' + p.owner + ' · ' + p.brgy; }
  function findProp(pin) { return S.props.filter(function (p) { return p.pin === pin; })[0]; }

  // ------------------------------------------------------------------ page frame
  function frame(body) {
    var R = ROLES[S.role], navy = '#1a2f66';
    var vars = '--a:' + R.a + ';--sel:' + R.sel + ';--tint:' + R.tint + ';--msel:' + blend(navy, R.sel, 0.55) + ';--appc:' + blend(R.tint, '#ffffff', 0.35) +
      ';--pill:' + blend(R.a, '#ffffff', 0.16) + ';--pillh:' + blend(R.a, '#ffffff', 0.30) + ';--hov:' + blend(R.sel, '#ffffff', 0.88) +
      ';--sideh:' + blend(navy, '#ffffff', 0.10);
    var menu = '';
    MENUS[S.role].forEach(function (m) {
      if (m[0] === '#') { menu += '<div class="head">' + esc(m[1]) + '</div>'; return; }
      var cls = (m[0] === S.page ? 'on' : '') + (m[0] === 'home' ? ' homelink' : '');
      menu += '<a href="#' + S.role + '-' + m[0] + '" class="' + cls.trim() + '"' + (m[0] === S.page ? ' aria-current="page"' : '') + '>' + esc(m[1]) + '</a>';
    });
    if (S.role !== 'sys') menu = '<div class="head">MY WORK</div>' + menu;
    var fl = S.flash ? '<div class="msg ' + S.flash[0] + '">' + S.flash[1] + '</div>' : '';
    S.flash = null;
    return '<div style="' + vars + '"><div class="top"><span class="badge">' + R.page + '</span>' +
      '<span class="app">Automated Local Treasury Operations System · ' + esc(R.user) + '</span>' +
      '<a class="pill" href="#" title="Back to the sign-in page, to pick another working page">Log Out</a></div>' +
      '<div class="strip"><i style="background:#7cc2ff"></i><i style="background:#4be3a8"></i><i style="background:#ff8a8a"></i><i style="background:#d1b6ff"></i></div>' +
      '<div class="wrap"><nav class="side" aria-label="' + esc(R.label) + ' menu">' + menu + '</nav><div class="content"><main class="fadein">' + tourBar() + fl + body + '</main></div></div></div>';
  }
  function about(text) { return '<div class="about"><i></i><p>' + text + '</p></div>'; }
  function go(role, page) { location.hash = role + '-' + page; }
  function flash(kind, html) { S.flash = [kind, html]; }

  // ------------------------------------------------------------------ the sign-in page: pick a working page
  function pickPage() {
    var now = phNow(), i = tourAt();
    var wp = function (r) { return '<button type="button" class="wpb" data-role="' + r + '"><i style="background:' + ROLES[r].key + '"></i>' + ROLES[r].label + '</button>'; };
    var start = i < TOUR.length
      ? '<a class="tourgo" href="#' + TOUR[i].role + '-' + TOUR[i].page + '">' + (i ? 'Continue the tour, step ' + (i + 1) : 'Start the guided tour') + '</a>'
      : '<p class="note"><b>Tour complete.</b> <a href="#" data-act="restart">Start the demo again</a>.</p>';
    return '<div class="lcard"><h1>WELCOME<span style="color:#c2185b">!</span></h1><div class="acc4"><i style="background:#2f80d8"></i>' +
      '<i style="background:#22a06b"></i><i style="background:#bf4040"></i><i style="background:#7d58d6"></i></div>' +
      '<p class="note">In ALTOS each officer signs in with the username and password given by the System Administrator. ' +
      'In this demo, follow the guided tour or open a working page.</p>' + start +
      '<details class="steps"><summary>The 9 steps of the tour</summary><ol class="tourlist">' +
      TOUR.map(function (t) { return '<li class="' + (t.done() ? 'ok' : '') + '"><span style="color:' + ROLES[t.role].key + '">' + ROLES[t.role].label + ':</span> ' + t.title + '</li>'; }).join('') +
      '</ol></details>' +
      '<div class="rule"></div><div class="wp">WORKING PAGES</div><div class="wpg">' + wp('col') + wp('lo') + wp('do') + wp('sys') + '</div></div>' +
      '<div class="lfoot"><div>' + DAYS[now.getUTCDay()] + ', ' + longDate(TODAY) + '</div>' +
      '<div class="cp">© ' + YEAR + ' aumahinay. All rights reserved. · <a href="/projects/">About ALTOS</a></div></div>' +
      // Butch's wording, from his Google Doc "aumahinay.dev Educational & Tax Disclaimers", part 4 (2026-11-20)
      '<div class="notice"><div class="nt">Software Demonstration &amp; Simulation Notice</div>' +
      '<p>This interactive demo of the Automated Local Treasury Operations System (ALTOS) runs on 100% fictitious sample data in a temporary browser session—nothing you enter or modify is saved, and this environment is not connected to any Local Government Unit (LGU) or treasury database.</p>' +
      '<p>Developed independently by Ambrosio U. Mahinay in his private capacity for educational and architectural evaluation only. Not an official system or endorsement of any LGU, BLGF, DOF, or COA. Do not enter real taxpayer or official government records.</p>' +
      '<p class="lk"><a href="/terms/">Terms of Use</a> · <a href="/privacy/">Privacy Policy</a></p></div>';
  }

  // ------------------------------------------------------------------ Home of each working page
  // the Home banner's words, as in ALTOS's web pages (DUTIES and ACTIONS)
  var DUTIES = {
    col: ['As Collecting Officer you may:', ['issue official receipts from the OR series assigned to you, in serial order', 'view your own collections',
      'prepare your own daily RCD per bank account and remit it to the Liquidating Officer'],
      "You cannot see other collecting officers' records or change system settings."],
    lo: ['As Liquidating Officer you may:', ['receive the RCDs and collections of all collecting officers',
      "consolidate the collecting officers' RCDs of the same bank account into one RCD and record the bank deposit",
      'refuse a short remittance or a wrong report, with the reason', 'keep the Cash Book'],
      "You cannot manage users, OR series or bank accounts: that is the System Administrator's page."],
    do: ['As Disbursing Officer you may:', ['prepare checks from the check booklets assigned to you, in serial order',
      'release checks to payees', 'keep the Cash Book'],
      'Every check you prepare is captured automatically in the Cash Book.'],
    sys: ['As System Administrator, on the web you may:', ['monitor all collections, RCDs, checks and disbursements',
      'read everything done in the system in the Activity Log', 'follow the Cash Book'],
      'In ALTOS the System Administrator also manages users, OR series, check booklets, bank accounts and every setting of the system.']
  };
  var ACTIONS = {
    col: [['issue', 'Issue Official Receipt'], ['rcd', 'Prepare My RCD'], ['collections', 'My Collections']],
    lo: [['crcd', 'Consolidated RCD'], ['register', 'Collections Register'], ['refused', 'Refused Reports']],
    do: [['prepare', 'Prepare Check'], ['checks', 'Check Issuance'], ['cashbook', 'Cash Book']],
    sys: [['register', 'Collections Register'], ['dashboard', 'Collections Dashboard'], ['log', 'Activity Log']]
  };
  function home() {
    var R = ROLES[S.role], todo = [];
    if (S.role === 'col') {
      var un = myOrs().filter(function (o) { return !o.reported; });
      todo.push(un.length ? ['', un.length + ' official receipts not yet in an RCD (' + peso(sumOrs(un)) + '). <a href="#col-rcd">Close the day →</a>']
        : ['done', 'All your official receipts are in an RCD. The Liquidating Officer has your collections.']);
      todo.push(['', 'A taxpayer is at the window. <a href="#col-issue">Issue an official receipt →</a>']);
      todo.push(S.raaf.col ? ['done', 'Your RAAF for ' + RAAF_MONTH + ' is with the Liquidating Officer.']
        : ['', 'Your RAAF for ' + RAAF_MONTH + ' is due on or before ' + RAAF_DUE + '. <a href="#col-raaf">Prepare it →</a>']);
    } else if (S.role === 'lo') {
      var sub = S.rcds.filter(function (r) { return r.status === 'Submitted'; });
      sub.forEach(function (r) {
        todo.push(['', esc(r.officer) + ' remitted ' + esc(r.no) + ' (' + ACCOUNTS[r.account].name + ', ' + peso(r.total) + '). <a href="#lo-crcd">Count the money →</a>']);
      });
      if (!sub.length) todo.push(['done', 'No RCD is waiting. Every remittance today has been counted.']);
      var nr = OFFICERS.filter(function (o) { return S.raaf[o[0]]; }).length;
      todo.push(['', 'RAAFs for ' + RAAF_MONTH + ': ' + nr + ' of ' + OFFICERS.length + ' received, due on or before ' + RAAF_DUE + '. <a href="#lo-craaf">RAAF &amp; CRAAF →</a>']);
    } else if (S.role === 'do') {
      var prep = S.checks.filter(function (c) { return c.status === 'Prepared'; });
      prep.forEach(function (c) { todo.push(['', 'Check No. ' + c.no + ' to ' + esc(c.payee) + ' (' + peso(c.amount) + ') is ready for release. <a href="#do-checks">Release it →</a>']); });
      todo.push(['', 'General Fund balance in the Cash Book: <b>' + peso(balance('GF')) + '</b>. <a href="#do-prepare">Prepare a check →</a>']);
    } else {
      var t = S.ors.filter(function (o) { return o.date === TODAY; });
      todo.push(['', 'Collections today: <b>' + peso(sumOrs(t)) + '</b> on ' + t.length + ' official receipts. <a href="#sys-dashboard">Open the dashboard →</a>']);
      todo.push(['', S.log.length + ' actions recorded today. <a href="#sys-log">Open the Activity Log →</a>']);
    }
    var D = DUTIES[S.role];
    return '<div class="banner"><h1>WELCOME!</h1><div class="pos">' + esc(R.user) + ' · ' + R.label + '</div><ul><li style="list-style:none;margin-left:-20px"><b>' + D[0] + '</b></li>' +
      D[1].map(function (d) { return '<li>' + d + '</li>'; }).join('') + '</ul><div class="note">' + D[2] + '</div></div>' +
      '<div class="acts">' + ACTIONS[S.role].map(function (a) { return '<a class="btn primary" href="#' + S.role + '-' + a[0] + '">' + a[1] + '</a>'; }).join('') + '</div>' +
      '<h2>What needs attention today</h2><ul class="todo">' + todo.map(function (x) { return '<li class="' + x[0] + '">' + x[1] + '</li>'; }).join('') + '</ul>' +
      '<p class="muted">' + DAYS[phNow().getUTCDay()] + ', ' + longDate(TODAY) + ' · ' + LGU.name + ' (a made-up LGU)</p>';
  }

  // ------------------------------------------------------------------ Collecting Officer
  function myOrs() { return S.ors.filter(function (o) { return o.officer === 'col'; }); }
  var draft = null;  // the OR being written
  function newDraft(form) {
    draft = { form: form || '51', payor: '', lines: [{ fee: 0, amount: FEES[0].amount }], pin: S.props[0].pin, wholeYear: false };
  }
  function issue() {
    if (!draft) newDraft('51');
    var d = draft, next = d.form === '51' ? S.next.or51 : S.next.or56, total = 0, form;
    if (d.form === '51') {
      form = d.lines.map(function (l, i) {
        total += num(l.amount);
        return '<div class="line"><div><label for="fee' + i + '">Nature of Payment</label><select id="fee' + i + '" data-line="' + i + '" data-f="fee">' +
          FEES.map(function (f, k) { return '<option value="' + k + '"' + (k === +l.fee ? ' selected' : '') + '>' + esc(f.name) + '</option>'; }).join('') +
          '</select></div><div><label for="amt' + i + '">Amount</label><input id="amt' + i + '" inputmode="decimal" data-line="' + i + '" data-f="amount" value="' +
          (l.amount === '' ? '' : esc(l.amount)) + '"></div><div><button type="button" class="small" data-act="del-line" data-line="' + i + '" aria-label="Remove line"' +
          (d.lines.length < 2 ? ' disabled' : '') + '>✕</button></div></div>';
      }).join('') + '<button type="button" class="small" data-act="add-line">+ Add a line</button>' +
        '<p class="muted">Amounts come from the Revenue Code schedule. Taxes and fees with no set amount are typed in.</p>';
    } else {
      var p = findProp(d.pin), rows = rptDue(p, TODAY, d.wholeYear);
      total = r2(rows.reduce(function (s, r) { return s + r.due; }, 0));
      form = '<label for="pin">Property (PIN · owner · barangay)</label><select id="pin" data-f="pin">' +
        S.props.map(function (q) { return '<option value="' + q.pin + '"' + (q.pin === d.pin ? ' selected' : '') + '>' + esc(propLabel(q)) + '</option>'; }).join('') +
        '</select><p class="muted">' + esc(p.td) + ' · ' + esc(p.kind) + ' · assessed value ' + peso(p.av) + ' · paid up to ' + p.paid[0] + ' Q' + p.paid[1] + '</p>' +
        '<label><input type="checkbox" data-f="whole"' + (d.wholeYear ? ' checked' : '') + '>Pay the whole year now</label>' + rptTable(rows);
    }
    var can = total > 0 && (d.form === '56' || String(d.payor).trim());
    return '<h1>Issue Official Receipt</h1>' +
      about('Issue the official receipt in serial order: the payor, then the Nature of Payment from the Revenue Code Schedule (the amount fills in). For the AF 56, pick the PIN: the real property tax due is computed for you.') +
      '<div class="tabs"><button type="button" class="tab' + (d.form === '51' ? ' on' : '') + '" data-act="form" data-v="51">AF 51 · General</button>' +
      '<button type="button" class="tab' + (d.form === '56' ? ' on' : '') + '" data-act="form" data-v="56">AF 56 · Real Property Tax</button></div>' +
      '<div class="card"><div class="row"><div><label>Next OR No.</label><input readonly value="' + next + '"></div>' +
      '<div><label>Date</label><input readonly value="' + longDate(TODAY) + '"></div></div>' +
      (d.form === '51' ? '<label for="payor">Payor</label><input id="payor" data-f="payor" autocomplete="off" placeholder="Name of the person or business paying" value="' + esc(d.payor) + '">' : '') +
      form + '<p>Total: <span class="total" id="or-total">' + peso(total) + '</span></p>' +
      '<button type="button" class="primary" data-act="issue"' + (can ? '' : ' disabled') + '>Issue OR No. ' + next + '</button>' +
      (d.form === '51' && !String(d.payor).trim() ? '<span class="muted">Type the payor\'s name first.</span>' : '') + '</div>';
  }
  function orPaper(o) {
    var lines = o.lines.map(function (l) { return '<tr><td>' + esc(l.nature) + '</td><td class="r">' + money(l.amount) + '</td></tr>'; }).join('');
    return '<div class="paper"><div class="ph">Republic of the Philippines<br><b>' + LGU.name + ' (sample)</b><br>' + LGU.office +
      '<br>Accountable Form No. ' + o.form + (o.form === '56' ? ' · Real Property Tax Receipt' : ' · Official Receipt') + '</div>' +
      '<p>No. <span class="no">' + o.no + '</span> &nbsp; Date: ' + longDate(o.date) + '</p><p>Payor: <b>' + esc(o.payor) + '</b>' +
      (o.pin ? '<br>PIN ' + esc(o.pin) : '') + '</p><table><thead><tr><th>Nature of collection</th><th class="r">Amount</th></tr></thead><tbody>' + lines +
      '<tr class="sum"><td>Total</td><td class="r">' + money(o.total) + '</td></tr></tbody></table>' +
      '<p>Collecting Officer: ' + esc(o.name) + '</p><div class="void">A sample from the ALTOS demo. Not an official receipt.</div></div>';
  }
  function collections() {
    var mine = myOrs(), sel = S.view && findOr(S.view);
    S.view = null;
    return '<h1>My Collections</h1>' + about('Your official receipts for the period, with the total. Tap an OR No. to see it.') +
      (sel ? orPaper(sel) : '') +
      '<div class="tbl"><table><thead><tr><th>OR No.</th><th>Form</th><th>Time</th><th>Payor</th><th class="r">Amount</th><th>In an RCD?</th></tr></thead><tbody>' +
      mine.slice().reverse().map(function (o) {
        return '<tr><td><a href="#col-collections" data-act="view-or" data-v="' + o.no + '">' + o.no + '</a></td><td class="nw">AF ' + o.form + '</td><td class="nw">' + o.time +
          '</td><td>' + esc(o.payor) + '</td><td class="r">' + money(o.total) + '</td><td>' + (o.reported ? '<span class="chip g">Yes</span>' : '<span class="chip y">Not yet</span>') + '</td></tr>';
      }).join('') + '<tr class="sum"><td colspan="4">Total, ' + mine.length + ' receipts</td><td class="r">' + money(sumOrs(mine)) + '</td><td></td></tr></tbody></table></div>';
  }
  function findOr(no) { return S.ors.filter(function (o) { return o.no === no; })[0]; }
  function seriesRange(list) {
    if (!list.length) return ['', '', 0];
    var n = list.map(function (o) { return +o.no; }).sort(function (a, b) { return a - b; });
    return [n[0], n[n.length - 1], n.length];
  }
  function rcd() {
    var un = myOrs().filter(function (o) { return !o.reported; });
    var mine = S.rcds.filter(function (r) { return r.officer === 'Maria Santos'; });
    var view = S.viewRcd && S.rcds.filter(function (r) { return r.no === S.viewRcd; })[0];
    S.viewRcd = null;
    var past = mine.length ? '<h2>My RCDs today</h2><div class="tbl"><table><thead><tr><th>RCD No.</th><th>Account</th><th class="r">Amount</th><th>Status</th><th></th></tr></thead><tbody>' +
      mine.map(function (r) {
        return '<tr><td class="nw">' + esc(r.no) + '</td><td>' + ACCOUNTS[r.account].name + '</td><td class="r">' + money(r.total) + '</td><td>' + statusChip(r.status) +
          '</td><td><button type="button" class="small" data-act="view-rcd" data-v="' + esc(r.no) + '">View RCD</button></td></tr>';
      }).join('') + '</tbody></table></div>' : '';
    var head = '<h1>My RCD</h1>' +
      about('Close the day per bank account: the RCD covers all your unreported ORs up to the date, with C. Accountability for Accountable Forms and D. Summary of Collections and Remittances/Deposits. Remit your collections to the Liquidating Officer.');
    if (view) return head + rcdBlock(view, 'Remitted at ' + view.time + '. Status: ' + view.status + '.') + past;
    if (!un.length) return head + '<div class="msg ok">All your official receipts are in an RCD. Issue a new OR to start another.</div>' + past;
    var accts = ['GF', 'SEF'].filter(function (k) { return sumOrs(un, k) > 0; });
    var n = S.next.rcd;
    var forms = accts.map(function (k, i) {
      var draftRcd = { no: 'RCD ' + YEAR + '-' + pad(MONTH + 1) + '-' + pad3(n + i), officer: 'Maria Santos', account: k, date: TODAY,
        ors: un.filter(function (o) { return sumOrs([o], k) > 0; }), total: sumOrs(un, k), cash: sumOrs(un, k), time: timeNow() };
      return rcdBlock(draftRcd);
    }).join('');
    return head + '<div class="msg info">Your unreported ORs make ' + (accts.length > 1 ? accts.length + ' RCDs, one per bank account' : 'one RCD') +
      ', ' + peso(sumOrs(un)) + ' in all. Check them, then remit.</div>' + forms +
      '<button type="button" class="primary" data-act="remit">Close the day and remit ' + peso(sumOrs(un)) + '</button>' + past;
  }
  // ------------------------------------------------------------------ the RCD form, laid out as ALTOS prints it (LTOM, Annex 18)
  var W_ONES = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'];
  var W_TENS = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'];
  function bigWords(n) {
    if (n < 20) return W_ONES[n];
    if (n < 100) return W_TENS[Math.floor(n / 10)] + (n % 10 ? '-' + W_ONES[n % 10] : '');
    if (n < 1000) return W_ONES[Math.floor(n / 100)] + ' Hundred' + (n % 100 ? ' ' + bigWords(n % 100) : '');
    var units = [[1e9, 'Billion'], [1e6, 'Million'], [1000, 'Thousand']];
    for (var i = 0; i < units.length; i++) {
      var d = units[i][0];
      if (n >= d) return bigWords(Math.floor(n / d)) + ' ' + units[i][1] + (n % d ? ' ' + bigWords(n % d) : '');
    }
    return '';
  }
  // "Fifty thousand three hundred eighty-six pesos & 30/100." as written on the RCD
  function rcdWords(amount) {
    var cents = Math.round(amount * 100), p = Math.floor(cents / 100), c = cents % 100;
    var w = (bigWords(p) || 'Zero').toLowerCase();
    w = w.charAt(0).toUpperCase() + w.slice(1) + (p === 1 ? ' peso' : ' pesos');
    return w + (c ? ' & ' + pad(c) + '/100.' : ' only.');
  }
  function orAmount(o, acct) { return sumOrs([o], acct); }
  // the ORs of an RCD grouped into unbroken series per form: [form, from, to, amount]
  function orRanges(ors, acct) {
    var out = [];
    ors.slice().sort(function (a, b) { return a.form === b.form ? +a.no - +b.no : (a.form < b.form ? -1 : 1); }).forEach(function (o) {
      var last = out[out.length - 1];
      if (last && last[0] === o.form && last[2] + 1 === +o.no) { last[2] = +o.no; last[3] = r2(last[3] + orAmount(o, acct)); }
      else out.push([o.form, +o.no, +o.no, orAmount(o, acct)]);
    });
    return out;
  }
  var SERIES_END = { '51': 1234550, '56': 5670060, '51b': 1234600, '51c': 1234650 };
  function seriesEnd(o) { return o.officer === 'col2' ? 1234600 : o.officer === 'col3' ? 1234650 : SERIES_END[o.form]; }
  function accountability(ors) {
    var forms = {};
    ors.forEach(function (o) { (forms[o.form] = forms[o.form] || []).push(o); });
    return Object.keys(forms).sort().map(function (f) {
      var n = forms[f].map(function (o) { return +o.no; }).sort(function (a, b) { return a - b; });
      var lo = n[0], hi = n[n.length - 1], end = seriesEnd(forms[f][0]);
      return { form: 'AF ' + f + (f === '56' ? ' (Real Property Tax Receipt)' : ' (Official Receipt)'), beg: [end - lo + 1, lo, end], rec: null,
        iss: [hi - lo + 1, lo, hi], end: hi < end ? [end - hi, hi + 1, end] : null };
    });
  }
  function qft(t) { return t ? '<td class="c">' + t[0] + '</td><td class="c">' + t[1] + '</td><td class="c">' + t[2] + '</td>' : '<td></td><td></td><td></td>'; }
  function sigLine(name, cap, date) {
    return '<table class="sigline"><tr><td class="nm">' + (esc(name) || '&nbsp;') + '</td><td class="dt">' + date + '</td></tr><tr><td class="cap">' + cap + '</td><td class="cap">Date</td></tr></table>';
  }
  // r: an RCD of a Collecting Officer, or a consolidated RCD (r.kids = its Collecting Officers' RCDs)
  function rcdSheet(r) {
    var lo = !!r.kids, acct = r.account, when = longDate(r.date);
    var ors = lo ? r.kids.reduce(function (a, k) { return a.concat(k.ors); }, []) : r.ors;
    var collections = lo ? r.total : r.total, remitted = lo ? r.total : r.cash;
    var checks = ors.filter(function (o) { return o.check && orAmount(o, acct) > 0; });
    var chkTotal = r2(checks.reduce(function (t, o) { return t + orAmount(o, acct); }, 0));
    var officer = lo ? LGU.treasurer : r.officer;
    var a1 = lo ? '' : '<div class="ind">1. For Collectors</div><table class="g"><tr><th rowspan="2">Type (Form No.)</th><th colspan="2">Official Receipt/Serial No.</th><th rowspan="2">Amount</th></tr><tr><th>From</th><th>To</th></tr>' +
      orRanges(ors, acct).map(function (x) { return '<tr><td>AF ' + x[0] + '</td><td class="c">' + x[1] + '</td><td class="c">' + x[2] + '</td><td class="r">' + money(x[3]) + '</td></tr>'; }).join('') + '</table>';
    var a2rows = lo ? r.kids.map(function (k) { return '<tr><td>' + esc(k.officer) + '</td><td class="c">' + esc(k.no.replace('RCD ', '')) + '</td><td class="r">' + money(k.total) + '</td></tr>'; }).join('')
      : '<tr><td>&nbsp;</td><td></td><td></td></tr>';
    var c = lo ? [] : accountability(ors);
    var cBody = c.length ? c.map(function (x) { return '<tr><td>' + x.form + '</td>' + qft(x.beg) + qft(x.rec) + qft(x.iss) + qft(x.end) + '</tr>'; }).join('')
      : '<tr><td colspan="13" class="c">None</td></tr>';
    var bal = r2(collections - remitted);
    var chkRows = checks.map(function (o) { return '<tr><td>' + esc(o.check) + '</td><td>' + esc(o.payor) + '</td><td class="r">' + money(orAmount(o, acct)) + '</td></tr>'; }).join('') ||
      '<tr><td class="c">-</td><td></td><td class="r">-</td></tr>';
    var bWho = lo ? LGU.treasurer : ROLES.lo.user, bRef = lo ? LGU.bank + ' DS# ' + r.slip.replace(/^DS\s*/, '') : LGU.bank;
    var cert = lo ? [ROLES.lo.user, 'Liquidating Officer'] : [r.officer, 'Collecting Officer'];
    var ver = lo ? [LGU.treasurer, LGU.treasurerTitle, 'Name and Signature – Cashier/Treasurer'] : [ROLES.lo.user, 'Liquidating Officer', 'Name and Signature'];
    return '<div class="sheet-wrap"><div class="sheet">' +
      '<div class="rcdtitle">REPORT OF COLLECTIONS AND DEPOSITS (RCD)</div>' +
      '<div style="text-align:center"><p class="lgu">' + LGU.short + '</p></div><p class="lgucap">Name of LGU</p>' +
      '<p class="printed">Printed: ' + longDate(TODAY) + '  ' + timeNow() + ' · Sample from the ALTOS demo, not a real report</p>' +
      '<table class="hdr"><tr><td style="width:24%;white-space:nowrap">Fund :</td><td class="u">' + ACCOUNTS[acct].line + '</td><td style="width:12%">Date :</td><td class="u" style="width:20%">' + when + '</td></tr>' +
      '<tr><td style="white-space:nowrap">Name of Accountable Officer :</td><td class="u">' + esc(officer).toUpperCase() + '</td><td>Report No. :</td><td class="u">' + esc(r.no.replace(/^C?RCD /, '')) + '</td></tr></table>' +
      '<div class="sec">A. COLLECTIONS' + (lo ? '' : ' &nbsp; <span style="font-weight:normal">' + ACCOUNTS[acct].name.toUpperCase() + '</span>') + '</div>' + a1 +
      '<div class="ind" style="margin-top:6px">2. For Liquidating Officers/Treasurers</div><table class="g"><tr><th>Name of Accountable Officer</th><th>Report No.</th><th>Amount</th></tr>' + a2rows +
      '<tr><td colspan="2" class="r b">Total</td><td class="r b">' + money(collections) + '</td></tr></table>' +
      '<div class="sec">B. REMITTANCES/DEPOSITS</div><table class="g"><tr><th>Accountable Officer/Bank</th><th>Reference</th><th>Amount</th></tr>' +
      '<tr><td>' + esc(bWho) + '</td><td>' + esc(bRef) + '</td><td class="r">' + money(remitted) + '</td></tr><tr><td colspan="2" class="r b">Total</td><td class="r b">' + money(remitted) + '</td></tr></table>' +
      '<div class="sec">C. ACCOUNTABILITY FOR ACCOUNTABLE FORMS</div><table class="g small"><tr><th rowspan="3">Name of Form &amp; No.</th><th colspan="3">Beginning Balance</th><th colspan="3">Receipts</th><th colspan="3">Issued</th><th colspan="3">Ending Balance</th></tr>' +
      '<tr>' + '<th rowspan="2">Qty.</th><th colspan="2">Inclusive Serial Nos.</th>'.repeat(4) + '</tr><tr>' + '<th>From</th><th>To</th>'.repeat(4) + '</tr>' + cBody + '</table>' +
      '<div class="sec">D. SUMMARY OF COLLECTIONS AND REMITTANCES/DEPOSITS</div><table class="two"><tr><td><table class="dsum">' +
      '<tr><td colspan="2">Beginning Balance:</td><td class="amt">-</td></tr><tr><td colspan="3">Add: Collections</td></tr>' +
      '<tr><td style="width:20px"></td><td>Cash:</td><td class="amt">' + money(r2(collections - chkTotal)) + '</td></tr>' +
      '<tr><td></td><td>Checks:</td><td class="amt">' + (chkTotal ? money(chkTotal) : '-') + '</td></tr>' +
      '<tr><td></td><td class="b">TOTAL:</td><td class="amt b">' + money(collections) + '</td></tr>' +
      '<tr><td colspan="2">Less: Remittance/Deposit to Cashier/Treasurer/Depository Bank:</td><td class="amt">' + money(remitted) + '</td></tr>' +
      '<tr><td colspan="2" class="b">Balance:</td><td class="amt b">' + (bal ? money(bal) : '-') + '</td></tr></table></td>' +
      '<td><div class="ind">List of Checks</div><table class="g small"><tr><th>Check No.</th><th>Payee</th><th>Amount</th></tr>' + chkRows + '</table></td></tr></table>' +
      '<table class="certbox"><tr><td><div class="b c">CERTIFICATION</div><p>I hereby certify that the foregoing report of collections and deposits and accountability of accountable forms is true and correct.</p>' +
      sigLine(cert[0].toUpperCase(), 'Name and Signature – Accountable Officer', when) + '<p class="small c" style="margin:0">' + cert[1] + '</p></td>' +
      '<td><div class="b c">VERIFICATION AND ACKNOWLEDGMENT</div><p>I hereby certify that the foregoing report of the collection has been verified and acknowledge receipt of ' + esc(rcdWords(remitted)) + '</p>' +
      '<p class="r b">PHP ' + money(remitted) + '</p>' + sigLine(ver[0].toUpperCase(), ver[2], when) + '<p class="small c" style="margin:0">' + ver[1] + '</p></td></tr></table>' +
      '</div></div>';
  }
  // the form keeps its A4 layout and is scaled down to fit a phone; pinch to zoom in
  function fitSheets() {
    Array.prototype.forEach.call(root.querySelectorAll('.sheet-wrap'), function (w) {
      var sh = w.firstChild, k = Math.min(1, w.clientWidth / sh.offsetWidth);
      sh.style.transform = k < 1 ? 'scale(' + k + ')' : '';
      w.style.height = (sh.offsetHeight * k) + 'px';
    });
  }
  window.addEventListener('resize', fitSheets);
  function rcdBlock(r, note) {
    return '<div class="card"><h2>' + esc(r.no) + ' · ' + ACCOUNTS[r.account].name + '</h2>' + (note ? '<p class="muted">' + note + '</p>' : '') + rcdSheet(r) +
      '<p class="muted pinch">The form keeps its A4 layout. Pinch to zoom in.</p></div>';
  }

  // ------------------------------------------------------------------ RAAF and CRAAF (LTOM Book II, Annexes 16 and 17), as ALTOS prints them
  // The OR booklets of the month. beg: the first serial in the officer's hands when the month began (null: received this month);
  // upto: the booklet was used up earlier this month, before the demo's records start.
  var BOOKLETS = [
    { off: 'col', name: 'Maria Santos', form: '51', from: 1234451, to: 1234500, beg: 1234478, upto: 1234500 },
    { off: 'col', name: 'Maria Santos', form: '51', from: 1234501, to: 1234550, beg: null },
    { off: 'col', name: 'Maria Santos', form: '56', from: 5670011, to: 5670060, beg: 5670011 },
    { off: 'col2', name: 'Jose Reyes', form: '51', from: 1234401, to: 1234450, beg: 1234436, upto: 1234450 },
    { off: 'col2', name: 'Jose Reyes', form: '51', from: 1234551, to: 1234600, beg: null },
    { off: 'col3', name: 'Luz Ramos', form: '51', from: 1234351, to: 1234400, beg: 1234390, upto: 1234400 },
    { off: 'col3', name: 'Luz Ramos', form: '51', from: 1234601, to: 1234650, beg: null }
  ];
  // the Treasurer's stock: forms bought from the supplier, then issued to the officers in booklets of 50
  var STOCK = [
    { form: '51', from: 1234001, to: 1235000, beg: 1234501 },
    { form: '56', from: 5670011, to: 5670510, beg: 5670061 }
  ];
  var OFFICERS = [['col', 'Maria Santos'], ['col2', 'Jose Reyes'], ['col3', 'Luz Ramos']];
  function afName(f) { return 'AF ' + f + (f === '56' ? ' (Real Property Tax Receipt)' : ' (Official Receipt)'); }
  var RAAF_MONTH = MONTHS[MONTH] + ' ' + YEAR;
  var RAAF_DUE = longDate((MONTH === 11 ? YEAR + 1 : YEAR) + '-' + pad(MONTH === 11 ? 1 : MONTH + 2) + '-05');
  function bookletRow(b) {
    var nums = S.ors.filter(function (o) { return o.officer === b.off && o.form === b.form && +o.no >= b.from && +o.no <= b.to; })
      .map(function (o) { return +o.no; });
    var start = b.beg != null ? b.beg : b.from, hi = Math.max.apply(null, nums.concat([b.upto || 0]));
    var whole = [b.to - start + 1, start, b.to];
    var used = hi >= start;
    return { first: afName(b.form), beg: b.beg != null ? whole : null, rec: b.beg != null ? null : whole,
      iss: used ? [hi - start + 1, start, hi] : null, end: !used ? whole : hi < b.to ? [b.to - hi, hi + 1, b.to] : null };
  }
  function stockRows() {
    var out = BOOKLETS.filter(function (b) { return b.beg == null; });
    return STOCK.map(function (p) {
      var mine = out.filter(function (b) { return b.form === p.form; });
      var n = mine.reduce(function (s, b) { return s + b.to - b.from + 1; }, 0);
      var whole = [p.to - p.beg + 1, p.beg, p.to], left = whole[0] - n;
      return { first: afName(p.form) + " – Treasurer's stock", beg: whole, rec: null,
        iss: n ? [n, p.beg, p.beg + n - 1] : null, end: left > 0 ? [left, p.to - left + 1, p.to] : null };
    });
  }
  function accTable(rows) {
    return '<table class="g small"><tr><th rowspan="3">Name of Form &amp; No.</th><th colspan="3">Beginning Balance</th><th colspan="3">Receipt</th>' +
      '<th colspan="3">Issued</th><th colspan="3">Ending Balance</th></tr><tr>' + '<th rowspan="2">Qty.</th><th colspan="2">Inclusive Serial Nos.</th>'.repeat(4) +
      '</tr><tr>' + '<th>From</th><th>To</th>'.repeat(4) + '</tr>' +
      rows.map(function (r) { return '<tr><td>' + esc(r.first) + '</td>' + qft(r.beg) + qft(r.rec) + qft(r.iss) + qft(r.end) + '</tr>'; }).join('') + '</table>';
  }
  function ltSig(name, cap) { return '<div class="ltsig"><div class="b">' + (esc(name) || '&nbsp;') + '</div><div class="ln">' + cap + '</div></div>'; }
  function ltHead(title, ref) {
    return '<p class="ref">' + ref + ' · LTOM, 2nd Edition</p><div class="lth">' + title + '</div>' +
      '<p class="ltlgu"><span>' + LGU.short + '</span></p><p class="ltcap">LGU</p>' +
      '<p class="printed">Printed: ' + longDate(TODAY) + '  ' + timeNow() + ' · Sample from the ALTOS demo, not a real report</p>' +
      '<p class="c">Month of <span class="fld">' + MONTHS[MONTH] + '</span> ' + YEAR + '</p>';
  }
  function raafSheet(off) {
    var who = OFFICERS.filter(function (x) { return x[0] === off; })[0][1];
    var rows = BOOKLETS.filter(function (b) { return b.off === off; }).map(bookletRow);
    return '<div class="sheet-wrap wide"><div class="sheet wide">' +
      ltHead('REPORT OF ACCOUNTABILITY FOR ACCOUNTABLE FORMS', 'Annex 16 – Report of Accountability for Accountable Forms (RAAF) – Annex 42 of MNGAS for LGUs, Vol. II') +
      '<p>Accountable Officer: <span class="fld">' + esc(who) + '</span> &nbsp;&nbsp; Designation: <span class="fld">Collecting Officer</span>' +
      '<span style="float:right">Report No.: <span class="fld">&nbsp;</span></span></p>' + accTable(rows) +
      '<p class="b" style="margin-top:12px">CERTIFICATION:</p><p>I hereby certify that the foregoing is a true statement of all accountable forms received, ' +
      'issued and transferred by me during the period above-stated and the correctness of the beginning balances.</p>' +
      '<div>' + ltSig(who, 'Name and Signature of the Accountable Officer') + ltSig(S.raaf[off] ? longDate(S.raaf[off].date) : '', 'Date') + '</div>' +
      '</div></div>';
  }
  function craafSheet() {
    var rows = stockRows();
    OFFICERS.forEach(function (o) {
      BOOKLETS.filter(function (b) { return b.off === o[0]; }).forEach(function (b) {
        var r = bookletRow(b); r.first = afName(b.form) + ' – ' + o[1]; rows.push(r);
      });
    });
    return '<div class="sheet-wrap wide"><div class="sheet wide">' +
      ltHead('CONSOLIDATED REPORT OF ACCOUNTABILITY FOR ACCOUNTABLE FORMS (CRAAF)', 'Annex 17 – Consolidated Report of Accountability for Accountable Forms (CRAAF) – Annex 43 of MNGAS for LGUs, Vol. II') +
      '<p>Treasurer: <span class="fld">' + esc(LGU.treasurer) + '</span><span style="float:right">Report No.: <span class="fld">&nbsp;</span></span></p>' + accTable(rows) +
      '<p class="b" style="margin-top:12px">Certified Correct:</p><div>' + ltSig(LGU.treasurer, LGU.treasurerTitle) + ltSig('', 'Date') + '</div>' +
      '</div></div>';
  }
  function raafBlock(off, title, note) {
    return '<div class="card"><h2>' + title + '</h2>' + (note ? '<p class="muted">' + note + '</p>' : '') + (off ? raafSheet(off) : craafSheet()) +
      '<p class="muted pinch">The form keeps its landscape layout. Pinch to zoom in.</p></div>';
  }
  function raaf() {
    var done = S.raaf.col;
    return '<h1>My RAAF</h1>' +
      about('Every month you render the Report of Accountability for Accountable Forms (RAAF, LTOM Book II Annex 16): the official receipts in your custody ' +
        'at the start of the month, received, issued and left at the end. Submit it to the Liquidating Officer on or before the 5th of the following month.') +
      (done ? '<div class="msg ok">Submitted to the Liquidating Officer on ' + longDate(done.date) + ' at ' + done.time + '.</div>'
        : '<div class="msg info">Your RAAF for ' + RAAF_MONTH + ' is due on or before ' + RAAF_DUE + '. It counts every OR you issue, so issue one and come back to see it change.</div>') +
      raafBlock('col', 'RAAF · ' + RAAF_MONTH, 'Issued: the ORs used this month, the last one being the latest you issued. Ending Balance: the ORs still in your hands.') +
      (done ? '' : '<button type="button" class="primary" data-act="submit-raaf">Submit my RAAF to the Liquidating Officer</button>');
  }
  function craaf() {
    var view = S.viewRaaf; S.viewRaaf = null;
    var rows = OFFICERS.map(function (o) {
      var s = S.raaf[o[0]];
      return '<tr><td>' + esc(o[1]) + '<div class="muted">Collecting Officer</div></td><td>' +
        (s ? '<span class="chip g">Submitted</span><div class="muted nw">' + shortDate(s.date) + ', ' + s.time + '</div>' : '<span class="chip y">Not yet</span><div class="muted nw">due ' + RAAF_DUE + '</div>') +
        (s ? ' <button type="button" class="small" data-act="view-raaf" data-v="' + o[0] + '">View RAAF</button>' : '') + '</td></tr>';
    }).join('');
    var n = OFFICERS.filter(function (o) { return S.raaf[o[0]]; }).length;
    var who = view && OFFICERS.filter(function (o) { return o[0] === view; })[0][1];
    return '<h1>RAAF &amp; CRAAF</h1>' +
      about('Every accountable officer submits his or her RAAF (Annex 16) and the Liquidating Officer the Consolidated RAAF (CRAAF, Annex 17) on or before the 5th of ' +
        'the following month. This page shows who has submitted, who is late and what is still missing.') +
      '<div class="card"><h2>RAAFs for ' + RAAF_MONTH + '</h2><p class="muted">' + n + ' of ' + OFFICERS.length + ' submitted. Nobody is late: they are due on or before ' + RAAF_DUE + '.' +
      (S.raaf.col ? '' : ' Sign in as Collecting Officer and submit Maria Santos\'s RAAF to see it arrive here.') + '</p>' +
      '<div class="tbl"><table><thead><tr><th>Accountable Officer</th><th>RAAF</th></tr></thead><tbody>' + rows + '</tbody></table></div></div>' +
      (view ? raafBlock(view, 'RAAF of ' + esc(who) + ' · ' + RAAF_MONTH, 'Submitted on ' + longDate(S.raaf[view].date) + ' at ' + S.raaf[view].time + '.') : '') +
      raafBlock(null, 'CRAAF · ' + RAAF_MONTH, 'Prepared by the Liquidating Officer and certified correct by the Treasurer: the Treasurer\'s stock of forms, then the forms in the hands of every accountable officer.' +
        ' It goes to the Treasurer once every RAAF is in.');
  }

  function statusChip(s) {
    return '<span class="chip ' + ({ Submitted: 'y', Consolidated: 'g', Refused: 'r', Released: 'g', Prepared: 'y' }[s] || '') + '">' + s + '</span>';
  }
  function rptcalc() {
    if (!S.calc) S.calc = { pin: S.props[0].pin, date: TODAY, whole: false };
    var c = S.calc, p = findProp(c.pin), rows = rptDue(p, c.date, c.whole);
    return '<h1>RPT Tax Calculator</h1>' +
      about('Pick the PIN: the property and its tax due appear, with the discount for paying on time or the interest for paying late. Change the date to see what the owner would pay on another day.') +
      '<div class="card"><label for="cpin">Property</label><select id="cpin" data-f="cpin">' +
      S.props.map(function (q) { return '<option value="' + q.pin + '"' + (q.pin === c.pin ? ' selected' : '') + '>' + esc(propLabel(q)) + '</option>'; }).join('') +
      '</select><div class="row"><div><label for="cdate">Date of payment</label><input type="date" id="cdate" data-f="cdate" min="' + YEAR + '-01-01" max="' + (YEAR + 1) + '-12-31" value="' + c.date + '"></div>' +
      '<div><label>Assessed value</label><input readonly value="' + peso(p.av) + '"></div></div>' +
      '<label><input type="checkbox" data-f="cwhole"' + (c.whole ? ' checked' : '') + '>Include the rest of the year</label>' +
      '<p class="muted">' + esc(p.td) + ' · ' + esc(p.kind) + ' · owner ' + esc(p.owner) + ' · paid up to ' + p.paid[0] + ' Q' + p.paid[1] + '</p>' + rptTable(rows) + '</div>' +
      '<p class="muted">Demo settings: basic tax 1% and SEF 1% of the assessed value, each quarter due on the last day of March, June, September and December, ' +
      '10% discount for a quarter paid on time when nothing earlier is unpaid, and 2% interest a month (up to 36 months) for a late quarter. ' +
      'A real LGU\'s rates and discounts are in its own Revenue Code.</p>';
  }

  // ------------------------------------------------------------------ Liquidating Officer
  var DENOS = [1000, 500, 200, 100, 50, 20, 10, 5, 1, 0.25];
  function crcd() {
    if (!S.cr) S.cr = { account: 'GF', picked: {}, count: {}, slip: 'DS ' + (70300 + S.next.crcd) };
    var c = S.cr, sub = S.rcds.filter(function (r) { return r.status === 'Submitted' && r.account === c.account; });
    var tot = 0, cash = 0;
    sub.forEach(function (r) { if (c.picked[r.no]) { tot += r.total; cash += r.cash; } });
    tot = r2(tot); cash = r2(cash);
    var counted = r2(DENOS.reduce(function (s, d) { return s + d * num(c.count[d]); }, 0));
    var anyPicked = sub.some(function (r) { return c.picked[r.no]; });
    var diff = r2(counted - tot), state;
    if (!anyPicked) state = '<div class="msg info">Tick the RCDs you received, then count the money.</div>';
    else if (!counted) state = '<div class="msg info">Count the money: type how many of each bill and coin, or tap "Fill in the money received".</div>';
    else if (diff === 0) state = '<div class="msg ok">The count agrees with the RCDs to the last centavo. Record the deposit.</div>';
    else state = '<div class="msg bad">The count is ' + (diff < 0 ? 'short by ' + peso(-diff) : 'over by ' + peso(diff)) +
      '. ALTOS will not accept it. Find the report with the difference and <a href="#lo-refused">refuse it</a> with the reason.</div>';
    var rows = sub.map(function (r) {
      return '<tr><td class="nw"><label style="margin:0;font-weight:400"><input type="checkbox" data-f="pick" data-v="' + esc(r.no) + '"' + (c.picked[r.no] ? ' checked' : '') + '>' + esc(r.no) + '</label></td><td>' + esc(r.officer) +
        '</td><td class="nw">' + r.ors.length + ' ORs</td><td class="r">' + money(r.total) + '</td><td class="nw">' + r.time +
        '</td><td><button type="button" class="small" data-act="view-rcd" data-v="' + esc(r.no) + '">View</button></td></tr>';
    }).join('');
    var done = S.crcds.filter(function (x) { return x.account === c.account; });
    var view = S.viewRcd && (S.crcds.concat(S.rcds)).filter(function (x) { return x.no === S.viewRcd; })[0];
    S.viewRcd = null;
    return '<h1>Consolidated RCD</h1>' +
      about("Collecting Officers whose ORs belong to the same bank account are merged into one RCD. Count the money, select the account, tick the RCDs, then record the deposit slip. The deposit enters the Cash Book on the date of the RCD.") +
      '<div class="tabs">' + ['GF', 'SEF'].map(function (k) { return '<button type="button" class="tab' + (k === c.account ? ' on' : '') + '" data-act="cr-acct" data-v="' + k + '">' + ACCOUNTS[k].name + '</button>'; }).join('') + '</div>' +
      (sub.length ? (view ? rcdBlock(view, view.kids ? 'Consolidated RCD with its deposit slip.' : 'The RCD remitted by ' + esc(view.officer) + '.') : '') +
      '<div class="tbl"><table><thead><tr><th>RCD</th><th>Collecting Officer</th><th>ORs</th><th class="r">Amount</th><th>Remitted</th><th></th></tr></thead><tbody>' + rows +
        '<tr class="sum"><td colspan="3">Total of the ticked RCDs</td><td class="r">' + money(tot) + '</td><td></td><td></td></tr></tbody></table></div>' +
        '<div class="card"><h2>Cash count</h2><div class="deno">' + DENOS.map(function (d) {
          return '<div><label for="d' + d + '">' + (d < 1 ? '25¢' : '₱' + d.toLocaleString('en-PH')) + ' ×</label><input id="d' + d + '" inputmode="numeric" data-f="count" data-v="' + d + '" value="' + esc(c.count[d] || '') + '"></div>';
        }).join('') + '</div><p>Counted: <span class="total" id="counted">' + peso(counted) + '</span></p>' +
        '<button type="button" class="small" data-act="fill"' + (anyPicked ? '' : ' disabled') + '>Fill in the money received</button> ' +
        '<button type="button" class="small" data-act="clear-count">Clear</button>' + state +
        '<div class="row"><div><label for="slip">Deposit slip No.</label><input id="slip" data-f="slip" value="' + esc(c.slip) + '"></div>' +
        '<div><label>Date</label><input readonly value="' + longDate(TODAY) + '"></div></div>' +
        '<button type="button" class="primary" data-act="deposit"' + (anyPicked && counted && diff === 0 ? '' : ' disabled') + '>Record the deposit of ' + peso(tot) + '</button></div>'
        : (view ? rcdBlock(view, view.kids ? 'Consolidated RCD with its deposit slip.' : '') : '') + '<div class="msg ok">No RCD of the ' + ACCOUNTS[c.account].name + ' is waiting.' + (S.rcds.some(function (r) { return r.status === 'Submitted'; }) ? ' See the other account.' : '') + '</div>') +
      (done.length ? '<h2>Consolidated today</h2><div class="tbl"><table><thead><tr><th>Consolidated RCD</th><th>Deposit slip</th><th>RCDs</th><th class="r">Amount</th><th></th></tr></thead><tbody>' +
        done.map(function (x) { return '<tr><td class="nw">' + esc(x.no) + '</td><td class="nw">' + esc(x.slip) + '</td><td>' + x.rcds.map(esc).join(', ') + '</td><td class="r">' + money(x.total) +
          '</td><td><button type="button" class="small" data-act="view-rcd" data-v="' + esc(x.no) + '">View RCD</button></td></tr>'; }).join('') + '</tbody></table></div>' : '');
  }
  function refused() {
    var sub = S.rcds.filter(function (r) { return r.status === 'Submitted'; });
    var gone = S.rcds.filter(function (r) { return r.status === 'Refused'; });
    if (S.refPick && !sub.some(function (r) { return r.no === S.refPick; })) S.refPick = null;
    var pick = S.refPick || (sub.filter(function (r) { return r.cash !== r.total; })[0] || sub[0] || {}).no;
    var p = sub.filter(function (r) { return r.no === pick; })[0];
    var hint = p ? (p.cash < p.total ? 'Short by ' + peso(r2(p.total - p.cash)) + ': the money counted is ' + peso(p.cash) + ', the report says ' + peso(p.total) + '.' : '') : '';
    return '<h1>Refused Reports</h1>' +
      about('Refuse a short remittance or a wrong report, with the reason. It goes back to the Collecting Officer to correct, and the refusal stays on record.') +
      (sub.length ? '<div class="card"><label for="ref-no">Report</label><select id="ref-no" data-f="refpick">' +
        sub.map(function (r) { return '<option value="' + esc(r.no) + '"' + (r.no === pick ? ' selected' : '') + '>' + esc(r.no + ' · ' + r.officer + ' · ' + peso(r.total)) + '</option>'; }).join('') +
        '</select><label for="reason">Reason</label><textarea id="reason" rows="3">' + esc(hint) + '</textarea>' +
        '<button type="button" class="danger" data-act="refuse">Refuse this report</button></div>' : '<div class="msg ok">No report is waiting.</div>') +
      '<h2>Refused today</h2>' + (gone.length ? '<div class="tbl"><table><thead><tr><th>RCD</th><th>Collecting Officer</th><th class="r">Amount</th><th>Reason</th><th>Refused by</th></tr></thead><tbody>' +
        gone.map(function (r) { return '<tr><td class="nw">' + esc(r.no) + '</td><td>' + esc(r.officer) + '</td><td class="r">' + money(r.total) + '</td><td style="min-width:220px">' + esc(r.reason) + '</td><td class="nw">' + esc(r.by) + ', ' + r.when + '</td></tr>'; }).join('') +
        '</tbody></table></div>' : '<p class="muted">None.</p>');
  }
  function register() {
    var f = S.regFilter || 'all';
    var list = S.ors.filter(function (o) { return f === 'all' || o.name === f; });
    var names = S.ors.map(function (o) { return o.name; }).filter(function (n, i, a) { return a.indexOf(n) === i; });
    return '<h1>Collections Register</h1>' + about('All official receipts of all collecting officers for the period.') +
      '<div class="row"><div><label for="regf">Collecting Officer</label><select id="regf" data-f="regf"><option value="all">All officers</option>' +
      names.map(function (n) { return '<option' + (n === f ? ' selected' : '') + '>' + esc(n) + '</option>'; }).join('') + '</select></div><div></div></div>' +
      '<div class="tbl"><table><thead><tr><th>OR No.</th><th>Form</th><th>Officer</th><th>Payor</th><th class="r">General Fund</th><th class="r">SEF</th><th class="r">Total</th></tr></thead><tbody>' +
      list.map(function (o) {
        return '<tr><td>' + o.no + '</td><td class="nw">AF ' + o.form + '</td><td class="nw">' + esc(o.name) + '</td><td>' + esc(o.payor) + '</td><td class="r">' + money(sumOrs([o], 'GF')) +
          '</td><td class="r">' + money(sumOrs([o], 'SEF')) + '</td><td class="r">' + money(o.total) + '</td></tr>';
      }).join('') + '<tr class="sum"><td colspan="4">Total, ' + list.length + ' receipts</td><td class="r">' + money(sumOrs(list, 'GF')) + '</td><td class="r">' + money(sumOrs(list, 'SEF')) +
      '</td><td class="r">' + money(sumOrs(list)) + '</td></tr></tbody></table></div>';
  }
  function cashbook() {
    var k = S.cbAcct || 'GF', rows = S.cash[k], td = 0, tc = 0;
    var body = rows.map(function (e) {
      td += e.dr; tc += e.cr;
      return '<tr><td class="nw">' + shortDate(e.date) + '</td><td>' + esc(e.what) + (e.ref ? '<div class="muted">' + esc(e.ref) + '</div>' : '') + '</td><td class="r nw">' + (e.dr ? money(e.dr) : '') +
        '</td><td class="r nw">' + (e.cr ? money(e.cr) : '') + '</td><td class="r nw">' + money(e.bal) + '</td></tr>';
    }).join('');
    return '<h1>Cash Book</h1>' + about('Cash Book, Cash in Bank per account: DEBIT, deposits per consolidated RCD; CREDIT, checks issued; with the running balance.') +
      '<div class="tabs">' + ['GF', 'SEF'].map(function (a) { return '<button type="button" class="tab' + (a === k ? ' on' : '') + '" data-act="cb-acct" data-v="' + a + '">' + ACCOUNTS[a].name + '</button>'; }).join('') + '</div>' +
      '<p class="muted">' + ACCOUNTS[k].name + ' · ' + ACCOUNTS[k].bank + ' · ' + MONTHS[MONTH] + ' ' + YEAR + '</p>' +
      '<div class="tbl"><table class="cb"><thead><tr><th rowspan="2">Date</th><th rowspan="2">Particulars</th><th colspan="3" class="c">Cash in Bank</th></tr>' +
      '<tr><th class="r">Debit</th><th class="r">Credit</th><th class="r">Balance</th></tr></thead><tbody>' + body +
      '<tr class="sum"><td colspan="2">Totals / Balance as of ' + shortDate(TODAY) + '</td><td class="r nw">' + money(r2(td)) + '</td><td class="r nw">' + money(r2(tc)) + '</td><td class="r nw">' + money(balance(k)) + '</td></tr></tbody></table></div>' +
      '<p class="muted">Debit: money into the bank account (deposits of collections). Credit: money out (checks issued). Balance: what is left after each entry.</p>';
  }

  // ------------------------------------------------------------------ the accountable officers' own cash books (LTOM Forms 1 and 2)
  var MO = YEAR + '-' + pad(MONTH + 1) + '-';
  // Maria Santos's RCDs earlier this month, all remitted in full
  var COL_PAST = [[3, '007', 'GF', 12350], [5, '012', 'GF', 8940.5], [5, '013', 'SEF', 1980], [10, '027', 'GF', 15275]];
  // the Liquidating Officer's consolidated RCDs earlier this month: received from the collectors, then deposited the same day
  var LO_PAST = [[3, '004', 'GF', 'DS 70211', 186420.5], [5, '006', 'SEF', 'DS 70218', 23880], [10, '011', 'GF', 'DS 70240', 142310]];
  function bookTable(heads, rows, note) {
    var bal = 0, td = 0, tc = 0;
    var body = rows.map(function (e) {
      bal = r2(bal + e.dr - e.cr); td += e.dr; tc += e.cr;
      return '<tr><td class="nw">' + shortDate(e.date) + '</td><td>' + e.ref + (e.what ? '<div class="muted">' + e.what + '</div>' : '') + '</td><td class="r nw">' + (e.dr ? money(e.dr) : '') +
        '</td><td class="r nw">' + (e.cr ? money(e.cr) : '') + '</td><td class="r nw">' + money(bal) + '</td></tr>';
    }).join('') || '<tr><td colspan="5" class="c muted">No entries yet this month.</td></tr>';
    return '<div class="tbl"><table class="cb"><thead><tr><th>Date</th><th>' + heads + '</th><th class="r">Debit</th><th class="r">Credit</th><th class="r">Balance<br>on Hand</th></tr></thead><tbody>' + body +
      '<tr class="sum"><td colspan="2">Totals</td><td class="r nw">' + money(r2(td)) + '</td><td class="r nw">' + money(r2(tc)) + '</td><td class="r nw">' + money(bal) + '</td></tr></tbody></table></div>' +
      '<p class="muted">' + note + '</p>';
  }
  function colCashbook() {
    var rows = COL_PAST.map(function (x) {
      return { date: dayOfMonth(x[0]), ref: 'RCD ' + MO + x[1], what: ACCOUNTS[x[2]].name, dr: x[3], cr: x[3] };
    });
    S.rcds.filter(function (r) { return r.officer === 'Maria Santos' && r.status !== 'Refused'; }).forEach(function (r) {
      rows.push({ date: r.date, ref: esc(r.no), what: ACCOUNTS[r.account].name, dr: r.total, cr: r.cash });
    });
    rows.sort(function (a, b) { return a.date < b.date ? -1 : a.date > b.date ? 1 : 0; });
    var un = myOrs().filter(function (o) { return !o.reported; });
    return '<h1>My Cash Book</h1>' +
      about('Cashbook of the Collecting Officer (LTOM Form No. 1): DEBIT, your collections per RCD; CREDIT, what you remitted to the Liquidating Officer; BALANCE ON HAND, the money still with you.') +
      '<p class="muted">Collector: ' + esc(ROLES.col.user) + ' · ' + MONTHS[MONTH] + ' ' + YEAR + '</p>' +
      bookTable('Report No.', rows, 'Debit: collections per RCD. Credit: remitted to the Liquidating Officer, ' + esc(ROLES.lo.user) + '. Balance on Hand: money you still hold.') +
      (un.length ? '<div class="msg info">' + peso(sumOrs(un)) + ' on ' + un.length + ' ORs today is not yet in an RCD. It enters this cash book when you <a href="#col-rcd">close the day</a>.</div>'
        : '<div class="msg ok">All your ORs are in an RCD and remitted. Nothing is left on hand.</div>');
  }
  function loCashbook() {
    var k = S.loAcct || 'GF', rows = [];
    LO_PAST.filter(function (x) { return x[2] === k; }).forEach(function (x) {
      rows.push({ date: dayOfMonth(x[0]), ref: 'CRCD ' + MO + x[1], what: 'From the collecting officers', dr: x[4], cr: 0 });
      rows.push({ date: dayOfMonth(x[0]), ref: 'CRCD ' + MO + x[1], what: 'Deposited, ' + x[3], dr: 0, cr: x[4] });
    });
    S.rcds.filter(function (r) { return r.account === k && r.status !== 'Refused'; }).forEach(function (r) {
      rows.push({ date: r.date, ref: esc(r.no), what: 'From ' + esc(r.officer) + (r.cash !== r.total ? ' (short ' + peso(r2(r.total - r.cash)) + ')' : ''), dr: r.cash, cr: 0 });
    });
    S.crcds.filter(function (c) { return c.account === k; }).forEach(function (c) {
      rows.push({ date: c.date, ref: esc(c.no), what: 'Deposited, ' + esc(c.slip), dr: 0, cr: c.total });
    });
    rows.sort(function (a, b) { return a.date < b.date ? -1 : a.date > b.date ? 1 : 0; });
    return '<h1>My Cash Book</h1>' +
      about('Cashbook of the Liquidating Officer (LTOM Form No. 2), per fund: DEBIT, collections turned over to you by the collecting officers; CREDIT, what you deposited in the bank; BALANCE ON HAND, the money still with you.') +
      '<div class="tabs">' + ['GF', 'SEF'].map(function (a) { return '<button type="button" class="tab' + (a === k ? ' on' : '') + '" data-act="lo-acct" data-v="' + a + '">' + ACCOUNTS[a].name + '</button>'; }).join('') + '</div>' +
      '<p class="muted">Liquidating Officer: ' + esc(ROLES.lo.user) + ' · Fund: ' + ACCOUNTS[k].name + ' · ' + MONTHS[MONTH] + ' ' + YEAR + '</p>' +
      bookTable('Report No.', rows, 'Debit: money received from the collecting officers. Credit: deposited in ' + LGU.bank + '. Balance on Hand: money received but not yet deposited. ' +
        '<a href="#lo-crcd">Count and deposit it in Consolidated RCD →</a>');
  }

  // ------------------------------------------------------------------ Disbursing Officer
  function prepare() {
    if (!S.ck) S.ck = { account: 'GF', payee: '', what: '', amount: '' };
    var c = S.ck, nextNo = pad4(S.next.check[c.account]), bal = balance(c.account);
    return '<h1>Prepare Check</h1>' +
      about('Prepare the next check in serial order from your check booklet. A check above the Cash Book balance is refused.') +
      '<div class="card"><div class="row"><div><label for="ck-acct">Bank account</label><select id="ck-acct" data-f="ck-account">' +
      ['GF', 'SEF'].map(function (k) { return '<option value="' + k + '"' + (k === c.account ? ' selected' : '') + '>' + ACCOUNTS[k].name + '</option>'; }).join('') +
      '</select></div><div><label>Cash Book balance</label><input readonly value="' + peso(bal) + '"></div></div>' +
      '<div class="row"><div><label>Next check No.</label><input readonly value="' + nextNo + '"></div><div><label>DV No.</label><input readonly value="DV ' + YEAR + '-' + pad(MONTH + 1) + '-' + pad3(S.next.dv) + '"></div></div>' +
      '<label for="ck-payee">Payee</label><input id="ck-payee" data-f="ck-payee" autocomplete="off" placeholder="e.g. Sample Office Supply Co." value="' + esc(c.payee) + '">' +
      '<label for="ck-what">Particulars</label><input id="ck-what" data-f="ck-what" autocomplete="off" placeholder="e.g. Office supplies" value="' + esc(c.what) + '">' +
      '<label for="ck-amt">Amount</label><input id="ck-amt" data-f="ck-amount" inputmode="decimal" placeholder="0.00" value="' + esc(c.amount) + '">' +
      '<button type="button" class="primary" data-act="check">Prepare Check No. ' + nextNo + '</button>' +
      '<p class="muted">Try an amount above the balance to see ALTOS refuse it.</p></div>' + (S.lastCheck ? checkPaper(S.lastCheck) : '');
  }
  function pad3(n) { return ('00' + n).slice(-3); }
  function pad4(n) { return ('000000' + n).slice(-7); }
  function words(n) {
    var ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
    var tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
    function under1000(x) {
      var s = '';
      if (x >= 100) { s += ones[Math.floor(x / 100)] + ' hundred'; x %= 100; if (x) s += ' '; }
      if (x >= 20) { s += tens[Math.floor(x / 10)]; if (x % 10) s += '-' + ones[x % 10]; } else if (x) s += ones[x];
      return s;
    }
    var pesos = Math.floor(n), cents = Math.round((n - pesos) * 100), parts = [], units = ['', ' thousand', ' million', ' billion'], i = 0;
    if (!pesos) parts.push('zero');
    while (pesos > 0) { var c = pesos % 1000; if (c) parts.unshift(under1000(c) + units[i]); pesos = Math.floor(pesos / 1000); i++; }
    var s = parts.join(' ') + ' pesos';
    if (cents) s += ' and ' + cents + '/100';
    return s.charAt(0).toUpperCase() + s.slice(1) + ' only';
  }
  function checkPaper(c) {
    return '<div class="paper check"><div style="display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap"><b>Sample Bank · ' + ACCOUNTS[c.account].name + '</b><span>No. <span class="no">' + c.no + '</span></span></div>' +
      '<p style="text-align:right;margin:6px 0">Date: ' + longDate(c.date) + '</p><p>Pay to the order of <b>' + esc(c.payee) + '</b></p>' +
      '<p class="amt">' + peso(c.amount) + '</p><p>' + esc(words(c.amount)) + '</p><p class="muted">' + esc(c.dv) + ' · ' + esc(c.what) + '</p>' +
      '<div class="void">A sample from the ALTOS demo. Not a check, not negotiable.</div></div>';
  }
  function checks() {
    var list = S.checks.slice().reverse();
    return '<h1>Check Issuance</h1>' + about('Release a prepared check when the payee receives it. Every check is in the Cash Book from the day it is prepared.') +
      '<div class="tbl"><table><thead><tr><th>Check No.</th><th>Date</th><th>Account</th><th>Payee</th><th class="r">Amount</th><th>Status</th><th></th></tr></thead><tbody>' +
      list.map(function (c) {
        return '<tr><td>' + c.no + '</td><td class="nw">' + shortDate(c.date) + '</td><td>' + (c.account === 'GF' ? 'General Fund' : 'SEF') + '</td><td>' + esc(c.payee) +
          '<div class="muted">' + esc(c.what) + '</div></td><td class="r">' + money(c.amount) + '</td><td>' + statusChip(c.status) +
          (c.to ? '<div class="muted">to ' + esc(c.to) + '</div>' : '') + '</td><td>' + (c.status === 'Prepared' ? '<button type="button" class="small primary" data-act="release" data-v="' + c.no + '">Release</button>' : '') + '</td></tr>';
      }).join('') + '</tbody></table></div>';
  }

  // ------------------------------------------------------------------ System Administrator
  // collections before today, by month (sample figures)
  var PAST = [4820500, 1152300, 986400, 742150, 689900, 812300, 884600, 621750, 709300, 664200, 731400, 0];
  function dashboard() {
    var today = S.ors.filter(function (o) { return o.date === TODAY; });
    var monthToDate = r2(412640.5 + sumOrs(today));
    var months = PAST.slice(0, MONTH).concat([monthToDate]);
    var max = Math.max.apply(null, months);
    var bars = months.map(function (v, i) {
      return '<div class="bar"><span>' + MONTHS[i].slice(0, 3) + '</span><div><div class="b' + (i === MONTH ? ' now' : '') + '" style="width:' + Math.max(1, v / max * 100).toFixed(1) + '%"></div></div><span class="r">' + money(v) + '</span></div>';
    }).join('');
    var year = r2(months.reduce(function (s, v) { return s + v; }, 0));
    var bySrc = {};
    today.forEach(function (o) {
      o.lines.forEach(function (l) {
        var k = /Real Property/.test(l.nature) ? 'Real property tax' : /Business Tax/.test(l.nature) ? 'Business tax' : /Rental/.test(l.nature) ? 'Market and other rentals' : 'Fees and charges';
        bySrc[k] = r2((bySrc[k] || 0) + l.amount);
      });
    });
    var src = Object.keys(bySrc).sort(function (a, b) { return bySrc[b] - bySrc[a]; });
    var byOff = {};
    today.forEach(function (o) { byOff[o.name] = r2((byOff[o.name] || 0) + o.total); });
    return '<h1>Collections Dashboard</h1>' + about("Today's and the year's collections at a glance. Every chart has its table, and the figures come from the same records.") +
      '<div class="tiles"><div class="tile"><div class="k">Collections today</div><div class="v">' + peso(sumOrs(today)) + '</div><div class="s">' + today.length + ' official receipts</div></div>' +
      '<div class="tile"><div class="k">' + MONTHS[MONTH] + ' so far</div><div class="v">' + peso(monthToDate) + '</div><div class="s">to ' + longDate(TODAY) + '</div></div>' +
      '<div class="tile"><div class="k">Year to date</div><div class="v">' + peso(year) + '</div><div class="s">January to ' + MONTHS[MONTH] + '</div></div>' +
      '<div class="tile"><div class="k">Waiting for deposit</div><div class="v">' + peso(r2(S.rcds.filter(function (r) { return r.status === 'Submitted'; }).reduce(function (s, r) { return s + r.total; }, 0))) +
      '</div><div class="s">RCDs not yet consolidated</div></div></div>' +
      '<div class="card"><h2>Collections by month, ' + YEAR + '</h2><div class="bars">' + bars + '</div><p class="muted">January is the highest: business taxes and permits are due then.</p></div>' +
      '<div class="card"><h2>Today by source</h2><div class="tbl"><table><thead><tr><th>Source</th><th class="r">Amount</th><th class="r">Share</th></tr></thead><tbody>' +
      src.map(function (k) { return '<tr><td>' + k + '</td><td class="r">' + money(bySrc[k]) + '</td><td class="r">' + (bySrc[k] / sumOrs(today) * 100).toFixed(1) + '%</td></tr>'; }).join('') +
      '</tbody></table></div><h2>Today by Collecting Officer</h2><div class="tbl"><table><thead><tr><th>Collecting Officer</th><th class="r">Amount</th></tr></thead><tbody>' +
      Object.keys(byOff).map(function (k) { return '<tr><td>' + esc(k) + '</td><td class="r">' + money(byOff[k]) + '</td></tr>'; }).join('') + '</tbody></table></div></div>';
  }
  function activity() {
    return '<h1>Activity Log</h1>' + about('Every action, by whom and when. In ALTOS the log is sealed: no one can change or delete an entry, not even the System Administrator.') +
      '<div class="tbl"><table><thead><tr><th>Time</th><th>User</th><th>Action</th></tr></thead><tbody>' +
      S.log.slice().reverse().map(function (x) { return '<tr><td class="nw">' + x.time + '</td><td class="nw">' + esc(x.user) + '<div class="muted">' + esc(x.role) + '</div></td><td>' + esc(x.what) + '</td></tr>'; }).join('') +
      '</tbody></table></div><p class="muted">What you do in this demo appears here too. It is gone when you reload the page.</p>';
  }

  // ------------------------------------------------------------------ the guided tour: one day's work in ALTOS, step by step
  // Each step names the working page, what to do there, and when it counts as done (read from the demo's records).
  var TOUR = [
    { role: 'col', page: 'issue', title: 'Issue an official receipt',
      how: 'Type any name in <b>Payor</b>, keep the fee or pick another one, then tap <b>Issue OR</b>.',
      done: function () { return myOrs().length > 4; } },
    { role: 'col', page: 'rcd', title: 'Close the day in My RCD',
      how: 'Your receipts are now on the Report of Collections and Deposits (RCD). Scroll down and tap <b>Close the day and remit</b>.',
      done: function () { return S.rcds.some(function (r) { return r.officer === 'Maria Santos'; }); } },
    { role: 'col', page: 'raaf', title: 'Submit your RAAF',
      how: 'The RAAF shows the receipts you used this month and the ones left. Tap <b>Submit my RAAF</b>.',
      done: function () { return !!S.raaf.col; } },
    { role: 'lo', page: 'refused', title: 'Refuse a short remittance',
      how: 'Luz Ramos handed in ₱50.00 less than her RCD says. Her RCD and the reason are already filled in. Tap <b>Refuse this report</b>.',
      done: function () { return S.rcds.some(function (r) { return r.status === 'Refused'; }); } },
    { role: 'lo', page: 'crcd', title: 'Count the money and deposit it',
      how: 'Tick every RCD on the list, tap <b>Fill in the money received</b>, then tap <b>Record the deposit</b>.',
      done: function () { return S.crcds.length > 0; } },
    { role: 'lo', page: 'cashbook', title: 'See the deposit in the Cash Book',
      how: 'Your deposit is the newest line, under <b>Debit</b> (money into the bank). Scroll down to see it.',
      done: function () { return !!S.seen['lo-cashbook'] && S.crcds.length > 0; } },
    { role: 'do', page: 'prepare', title: 'Write a check',
      how: 'Type a payee, what it is for and an amount, then tap <b>Prepare Check</b>. Try an amount above the balance first to see ALTOS refuse it.',
      done: function () { return S.checks.length > 5; } },
    { role: 'do', page: 'checks', title: 'Release the check',
      how: 'Tap <b>Release</b> beside a check that says Prepared, as if the payee came to receive it.',
      done: function () { return S.checks.filter(function (c) { return c.status === 'Released'; }).length > 4; } },
    { role: 'sys', page: 'log', title: 'Read the Activity Log',
      how: 'Everything you just did is recorded here, with the time and the officer. In ALTOS nothing escapes this log.',
      done: function () { return !!S.seen['sys-log']; } }
  ];
  function tourAt() { for (var i = 0; i < TOUR.length; i++) if (!TOUR[i].done()) return i; return TOUR.length; }
  function tourBar() {
    var i = tourAt(), n = TOUR.length;
    if (S.tourOff) return '<div class="tour off"><span>Guided tour: step ' + Math.min(i + 1, n) + ' of ' + n + '</span><button type="button" class="small" data-act="tour-on">Show</button></div>';
    var dots = TOUR.map(function (t, k) { return '<i class="' + (k < i ? 'd' : k === i ? 'c' : '') + '" style="background:' + (k <= i ? ROLES[t.role].key : '') + '"></i>'; }).join('');
    if (i >= n) {
      return '<div class="tour done"><div class="th"><b>Guided tour complete</b><button type="button" class="small" data-act="tour-off">Hide</button></div>' +
        '<p>That was one day in a local treasury: receipts issued, the day closed, the money counted and deposited, a check written and released, and every step in the log. ' +
        'Keep exploring the menus, or <a href="#" data-act="restart">start the demo again</a>.</p><div class="dots">' + dots + '</div></div>';
    }
    var t = TOUR[i], here = S.role === t.role && S.page === t.page, R = ROLES[t.role];
    return '<div class="tour" style="--tk:' + R.key + '"><div class="th"><span class="tn">Step ' + (i + 1) + ' of ' + n + ' · ' + R.label + '</span>' +
      '<button type="button" class="small" data-act="tour-off">Hide</button></div>' +
      '<div class="tt">' + t.title + '</div><p>' + (here ? t.how : 'Go to the <b>' + R.label + '</b> page, <b>' + TITLES[t.page] + '</b>.') + '</p>' +
      (here ? '' : '<a class="go" href="#' + t.role + '-' + t.page + '">Take me there →</a>') + '<div class="dots">' + dots + '</div></div>';
  }
  // on phones a wide table becomes one small card per row, each value with its column name
  function stackTables() {
    Array.prototype.forEach.call(root.querySelectorAll('.tbl table:not(.cb)'), function (tb) {
      var heads = Array.prototype.map.call(tb.querySelectorAll('thead th'), function (th) { return th.textContent; });
      if (heads.length < 5 && !tb.classList.contains('stk')) return;
      tb.classList.add('stk');
      Array.prototype.forEach.call(tb.querySelectorAll('tbody tr'), function (tr) {
        var col = 0;
        Array.prototype.forEach.call(tr.children, function (td) {
          var span = td.colSpan || 1, l = span === 1 ? (heads[col] || '') : '';
          col += span;
          td.setAttribute('data-l', l);
          if (l && td.childNodes.length) {  // one box for the value, so the column name sits on the left and the value on the right
            var v = document.createElement('span'); v.className = 'v';
            while (td.firstChild) v.appendChild(td.firstChild);
            td.appendChild(v);
          }
        });
      });
    });
  }

  // ------------------------------------------------------------------ drawing and routing
  var SCREENS = {
    col: { home: home, issue: issue, rptcalc: rptcalc, collections: collections, rcd: rcd, raaf: raaf, cashbook: colCashbook },
    lo: { home: home, crcd: crcd, refused: refused, craaf: craaf, register: register, locash: loCashbook, cashbook: cashbook },
    do: { home: home, prepare: prepare, checks: checks, cashbook: cashbook },
    sys: { home: home, dashboard: dashboard, register: register, cashbook: cashbook, log: activity }
  };
  var TITLES = { home: 'Home', issue: 'Issue Official Receipt', rptcalc: 'RPT Tax Calculator', collections: 'My Collections', rcd: 'My RCD', raaf: 'My RAAF', craaf: 'RAAF & CRAAF', locash: 'My Cash Book',
    crcd: 'Consolidated RCD', refused: 'Refused Reports', register: 'Collections Register', cashbook: 'Cash Book', prepare: 'Prepare Check',
    checks: 'Check Issuance', dashboard: 'Collections Dashboard', log: 'Activity Log' };
  var LOGIN = root.innerHTML;
  function draw(keepScroll) {
    var y = window.scrollY;
    if (!S.role) {
      root.innerHTML = LOGIN;
      document.body.classList.add('signin');
      root.querySelector('#pick').innerHTML = pickPage();
      document.title = 'ALTOS Demo: Try the Treasury Software · Butch Mahinay';
      return;
    }
    document.body.classList.remove('signin');
    root.innerHTML = frame(SCREENS[S.role][S.page]());
    stackTables();
    fitSheets();
    document.title = TITLES[S.page] + ' · ALTOS Demo';
    if (keepScroll) window.scrollTo(0, y);
    var on = root.querySelector('.side a.on');
    if (on && on.scrollIntoView && window.innerWidth <= 820) on.scrollIntoView({ block: 'nearest', inline: 'center' });
  }
  function route() {
    var h = location.hash.replace(/^#/, '').split('-');
    if (ROLES[h[0]]) {
      var first = S.role !== h[0];
      S.role = h[0];
      S.page = SCREENS[S.role][h[1]] ? h[1] : 'home';
      S.seen[S.role + '-' + S.page] = true;
      if (first) log('Signed in (demo)');
      draw(false);
      window.scrollTo(0, 0);
    } else {
      S.role = null;
      draw(false);
    }
  }

  // ------------------------------------------------------------------ what each tap and entry does
  root.addEventListener('click', function (e) {
    var b = e.target.closest('[data-role],[data-act]');
    if (!b) return;
    if (b.dataset.role) { go(b.dataset.role, 'home'); return; }
    var act = b.dataset.act, v = b.dataset.v;
    if (act === 'tour-off' || act === 'tour-on') { S.tourOff = act === 'tour-off'; draw(true); return; }
    if (act === 'restart') { e.preventDefault(); fresh(); history.replaceState(null, '', location.pathname); route(); window.scrollTo(0, 0); return; }
    if (act === 'form') { newDraft(v); draw(true); }
    else if (act === 'add-line') { draft.lines.push({ fee: 0, amount: FEES[0].amount }); draw(true); }
    else if (act === 'del-line') { draft.lines.splice(+b.dataset.line, 1); draw(true); }
    else if (act === 'issue') doIssue();
    else if (act === 'view-or') { e.preventDefault(); S.view = v; draw(false); window.scrollTo(0, 0); }
    else if (act === 'remit') doRemit();
    else if (act === 'submit-raaf') {
      S.raaf.col = { date: TODAY, time: timeNow() };
      log('Submitted RAAF for ' + RAAF_MONTH + ' to the Liquidating Officer');
      draw(true);
    }
    else if (act === 'view-raaf') { S.viewRaaf = v; draw(false); var w = root.querySelectorAll('.sheet-wrap')[0]; if (w) w.parentNode.scrollIntoView(); }
    else if (act === 'view-rcd') { S.viewRcd = v; draw(false); var t = root.querySelector('.sheet-wrap'); if (t) t.parentNode.scrollIntoView(); else window.scrollTo(0, 0); }
    else if (act === 'cr-acct') { S.cr.account = v; S.cr.picked = {}; S.cr.count = {}; draw(true); }
    else if (act === 'fill') {
      var cash = r2(S.rcds.filter(function (r) { return S.cr.picked[r.no] && r.status === 'Submitted' && r.account === S.cr.account; })
        .reduce(function (s, r) { return s + r.cash; }, 0));
      S.cr.count = {};
      DENOS.forEach(function (d) { var n = Math.floor(r2(cash / d) + 1e-9); if (n > 0) { S.cr.count[d] = n; cash = r2(cash - n * d); } });
      draw(true);
    }
    else if (act === 'clear-count') { S.cr.count = {}; draw(true); }
    else if (act === 'deposit') doDeposit();
    else if (act === 'refuse') doRefuse();
    else if (act === 'cb-acct') { S.cbAcct = v; draw(true); }
    else if (act === 'lo-acct') { S.loAcct = v; draw(true); }
    else if (act === 'check') doCheck();
    else if (act === 'release') {
      var c = S.checks.filter(function (x) { return x.no === v; })[0];
      c.status = 'Released'; c.to = c.payee;
      log('Released Check No. ' + c.no + ' to ' + c.payee);
      flash('ok', 'Check No. ' + c.no + ' released to ' + esc(c.payee) + '.');
      draw(true);
    }
  });
  function field(e) {
    var el = e.target, f = el.dataset && el.dataset.f;
    if (!f) return null;
    return { el: el, f: f, val: el.type === 'checkbox' ? el.checked : el.value };
  }
  // typing updates the record without redrawing (so the keyboard stays open); choices redraw at once
  root.addEventListener('input', function (e) {
    var x = field(e); if (!x) return;
    if (x.f === 'payor') { draft.payor = x.val; syncIssue(); }
    else if (x.f === 'amount') { draft.lines[+x.el.dataset.line].amount = x.val; syncIssue(); }
    else if (x.f === 'count') {
      S.cr.count[x.el.dataset.v] = x.val.replace(/[^0-9]/g, '');
      var counted = r2(DENOS.reduce(function (s, d) { return s + d * num(S.cr.count[d]); }, 0));
      var out = document.getElementById('counted'); if (out) out.textContent = peso(counted);
    }
    else if (x.f === 'slip') S.cr.slip = x.val;
    else if (x.f === 'ck-payee') S.ck.payee = x.val;
    else if (x.f === 'ck-what') S.ck.what = x.val;
    else if (x.f === 'ck-amount') S.ck.amount = x.val;
  });
  root.addEventListener('change', function (e) {
    var x = field(e); if (!x) return;
    if (x.f === 'fee') { var l = draft.lines[+x.el.dataset.line]; l.fee = +x.val; l.amount = FEES[l.fee].amount || ''; draw(true); }
    else if (x.f === 'pin') { draft.pin = x.val; draw(true); }
    else if (x.f === 'whole') { draft.wholeYear = x.val; draw(true); }
    else if (x.f === 'cpin') { S.calc.pin = x.val; draw(true); }
    else if (x.f === 'cdate') { if (x.val) { S.calc.date = x.val; draw(true); } }
    else if (x.f === 'cwhole') { S.calc.whole = x.val; draw(true); }
    else if (x.f === 'pick') { S.cr.picked[x.el.dataset.v] = x.val; draw(true); }
    else if (x.f === 'count') draw(true);
    else if (x.f === 'refpick') { S.refPick = x.val; draw(true); }
    else if (x.f === 'regf') { S.regFilter = x.val; draw(true); }
    else if (x.f === 'ck-account') { S.ck.account = x.val; draw(true); }
  });
  function syncIssue() {
    var total = r2(draft.lines.reduce(function (s, l) { return s + num(l.amount); }, 0));
    var t = document.getElementById('or-total'); if (t) t.textContent = peso(total);
    var b = root.querySelector('[data-act="issue"]');
    if (b) b.disabled = !(total > 0 && String(draft.payor).trim());
  }

  function doIssue() {
    var d = draft, o;
    if (d.form === '51') {
      var lines = d.lines.filter(function (l) { return num(l.amount) > 0; }).map(function (l) { return [FEES[l.fee].name, r2(num(l.amount)), FEES[l.fee].fund]; });
      if (!lines.length || !String(d.payor).trim()) { flash('bad', 'Type the payor and at least one amount.'); draw(true); return; }
      o = addOr('col', 'Maria Santos', '51', S.next.or51++, String(d.payor).trim(), lines);
    } else {
      var p = findProp(d.pin), rows = rptDue(p, TODAY, d.wholeYear);
      if (!rows.length) { flash('bad', 'Nothing is due on this property.'); draw(true); return; }
      var span = rows[0].year + ' Q' + rows[0].q + (rows.length > 1 ? ' to ' + rows[rows.length - 1].year + ' Q' + rows[rows.length - 1].q : '');
      var b = r2(rows.reduce(function (s, r) { return s + r.bdue; }, 0)), s2 = r2(rows.reduce(function (s, r) { return s + r.sdue; }, 0));
      o = addOr('col', 'Maria Santos', '56', S.next.or56++, p.owner, [['Real Property Tax – Basic (' + span + ')', b, 'GF'], ['Real Property Tax – SEF (' + span + ')', s2, 'SEF']], null, p.pin);
      var last = rows[rows.length - 1]; p.paid = [last.year, last.q];
    }
    log('Issued OR No. ' + o.no + ' (AF ' + o.form + ') for ' + peso(o.total));
    newDraft(d.form);
    flash('ok', 'OR No. ' + o.no + ' issued for ' + peso(o.total) + '. Issue another, or <a href="#col-rcd">close the day in My RCD</a>.');
    S.view = o.no;
    go('col', 'collections');
  }
  function doRemit() {
    var un = myOrs().filter(function (o) { return !o.reported; });
    var made = [];
    ['GF', 'SEF'].forEach(function (k) {
      var amt = sumOrs(un, k);
      if (!amt) return;
      var no = 'RCD ' + YEAR + '-' + pad(MONTH + 1) + '-' + pad3(S.next.rcd++);
      S.rcds.push({ no: no, officer: 'Maria Santos', account: k, date: TODAY, ors: un.filter(function (o) { return sumOrs([o], k) > 0; }), total: amt, cash: amt, status: 'Submitted', time: timeNow() });
      log('Remitted ' + no + ' (' + ACCOUNTS[k].name + ') for ' + peso(amt));
      made.push(no + ' (' + ACCOUNTS[k].name + ', ' + peso(amt) + ')');
    });
    un.forEach(function (o) { o.reported = true; });
    S.viewRcd = S.rcds[S.rcds.length - made.length].no;
    flash('ok', 'Remitted ' + made.join(' and ') + ' to the Liquidating Officer. Next: <a href="#lo-crcd">count the money as Liquidating Officer →</a>');
    draw(false); window.scrollTo(0, 0);
  }
  function doDeposit() {
    var c = S.cr, picked = S.rcds.filter(function (r) { return c.picked[r.no] && r.status === 'Submitted' && r.account === c.account; });
    var tot = r2(picked.reduce(function (s, r) { return s + r.total; }, 0));
    var no = 'CRCD ' + YEAR + '-' + pad(MONTH + 1) + '-' + pad3(20 + S.next.crcd++);
    var slip = String(c.slip || '').trim() || 'DS (no number)';
    picked.forEach(function (r) { r.status = 'Consolidated'; });
    S.crcds.push({ no: no, account: c.account, slip: slip, rcds: picked.map(function (r) { return r.no; }), kids: picked, total: tot, date: TODAY, time: timeNow() });
    S.viewRcd = no;
    cashIn(c.account, TODAY, no + ' / ' + slip, 'Deposit of collections (' + picked.map(function (r) { return r.officer; }).join(', ') + ')', tot);
    log('Consolidated ' + picked.length + ' RCD(s) into ' + no + ' and recorded deposit ' + slip + ' for ' + peso(tot));
    S.cr = { account: c.account, picked: {}, count: {}, slip: 'DS ' + (70300 + S.next.crcd) };
    flash('ok', no + ' recorded: ' + peso(tot) + ' deposited to the ' + ACCOUNTS[c.account].name + '. It is now in the <a href="#lo-cashbook">Cash Book</a>.');
    draw(false); window.scrollTo(0, 0);
  }
  function doRefuse() {
    var sel = document.getElementById('ref-no'), why = document.getElementById('reason').value.trim();
    if (!why) { flash('bad', 'Write the reason. A refusal always needs one.'); draw(true); return; }
    var r = S.rcds.filter(function (x) { return x.no === sel.value; })[0];
    r.status = 'Refused'; r.reason = why; r.by = ROLES[S.role].user; r.when = timeNow();
    r.ors.forEach(function (o) { o.reported = false; });
    log('Refused ' + r.no + ' of ' + r.officer + ': ' + why);
    S.refPick = null;
    flash('ok', r.no + ' refused and sent back to ' + esc(r.officer) + '. The refusal stays on record below.');
    draw(false); window.scrollTo(0, 0);
  }
  function doCheck() {
    var c = S.ck, amt = r2(num(c.amount)), bal = balance(c.account);
    if (!String(c.payee).trim() || !String(c.what).trim() || amt <= 0) { flash('bad', 'Type the payee, the particulars and the amount.'); draw(true); return; }
    if (amt > bal) {
      log('Check refused: ' + peso(amt) + ' is above the ' + ACCOUNTS[c.account].name + ' balance');
      flash('bad', 'Refused: the check of ' + peso(amt) + ' is above the Cash Book balance of the ' + ACCOUNTS[c.account].name + ', ' + peso(bal) + '.');
      draw(true); return;
    }
    var k = { no: pad4(S.next.check[c.account]++), account: c.account, date: TODAY, payee: String(c.payee).trim(), what: String(c.what).trim(),
      dv: 'DV ' + YEAR + '-' + pad(MONTH + 1) + '-' + pad3(S.next.dv++), amount: amt, status: 'Prepared', to: '' };
    S.checks.push(k);
    cashOut(c.account, TODAY, 'Check ' + k.no, k.payee + ' – ' + k.what + ' (' + k.dv + ')', amt);
    log('Prepared Check No. ' + k.no + ' (' + ACCOUNTS[c.account].name + ') to ' + k.payee + ' for ' + peso(amt));
    S.lastCheck = k;
    S.ck = { account: c.account, payee: '', what: '', amount: '' };
    flash('ok', 'Check No. ' + k.no + ' prepared. The Cash Book balance is now ' + peso(balance(c.account)) + '. <a href="#do-checks">Release it →</a>');
    draw(false); window.scrollTo(0, 0);
  }

  fresh();
  window.addEventListener('hashchange', route);
  route();
})();
