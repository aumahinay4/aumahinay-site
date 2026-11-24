"""Page builders. Each function returns a full HTML document as a string."""

import hashlib
import json
from urllib.parse import quote
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

import tags as t
from content import ABOUT, ALTOS, ALTOS_SERIES, BLOG, BLOG_CATEGORIES, CERTIFICATES, DISCLAIMER, LEARN_SERIES, PRIVACY, SITE, SUBSYSTEMS, TERMS, TRAININGS
from highlight import highlight
from share_cards import card_for
from glossary import GLOSSARY, GLOSSARY_INTRO
from lessons import LAST_CHECKED, LESSONS, TUTORIAL
from vocab import MODULES, VOCAB, module_url, word_source
from notes import NOTES, NOTES_INFO, OUTLINE, note_url
from rpt import RPT_URL, rpt_page
from altos_demo import DEMO_URL, demo_page
import book as BOOK
from style import CSS
from tags import Raw

STATIC = Path(__file__).parent / "static"
TUTORIALS = Path(__file__).parent / "tutorials"


ANCHOR_SCRIPT = (
    '(function(){if(location.hash.length<2)return;var stop=false;'
    'var el=function(){var id=decodeURIComponent(location.hash.slice(1));'
    'return document.getElementById(/^cat-/.test(id)?"blog-cats":id);};'  # blog topic links: the category button, not its hidden radio
    'var go=function(){var e=!stop&&el();if(e)e.scrollIntoView({behavior:"instant"});};'
    '["wheel","touchstart","keydown","mousedown"].forEach(function(n){addEventListener(n,function(){stop=true;},{passive:true});});'
    'document.addEventListener("DOMContentLoaded",function(){go();if(window.ResizeObserver){var r=new ResizeObserver(go);'
    'r.observe(document.body);setTimeout(function(){r.disconnect();},5000);}});addEventListener("load",go);})();'
)


def asset_url(name):
    """URL of a file in static/, with ?v=<content hash> so phones and Cloudflare
    fetch a changed picture right away instead of showing an old cached copy.
    preview.py swaps this for inline data URLs."""
    f = STATIC / name
    if not f.exists():
        return "/static/" + name
    return "/static/" + name + "?v=" + hashlib.sha1(f.read_bytes()).hexdigest()[:8]


# The full-screen button in the top bar.
FULLSCREEN_SCRIPT = """
(function () {
  var d = document, b = d.getElementById("fs");
  var on = d.fullscreenEnabled || d.webkitFullscreenEnabled;
  if (!b || !on) return;  // e.g. iPhone Safari: no full-screen support, so the button stays hidden
  function current() { return d.fullscreenElement || d.webkitFullscreenElement; }
  function sync() {
    var full = !!current();
    b.setAttribute("aria-pressed", full);
    b.setAttribute("aria-label", full ? "Exit full screen" : "Full screen");
    b.title = full ? "Exit full screen" : "Full screen";
  }
  b.hidden = false;
  b.addEventListener("click", function () {
    var e = d.documentElement;
    if (current()) (d.exitFullscreen || d.webkitExitFullscreen).call(d);
    else (e.requestFullscreen || e.webkitRequestFullscreen).call(e);
  });
  d.addEventListener("fullscreenchange", sync);
  d.addEventListener("webkitfullscreenchange", sync);
  sync();
})();
"""

FULLSCREEN_ICON = Raw(
    '<svg class="enter" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4v5H4M20 9h-5V4M15 20v-5h5M4 15h5v5"/></svg>'
    '<svg class="exit" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5"/></svg>'
)

# Projects page removed (Butch 2026-11-20): ALTOS now lives on Home at /#altos
NAV = [("/", "Home"), ("/study-notes/", "Study Notes"), ("/tutorials/", "Tutorials"), ("/blog/", "Blog"), ("/about/", "About")]

CERT_SCRIPT = """
(function () {
  var dlg = document.getElementById("cert-view");
  if (!dlg || !dlg.showModal) return;  // very old browsers just open the picture
  var img = dlg.querySelector("img"), ver = dlg.querySelector(".cert-verify");
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a.cert-thumb");
    if (!a) return;
    e.preventDefault();
    img.src = a.getAttribute("data-cert");
    img.alt = a.getAttribute("data-name") + " certificate";
    ver.href = a.getAttribute("data-verify");
    dlg.showModal();
  });
  dlg.addEventListener("click", function (e) { if (e.target === dlg || e.target.closest(".cert-close")) dlg.close(); });
})();
"""

# One full-screen certificate viewer per page that lists certificates
CERT_VIEWER = [
    t.dialog(
        t.button("×", type="button", class_="cert-close", aria_label="Close"),
        t.img(src="", alt=""),
        t.div(t.a("Verify on Coursera →", href="#", class_="cert-verify", target="_blank", rel="noopener"),
              t.button("Close", type="button", class_="cert-close btn ghost"), class_="cert-bar"),
        id="cert-view", class_="cert-view", aria_label="Certificate",
    ),
    t.script(Raw(CERT_SCRIPT)),
]

# The three-bar (hamburger) menu: tap it and the menu fills the screen in navy, like a news site's
# phone menu; tapping outside it, Esc, or tapping a link closes it (no X, Butch 2026-11-10). Contact and Privacy are in the menu but not in the swipe order.
MENU = NAV[:2] + [(RPT_URL, "RPT Calculator"), ("/projects/altos-book/", "The ALTOS Book")] + NAV[2:] + [("/contact/", "Contact"), ("/privacy/", "Privacy Policy"), ("/terms/", "Terms of Use")]


def menu_items():
    """The menu as built today. Study Notes appears only once a note is live, so the menu never leads to an
    empty hub page (AdSense "under construction" risk, Butch's audit 2026-11-10). The hourly build adds it on
    the first note's publish time."""
    return [(href, label) for href, label in MENU if href != "/study-notes/" or live_notes()]


CLOSE_ICON = Raw('<svg class="i-close" viewBox="0 0 24 24" aria-hidden="true"><path d="M4.5 12.5l5 5L19.5 7"/></svg>')  # a check mark, not an X, while the phone menu is open (Butch 2026-11-24)


def page_label(active):
    """The small orange label beside the phone menu button."""
    labels = {"/": "Public finance & civic tech", "/blog/": "Blog", "/tutorials/": "Tutorials", "/study-notes/": "Study Notes",
              BOOK_URL: "The ALTOS Book", "/about/": "About", "/contact/": "Contact", RPT_URL: "Free Tools",
              "/privacy/": "Privacy Policy", "/terms/": "Terms of Use", "/disclaimer/": "Disclaimer"}
    return labels.get(active, "Menu")


def phone_menu(active):
    """The phone menu card: the same entries as the computer menu; Free Tools and Study Notes & Book open in place."""
    out = []
    for a, b in top_items():
        if isinstance(b, list):
            here = any(href == active for href, _ in b)
            out.append(t.details(
                t.summary(a, CHEVRON, class_="active" if here else None),
                [t.a(label, href=href, class_="active" if href == active else None, aria_current="page" if href == active else None)
                 for href, label in b],
                class_="pm-group", open=here or None))
        else:
            out.append(t.a(b, href=a, class_="active" if a == active else None, aria_current="page" if a == active else None))
    return out


CHEVRON = Raw('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>')


def top_items():
    """Menu across the top on computers, as in Butch's chosen pattern file aumahinay_dev_homepage_preview
    (Butch 2026-11-23): Home, Free Tools (drop-down), Tutorials, Study Notes & Book, Blog, About, Contact.
    Each entry is (href, label) or (label, [(href, label), ...]) for a drop-down. Phones keep the three-bar menu."""
    books = [("/study-notes/", "Study Notes")] if live_notes() else []
    books.append((BOOK_URL, "The ALTOS Book"))
    return [("/", "Home"),
            ("Free Tools", [(RPT_URL, "Real Property Tax Calculator"), (DEMO_URL, "ALTOS Browser Demo")]),
            ("/tutorials/", "Tutorials"),
            ("Study Notes & Book", books) if len(books) > 1 else (BOOK_URL, "Book"),
            ("/blog/", "Blog"), ("/about/", "About"), ("/contact/", "Contact")]


def top_nav(active):
    out = []
    for a, b in top_items():
        if isinstance(b, list):
            here = any(href == active for href, _ in b)
            out.append(t.div(
                t.button(a, CHEVRON, type="button", class_="drop-btn" + (" active" if here else ""), aria_haspopup="true"),
                t.div([t.a(label, href=href, aria_current="page" if href == active else None) for href, label in b], class_="drop"),
                class_="top-drop"))
        else:
            out.append(t.a(b, href=a, class_="active" if a == active else None, aria_current="page" if a == active else None))
    return t.nav(out, class_="top-nav", aria_label="Top menu")


MENU_ICON = Raw('<svg viewBox="0 0 24 24" aria-hidden="true"><path class="b1" d="M3 6h18"/><path class="b2" d="M3 12h14"/><path class="b3" d="M3 18h10"/></svg>')  # bars long, medium, short, left-aligned (Butch 2026-11-14)
MENU_SCRIPT = """
(function () {
  var root = document.documentElement, btn = document.getElementById("menu-open"),
      menu = document.getElementById("site-menu");
  if (!btn || !menu) return;
  root.classList.add("menu-js");
  function set(open) {
    root.classList.toggle("menu-open", open);
    btn.setAttribute("aria-expanded", open);
    if (open) { var a = menu.querySelector("a.active") || menu.querySelector("a"); if (a) a.focus({ preventScroll: true }); }
    else btn.focus({ preventScroll: true });
  }
  btn.addEventListener("click", function () { set(!root.classList.contains("menu-open")); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && root.classList.contains("menu-open")) set(false); });
  // tap anywhere outside the half-screen menu to close it
  document.addEventListener("click", function (e) {
    if (root.classList.contains("menu-open") && !menu.contains(e.target) && !btn.contains(e.target)) set(false);
  });
  addEventListener("pageshow", function () { root.classList.remove("menu-open"); btn.setAttribute("aria-expanded", "false"); });
})();
"""

SWIPE_SCRIPT = """
(function () {
  // Phones: swipe left for the next menu page, swipe right for the previous one (wraps around).
  // Ignored when the swipe starts on something that scrolls sideways (code boxes, tables, the menu),
  // near the screen edge (the phone's own back/forward swipe), with two fingers, or while zoomed in.
  var pages = %s;
  var path = location.pathname, here = -1;
  pages.forEach(function (p, i) { if (path === p || (p !== "/" && path.indexOf(p) === 0)) here = i; });
  if (here < 0) return;  // e.g. the "page not found" page
  var x0, y0, t0, ok;
  function scrollsSideways(el) {
    for (; el && el !== document.body; el = el.parentElement) {
      var ox = getComputedStyle(el).overflowX;
      if ((ox === "auto" || ox === "scroll") && el.scrollWidth > el.clientWidth + 1) return true;
      if (/^(TEXTAREA|SELECT)$/.test(el.tagName) || (el.tagName === "INPUT" && !/^(radio|checkbox)$/.test(el.type))) return true;
      if (el.hasAttribute("data-noswipe")) return true;  // the book reader turns its own pages
    }
    return false;
  }
  document.addEventListener("touchstart", function (e) {
    if (document.documentElement.classList.contains("menu-open")) { ok = false; return; }
    var p = e.touches[0], edge = 24;
    ok = e.touches.length === 1 && p.clientX > edge && p.clientX < innerWidth - edge &&
         !(window.visualViewport && visualViewport.scale > 1.05) && !scrollsSideways(e.target);
    x0 = p.clientX; y0 = p.clientY; t0 = Date.now();
  }, { passive: true });
  document.addEventListener("touchmove", function (e) { if (e.touches.length > 1) ok = false; }, { passive: true });
  document.addEventListener("touchend", function (e) {
    if (!ok) return;
    ok = false;
    var p = e.changedTouches[0], dx = p.clientX - x0, dy = p.clientY - y0;
    if (Date.now() - t0 > 700 || Math.abs(dx) < Math.min(90, innerWidth * 0.25) || Math.abs(dx) < 2 * Math.abs(dy)) return;
    if (window.getSelection && String(getSelection())) return;  // selecting text, not swiping
    var step = dx < 0 ? 1 : -1, n = pages.length;
    var main = document.querySelector("main");
    if (main) main.classList.add(step > 0 ? "swipe-next" : "swipe-prev");
    setTimeout(function () { location.href = pages[(here + step + n) %% n]; }, 140);
  }, { passive: true });
  // coming back with the Back button: undo the slide-out
  addEventListener("pageshow", function () { var m = document.querySelector("main"); if (m) m.classList.remove("swipe-next", "swipe-prev"); });
})();
"""  # filled in at build time with the menu order (incl. RPT Calculator), see layout()



def person_json_ld():
    """Structured data for Google: who the site is about. Public facts only."""
    import json
    url = f"https://{SITE['domain']}/"
    profiles = [SITE[k] for k in ("linkedin", "github", "coursera") if SITE.get(k)]
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": url + "#website",
                "url": url,
                # Google shows this site name beside the photo in search results
                "name": SITE["short_name"],
                "alternateName": [SITE["name"], SITE["domain"]],
                "inLanguage": "en",
            },
            {
                "@type": "Person",
                "@id": url + "#person",
                "name": SITE["name"],
                "alternateName": SITE["short_name"],
                "url": url,
                "image": url + "static/avatar.png",
                "description": SITE["tagline"],
                "knowsAbout": ["Public finance", "Local government treasury operations", "Python", "Software development"],
                **({"sameAs": profiles} if profiles else {}),
            },
        ],
    }
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def layout(title, active, body, description=None, url=None, og_type="website", seo_title=None, json_ld=None,
           share_image=None):
    url = url or active
    # his name in every title, so a search for "Butch Mahinay" finds the site; a page may give its own search
    # title (seo_title), and a long title drops the name so search results don't cut off its key words
    if seo_title:
        page_title = seo_title
    elif active == "/":
        page_title = f"{SITE['short_name']} · {SITE['tagline_short']}"
    else:
        page_title = f"{title} · {SITE['short_name']}"
        if len(page_title) > 70:
            page_title = title
    doc = t.html(
        t.head(
            t.meta(charset="utf-8"),
            t.meta(name="viewport", content="width=device-width, initial-scale=1"),
            # Google AdSense code, only once SITE["adsense_client"] is set (Butch applies; see content.py).
            # Never on the 404 page (active is None): AdSense allows no ads on error pages.
            t.script(src=f"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={SITE['adsense_client']}",
                     crossorigin="anonymous", **{"async": "async"}) if SITE.get("adsense_client") and active is not None else None,
            # paint the phone's browser bars in the top bar's navy, so the site looks full-screen
            t.meta(name="theme-color", content="#f3f6fc", media="(prefers-color-scheme: light)"),
            t.meta(name="theme-color", content="#071631", media="(prefers-color-scheme: dark)"),
            t.title(page_title),
            # https://aumahinay.dev is the only address: test copies on *.pages.dev, www. and plain http jump to it
            t.script(Raw(f'if (/\\.pages\\.dev$/.test(location.hostname) || location.hostname === "www.{SITE["domain"]}" || (location.protocol === "http:" && location.hostname === "{SITE["domain"]}")) location.replace("https://{SITE["domain"]}" + location.pathname + location.search + location.hash);')),
            # links to a spot on a page (/#altos, /blog/#cat-finance, "In this article") land on that spot even when
            # pictures and fonts load later and push it down; stops as soon as the visitor scrolls or taps (Butch 2026-11-24)
            t.script(Raw(ANCHOR_SCRIPT)),
            t.link(rel="alternate", type="application/rss+xml", title=f"{SITE['short_name']}: new posts and lessons", href="/feed.xml"),
            t.link(rel="canonical", href=f"https://{SITE['domain']}{url}") if url else None,
            t.meta(name="description", content=description or SITE["tagline"]),
            # the 404 page, and pages Google can't read as text (AdSense "low-value content", Butch 2026-11-20)
            t.meta(name="robots", content="noindex") if active is None or url in NOINDEX_URLS else None,
            t.script(Raw(person_json_ld()), type="application/ld+json") if active == "/" else None,
            t.script(Raw(json.dumps(json_ld, ensure_ascii=False).replace("</", "<\\/")), type="application/ld+json") if json_ld else None,
            # link previews on Facebook, Messenger, Viber, LinkedIn and X
            t.meta(property="og:type", content=og_type),
            t.meta(property="og:site_name", content=SITE["short_name"]),  # his name, not the domain
            t.meta(property="og:title", content=page_title),
            t.meta(property="og:description", content=description or SITE["tagline"]),
            t.meta(property="og:url", content=f"https://{SITE['domain']}{url}"),
            # a post with a picture shares its own card (share_cards.py); every other page shares share.jpg.
            # ?v= is the picture's hash: new picture = new link, so Facebook fetches it again
            t.meta(property="og:image", content=f"https://{SITE['domain']}" + asset_url(share_image or "share.jpg")),
            t.meta(property="og:image:width", content="1200"),
            t.meta(property="og:image:height", content="630"),
            t.meta(property="og:image:alt", content=title if share_image else f"{SITE['short_name']}, {SITE['domain']}"),
            t.meta(name="twitter:card", content="summary_large_image"),
            t.link(rel="icon", href="/favicon.ico", sizes="any"),
            t.link(rel="icon", type="image/png", sizes="32x32", href=asset_url("favicon-32.png")),
            t.link(rel="apple-touch-icon", href=asset_url("apple-touch-icon.png")),
            t.link(rel="preconnect", href="https://fonts.googleapis.com"),
            t.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
            t.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Figtree:wght@400;500;600;700&display=swap"),
            t.style(Raw(CSS)),
        ),
        t.body(
            t.header(
                t.div(
                    # name and tagline at the left of the top bar, as in the downloaded pattern (Butch 2026-11-23)
                    t.a(t.span(SITE["short_name"], class_="bn"), t.span(SITE["tagline_short"], class_="bt"),
                        href="/", class_="brand-line", aria_label=f"{SITE['short_name']}, home"),
                    top_nav(active),
                    # phones and tablets (Butch 2026-11-23, mobile pattern file): a second line in the top bar with a round
                    # menu button beside the page's label; it opens a small rounded card and turns into a check mark
                    t.div(
                        t.button(MENU_ICON, CLOSE_ICON, type="button", id="menu-open", class_="menu-btn", aria_label="Open menu",
                                 aria_controls="site-menu", aria_expanded="false"),
                        t.span(page_label(active), class_="page-label"),
                        t.nav(phone_menu(active), id="site-menu", aria_label="Main menu"),
                        class_="phone-row",
                    ),
                    class_="wrap",
                ),
                class_="site",
            ),
            t.main(t.div(body, class_="wrap")),
            # small footer at the bottom of every page: "Built in Python" + Privacy Policy link (Butch 2026-11-10)
            # footer: the disclaimer in a box, then the copyright and policy links (Butch 2026-11-23, downloaded pattern)
            t.footer(t.div(
                           t.p(t.b("Disclaimer: "), "All book chapters, articles, calculators, code samples and study notes on ",
                               t.b(SITE["domain"]), " are written and published by Ambrosio U. Mahinay strictly in his "
                               "personal capacity, outside official working hours, for educational and informational "
                               "purposes. Content reflects the personal views and independent technical work of the "
                               "author and does not constitute an official government issuance, legal advice, a formal "
                               "tax assessment, or an endorsement by any Local Government Unit (LGU), the Bureau of Local "
                               "Government Finance (BLGF), the Commission on Audit (COA) or any government agency. "
                               "Always consult your local treasurer's office or qualified professionals for official "
                               "transactions. ", t.a("Full disclaimer", href="/disclaimer/"),
                               class_="disclaimer-box"),
                           t.div(
                               t.span(f"© {ph_today()[:4]} Ambrosio U. Mahinay", class_="copy"),
                               t.span(t.a("Privacy Policy", href="/privacy/", aria_current="page" if active == "/privacy/" else None),
                                      t.a("Terms of Use", href="/terms/", aria_current="page" if active == "/terms/" else None),
                                      t.a("Disclaimer", href="/disclaimer/", aria_current="page" if active == "/disclaimer/" else None),
                                      t.span("Built in Python", class_="built"),
                                      class_="legal-links"),
                               class_="foot-row"),
                           class_="wrap"), class_="legal"),
            t.script(Raw(MENU_SCRIPT)),
            t.script(Raw(SWIPE_SCRIPT % json.dumps([href for href, _ in menu_items() if href not in ("/contact/", "/privacy/", "/terms/", "/disclaimer/", "/projects/altos-book/")]))),
            CERT_VIEWER if 'class="cert-thumb"' in t.render(body) else None,
        ),
        lang="en",
    )
    return "<!doctype html>\n" + doc


def article_ld(headline, description, url, day=None, image=None, kind="BlogPosting"):
    """Structured data for a post, lesson or note: tells search engines its title, author and date."""
    site = f"https://{SITE['domain']}"
    data = {
        "@context": "https://schema.org",
        "@type": kind,
        "headline": headline,
        "description": description,
        "url": site + url,
        "mainEntityOfPage": site + url,
        "inLanguage": "en",
        "image": site + "/static/" + (image or "share.jpg"),
        "author": {"@type": "Person", "name": SITE["name"], "alternateName": SITE["short_name"], "url": site + "/about/"},
        "publisher": {"@type": "Person", "name": SITE["name"], "url": site + "/"},
    }
    if day:
        data["datePublished"] = day
    return data


def part(title, active, *body, description=None, url=None, og_type="website", seo_title=None, json_ld=None,
         share_image=None):
    """The pieces of one page, before it is wrapped in the site layout. seo_title (optional) is the full
    browser and search-result title; json_ld (optional) is structured data for search engines."""
    return {"title": title, "active": active, "body": list(body), "description": description, "url": url,
            "og_type": og_type, "seo_title": seo_title, "json_ld": json_ld, "share_image": share_image}


def tag_list(items):
    return t.div([t.span(item, class_="tag") for item in items], class_="tags") if items else None


def wordmark(word="ALTOS"):
    """ALTOS in its five letter colours, as on the book cover."""
    return [t.span(ch, class_=f"l{i}") for i, ch in enumerate(word)]


def cover_img(class_):
    return t.img(src=asset_url("altos-cover.jpg"), alt=f"Cover of {ALTOS['book']['title']}", class_=class_, width="600", height="900")


def subsystem_node(sub, summary=True):
    return t.div(
        t.div(t.span(sub["code"], class_="code"), t.span(sub["status"], class_="status" if sub["status"] == "Planned" else "status live"), class_="node-head"),
        t.p(sub["summary"]) if summary else None,
        t.div(sub["movement"], class_="forms"),
        # the whole box opens that officer's side of the demo (Butch 2026-11-20: Home as clickable as possible)
        t.a("Open it in the demo →", href=DEMO_URL + ("#do-home" if "Disbursement" in sub["code"] else "#col-home"), class_="go stretch"),
        class_="node child",
    )


def family():
    """ALTOS as the mother system with its subsystems branching below."""
    return t.div(
        t.div(
            t.div(t.span(t.span(wordmark(), class_="wordmark"), class_="code"), class_="node-head"),
            # full name left out: the ALTOS box below shows it (no duplicates, Butch 2026-11-20)
            t.p("Collect, Disburse and Report in one database, with the ALTOS Framework built in."),
            t.a("Try the demo →", href=DEMO_URL, class_="go stretch"),
            class_="node mother",
        ),
        t.div(class_="branch", aria_hidden="true"),
        t.div([subsystem_node(sub) for sub in SUBSYSTEMS], class_="children"),
        class_="family",
    )


def cert_image(c):
    """static/certs/<Coursera id>.jpg, the certificate itself (from Coursera's own share image)."""
    return "certs/" + c["verify"].rstrip("/").split("/")[-1] + ".jpg"


def cert_card(c):
    img = cert_image(c)
    return t.div(
        # the certificate picture; tapping it opens it full screen (CERT_SCRIPT); without JS the link opens the picture
        t.a(t.img(src=asset_url(img), alt=f"{c['name']} certificate", loading="lazy", width="1164", height="928"),
            href=asset_url(img), class_="cert-thumb", data_cert=asset_url(img), data_name=c["name"], data_verify=c["verify"],
            aria_label=f"View the {c['name']} certificate"),
        t.div(t.span(c["kind"], class_="badge" if c["kind"].startswith("Prof") else "badge spec"), class_="meta"),
        t.h3(c["name"]),
        t.div(f"Completed {c['date']} · {c['courses']} courses · Coursera", class_="meta"),
        t.details(t.summary("Show courses"), t.ul([t.li(x) for x in c["course_list"]])),
        t.div(t.a("Verify on Coursera →", href=c["verify"], target="_blank", rel="noopener"), class_="foot"),
        class_="card",
    )


def photo_title(*h1_args, photo=False, **h1_kw):
    """Page title. Butch's ringed photo shows only on About (Butch 2026-11-10: no photo elsewhere)."""
    if not photo:
        return t.h1(*h1_args, **h1_kw)
    return t.div(t.img(src=asset_url("hero-photo.jpg"), alt="Photo of Ambrosio “Butch” U. Mahinay", width="400", height="400", class_="hero-photo"),
                 t.h1(*h1_args, **h1_kw), class_="about-hello")


def section_head(title, link_text, href):
    return t.div(t.h2(title), t.a(f"{link_text} →", href=href, class_="more"), class_="section-head")


def kicked(kicker, head):
    """Small orange label above a section heading (Butch 2026-11-23, downloaded pattern)."""
    return t.div(t.p(kicker, class_="eyebrow"), head, class_="kick")


HERO_ART = Raw(
    '<div class="home-art" aria-hidden="true"><div class="art-in">'
    '<div class="art-bars"><span class="peso">₱</span><i></i><i></i><i></i></div>'
    '<div class="art-doc"><i></i><i></i><i></i><i></i></div><span class="art-arrow">→</span>'
    '<div class="art-code"><span class="dots"><i></i><i></i><i></i></span>'
    '<pre><b>def</b> <em>compute_rpt</em>(av):\n    basic = av * <u>0.01</u>\n    sef = av * <u>0.01</u>\n    <b>return</b> basic + sef</pre>'
    '</div></div></div>')


ESSENTIAL_GUIDES = ["how-to-use-the-rpt-calculator", "year-end-in-the-treasury", "why-i-built-altos"]


def home():
    """Home: what the site offers (blog, free Python lessons, ALTOS), the newest writing first,
    then topics, lessons, the project and a short note about the author (Butch 2026-11-09:
    make Home relevant to the whole site and ready for an AdSense review)."""
    posts = sorted(live_posts(), key=post_day, reverse=True)
    lessons = [x for x in LESSONS if lesson_is_live(x)]
    topics = [(key, label, sum(b["category"] == key for b in posts)) for key, label, _ in BLOG_CATEGORIES]
    # cornerstone posts picked by hand; a scheduled one shows only once it is live
    guides = [b for slug in ESSENTIAL_GUIDES for b in posts if b["slug"] == slug]
    topic_text = {
        "software": "Building ALTOS, Python, and software that keeps public money accountable.",
        "finance": "Stand-alone posts on public money: local taxes, tools like the RPT calculator, and the rules behind them.",
        "treasury": "Everyday work inside a local treasury: taxes, receipts, budgets, checks, year-end and audits.",
        "personal": "The farm, the province, and life beyond the office.",
        "learn": "Short series on cybersecurity, data analytics, business intelligence and project management, "
                 "in plain words for people who work in local government.",
    }
    return part(
        "Home", "/",
        # hero as in the downloaded desktop/phone pattern (Butch 2026-11-23): words at the left, two buttons,
        # a small treasury-and-code picture at the right (below the words on phones)
        t.div(
            t.div(
                t.p("Public finance & civic tech", class_="eyebrow"),
                t.h1("Where public finance meets Python"),
                t.p("Plain-language writing on local treasury work and public finance, free tutorials (Python "
                    "for treasury staff and Civil Service exam vocabulary), a free real property tax calculator, "
                    "and notes from building ALTOS. Everything here, this website included, is the work of a "
                    "treasury worker who builds software and websites.",
                    class_="lead"),
                t.div(
                    t.a("Open RPT Calculator →", href=RPT_URL, class_="btn blue"),
                    t.a("Explore ALTOS", href=ALTOS_URL, class_="btn outline"),
                    class_="btns",
                ),
                class_="home-copy",
            ),
            HERO_ART,
            class_="home-hero",
        ),
        # "Start here" (Butch 2026-11-23, AdSense blueprint): three ways in, replacing "What you'll find here"
        # and the separate "Free tool" box, so nothing on Home is listed twice
        kicked("Quick entry", t.h2("Start Here")),
        t.div(
            [
                t.div(t.p(kicker, class_="eyebrow"), t.h3(title), t.p(text),
                      t.p([t.a(go, href=href) for go, href in links], class_="go-links"), class_="card start")
                for kicker, title, text, links in (
                    ("Free tool", "Real Property Tax Calculator",
                     "Work out the basic real property tax and the Special Education Fund on any assessed value, "
                     "with the discount or interest, and see how the tax is shared.",
                     [("Open the calculator →", RPT_URL)]),
                    ("Learn and practice", "Study Notes and Tutorials",
                     "Local treasury work in plain words, each note with a short quiz, plus beginner-friendly "
                     "Python lessons and English vocabulary for the Civil Service exam.",
                     [*([("Read the study notes →", NOTES_INFO["url"])] if live_notes() else []),
                      ("Start the tutorials →", "/tutorials/"),
                      # English vocabulary link (Butch 2026-11-23: "add in the learn & practice the english vocabulary")
                      *([("Practice English vocabulary →", f"/tutorials/#{VOCAB['slug']}")] if live_modules() else [])]),
                    ("The project", "ALTOS and the Book",
                     "The Automated Local Treasury Operations System, a browser demo with made-up data, and the "
                     "book behind it, 360° Accountability.",
                     [("Explore ALTOS →", ALTOS_URL), ("Read the book →", BOOK_URL)]),
                )
            ],
            class_="grid three start-here",
        ),
        *([kicked("Cornerstone reading", t.h2("Essential Guides")),
           t.div([t.a(t.span(category_label(p), t.span(f"{reading_minutes(p)} min read", class_="muted")),
                      t.b(p["title"]), href=post_url(p), class_="related-card") for p in guides],
                 class_="related guides")] if guides else []),
        kicked("Writing", section_head("Latest posts", f"All {len(posts)} posts", "/blog/")),
        t.div([post_card(b) for b in [p for p in posts if p not in guides][:3]], class_="post-list home-posts"),
        # every topic in one box, as buttons with their post counts (downloaded pattern)
        t.div(
            t.div(t.div(t.h2("Browse by topic"), t.p("Each topic opens the blog with only its posts.", class_="muted")),
                  t.span(f"{len(posts)} posts", class_="badge checked"), class_="topic-top"),
            t.div([t.a(t.b(label), t.span(f"{n} post{'s' if n != 1 else ''} →"), href=f"/blog/#cat-{key}", class_="topic-pill",
                       title=topic_text.get(key)) for key, label, n in topics if n], class_="topic-pills"),
            class_="topic-box",
        ),
        kicked("Learn", section_head(TUTORIAL["title"], "All lessons", "/tutorials/")),
        t.div([lesson_card(x, mini=True) for x in lessons[::-1][:3]], class_="grid three"),
        *altos_section(),
        t.h2("About the author"),
        author_card(),
        description="Plain-language writing on Philippine local treasury work and public finance, free Python "
                    "lessons, Civil Service exam vocabulary and a real property tax calculator.",
    )


def author_head(h1=False):
    """Ringed photo, name and the three roles one per line, then a thin line under them. The same head on the
    About page, the author card and the side author box (Butch 2026-11-24: "for uniformity")."""
    name = "Ambrosio “Butch” U. Mahinay, MPA"
    photo = t.img(src=asset_url("hero-photo.jpg"), alt="Ambrosio “Butch” U. Mahinay", width="400", height="400",
                  class_="hero-photo author-photo", loading=None if h1 else "lazy")
    return t.div(
        photo if h1 else t.a(photo, href="/about/", aria_label="About Ambrosio “Butch” U. Mahinay"),
        t.div(
            t.h1(name, class_="author-name") if h1 else t.p(t.a(name, href="/about/"), class_="author-name"),
            t.p([t.span(r) for r in ABOUT["roles"].split(" · ")], class_="author-roles"),  # one role per line
        ),
        class_="author-top",
    )


def author_card():
    """Short author box: on Home and at the end of every blog post. Matches the About page (Butch 2026-11-10:
    "be consistent"): same name, same violet roles line and the same facts, in third person ("he", Butch 2026-11-10) as the About intro."""
    return t.div(
        author_head(),
        t.p("He is a public administration practitioner, author, and self-taught software developer in Quezon "
            "Province, Philippines, with over 15 years in government service, more than 13 of them in local treasury "
            "work. He has earned 7 Google Professional Certificates and 3 Specializations on Coursera. "
            "He writes, teaches and builds software in his personal capacity, outside official working hours.",
            class_="author-bio"),
        # Contact and Privacy Policy left out: the menu and the footer already have them (Butch 2026-11-20)
        t.p(t.a("Full profile", href="/about/"), class_="author-links"),
        class_="card author",
    )


def contact():
    return part(
        "Contact", "/contact/",
        t.p("Contact", class_="eyebrow"),
        photo_title("Get in touch"),
        t.p("For questions about a blog post or lesson, feedback on the ALTOS book, speaking inquiries, "
            "or technical discussions on civic tech and data analytics, email me.", class_="lead"),
        t.ul(
            t.li(t.b("Email: "), t.a(SITE["email"], href=f"mailto:{SITE['email']}")),
            t.li(t.b("Website: "), t.a(f"https://{SITE['domain']}", href="/")),
            class_="plain-list",
        ),
        t.h2("Good reasons to write"),
        t.ul(
            t.li(t.b("A question about a post, lesson or study note. "), "If something is unclear, others are "
                 "probably wondering too, and I may answer it in a future post."),
            t.li(t.b("A correction. "), "Laws, rates and procedures change. If you spot an error or an outdated "
                 "rule, tell me and I will check it and fix it."),
            t.li(t.b("The ALTOS book. "), "Questions and feedback on any chapter of the book."),
            t.li(t.b("Talks and trainings. "), "Invitations to speak about treasury work, Python for government "
                 "offices or staying safe online."),
            class_="reasons",
        ),
        t.p("Please don't send personal data you don't want me to keep. How I handle what you send is explained "
            "in the ", t.a("Privacy Policy", href="/privacy/"), "."),
        t.p("Views on this site are my own, written in my personal capacity, and do not represent any government office.",
            class_="muted note"),
        description=f"Email {SITE['short_name']} about the blog, the free Python lessons, the ALTOS book, speaking "
                    "invitations, or civic tech and data analytics.",
        seo_title=f"Contact {SITE['short_name']}",
        url="/contact/",
    )


# where each Home ALTOS box leads in the demo (/projects/altos-demo/#<role>-<screen>)
MOVEMENT_DEMO = {"Collect": "#col-issue", "Disburse": "#do-prepare", "Report": "#lo-craaf"}
FEATURE_DEMO = {"Built from the forms": "#col-issue", "Rules, not just records": "#col-issue",
                "Deadlines that count down": "#lo-craaf", "The sealed ledger": "#sys-log",
                "Security Center": "#sys-home", "Correction without concealment": "#sys-log",
                "Turnover built in": "#sys-home", "Data Analytics and Insights": "#sys-dashboard"}


def principle_url(n):
    """Principle n's blog post when it is live, else the series page (never a link to an unpublished post)."""
    for label, _, b, live in series_posts():
        if label == f"Principle {n}":
            return post_url(b) if live else SERIES_URL
    return SERIES_URL


ALTOS_URL = "/#altos"  # the ALTOS section of Home (was the Projects page, /projects/, until 2026-11-20)


def altos_section():
    """ALTOS on Home (Butch 2026-11-20: the Projects page is no longer needed; its content moved here).
    /projects/ now redirects to /#altos."""
    book = ALTOS["book"]
    return [
        t.h2("Project: ALTOS", id="altos", class_="altos-anchor"),
        # after pictures above it load, land on the heading again (old /projects/ links come here)
        # Explore ALTOS jumps there at once, not a slow smooth scroll down Home (Butch 2026-11-24: "direct it immediately")
        t.script(Raw('(function(){var go=function(){document.getElementById("altos").scrollIntoView({behavior:"instant"});};'
                     'addEventListener("load",function(){if(location.hash==="#altos")go();});'
                     'document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest(\'a[href="/#altos"],a[href="#altos"]\');'
                     'if(!a||e.ctrlKey||e.metaKey||e.shiftKey||e.button)return;e.preventDefault();'
                     'if(location.hash!=="#altos")history.pushState(null,"","#altos");go();});})();')),
        t.p(
            "ALTOS is the mother system. Its two subsystems are now ready: the Treasury Collection System for collections "
            "and the Treasury Disbursement System for disbursements, each with its own reports.",
            class_="lead",
        ),
        family(),
        t.h2("ALTOS, the mother system"),
        t.div(
            t.div(
                t.p(wordmark(), class_="wordmark big-wordmark", aria_label="ALTOS"),  # a p, so the page keeps one h1
                t.p(ALTOS["full_name"], class_="subtitle"),
                t.p(ALTOS["summary"], class_="lead"),
                tag_list(ALTOS["stack"]),
                # no second demo button (the Home hero has "ALTOS Demo"); the whole box opens the demo instead
                t.a("", href=DEMO_URL, class_="stretch", aria_label="Try the ALTOS demo"),
            ),
            class_="altos-hero",
        ),
        t.blockquote(t.p(ALTOS["principle"]), t.footer(t.a("The ALTOS principle →", href=SERIES_URL, class_="stretch"))),
        t.figure(
            t.a(t.img(src=asset_url("altos-loop.png"), alt="The ALTOS loop: Collect (OR, RCD, deposit) leads to Disburse (voucher, check, cash advance), which leads to Report (RAAF, CRAAF, RCI, BRS, SRE), which sets the targets and budgets for the next cycle of collections. At the center: 360° accountability, a named officer at every step.", width="1395", height="680", loading="lazy"),
                href=BOOK.chapter_url(1), aria_label="Read Chapter 1 of the ALTOS book, where this figure comes from"),
            t.figcaption("Figure 1.1 — The ALTOS loop. The three are not a line but a loop: three movements, one accountable officer at each step. ",
                         t.a("Read Chapter 1 of the book →", href=BOOK.chapter_url(1))),
            class_="screenshot diagram",
        ),
        t.h2("Three movements of public money"),
        t.p("Every transaction in a local treasury belongs to one of three movements. ALTOS follows each one, with a named officer answerable at every step.", class_="muted"),
        t.div(
            [t.div(t.h3(name), t.p(desc), t.div(forms, class_="forms"),
                   t.a("See it in the demo →", href=DEMO_URL + MOVEMENT_DEMO.get(name, ""), class_="go stretch"), class_="card")
             for name, desc, forms in ALTOS["movements"]],
            class_="grid three",
        ),
        t.h2("What ALTOS does"),
        t.div([t.div(t.h3(title), t.p(desc), t.a("See it in the demo →", href=DEMO_URL + FEATURE_DEMO.get(title, ""), class_="go stretch"), class_="card")
               for title, desc in ALTOS["features"]], class_="grid four"),
        section_head("The ALTOS Framework", "Read the series", SERIES_URL),
        t.p("Ten principles for Philippine public fiscal administration. ALTOS checks its own records against each one in a quarterly self-assessment.", class_="muted"),
        # each principle opens its blog post once that part is live, otherwise the series page
        t.ol([t.li(t.b(t.a(name, href=principle_url(i), class_="stretch")), t.span(desc))
              for i, (name, desc) in enumerate(ALTOS["principles"], 1)], class_="principles"),
        t.h2("The book"),
        t.div(
            t.a(cover_img("book-cover"), href=BOOK_URL, aria_label="Read the ALTOS book", class_="book-link"),
            t.div(
                t.span(book["status"], class_="badge spec"),
                t.h3(book["title"]),
                t.p(book["subtitle"], t.br(), f"{book['pages']} pages", class_="muted"),
                t.p(book["blurb"]),
                t.a("Read the book →", href=BOOK_URL, class_="btn white"),
            ),
            class_="card book",
        ),
        t.p(t.a(t.em(ALTOS["motto"]), href=BOOK_URL), class_="motto"),
    ]


BOOK_URL = "/projects/altos-book/"
# Kept on the site but hidden from Google and the sitemap: the book preview is pictures and the
# ALTOS demo is drawn by JavaScript, so Google sees almost no text (AdSense check, Butch 2026-11-20)
NOINDEX_URLS = {DEMO_URL}  # the book is text now (Butch 2026-11-23), so Google may read it

# The book reader: one page at a time, Previous/Next, arrow keys, and swipe on the page.
# Saving is made harder (no download link, no right-click or long-press save, no dragging),
# but no website can block the phone's or computer's own screenshot keys.
LOOP_ALT = ("The ALTOS loop: Collect (OR, RCD, deposit) leads to Disburse (voucher, check, cash advance), which leads to "
            "Report (RAAF, CRAAF, RCI, BRS, SRE), which sets the targets and budgets for the next cycle of collections. "
            "At the center: 360° accountability, a named officer at every step.")
# read online only: no right-click menu, copying or text selection on the book text (casual protection only)
BOOK_TEXT_SCRIPT = """
(function () {
  // The book is read online only (Butch 2026-11-23): no download, print, save or copy. Google still reads the text.
  var el = document.querySelector('.book-text') || document.querySelector('.book-col');
  if (!el) return;
  ['contextmenu', 'copy', 'cut', 'dragstart', 'selectstart'].forEach(function (k) {
    el.addEventListener(k, function (e) { e.preventDefault(); });
  });
  document.addEventListener('contextmenu', function (e) { if (e.target.closest('.book-col')) e.preventDefault(); });
  document.addEventListener('keydown', function (e) {
    var k = (e.key || '').toLowerCase();
    if ((e.ctrlKey || e.metaKey) && (k === 's' || k === 'p' || k === 'c' || k === 'a' || k === 'x')) e.preventDefault();
  });
  el.querySelectorAll('img').forEach(function (i) { i.setAttribute('draggable', 'false'); });
})();
"""


def book_rich(rich):
    out = []
    for style, text in rich:
        out.append(t.strong(text) if style == "b" else t.em(text) if style == "i" else text)
    return out


def book_block(b):
    k = b["t"]
    if k == "h":
        return t.h2(b["text"], id=heading_id(b["text"]))
    if k == "p":
        return t.p(book_rich(b["r"]))
    if k in ("ul", "ol"):
        items = [t.li(book_rich(it)) for it in b["items"]]
        return t.ul(items) if k == "ul" else t.ol(items)
    if k == "box":
        label = b["label"].capitalize().replace("Altos", "ALTOS")
        return t.aside(t.p(t.b(label + "."), " ", book_rich(b["r"])), class_="book-box")
    if k == "table":
        return t.div(t.table(t.thead(t.tr([t.th(h) for h in b["head"]])),
                             t.tbody([t.tr([t.td(book_rich(c), data_label=h) for h, c in zip(b["head"], row)]) for row in b["rows"]])),
                     class_="table-wrap")
    if k == "fig":
        return t.figure(t.img(src=asset_url("altos-loop.png"), alt=LOOP_ALT, width="1395", height="680", loading="lazy"),
                        t.figcaption("Figure 1.1. The ALTOS loop: three movements, one accountable officer at each step."),
                        class_="screenshot diagram")
    if k == "ref":
        return t.li(book_rich(b["r"]))
    raise ValueError(k)


def book_blocks(blocks):
    """Book blocks to HTML; consecutive references become one list."""
    out, refs = [], []
    for b in blocks:
        if b["t"] == "ref":
            refs.append(book_block(b))
            continue
        if refs:
            out.append(t.ul(refs, class_="refs")); refs = []
        out.append(book_block(b))
    if refs:
        out.append(t.ul(refs, class_="refs"))
    return out


def book_pages():
    """Every web page of the book in reading order: (url, label, title)."""
    pages = [(BOOK.chapter_url(c["n"]), f"Chapter {c['n']}", c["title"]) for c in BOOK.CHAPTERS]
    return pages + [(BOOK.GLOSSARY_URL, "Glossary", "Glossary"), (BOOK.REFERENCES_URL, "References", "References"),
                    (BOOK.AUTHOR_URL, "About the Author", "About the Author")]


def book_nav(url):
    pages = book_pages()
    i = next(n for n, p in enumerate(pages) if p[0] == url)

    def step(n, word, cls):
        if not 0 <= n < len(pages):
            return t.span()
        u, label, title = pages[n]
        return t.a(t.span(f"{word} · {label}", class_="muted"), t.b(title), href=u, class_=cls)

    return t.nav(step(i - 1, "Previous", "newer"), step(i + 1, "Next", "older"), class_="post-steps book-steps",
                 aria_label="Book pages")


def book_crumbs(trail):
    return t.nav(t.ol([t.li(t.a(label, href=href) if href else t.span(label, aria_current="page")) for label, href in trail]),
                 class_="crumbs", aria_label="Breadcrumb")


def book_home():
    """The book's contents page: every part and chapter, each chapter a page of its own."""
    b = ALTOS["book"]
    return part(
        "360° Accountability", BOOK_URL,
        t.div(
            book_crumbs([("Home", "/"), ("ALTOS", ALTOS_URL), ("The book", None)]),
            t.div(
                cover_img("book-cover"),
                t.div(
                    t.p("The ALTOS principles · free to read online", class_="eyebrow"),
                    t.h1(b["title"]),
                    t.p(b["subtitle"], " · ", b["status"], class_="muted"),
                    t.p(b["blurb"]),
                    t.a("Start with Chapter 1 →", href=BOOK.chapter_url(1), class_="btn primary"),
                ),
                class_="book-head book-banner",
            ),
            t.h2("Contents"),
            [t.section(
                t.h3(f"Part {num} · {name}"),
                t.p(sub, class_="muted"),
                t.ol([t.li(t.a(t.span(f"Chapter {c['n']}", class_="muted"), t.b(c["title"]), href=BOOK.chapter_url(c["n"])))
                      for c in BOOK.CHAPTERS if c["n"] in rng], class_="book-toc"),
                class_="book-part", id=f"part-{num.lower()}")
             for num, name, sub, rng in BOOK.PARTS],
            t.section(t.h3("At the back of the book"),
                      t.ol(t.li(t.a(t.b("Glossary"), href=BOOK.GLOSSARY_URL)), t.li(t.a(t.b("References"), href=BOOK.REFERENCES_URL)),
                           t.li(t.a(t.b("About the Author"), href=BOOK.AUTHOR_URL)),
                           class_="book-toc"), class_="book-part"),
            t.p("Read online only: the book cannot be downloaded, printed or copied. Please quote short parts with a link back. "
                "Laws and circulars change: confirm the current text before relying on any rule described here.",
                class_="muted note"),
            t.script(Raw(BOOK_TEXT_SCRIPT)),  # same no-copy guard as the chapters
            class_="blog-col book-col",
        ),
        description=f"Read {b['title']} by {SITE['name']} free online: fifteen chapters joining public administration "
                    "theory with Philippine local treasury law and the lessons of building ALTOS.",
        seo_title=f"360° Accountability: The ALTOS Book, Free to Read Online · {SITE['short_name']}",
        url=BOOK_URL,
        json_ld={"@context": "https://schema.org", "@type": "Book", "name": b["title"], "alternativeHeadline": b["subtitle"],
                 "author": {"@type": "Person", "name": SITE["name"]}, "bookEdition": b["status"], "inLanguage": "en",
                 "url": f"https://{SITE['domain']}{BOOK_URL}"},
    )


def book_side(url):
    """Every chapter in a list for the side column on computers, this one marked."""
    rows = []
    for u, label, title in book_pages():
        inner = [t.span(label if label.startswith("Chapter") else "", class_="muted"), t.b(title)]
        rows.append(t.li(t.span(inner, aria_current="page"), class_="here") if u == url else t.li(t.a(inner, href=u)))
    return t.nav(t.p(t.a("The book", href=BOOK_URL), class_="eyebrow"), t.ol(rows, class_="side-chapters"),
                 class_="side-box", aria_label="Chapters")


def book_chapter(c):
    num, name, _, _ = BOOK.part_of(c["n"])
    url = BOOK.chapter_url(c["n"])
    heads = [b["text"] for b in c["blocks"] if b["t"] == "h"]
    minutes = max(1, round(BOOK.words(c) / 200))
    title = f"Chapter {c['n']}: {c['title']}"
    lead = BOOK.plain(next(b["r"] for b in c["blocks"] if b["t"] == "p"))
    return part(
        title, BOOK_URL,
        # computers: chapter list at the left, the chapter at the right (downloaded book-reader pattern, Butch 2026-11-23)
        t.div(
            t.aside(book_side(url), class_="read-side", aria_label="Book chapters"),
            t.div(
                book_crumbs([("The book", BOOK_URL), (f"Part {num}", BOOK_URL + f"#part-{num.lower()}"), (f"Chapter {c['n']}", None)]),
                t.article(
                    t.p(f"Part {num} · {name}", class_="eyebrow"),
                    t.h1(title),
                    t.p("By ", t.a("Ambrosio “Butch” U. Mahinay, MPA", href="/about/"), f" · {minutes} min read", class_="byline"),
                    t.details(t.summary("In this chapter"), t.ol([t.li(t.a(h, href=f"#{heading_id(h)}")) for h in heads]),
                              class_="toc", open=True) if len(heads) >= 3 else "",
                    book_blocks(c["blocks"]),
                    class_="post book-text",
                ),
                book_nav(url),
                t.p(t.a("All chapters", href=BOOK_URL), " · From ", t.em(ALTOS["book"]["title"]), ", ", ALTOS["book"]["status"], ".",
                    class_="muted note"),
                t.script(Raw(BOOK_TEXT_SCRIPT)),
                class_="blog-col book-col read-main",
            ),
            class_="read-grid side-left",
        ),
        description=lead if len(lead) <= 160 else lead[:157].rsplit(" ", 1)[0] + "…",
        seo_title=f"{title} · 360° Accountability",
        url=url,
        json_ld=article_ld(title, lead, url, kind="Article"),
    )


def book_back(section, url, intro):
    is_author = url == BOOK.AUTHOR_URL
    return part(
        section["title"], BOOK_URL,
        t.div(
            t.aside(book_side(url), class_="read-side", aria_label="Book chapters"),
            t.div(
                book_crumbs([("The book", BOOK_URL), (section["title"], None)]),
                t.article(t.p("360° Accountability", class_="eyebrow"), t.h1(section["title"]),
                          None if is_author else t.p(intro, class_="lead"),
                          author_head() if is_author else None,  # same head as the About page (short version, Butch 2026-11-24)
                          book_blocks(section["blocks"]),
                          t.p(t.a("Full profile on the About page →", href="/about/")) if is_author else None,
                          class_="post book-text"),
                book_nav(url),
                t.script(Raw(BOOK_TEXT_SCRIPT)),
                class_="blog-col book-col read-main",
            ),
            class_="read-grid side-left",
        ),
        description=intro,
        seo_title=f"{section['title']} · 360° Accountability",
        url=url,
    )


def note_is_live(n):
    return n.get("publish_on") is None or n["publish_on"] <= ph_now()


def live_notes():
    return [n for n in NOTES if SHOW_SCHEDULED or note_is_live(n)]


def note_card(n):
    return t.a(
        t.div(t.span(f"Note {n['number']}", class_="badge"), t.span("explainer · example · 10-question quiz", class_="muted"), class_="meta"),
        t.h3(n["title"]),
        t.p(n["summary"]),
        t.span("Read the note →", class_="go"),
        href=note_url(n), class_="card lesson",
    )


def courses():
    """Study Notes (was Courses, Butch 2026-11-10): treasury notes only (My learning and trainings removed)."""
    live = live_notes()
    upcoming = [title for i, title in enumerate(OUTLINE, 1) if i > len(live)]
    nxt = next((n for n in NOTES if n not in live), None)
    return part(
        "Study Notes", NOTES_INFO["url"],
        t.p("Treasury", class_="eyebrow"),
        photo_title(NOTES_INFO["title"]),
        t.p(NOTES_INFO["intro"], class_="lead"),
        t.p(NOTES_INFO["disclaimer"], class_="muted"),
        t.div([note_card(n) for n in live], class_="lesson-list") if live else
        None,  # no "comes out" banner or "Coming next" list: AdSense treats upcoming rosters as unfinished pages
        description=f"Free study notes on local treasury work in the Philippines: local revenue, "
                    f"real property and business taxes, collections and disbursements, by {SITE['short_name']}.",
        seo_title=f"Local Treasury Study Notes (Philippines) · {SITE['short_name']}",
    )


def note_block(b):
    if isinstance(b, str):
        return t.p(b)
    kind = b[0]
    if kind == "h":
        return t.h2(b[1])
    if kind == "list":
        return t.ul([t.li(x) for x in b[1]])
    if kind == "tip":
        return t.p(t.b("Tip: "), b[1], class_="tip")
    if kind == "table":
        # shown as stacked rows (label, then text) so it reads well on phones
        return t.div([t.div(t.p(t.b(row[0]), class_="row-label"), t.p(row[1]), class_="level-row") for row in b[2]], class_="level-rows")
    raise ValueError(kind)


def note_page(n):
    i = NOTES.index(n)
    nxt = NOTES[i + 1] if i + 1 < len(NOTES) else None
    letters = "ABCD"
    ex_title, steps, ex_answer = n["example"]
    return part(
        f"Study Note {n['number']}: {n['title']}", NOTES_INFO["url"],
        t.div(
            t.a("← " + NOTES_INFO["title"], href=NOTES_INFO["url"], class_="crumb"),
            t.p(f"{NOTES_INFO['title']} · Note {n['number']}", class_="eyebrow"),
            t.h1(n["title"], class_="lesson-title"),
            t.p(n["summary"], class_="lead"),
            t.p("✓ Last checked: " + NOTES_INFO["checked"] + " · against " + n.get("checked_against", "RA 7160 (Local Government Code) and its amendments"), class_="checked"),
            [note_block(b) for b in n["body"]],
            t.div(t.h3(ex_title), t.ol([t.li(s_) for s_ in steps]), t.p(t.b("Answer: "), ex_answer), class_="card example"),
            t.p(n["link"][0], " ", t.a(n["link"][1] + " →", href=n["link"][2])) if n.get("link") else None,
            t.h2("Practice"),
            t.p("Tap your answer. A green ✓ means you got it right; a red ✗ means try to learn the right one, shown in green."),
            practice_list(n["practice"]),
            [t.h2("Laws and rules cited"), t.ul([t.li(x) for x in n["sources"]], class_="note-sources")] if n.get("sources") else None,
            t.p(NOTES_INFO["disclaimer"], class_="muted"),
            react_box(note_url(n)),
            t.div(
                t.span(),
                t.a(f"Note {nxt['number']} →", href=note_url(nxt)) if nxt and (SHOW_SCHEDULED or note_is_live(nxt))
                else t.span(),  # no "comes out" line for unpublished notes (AdSense)
                class_="lesson-nav",
            ),
            class_="lesson-page vocab-page notes-page",
        ),
        description=f"Study Note {n['number']}: {n['summary']}",
        url=note_url(n),
        seo_title=f"{n['title'][:1].upper() + n['title'][1:]} in the Philippines · Study Note {n['number']}",
        og_type="article",
        json_ld=article_ld(n["title"], n["summary"], note_url(n), kind="Article"),  # its own address, so Share and Google point to the note, not the Study Notes page
    )


# ---- Python for Treasury Work (tutorials) ----

PH = timezone(timedelta(hours=8))  # Philippine time


def ph_today():
    return datetime.now(PH).date().isoformat()


def nice_date(iso):
    d = datetime.strptime(iso[:10], "%Y-%m-%d")
    return f"{d:%B} {d.day}, {d.year}"


def lesson_is_live(x):
    """Live from midnight PH for a date ("2026-11-14"), or from that minute for a date and time
    ("2026-11-21 21:00"); scheduled lessons go live at 9 pm PH like every other scheduled post."""
    if "publish_on" not in x:
        return True
    day = x["publish_on"]
    return day is not None and day <= (datetime.now(PH).strftime("%Y-%m-%d %H:%M") if len(day) > 10 else ph_today())


# preview.py sets SHOW_SCHEDULED so lessons can be reviewed before their date,
# and turns DOWNLOADS off because the one-file preview has no files to download
SHOW_SCHEDULED = False
SHOW_CERTIFICATES = False  # Butch 2026-11-09: hide all certificates (Home, Courses, About)
DOWNLOADS = True


def lesson_url(x):
    return f"/tutorials/{x['slug']}/"


def visible_lessons():
    return [x for x in LESSONS if SHOW_SCHEDULED or lesson_is_live(x)]


def home_lessons():
    """Newest live lessons first, then the next ones coming; three in all."""
    live = [x for x in LESSONS if lesson_is_live(x)]
    return live[::-1][:3]  # only published lessons (Butch 2026-11-09)


def lesson_meta(x):
    return f"Lesson {x['number']} · {x['level']} · {x['minutes']} min"


def short_month(text):
    """'November 2026' -> 'Nov 2026'."""
    month, _, year = text.partition(" ")
    return f"{month[:3]} {year}".strip()


def lesson_card(x, mini=False):
    open_ = SHOW_SCHEDULED or lesson_is_live(x)
    when = None if lesson_is_live(x) else t.span("Coming " + nice_date(x["publish_on"]) if x.get("publish_on") else "Coming soon", class_="badge soon")
    inner = [
        t.div(t.span(f"Lesson {x['number']}", class_="badge"), when, t.span(f"{x['level']} · {x['minutes']} min", class_="muted"),
              # "Checked Nov 2026" from LAST_CHECKED (Butch 2026-11-23, AdSense blueprint)
              t.span("Checked " + short_month(LAST_CHECKED[x["number"]]), class_="badge checked") if LAST_CHECKED.get(x["number"]) and not mini else None,
              class_="meta"),
        t.h3(x["title"]),
        None if mini else t.p(x["summary"]),
        None if mini else tag_list(x["topics"]),
        t.span("Start the lesson →" if open_ else "Not yet published", class_="go"),
    ]
    cls = "card lesson" + (" mini" if mini else "") + ("" if open_ else " upcoming")
    return t.a(inner, href=lesson_url(x), class_=cls) if open_ else t.div(inner, class_=cls)


def lesson_file(x, name):
    return (TUTORIALS / x["folder"] / name).read_text(encoding="utf-8")


def code_box(label, code_html, download=None, kind="code"):
    return t.figure(
        t.figcaption(
            t.span(label, class_="fname"),
            t.span(
                t.button("Copy", type="button", class_="copy", data_copy=True),
                t.a("Download", href=download, download=True) if download and DOWNLOADS else None,
                class_="actions",
            ),
        ),
        t.pre(t.code(Raw(code_html))),
        class_=f"codebox {kind}",
    )


def lesson_block(x, b):
    if isinstance(b, str):
        return t.p(b)
    kind, *rest = b
    if kind == "h":
        return t.h2(rest[0])
    if kind == "code":
        return code_box(rest[0], highlight(lesson_file(x, rest[0])), download=lesson_url(x) + rest[0])
    if kind == "file":
        return code_box(rest[0], escape(lesson_file(x, rest[0]), quote=False), download=lesson_url(x) + rest[0], kind="data")
    if kind == "output":
        out = lesson_file(x, rest[0].rsplit(".", 1)[0] + ".out")
        return t.figure(t.figcaption(t.span("Output of " + rest[0], class_="fname")), t.pre(out), class_="codebox output")
    if kind == "point":
        return t.p(t.code(rest[0]), " ", rest[1], class_="point")
    if kind == "tip":
        return t.p(t.b("Note: "), rest[0], class_="tip")
    if kind == "try":
        return t.div(t.p("Practice", class_="eyebrow"), t.p(rest[0]), class_="card try")
    if kind == "list":
        return t.ul([t.li(i) for i in rest[0]])
    if kind == "line":
        return t.div(t.code(rest[0]), t.p(rest[1][:1].upper() + rest[1][1:]), class_="line")
    if kind == "steps":
        return t.ol([t.li(i) for i in rest[0]], class_="steps")
    if kind == "terminal":
        return code_box("Command Prompt / Terminal", escape(rest[0], quote=False), kind="terminal")
    if kind == "answer":
        return t.details(
            t.summary("Show answer"),
            lesson_block(x, ("code", rest[0])),
            lesson_block(x, ("output", rest[0])),
            class_="answer",
        )
    raise ValueError(f"unknown lesson block {kind!r}")


COPY_SCRIPT = """
document.addEventListener("click", function (e) {
  var b = e.target.closest("button[data-copy]");
  if (!b) return;
  var code = b.closest("figure").querySelector("pre").innerText;
  var pre = b.closest("figure").querySelector("pre");
  function done(label) { b.textContent = label; setTimeout(function () { b.textContent = "Copy"; }, 1600); }
  function select() {  // clipboard blocked: select the code so Ctrl+C / Cmd+C works
    var r = document.createRange(); r.selectNodeContents(pre);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); done("Selected");
  }
  if (!navigator.clipboard) return select();
  navigator.clipboard.writeText(code).then(function () { done("Copied"); }, select);
});
"""


def glossary_id(g):
    return "word-" + "".join(c if c.isalnum() else "-" for c in g["term"].lower())


def glossary_card(g):
    """One 'Words to know' entry: meaning, why it matters in treasury work, a real example and its output."""
    lesson = next((x for x in LESSONS if x["number"] == g["lesson"]), None)
    shown = lesson in visible_lessons()
    python = g["term"] not in ("pip", "CSV")  # these two show a terminal command and a data file
    code = highlight(g["code"]) if python else escape(g["code"], quote=False)
    return t.div(
        t.dt(g["term"], t.a(f"Lesson {g['lesson']}", href=lesson_url(lesson), class_="word-lesson") if shown else None),
        t.dd(
            t.p(g["means"]),
            t.p(t.b("Why it matters in treasury work. "), g["why"], class_="word-why"),
            code_box(g.get("label", "Example"), code, kind="code" if python else "data"),
            t.figure(t.figcaption(t.span("What it prints", class_="fname")), t.pre(g["output"]), class_="codebox output")
            if g.get("output") else None,
            t.p(g["after"], class_="word-after") if g.get("after") else None,
        ),
        class_="term", id=glossary_id(g),
    )


def words_to_know():
    return [
        t.h2("Words to know", id="words-to-know"),
        t.p(GLOSSARY_INTRO),
        t.p([t.a(g["term"], href="#" + glossary_id(g), class_="tag") for g in GLOSSARY], class_="word-index"),
        t.dl([glossary_card(g) for g in GLOSSARY], class_="glossary"),
    ]


def tutorials():
    shown = visible_lessons()
    return part(
        "Tutorials", "/tutorials/",
        t.p("Tutorials", class_="eyebrow"),
        photo_title(TUTORIAL["title"]),
        t.p(TUTORIAL["intro"], class_="lead"),
        t.div(t.p(t.b("Where to begin. "), TUTORIAL["setup"]), class_="card setup"),
        t.div(t.p(t.b("Our promise. "), TUTORIAL["pledge"]), class_="card setup pledge"),
        t.div([lesson_card(x) for x in shown], class_="lesson-list"),  # lessons not yet published stay hidden
        vocab_section(),
        *words_to_know(),
        t.p(
            "New lessons are added regularly. "
            "All names, receipt numbers and amounts in the examples are made up.",
            class_="muted note",
        ),
        description="Free, beginner-friendly Python lessons for Philippine local treasury staff, with real treasury "
                    "examples, plus Civil Service exam vocabulary modules with practice questions.",
        seo_title=f"Free Python Lessons for Treasury Work · {SITE['short_name']}",
    )


# ---- Civil Service Exam Vocabulary (second tutorial series, Butch 2026-11-09) ----

VOCAB_CHECKED = "November 2026"


def ph_now():
    return datetime.now(PH).strftime("%Y-%m-%d %H:%M")


def module_is_live(m):
    """Modules go live at their publish_on time, "YYYY-MM-DD HH:MM" Philippine time (Wednesdays 9 pm)."""
    return m.get("publish_on") is None or m["publish_on"] <= ph_now()


def module_when(m):
    d = datetime.strptime(m["publish_on"], "%Y-%m-%d %H:%M")
    return f"{d:%A}, {d:%B} {d.day}, {d:%-I} {d:%p}".replace("PM", "pm").replace("AM", "am")


def live_modules():
    return [m for m in MODULES if SHOW_SCHEDULED or module_is_live(m)]


def module_card(m):
    return t.a(
        t.div(t.span(f"Module {m['number']}", class_="badge"), t.span(f"{len(m['words'])} words · practice", class_="muted"),
              t.span("Checked " + short_month(VOCAB_CHECKED), class_="badge checked"), class_="meta"),
        t.h3(m["title"][:1].upper() + m["title"][1:]),
        t.p(m["summary"]),
        t.span("Start the module →", class_="go"),
        href=module_url(m), class_="card lesson",
    )


def vocab_section():
    mods = live_modules()
    if not mods:
        return None
    return [
        t.h2(VOCAB["title"], id=VOCAB["slug"]),
        t.p(VOCAB["intro"]),
        t.div([module_card(m) for m in mods], class_="lesson-list"),
    ]


def word_card(w):
    word, pos, meaning, example, syn, ant, note = w
    return t.div(
        t.h2(word, t.span(" " + pos, class_="pos")),
        t.p(meaning, class_="meaning"),
        t.p(t.b("Example: "), t.i(example)),
        t.p(t.b("Same meaning: "), ", ".join(syn)) if syn else None,
        t.p(t.b("Opposite: "), ", ".join(ant)) if ant else None,
        t.p(t.b("Exam tip: "), note, class_="tip") if note else None,
        t.p(t.a("Check the meaning in Merriam-Webster", href=word_source(word), target="_blank", rel="noopener"), class_="source"),
        class_="card word",
    )


QUIZ_SCRIPT = """
(function () {
  var list = document.querySelector('.lesson-page .practice'); if (!list) return;
  var qs = [].slice.call(list.children), line = document.querySelector('.quiz-score .score-line'),
      reset = document.querySelector('.quiz-score .quiz-reset'), total = qs.length;
  function update() {
    var done = list.querySelectorAll('li.done').length, right = list.querySelectorAll('li.done.got-it').length;
    line.textContent = done < total ? 'Score: ' + right + ' correct, ' + done + ' of ' + total + ' answered'
      : 'You got ' + right + ' of ' + total + ' correct.' + (right === total ? ' Perfect!' : right >= 8 ? ' Very good!' : ' Review the words and try again.');
    reset.hidden = done === 0;
  }
  list.addEventListener('click', function (ev) {
    var b = ev.target.closest('button.choice'); if (!b) return;
    var li = b.closest('.practice > li'); if (li.classList.contains('done')) return;
    li.classList.add('done'); var ok = b.dataset.ok === '1';
    if (ok) li.classList.add('got-it');
    b.classList.add(ok ? 'right' : 'wrong'); b.setAttribute('aria-label', b.textContent + (ok ? ', correct' : ', wrong'));
    li.querySelectorAll('button.choice').forEach(function (c) { c.disabled = true; if (c.dataset.ok === '1') c.classList.add('right'); });
    var d = li.querySelector('details.answer'); if (d) d.open = true;
    update();
  });
  reset.addEventListener('click', function () {
    qs.forEach(function (li) {
      li.classList.remove('done', 'got-it');
      li.querySelectorAll('button.choice').forEach(function (c) { c.disabled = false; c.classList.remove('right', 'wrong'); c.removeAttribute('aria-label'); });
      var d = li.querySelector('details.answer'); if (d) d.open = false;
    });
    update(); list.scrollIntoView({behavior: 'smooth', block: 'start'});
  });
  document.documentElement.classList.add('quiz-js');
})();
"""


def practice_list(practice):
    letters = "ABCD"
    return [
        t.ol([
            t.li(
                t.p(q),
                t.ol([t.li(t.button(c, type="button", class_="choice", data_ok="1" if i == ans else "0"))
                      for i, c in enumerate(choices)], class_="choices", type="A"),
                t.details(t.summary("Show answer"), t.p(t.b(f"{letters[ans]}. {choices[ans]}"), " ", why), class_="answer"),
            )
            for q, choices, ans, why in practice
        ], class_="practice"),
        t.div(
            t.p(f"Score: 0 correct, 0 of {len(practice)} answered", class_="score-line", aria_live="polite"),
            t.button("Try again", type="button", class_="quiz-reset", hidden=True),
            class_="quiz-score",
        ),
        t.script(Raw(QUIZ_SCRIPT)),
    ]


def module_page(m):
    i = MODULES.index(m)
    nxt = MODULES[i + 1] if i + 1 < len(MODULES) else None
    letters = "ABCD"
    return part(
        f"Civil Service Exam Vocabulary, Module {m['number']}: {m['title']}", module_url(m),
        t.div(
            t.a("← " + VOCAB["title"], href=f"/tutorials/#{VOCAB['slug']}", class_="crumb"),
            t.p(f"{VOCAB['title']} · Module {m['number']}", class_="eyebrow"),
            t.h1(m["title"][:1].upper() + m["title"][1:], class_="lesson-title"),
            t.p(m["summary"], class_="lead"),
            t.p("✓ Last checked: " + VOCAB_CHECKED + " · meanings checked against Merriam-Webster", class_="checked"),
            t.p(VOCAB["note"].replace("Civil Service Commission.", ""), t.a("Civil Service Commission", href=VOCAB["csc_url"], target="_blank", rel="noopener"), ".", class_="muted"),
            [word_card(w) for w in m["words"]],
            t.h2("Practice"),
            t.p("Tap your answer. A green ✓ means you got it right; a red ✗ means try to learn the right one, shown in green."),
            practice_list(m["practice"]),
            react_box(module_url(m)),
            t.div(
                t.span(),
                t.a(f"Module {nxt['number']} →", href=module_url(nxt)) if nxt and (SHOW_SCHEDULED or module_is_live(nxt))
                else t.span() if nxt  # no "comes out" line for unpublished modules (AdSense)
                else t.span("This is the last module. Good luck on the exam!", class_="muted"),
                class_="lesson-nav",
            ),
            class_="lesson-page vocab-page",
        ),
        description=f"{VOCAB['title']}, Module {m['number']}: {m['summary']}",
        seo_title=f"{m['title'][:1].upper() + m['title'][1:]} · Civil Service Exam Vocabulary",
        og_type="article",
        json_ld=article_ld(f"{VOCAB['title']}, Module {m['number']}: {m['title']}", m["summary"], module_url(m),
                           kind="LearningResource"),
    )


def lesson_page(x):
    i = LESSONS.index(x)
    prev = LESSONS[i - 1] if i > 0 else None
    nxt = LESSONS[i + 1] if i + 1 < len(LESSONS) else None
    nxt_open = nxt and (SHOW_SCHEDULED or lesson_is_live(nxt))
    return part(
        x["title"], lesson_url(x),
        t.div(
            t.a("← " + TUTORIAL["title"], href="/tutorials/", class_="crumb"),
            t.p(lesson_meta(x), class_="eyebrow"),
            t.h1(x["title"], class_="lesson-title"),
            t.p(x["summary"], class_="lead"),
            t.p("✓ Last checked: " + LAST_CHECKED[x["number"]] + " · code run, output real, facts checked",
                class_="checked") if x["number"] in LAST_CHECKED else None,
            tag_list(x["topics"]),
            t.div(t.p("In this lesson", class_="eyebrow"), t.ul([t.li(item) for item in x["learn"]]), class_="card learn"),
            [lesson_block(x, b) for b in x["body"]],
            react_box(lesson_url(x)),
            t.div(
                t.a("← Lesson " + str(prev["number"]), href=lesson_url(prev)) if prev else t.span(),
                (t.a("Lesson " + str(nxt["number"]) + " →", href=lesson_url(nxt)) if nxt_open
                 else t.span()),  # no "comes out" line for unpublished lessons (AdSense)
                class_="lesson-nav",
            ),
            t.script(Raw(COPY_SCRIPT)),
            class_="lesson-page",
        ),
        description=f"Free Python lesson for treasury staff: {x['summary'][:1].lower() + x['summary'][1:]}",
        seo_title=f"{x['title']} (Python Lesson {x['number']})" if len(x["title"]) <= 50 else x["title"],
        og_type="article",
        json_ld=article_ld(x["title"], x["summary"], lesson_url(x), x.get("publish_on"), kind="LearningResource"),
    )


def heading_id(text):
    """Anchor for a post heading, so "In this article" can link to it: "1. Why It Matters" -> "why-it-matters"."""
    words = "".join(c.lower() if c.isalnum() else " " for c in text).split()
    return "-".join(w for w in words if not w.isdigit()) or "section"


def post_contents(b):
    """'In this article' box: the post's headings as links (Butch 2026-11-23, AdSense blueprint).
    Only on posts with four or more headings."""
    heads = [x[1] for x in b["body"] if isinstance(x, tuple) and x[0] == "h"]
    if len(heads) < 4:
        return ""
    return t.details(
        t.summary("In this article"),
        t.ol([t.li(t.a(h, href=f"#{heading_id(h)}")) for h in heads]),
        class_="toc narrow-only", open=True,
    )


def blog_block(x):
    if isinstance(x, str):
        return t.p(x)
    kind, *rest = x
    if kind == "h":
        return t.h3(rest[0], id=heading_id(rest[0]))
    if kind == "quote":
        return t.blockquote(t.p(rest[0]))
    if kind == "photo":
        path, caption, *size = rest
        if not (STATIC / path).exists():  # photo not uploaded yet
            return ""
        return t.figure(t.img(src=asset_url(path), alt=caption, loading="lazy"), t.figcaption(caption),
                        class_=" ".join(["screenshot", *size]))
    if kind == "point":
        return t.p(t.b(rest[0] + "."), " ", rest[1], class_="point")
    if kind == "source":
        before, label, url, after = rest
        return t.p(before, t.a(label, href=url, target="_blank", rel="noopener"), after, class_="muted source")
    if kind == "cta":  # a button link inside a post, e.g. ("cta", "Open the RPT Calculator", "/tools/rpt-calculator/")
        if not post_is_live(rest[1]):  # a button to a scheduled post appears only once that post is live
            return ""
        return t.p(t.a(rest[0], href=rest[1], class_="btn primary"), class_="cta")
    if kind == "ask":
        return t.p(rest[0], " ", t.a("Email me", href=f"mailto:{SITE['email']}"), ".", class_="ask")
    raise ValueError(f"unknown blog block {kind!r}")


CATEGORY = {key: (label, colour) for key, label, colour in BLOG_CATEGORIES}


def category_label(b):
    label, colour = CATEGORY[b["category"]]
    if b.get("series"):  # Learn posts keep their series name (Butch 2026-11-20)
        label = f"{label} · {LEARN_SERIES[b['series']]}"
    return t.span(label, class_=f"cat cat-{colour}")


def post_url(b):
    return f"/blog/{b['slug']}/"


def reading_minutes(b):
    words = sum(len(" ".join(str(y) for y in ([x] if isinstance(x, str) else x[1:])).split()) for x in b["body"])
    return max(1, round(words / 200))


def post_meta(b):
    return t.div(
        category_label(b),
        t.span(b["date"], class_="muted"),
        t.span("·", class_="muted dot"),
        t.span(f"{reading_minutes(b)} min read", class_="muted"),
        class_="meta",
    )


def post_teaser(b):
    """Short text for the Blog list: the summary, or the start of the first paragraph."""
    if b.get("summary"):
        return b["summary"]
    first = next(x for x in b["body"] if isinstance(x, str))
    return first if len(first) <= 200 else first[:200].rsplit(" ", 1)[0] + "…"


def post_card(b):
    return t.article(
        post_meta(b),
        t.h2(t.a(b["title"], href=post_url(b))),
        t.p(post_teaser(b), class_="teaser"),
        t.a("Read the post", Raw(" &rarr;"), href=post_url(b), class_="more"),
        class_="post-card",
        id=b["slug"],  # old /blog/#slug links still land on the right post
        data_cat=b["category"],
    )


# Listen (Butch, 2026-11-12; male Voice 1 from 2026-11-15): a post with a recording in static/audio/
# (made by audio.py with the free Kokoro voice "am_michael") plays it and highlights each paragraph as it
# is read. A post without one falls back to the reader's own phone voice (Web Speech API).
LISTEN_SCRIPT = r"""
(function start() {
  if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", start); return; }  // the paragraphs come after this script
  var box = document.querySelector(".listen"), post = box && box.closest(".post");
  if (!box || !post) return;
  var play = box.querySelector(".listen-play"), word = play.querySelector(".listen-word");
  var stopBtn = box.querySelector(".listen-stop"), speedBtn = box.querySelector(".listen-speed");
  var clock = box.querySelector(".listen-clock"), track = box.querySelector(".listen-progress");
  var fill = track.querySelector(".listen-fill");
  var speeds = [1, 1.25, 1.5, 0.75], sp = 0, lit = null;
  try { sp = Math.max(0, speeds.indexOf(+localStorage.getItem("listenSpeed"))); } catch (e) {}
  speedBtn.textContent = speeds[sp] + "×";
  // The parts that are read aloud, in page order (audio.py reads the same parts).
  var parts = Array.prototype.slice.call(post.querySelectorAll(
    ":scope > h1, :scope > .lead, :scope > p:not(.byline):not(.series-line):not(.source):not(.cta):not(.ask), "
    + ":scope > h3, :scope > blockquote"));
  var bar = document.querySelector("header.site");
  function fitUnderBar() { if (bar) box.style.setProperty("--listen-top", bar.offsetHeight + "px"); }
  fitUnderBar(); addEventListener("resize", fitUnderBar);
  function light(el) {
    if (lit === el) return;
    if (lit) lit.classList.remove("reading");
    lit = el;
    if (!el) return;
    el.classList.add("reading");
    var r = el.getBoundingClientRect();
    if (r.top < box.getBoundingClientRect().bottom || r.top > innerHeight * 0.7) el.scrollIntoView({ behavior: "smooth", block: "center" });
  }
  function show(state) {
    box.setAttribute("data-state", state);
    word.textContent = state === "playing" ? "Pause" : state === "paused" ? "Resume" : "Listen";
    play.setAttribute("aria-pressed", state === "playing");
    stopBtn.hidden = state === "idle";
  }
  function saveSpeed() {
    speedBtn.textContent = speeds[sp] + "×";
    try { localStorage.setItem("listenSpeed", speeds[sp]); } catch (e) {}
  }
  if (box.getAttribute("data-audio")) recording(); else phoneVoice();

  // A recording of the post (Voice 1). Keeps playing with the screen off, and the phone's
  // lock screen shows play and pause.
  function recording() {
    var a = new Audio(), started = false, total = +box.getAttribute("data-duration") || 0;
    var starts = (box.getAttribute("data-starts") || "").split(",").map(Number);
    if (starts.length !== parts.length) starts = null;  // words changed: play without highlighting
    a.preload = "none";
    a.src = box.getAttribute("data-audio");
    function mmss(s) { s = Math.max(0, Math.floor(s || 0)); return Math.floor(s / 60) + ":" + ("0" + s % 60).slice(-2); }
    function tick() {
      var d = a.duration && isFinite(a.duration) ? a.duration : total, now = a.currentTime;
      clock.textContent = mmss(now) + " / " + mmss(d);
      fill.style.width = d ? Math.min(100, now / d * 100) + "%" : "0";
      if (starts) {
        var i = 0;
        while (i + 1 < starts.length && starts[i + 1] <= now + 0.1) i += 1;
        light(parts[i]);
      }
    }
    function rate() { a.defaultPlaybackRate = a.playbackRate = speeds[sp]; }
    play.addEventListener("click", function () {
      if (!a.paused) { a.pause(); return; }
      rate();
      if (!started) { started = true; show("playing"); tick(); }
      var p = a.play();
      if (p && p.catch) p.catch(function () { if (a.paused) show(a.currentTime ? "paused" : "idle"); });
    });
    a.addEventListener("play", function () { show("playing"); });
    a.addEventListener("pause", function () { if (started && !a.ended) show("paused"); });
    a.addEventListener("timeupdate", tick);
    a.addEventListener("ended", done);
    function done() { a.pause(); try { a.currentTime = 0; } catch (e) {} started = false; light(null); fill.style.width = "0"; show("idle"); }
    stopBtn.addEventListener("click", done);
    speedBtn.addEventListener("click", function () { sp = (sp + 1) % speeds.length; saveSpeed(); rate(); });
    track.addEventListener("click", function (e) {  // tap the line to jump
      var r = track.getBoundingClientRect(), d = a.duration && isFinite(a.duration) ? a.duration : total;
      if (!d) return;
      a.currentTime = Math.max(0, Math.min(1, (e.clientX - r.left) / r.width)) * d; tick();
    });
    if ("mediaSession" in navigator) {
      try {
        var img = document.querySelector('meta[property="og:image"]');
        navigator.mediaSession.metadata = new MediaMetadata({ title: post.querySelector("h1").textContent,
          artist: "Butch Mahinay", album: "aumahinay.dev", artwork: img ? [{ src: img.content, sizes: "1200x630", type: "image/jpeg" }] : [] });
        navigator.mediaSession.setActionHandler("play", function () { play.click(); });
        navigator.mediaSession.setActionHandler("pause", function () { a.pause(); });
        navigator.mediaSession.setActionHandler("seekbackward", function () { a.currentTime = Math.max(0, a.currentTime - 10); });
        navigator.mediaSession.setActionHandler("seekforward", function () { a.currentTime = a.currentTime + 10; });
      } catch (e) {}
    }
    box.hidden = false;
  }

  // No recording yet: the phone's own voice reads it (Web Speech API). Pause stops and starts
  // again from the same sentence, because pause() is unreliable on Android phones.
  function phoneVoice() {
    var say = window.speechSynthesis;
    if (!say || !window.SpeechSynthesisUtterance) return;
    var chunks = [], at = 0, on = false, voice = null, current = null;
    function pickVoice() {
      var all = say.getVoices().filter(function (x) { return /^en[-_]/i.test(x.lang); });
      var rank = ["en-PH", "en-US", "en-GB", "en-AU"];
      all.sort(function (a, b) {
        function r(x) { var i = rank.indexOf(x.lang.replace("_", "-")); return (i < 0 ? 9 : i) - (x.localService ? 0.5 : 0); }
        return r(a) - r(b);
      });
      voice = all[0] || null;
    }
    pickVoice();
    if ("onvoiceschanged" in say) say.addEventListener("voiceschanged", pickVoice);
    function build() {
      chunks = [];
      parts.forEach(function (el) {
        var text = el.textContent.replace(/\s+/g, " ").trim(), cur = "";
        if (!text) return;
        (text.match(/[^.!?]+[.!?]+["”’)]*\s*|[^.!?]+$/g) || [text]).forEach(function (s) {
          if (cur && (cur + s).length > 220) { chunks.push({ el: el, text: cur }); cur = ""; }
          cur += s;
        });
        if (cur.trim()) chunks.push({ el: el, text: cur });
      });
    }
    function speak() {
      if (at >= chunks.length) { done(); return; }
      var c = chunks[at], u = new SpeechSynthesisUtterance(c.text);
      if (voice) { u.voice = voice; u.lang = voice.lang; } else u.lang = "en-US";
      u.rate = speeds[sp];
      u.onend = function () { if (on && u === current) { at += 1; speak(); } };
      u.onerror = function (e) { if (on && u === current && e.error !== "interrupted" && e.error !== "canceled") { at += 1; speak(); } };
      current = u;
      light(c.el);
      say.speak(u);
    }
    function halt() { on = false; current = null; say.cancel(); }
    function done() { halt(); at = 0; light(null); show("idle"); }
    play.addEventListener("click", function () {
      if (on) { halt(); show("paused"); return; }
      if (!chunks.length) build();
      if (!chunks.length) return;
      say.cancel();
      on = true; show("playing"); speak();
    });
    stopBtn.addEventListener("click", done);
    speedBtn.addEventListener("click", function () {
      sp = (sp + 1) % speeds.length; saveSpeed();
      if (on) { halt(); on = true; speak(); }
    });
    addEventListener("pagehide", function () { say.cancel(); });
    say.cancel();
    box.hidden = false;
  }
})();
"""

LISTEN_ICON = Raw('<svg class="i-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l10.5-6.5z"/></svg>'
                  '<svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13M16 5.5v13"/></svg>')
STOP_ICON = Raw('<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6.5" y="6.5" width="11" height="11" rx="1.5"/></svg>')


def recording(b):
    """The post's recording from audio.py as (mp3 url, info), or None if it has none or its words changed since."""
    import audio
    j = STATIC / "audio" / f"{b['slug']}.json"
    if not j.exists() or not (STATIC / "audio" / f"{b['slug']}.mp3").exists():
        return None
    info = json.loads(j.read_text())
    return (asset_url(f"audio/{b['slug']}.mp3"), info) if info["hash"] == audio.words_hash(b) else None


def listen_minutes(b, rec=None):
    """Minutes the recording runs; without one, reading aloud at about 160 words a minute."""
    if rec:
        return max(1, round(rec[1]["duration"] / 60))
    return max(1, round(reading_minutes(b) * 200 / 160))


def listen_box(b):
    """Listen bar under a post's byline (hidden until the script knows it can play)."""
    rec = recording(b)
    data = {"data_audio": rec[0], "data_starts": ",".join(str(x) for x in rec[1]["starts"]),
            "data_duration": rec[1]["duration"]} if rec else {}
    return [
        t.div(
            t.button(LISTEN_ICON, t.span("Listen", class_="listen-word"), type="button", class_="listen-play",
                     aria_pressed="false"),
            t.span(f"{listen_minutes(b, rec)} min", class_="listen-time muted",
                   title="Read aloud by a computer voice, not by the author"),  # be open that it is not Butch reading (Butch, 2026-11-15); visible 'AI voice' dropped for AdSense (Butch, 2026-11-20)
            t.span(class_="listen-clock muted", aria_hidden="true"),
            t.button("1\u00d7", type="button", class_="listen-speed", aria_label="Reading speed", title="Reading speed"),
            t.button(STOP_ICON, type="button", class_="listen-stop", aria_label="Stop reading", title="Stop", hidden=True),
            t.div(t.span(class_="listen-fill"), class_="listen-progress", aria_hidden="true"),
            class_="listen", data_state="idle", hidden=True, role="group", aria_label="Listen to this post", **data,
        ),
        t.script(Raw(LISTEN_SCRIPT)),
    ]


def blog_post(b):
    return t.article(
        post_meta(b),
        t.h1(b["title"]),
        t.p("By ", t.a("Ambrosio “Butch” U. Mahinay", href="/about/"), class_="byline"),
        series_line(b),
        listen_box(b),
        t.p(b["summary"], class_="lead") if b.get("summary") else "",
        t.hr(class_="lead-rule") if b.get("summary") else "",
        post_contents(b),
        [blog_block(x) for x in b["body"]],
        class_="post",
        data_cat=b["category"],
    )


def live_posts():
    """Posts without publish_on, or whose publish_on has arrived (Philippine time). publish_on is a date
    ("2026-11-03", live from midnight) or a date and time ("2026-11-14 22:00", live from that minute)."""
    now = datetime.now(timezone(timedelta(hours=8)))
    today, minute = now.date().isoformat(), now.strftime("%Y-%m-%d %H:%M")
    return [b for b in BLOG if "publish_on" not in b
            or (b["publish_on"] and b["publish_on"] <= (minute if len(b["publish_on"]) > 10 else today))]


def post_is_live(url):
    """True when url is a blog post that is live now (or not a blog post at all)."""
    if not url.startswith("/blog/") or url in ("/blog/", SERIES_URL):
        return True
    return any(post_url(b) == url for b in live_posts())


def post_day(b):
    """A post's date as YYYY-MM-DD, for newest-first lists."""
    return b.get("publish_on") or datetime.strptime(b["date"], "%B %d, %Y").date().isoformat()


def blog_filters(posts):
    """Category menu (Butch 2026-11-10): a three-bar button showing the chosen category and its post count;
    tap it and the categories open as a vertical list. Plain radio buttons inside a <details>; CSS hides the
    other posts and shows the chosen name on the button, so it works without JavaScript. A tiny script only
    closes the list after a pick."""
    used = [(key, label) for key, label, _ in BLOG_CATEGORIES if any(b["category"] == key for b in posts)]
    if len(used) < 2:
        return ""
    choices = [("all", "All posts", len(posts))] + [(k, l, sum(b["category"] == k for b in posts)) for k, l in used]
    return t.details(
        t.summary(
            MENU_ICON,
            [t.span(l, " ", t.span(n, class_="count"), class_="cat-now", data_k=k) for k, l, n in choices],
            t.span(Raw("&#9662;"), class_="cat-caret", aria_hidden="true"),
        ),
        t.div(
            [[t.input(type="radio", name="blog-cat", id=f"cat-{k}", value=k, checked=(k == "all")),
              t.label(l, t.span(n, class_="count"), for_=f"cat-{k}")] for k, l, n in choices],
            class_="cat-list",
            role="radiogroup",
            aria_label="Show posts by category",
        ),
        class_="blog-filters",
        id="blog-cats",
    )


def blog():
    posts_live = live_posts()
    if posts_live:
        posts = [blog_filters(posts_live), t.div([post_card(b) for b in posts_live], class_="post-list")]
    else:
        posts = t.div(
            t.h3("First posts coming soon"),
            t.p("I'll share notes here on treasury work, building ALTOS, and what I learn along the way."),
            class_="card empty",
        )
    return part(
        "Blog", "/blog/",
        t.div(
            t.p("Writing", class_="eyebrow"),
            photo_title("Blog"),
            t.p(
                "My own stories and thoughts, from treasury work and building software to life beyond the office.",
                class_="lead",
            ),
            series_banner() if posts_live else "",
            posts,
            t.script(Raw(f'(function(){{var m=/^#cat-(\\w+)$/.exec(location.hash);var o={json.dumps({k: "learn" for k in LEARN_SERIES})};'
                         'var r=m&&document.getElementById("cat-"+(o[m[1]]||m[1]));if(r)r.checked=true;'
                         'var d=document.getElementById("blog-cats");if(d)d.addEventListener("change",function(){d.open=false;});})();')),
            t.p(
                "Views here are my own and do not represent any government office.",
                class_="muted note",
            ),
            class_="blog-col",
        ),
        description=f"Stories and notes by {SITE['short_name']} on Philippine local treasury work, public finance, "
                    "cybersecurity, building the ALTOS system, and life beyond the office.",
        seo_title=f"Blog on Local Treasury and Public Finance · {SITE['short_name']}",
    )


# Follow, Heart, Like and Share buttons under each blog post and lesson. The Follow
# (one count for the whole site), Heart and Like counts are kept by functions/api/likes.js on Cloudflare; those three buttons only
# appear once it answers, so they stay hidden when previewing locally or if the
# counter is switched off. Share always works: the phone's share menu, or on
# computers without one, it copies the page link.
REACT_SCRIPT = """
(function () {
  var box = document.querySelector(".react");
  if (!box) return;
  var page = box.getAttribute("data-page");
  var share = box.querySelector(".react-share"), shareWord = share.querySelector(".react-word");
  var shareCount = share.querySelector(".react-count"), now, v;
  function showShare(s) { if (s && s.share) shareCount.textContent = s.share.count ? s.share.count.toLocaleString("en") : ""; }
  share.addEventListener("click", function () {
    if (now && now.share && v) {  // every tap of Share adds one
      now.share.count += 1; showShare(now);
      fetch("/api/likes", { method: "POST", headers: { "content-type": "application/json" },
                            body: JSON.stringify({ page: page, v: v, kind: "share" }) })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (s) { if (s && s.share) { now.share = s.share; showShare(now); } })
        .catch(function () {});
    }
    var c = document.querySelector('link[rel="canonical"]');
    var url = c ? c.href : location.href, title = document.title;
    function copied(ok) {
      shareWord.textContent = ok ? "Link copied" : "Share";
      if (ok) setTimeout(function () { shareWord.textContent = "Share"; }, 2000);
    }
    if (navigator.share) { navigator.share({ title: title, url: url }).catch(function () {}); return; }
    if (navigator.clipboard) { navigator.clipboard.writeText(url).then(function () { copied(true); }, function () { prompt("Copy this link:", url); }); return; }
    prompt("Copy this link:", url);
  });
  if (!window.fetch) return;
  try { v = localStorage.getItem("visitor"); } catch (e) {}
  if (!/^[a-f0-9]{32}$/.test(v || "")) {
    var a = new Uint8Array(16);
    crypto.getRandomValues(a);
    v = Array.prototype.map.call(a, function (b) { return ("0" + b.toString(16)).slice(-2); }).join("");
    try { localStorage.setItem("visitor", v); } catch (e) {}
  }
  var btns = { follow: box.querySelector(".react-follow"), heart: box.querySelector(".react-heart"), like: box.querySelector(".react-like") };
  function show(kind, s) {
    var b = btns[kind];
    b.setAttribute("aria-pressed", s.on);
    if (kind === "follow") b.querySelector(".react-word").textContent = s.on ? "Following" : "Follow";
    b.querySelector(".react-count").textContent = s.count ? s.count.toLocaleString("en") : "";
    b.hidden = false;
  }
  function showAll(s) { Object.keys(btns).forEach(function (k) { if (s[k]) show(k, s[k]); }); showShare(s); }
  fetch("/api/likes?page=" + encodeURIComponent(page) + "&v=" + v)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (s) { if (s && s.heart && s.like && s.follow) { now = s; showAll(s); } })
    .catch(function () {});
  Object.keys(btns).forEach(function (kind) {
    var b = btns[kind];
    b.addEventListener("click", function () {
      if (!now || b.disabled) return;
      var want = !now[kind].on;
      show(kind, { on: want, count: Math.max(0, now[kind].count + (want ? 1 : -1)) });  // answer the tap right away
      b.disabled = true;
      fetch("/api/likes", { method: "POST", headers: { "content-type": "application/json" },
                            body: JSON.stringify({ page: page, v: v, kind: kind, on: want }) })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (s) { if (s && s.heart) now = s; showAll(now); })
        .catch(function () { showAll(now); })
        .then(function () { b.disabled = false; });
    });
  });
})();
"""

HEART_ICON = Raw('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20.5s-7.5-4.6-9.3-9.2C1.5 8 3.6 4.5 7.2 4.5c2 0 3.6 1.1 4.8 2.8 1.2-1.7 2.8-2.8 4.8-2.8 3.6 0 5.7 3.5 4.5 6.8-1.8 4.6-9.3 9.2-9.3 9.2z"/></svg>')
LIKE_ICON = Raw('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.5 10.5v9.5H4a1 1 0 0 1-1-1v-7.5a1 1 0 0 1 1-1zM7.5 10.5l3.6-7a2.2 2.2 0 0 1 3.9 1.9l-1 3.6h5.2a2 2 0 0 1 2 2.4l-1.4 6.9a2 2 0 0 1-2 1.7H7.5"/></svg>')
FOLLOW_ICON = Raw('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM2.5 21v-1a6 6 0 0 1 6-6h2a6 6 0 0 1 6 6v1"/><path class="plus" d="M19 8v6M16 11h6"/></svg>')
SHARE_ICON = Raw('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12M7.5 7.5 12 3l4.5 4.5M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7"/></svg>')


def react_box(url):
    def btn(icon, word, kind, label):
        return t.button(icon, t.span(word, class_="react-word"), t.span(class_="react-count"), type="button",
                        class_=f"react-btn react-{kind}", aria_pressed="false", aria_label=label, hidden=True)
    return [
        t.div(
            btn(FOLLOW_ICON, "Follow", "follow", f"Follow {SITE['short_name']}"),
            btn(HEART_ICON, "Heart", "heart", "Heart this"),
            btn(LIKE_ICON, "Like", "like", "Like this"),
            t.button(SHARE_ICON, t.span("Share", class_="react-word", aria_live="polite"), t.span(class_="react-count"), type="button",
                     class_="react-btn react-share"),
            class_="react", data_page=url,
        ),
        t.script(Raw(REACT_SCRIPT)),
    ]

def post_page(b):
    """One blog post on its own page, with links to the newer and older posts."""
    posts = live_posts()
    i = posts.index(b)
    newer = posts[i - 1] if i > 0 else None
    older = posts[i + 1] if i + 1 < len(posts) else None

    def step(p, label, class_):
        return t.a(t.span(label, class_="muted"), t.b(p["title"]), href=post_url(p), class_=class_) if p else t.span()

    return part(
        b["title"], "/blog/",
        # computers: the post at the left, a side column at the right that stays in view (In this article,
        # the series, the author), as in the downloaded desktop pattern (Butch 2026-11-23). Phones: one column, as before.
        # "← All posts" at the left, the breadcrumb at the right, above both columns (Butch's post pattern file, 2026-11-23)
        t.div(t.a("← All posts", href="/blog/", class_="back-all"), breadcrumb(b), class_="post-top"),
        t.div(
            t.div(
                blog_post(b),
                series_steps(b),
                t.div(learn_series_box(b), class_="narrow-only"),
                react_box(post_url(b)),
                t.div(t.h2("About the author", class_="post-section"), author_card(), class_="narrow-only"),
                related_posts(b, posts, skip=(newer, older)),  # the Newer/Older links below already show those two
                t.nav(step(newer, "Newer post", "newer"), step(older, "Older post", "older"), class_="post-steps",
                      aria_label="More posts"),
                t.p("Views here are my own and do not represent any government office.", class_="muted note"),
                class_="blog-col read-main",
            ),
            t.aside(t.div(side_contents([x[1] for x in b["body"] if isinstance(x, tuple) and x[0] == "h"], "In this article"),
                          side_series(b), side_author(), class_="side-card"),
                    class_="read-side", aria_label="About this post"),
            class_="read-grid",
        ),
        description=b.get("description") or b.get("summary") or post_teaser(b),
        url=post_url(b),
        og_type="article",
        json_ld=[article_ld(b["title"], b.get("description") or b.get("summary") or post_teaser(b), post_url(b),
                            post_day(b), post_photo(b)), breadcrumb_ld(b)],
        share_image=card_for(post_photo(b)) if post_photo(b) else None,  # link previews show the post's own picture
    )


def side_contents(heads, label):
    """'In this article' list for the side column on computers (four or more headings)."""
    if len(heads) < 4:
        return ""
    return t.nav(t.p(label, class_="eyebrow"), t.ol([t.li(t.a(h, href=f"#{heading_id(h)}")) for h in heads]),
                 class_="side-box side-toc", aria_label=label)


def side_series(b):
    """Series box for the side column: published parts only, this one highlighted ('2 / 3')."""
    if b.get("series"):
        parts = learn_parts(b)
        name, href = LEARN_SERIES[b["series"]] + " Series", f"/blog/#cat-{b['category']}"
        rows = [(p, (learn_part(p) or "") + ": " + (p["title"].split(": ", 1)[1] if ": " in p["title"] else p["title"])) for p in parts]
    else:
        sp = series_posts()
        if not any(p[2] is b for p in sp):
            return ""
        live = live_posts()
        parts = [p[2] for p in sp if p[2] in live]  # published parts only, never "coming" ones
        name, href = ALTOS_SERIES["title"], SERIES_URL
        rows = [(p, ("Introduction" if n == 0 else f"Principle {n}") + ": " + (p["title"].split(": ", 1)[1] if ": " in p["title"] else p["title"]))
                for n, p in enumerate(parts)]  # parts go live in order, so position n is Principle n
    if len(parts) < 2:
        return ""
    here = next(n for n, p in enumerate(parts) if p is b) + 1
    return t.nav(
        t.div(t.a(name, href=href, class_="eyebrow"), t.span(f"{here} / {len(parts)}", class_="muted"), class_="side-series-head"),
        t.ol([t.li(t.span(label, aria_current="page"), class_="here") if p is b else t.li(t.a(label, href=post_url(p)))
              for p, label in rows]),
        class_="side-box side-series", aria_label=name)


def learn_parts(b):
    return sorted((p for p in live_posts() if p.get("series") == b["series"]), key=post_day)


def side_author():
    """Short author box for the side column on computers; phones get the full author card under the post."""
    return t.div(
        t.p("About the author", class_="eyebrow"),
        author_head(),
        t.p("15+ years in government service (13+ years in public finance and local treasury work in Quezon Province), "
            "holder of 7 Google Professional Certificates, and a self-taught software developer. He writes in his personal "
            "capacity, outside official working hours."),
        t.p(t.a("Explore ALTOS & 360° Accountability →", href=ALTOS_URL)),
        class_="side-box side-author",
    )


def crumbs(b):
    """Blog / the post's series or topic / this part: (label, link) pairs, the last one without a link."""
    trail = [("Blog", "/blog/")]
    parts = series_posts()
    i = next((n for n, p in enumerate(parts) if p[2] is b), None)
    if i is not None:
        trail += [(ALTOS_SERIES["title"], SERIES_URL), ("Introduction" if i == 0 else f"Principle {i}", None)]
    elif b.get("series"):
        name = LEARN_SERIES[b["series"]]
        trail += [(name, f"/blog/#cat-{b['category']}"), (learn_part(b) or b["title"], None)]
    else:
        trail += [(CATEGORY[b["category"]][0], f"/blog/#cat-{b['category']}"), (b["title"], None)]
    return trail


def breadcrumb(b):
    """Line at the top of a post: Blog / series or topic / part (Butch 2026-11-23, AdSense blueprint)."""
    items = []
    for label, href in crumbs(b):
        items.append(t.li(t.a(label, href=href) if href else t.span(label, aria_current="page")))
    return t.nav(t.ol(items), class_="crumbs", aria_label="Breadcrumb")


def breadcrumb_ld(b):
    site = f"https://{SITE['domain']}"
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": n + 1, "name": label, "item": site + (href or post_url(b))}
        for n, (label, href) in enumerate(crumbs(b))]}


def learn_part(b):
    """'Part 2' from 'Cybersecurity Series, Part 2: Identity Is the New Perimeter', or None."""
    head = b["title"].split(":", 1)[0]
    return head.split(", ", 1)[1] if ", Part " in head else None


def learn_series_box(b):
    """Box under a Learn series post: every PUBLISHED part of that series in order, this one marked.
    Parts not out yet are never named or counted (no "under construction", Butch 2026-11-14)."""
    if not b.get("series"):
        return ""
    parts = sorted((p for p in live_posts() if p.get("series") == b["series"]), key=post_day)
    if len(parts) < 2:
        return ""

    def row(p):
        short = p["title"].split(": ", 1)[1] if ": " in p["title"] else p["title"]
        inner = [t.span(learn_part(p) or "", class_="muted"), t.b(short)]
        if p is b:
            return t.li(t.span(inner, aria_current="page"), class_="here")
        return t.li(t.a(inner, href=post_url(p)))

    return t.section(
        t.div(t.p("Series", class_="eyebrow"), t.b(LEARN_SERIES[b["series"]], class_="series-name"),
              t.span(f"{len(parts)} parts", class_="muted"), class_="series-head"),
        t.ol([row(p) for p in parts], class_="learn-parts"),
        class_="series-box learn-series",
        aria_label=LEARN_SERIES[b["series"]],
    )


def post_photo(b):
    """The post's first picture that exists in static/, or None."""
    return next((x[1] for x in b["body"] if isinstance(x, tuple) and x[0] == "photo" and (STATIC / x[1]).exists()), None)


def related_posts(b, posts, skip=()):
    """'Keep reading': up to three other live posts, same category first (newest first), then the newest others."""
    others = sorted((p for p in posts if p is not b and p not in skip), key=post_day, reverse=True)
    picks = [p for p in others if b.get("series") and p.get("series") == b["series"]][:3]  # same Learn series first
    picks += [p for p in others if p["category"] == b["category"] and p not in picks][:3 - len(picks)]
    picks += [p for p in others if p not in picks][:3 - len(picks)]
    if not picks:
        return ""
    return t.section(
        t.h2("Keep reading", class_="post-section"),
        t.div([t.a(t.span(category_label(p), t.span(f"{reading_minutes(p)} min read", class_="muted")),
                   t.b(p["title"]), href=post_url(p), class_="related-card") for p in picks],
              class_="related"),
        class_="keep-reading",
    )


# ---- The ALTOS Framework series page (Butch 2026-11-11) ----
SERIES_URL = f"/blog/{ALTOS_SERIES['slug']}/"


def series_posts():
    """The series in reading order: (part label, short title, post, is it live now)."""
    live = live_posts()
    out = []
    for i, slug in enumerate(ALTOS_SERIES["parts"]):
        b = next(x for x in BLOG if x["slug"] == slug)
        label = "Start here" if i == 0 else f"Principle {i}"
        short = b["title"].split(": ", 1)[1] if i else b["title"].split(": ", 1)[0]
        out.append((label, short, b, b in live))
    return out


def series_count():
    parts = series_posts()
    return sum(p[3] for p in parts), len(parts)


def series_line(b):
    """Small line under a series post's byline: which part it is, linking to the series page."""
    if b.get("series") and learn_part(b):
        parts = learn_parts(b)
        if len(parts) < 2:
            return ""
        n = next(k for k, p in enumerate(parts) if p is b) + 1
        return t.p(f"Part {n} of {len(parts)} in the series ", t.a(LEARN_SERIES[b["series"]] + " Series", href=f"/blog/#cat-{b['category']}"),
                   class_="series-line")
    parts = series_posts()
    i = next((n for n, p in enumerate(parts) if p[2] is b), None)
    if i is None:
        return ""
    where = "The introduction to" if i == 0 else f"Principle {i} of 10 in"
    return t.p(where, " the series ", t.a(ALTOS_SERIES["title"], href=SERIES_URL), class_="series-line")


def series_steps(b):
    """Box under a series post: the previous and next parts, and a link to the whole series.
    A next part that is not out yet shows its date instead of a link."""
    parts = series_posts()
    i = next((n for n, p in enumerate(parts) if p[2] is b), None)
    if i is None:
        return ""

    def step(n, word):
        if not 0 <= n < len(parts):
            return t.span()
        label, short, p, live = parts[n]
        inner = [t.span(f"{word} · {label}", class_="muted"), t.b(short)]
        if live:
            return t.a(inner, href=post_url(p), class_=word.lower())
        return t.span()  # a part not out yet stays hidden until its day (no "Coming" dates, for AdSense; Butch 2026-11-14)

    done, total = series_count()
    return t.section(
        t.div(t.p("Series", class_="eyebrow"), t.a(ALTOS_SERIES["title"], href=SERIES_URL, class_="series-name"),
              t.span(f"{done} parts", class_="muted"), class_="series-head"),
        t.div(step(i - 1, "Previous"), step(i + 1, "Next"), class_="series-pn"),
        t.a("See all parts of the series", Raw(" &rarr;"), href=SERIES_URL, class_="more"),
        class_="series-box",
        aria_label="The ALTOS Framework series",
    )


def series_banner():
    """Card on the Blog page that leads to the series page."""
    done, total = series_count()
    return t.a(
        t.p("Blog series", class_="eyebrow"),
        t.b(ALTOS_SERIES["title"], class_="series-name"),
        t.span(ALTOS_SERIES["tagline"] + ".", class_="series-tag"),
        t.span(f"{done} parts · read them in order", Raw(" &rarr;"), class_="more"),
        href=SERIES_URL,
        class_="series-banner",
    )


def series_page():
    parts = series_posts()
    done, total = series_count()
    # only published parts are listed; each new part appears on its own day (no "Coming" dates, Butch 2026-11-14)
    status = "Read them in order from the top."

    def row(n, label, short, p, live):
        inner = [
            t.span(n or Raw("&#9733;"), class_="num", aria_hidden="true"),
            t.div(
                t.div(t.span(label, class_="badge"),
                      t.span(p["date"], class_="muted") if live else t.span(f"Coming {p['date']}", class_="badge soon"),
                      t.span(f"{reading_minutes(p)} min read", class_="muted") if live else None,
                      class_="meta"),
                t.h3(t.a(short, href=post_url(p)) if live else short),
                t.p(p.get("summary") or post_teaser(p)),
                class_="body",
            ),
        ]
        return t.li(inner, class_="" if live else "upcoming")

    site = f"https://{SITE['domain']}"
    live_parts = [p for p in parts if p[3]]
    return part(
        ALTOS_SERIES["title"], "/blog/",
        t.div(
            t.a(Raw("&larr; "), "All posts", href="/blog/", class_="back"),
            t.p("Blog series", class_="eyebrow"),
            t.h1(ALTOS_SERIES["title"]),
            t.p(ALTOS_SERIES["tagline"] + ".", class_="lead"),
            [t.p(x) for x in ALTOS_SERIES["intro"]],
            t.p(status, class_="series-status"),
            t.ol([row(n, *p) for n, p in enumerate(parts) if p[3]], class_="learn-parts"),
            t.div(
                t.h2("Want to go deeper?"),
                t.p("The ten principles also form the closing part of my book, ",
                    t.i(ALTOS["book"]["title"].split(":")[0]), ". You can read its first pages for free, or see what "
                    "the ALTOS software does for collections and disbursements."),
                t.div(t.a("Read the book online", href=BOOK_URL, class_="btn primary"),
                      t.a("About ALTOS", href=ALTOS_URL, class_="btn white"), class_="actions"),
                class_="card series-more",
            ),
            t.p("Views here are my own and do not represent any government office.", class_="muted note"),
            class_="blog-col series-page",
        ),
        description=f"{ALTOS_SERIES['title']}: {ALTOS_SERIES['tagline'].lower()}. All parts of the blog series by "
                    f"{SITE['short_name']}, in reading order.",
        url=SERIES_URL,
        seo_title=f"{ALTOS_SERIES['title']}: Blog Series on Local Treasury Accountability · {SITE['short_name']}",
        json_ld={
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": ALTOS_SERIES["title"],
            "description": ALTOS_SERIES["tagline"],
            "url": site + SERIES_URL,
            "inLanguage": "en",
            "author": {"@type": "Person", "name": SITE["name"], "url": site + "/about/"},
            "mainEntity": {
                "@type": "ItemList",
                "itemListOrder": "https://schema.org/ItemListOrderAscending",
                "numberOfItems": len(live_parts),
                "itemListElement": [{"@type": "ListItem", "position": n + 1, "name": p[2]["title"],
                                     "url": site + post_url(p[2])} for n, p in enumerate(live_parts)],
            },
        },
    )


def post_parts():
    """Route -> page builder for every live post."""
    return {post_url(b): (lambda b=b: post_page(b)) for b in live_posts()}


# About story: the first paragraph shows; "View more" opens the rest of the story and
# Experience to Skills, and "View less" (after "...written into the software.") closes
# them again. "Get in touch" always shows. Without JavaScript all of it shows.
STORY_SCRIPT = """
(function () {
  var box = document.getElementById("story");
  if (!box) return;
  var more = document.getElementById("story-more-btn"), less = document.getElementById("story-less-btn");
  function set(open) {
    box.classList.toggle("closed", !open);
    more.setAttribute("aria-expanded", open);
    less.setAttribute("aria-expanded", open);
  }
  more.addEventListener("click", function () { set(true); });
  less.addEventListener("click", function () {
    set(false);
    if (box.getBoundingClientRect().top < 0) box.scrollIntoView({ block: "start" });
  });
  box.classList.add("js");
  set(false);
})();
"""


def about_story(paragraphs):
    first, *rest = paragraphs
    toggle = lambda label, id_: t.button(label, type="button", id=id_, class_="story-toggle", aria_controls="story-rest", aria_expanded="true")
    return t.div(
        t.p(first, " ", toggle("View more", "story-more-btn")),
        t.div(
            [t.p(x) for x in rest[:-1]],
            t.p(rest[-1], " ", toggle("View less", "story-less-btn")),
            id="story-rest",
        ),
        t.script(Raw(STORY_SCRIPT)),
        id="story",
        class_="story",
    )


def about():
    contact = t.ul(
        t.li(t.b("Email: "), t.a(SITE["email"], href=f"mailto:{SITE['email']}")),
        t.li(t.b("Website: "), t.a(f"https://{SITE['domain']}", href="/")),
        class_="plain-list",
    )
    return part(
        "About", "/about/",
        t.p("About me", class_="eyebrow"),
        author_head(h1=True),  # same head as the author card (Butch 2026-11-24)
        t.p(ABOUT["intro"], class_="lead"),
        about_story(ABOUT["paragraphs"]),
        # everything below hides together with the story's rest; Contact and the disclaimer always show
        t.div(
            t.h2("Professional Background"),
            t.div(
                [
                    t.div(
                        t.h3(x["title"]),
                        t.div(x["period"], class_="muted"),
                        t.ul(t.li(t.b("Role: "), x["role"]), t.li(t.b("Focus areas: "), x["focus"])),
                        class_="item",
                    )
                    for x in ABOUT["background"]
                ],
                class_="timeline",
            ),
            t.div(
                t.div(
                    t.h2("Education"),
                    t.ul([t.li(t.b(d), [t.br(), t.span(sch, class_="muted")] if sch else None)
                          for d, sch in ABOUT["education"]], class_="plain-list edu"),
                ),
                t.div(
                    t.h2("Eligibilities"),
                    t.ul([t.li(x) for x in ABOUT["eligibilities"]]),
                ),
                class_="two",
            ),
            # Microcredentials list right under Eligibilities (Butch 2026-11-10); certificate pictures stay hidden
            t.h2("Microcredentials"),
            t.p("Google Career Certificates earned on Coursera. Each one links to its Coursera verification page.",
                class_="muted"),
            t.ul([t.li(t.b(f"{c['name']} {c['kind']}"), t.br(),
                       t.span(f"Coursera · {c['date'].split()[0]} {c['date'].split()[-1]} · "
                              f"{c['courses']} courses · ", t.a("Verify", href=c["verify"], target="_blank", rel="noopener"),
                              class_="muted"))
                  for c in sorted(CERTIFICATES, key=lambda c: not c["kind"].startswith("Prof"))],
                 class_="plain-list edu"),
            t.h2("Independent Technical Work"),
            t.p(ABOUT["technical"]),
            t.h3("Development stack"),
            t.div([t.div(t.div(label, class_="stack-label"), tag_list(items), class_="stack-row")
                   for label, items in ABOUT["stack"]], class_="stack"),
            [t.h3("Professional certifications"), t.ul([t.li(x) for x in ABOUT["certifications"]])] if SHOW_CERTIFICATES else None,
            t.h2("Writing, Tutorials & Knowledge Sharing"),
            t.p(ABOUT["writing"]),
            t.h2("Beyond the Desk"),
            t.p(ABOUT["beyond"]),
            class_="story-extra",
        ),
        t.h2("Contact"),
        t.p(ABOUT["contact"]),
        contact,
        t.aside(t.h3(ABOUT["disclaimer_title"]), t.p(ABOUT["disclaimer"]), class_="disclaimer"),
        description=f"About {SITE['name']} (Butch), MPA: a treasury worker who builds software, with 15+ years in "
                    "Philippine local government, author of the ALTOS book and creator of the ALTOS treasury system.",
        seo_title=f"About Ambrosio “Butch” U. Mahinay, MPA",
    )


PRIVACY_URL = "/privacy/"


def _privacy_text(x):
    """One run of policy text: a plain string, or a list mixing strings and (label, link) pairs."""
    if isinstance(x, str):
        return x
    return [(t.a(p[0], href=p[1], target="_blank", rel="noopener") if p[1].startswith("http") else t.a(p[0], href=p[1]))
            if isinstance(p, tuple) else p for p in x]


def _policy_body(sections):
    """Headings, paragraphs, labelled lists and the contact block of a policy page (Privacy, Terms)."""
    body = []
    for heading, blocks in sections:
        body.append(t.h2(heading))
        for blk in blocks:
            if isinstance(blk, (str, list)):
                body.append(t.p(_privacy_text(blk)))
            elif blk[0] == "list":
                body.append(t.ul([t.li(t.b(label), " ", _privacy_text(text)) for label, text in blk[1]]))
            elif blk[0] == "contact":
                body.append(t.ul(
                    t.li(t.b("Email: "), t.a(SITE["email"], href=f"mailto:{SITE['email']}")),
                    t.li(t.b("Website: "), t.a(f"https://{SITE['domain']}", href="/")),
                    class_="plain-list"))
    return body


def _policy_page(title, url, eyebrow, policy, description):
    return part(
        title, url,
        t.p(eyebrow, class_="eyebrow"),
        t.h1(title),
        t.p(t.b("Effective date: "), policy["effective"], t.br(), t.b("Website: "),
            t.a(f"https://{SITE['domain']}", href="/"), class_="muted policy-meta"),
        t.p(policy["intro"], class_="lead"),
        *_policy_body(policy["sections"]),
        description=description,
        url=url,
    )


def privacy():
    return _policy_page(
        "Privacy Policy", PRIVACY_URL, "Privacy", PRIVACY,
        f"Privacy Policy of {SITE['domain']}: what information is collected, how it is used, "
        "and your rights under the Philippine Data Privacy Act of 2012 (RA 10173).")


TERMS_URL = "/terms/"


def terms():
    return _policy_page(
        "Terms of Use", TERMS_URL, "Terms & disclaimer", TERMS,
        f"Terms of Use and disclaimer of {SITE['domain']}: the posts, study notes, tutorials and RPT "
        "calculator are for learning, not legal or financial advice, and are written in a personal capacity.")


DISCLAIMER_URL = "/disclaimer/"


def disclaimer():
    return _policy_page(
        "Disclaimer", DISCLAIMER_URL, "Disclaimer", DISCLAIMER,
        f"Disclaimer of {SITE['domain']}: everything here is written in a personal capacity for learning, "
        "is not an official government issuance or legal advice, and is not endorsed by any office.")


PARTS = {"/": home, "/study-notes/": courses, "/tutorials/": tutorials, "/blog/": blog, "/about/": about, "/contact/": contact, PRIVACY_URL: privacy, TERMS_URL: terms, DISCLAIMER_URL: disclaimer, RPT_URL: rpt_page}


def _full_page(build):
    def render():
        p = build()
        return layout(p["title"], p["active"], p["body"], description=p["description"], url=p["url"],
                      og_type=p["og_type"], seo_title=p.get("seo_title"), json_ld=p.get("json_ld"),
                      share_image=p.get("share_image"))
    return render


ROUTES = {route: _full_page(build) for route, build in {**PARTS, **post_parts()}.items()}
ROUTES[BOOK_URL] = _full_page(book_home)
ROUTES.update({BOOK.chapter_url(c["n"]): _full_page(lambda c=c: book_chapter(c)) for c in BOOK.CHAPTERS})
ROUTES[BOOK.GLOSSARY_URL] = _full_page(lambda: book_back(BOOK.GLOSSARY, BOOK.GLOSSARY_URL,
    "The terms used in 360° Accountability, from accountable forms to the Seal of Good Local Governance."))
ROUTES[BOOK.REFERENCES_URL] = _full_page(lambda: book_back(BOOK.REFERENCES, BOOK.REFERENCES_URL,
    "The books, articles, laws and issuances behind 360° Accountability."))
ROUTES[BOOK.AUTHOR_URL] = _full_page(lambda: book_back(BOOK.AUTHOR, BOOK.AUTHOR_URL,
    "Who wrote 360° Accountability, and the work and study behind it."))
ROUTES[SERIES_URL] = _full_page(series_page)
ROUTES[DEMO_URL] = demo_page  # a whole page of its own: no site layout, so no ads on the demo
# one page per published lesson; scheduled lessons appear on their publish_on date
ROUTES.update({lesson_url(x): _full_page(lambda x=x: lesson_page(x)) for x in LESSONS if lesson_is_live(x)})
ROUTES.update({module_url(m): _full_page(lambda m=m: module_page(m)) for m in MODULES if module_is_live(m)})
ROUTES.update({note_url(n): _full_page(lambda n=n: note_page(n)) for n in NOTES if note_is_live(n)})


def not_found():
    """Shown by static hosts (Cloudflare Pages) for any address that doesn't exist."""
    return layout("Page not found", None, [
        t.p("404", class_="eyebrow"),
        t.h1("Page not found"),
        t.p("The page you are looking for doesn't exist or has moved.", class_="lead"),
        t.a("Back to home", href="/", class_="btn primary"),
    ])
