"""Page builders. Each function returns a full HTML document as a string."""

import hashlib
import json
from urllib.parse import quote
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

import tags as t
from content import ABOUT, ALTOS, BLOG, BLOG_CATEGORIES, CERTIFICATES, PRIVACY, SITE, SUBSYSTEMS, TRAININGS
from highlight import highlight
from lessons import GLOSSARY, LAST_CHECKED, LESSONS, TUTORIAL
from vocab import MODULES, VOCAB, module_url, word_source
from notes import NOTES, NOTES_INFO, OUTLINE, note_url
from rpt import RPT_URL, rpt_page
from style import CSS
from tags import Raw

STATIC = Path(__file__).parent / "static"
TUTORIALS = Path(__file__).parent / "tutorials"


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

NAV = [("/", "Home"), ("/projects/", "Projects"), ("/study-notes/", "Study Notes"), ("/tutorials/", "Tutorials"), ("/blog/", "Blog"), ("/about/", "About")]

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
MENU = NAV[:4] + [(RPT_URL, "RPT Calculator")] + NAV[4:] + [("/contact/", "Contact"), ("/privacy/", "Privacy Policy")]


def menu_items():
    """The menu as built today. Study Notes appears only once a note is live, so the menu never leads to an
    empty hub page (AdSense "under construction" risk, Butch's audit 2026-11-10). The hourly build adds it on
    the first note's publish time."""
    return [(href, label) for href, label in MENU if href != "/study-notes/" or live_notes()]


def _bar_title(active):
    """HOME in bold beside the three bars, on the Home page only, so it is clear you are home (Butch 2026-11-10)."""
    return t.a("HOME", href="/", class_="bar-title") if active == "/" else None


MENU_ICON = Raw('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>')
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
  btn.addEventListener("click", function () { set(true); });
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
                "jobTitle": "Acting Municipal Treasurer",
                "knowsAbout": ["Public finance", "Local government treasury operations", "Python", "Software development"],
                **({"sameAs": profiles} if profiles else {}),
            },
        ],
    }
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def layout(title, active, body, description=None, url=None, og_type="website"):
    url = url or active
    # his name in every title, so a search for "Butch Mahinay" finds the site
    page_title = f"{SITE['short_name']} · {SITE['tagline_short']}" if active == "/" else f"{title} · {SITE['short_name']}"
    doc = t.html(
        t.head(
            t.meta(charset="utf-8"),
            t.meta(name="viewport", content="width=device-width, initial-scale=1"),
            # Google AdSense code, only once SITE["adsense_client"] is set (Butch applies; see content.py)
            t.script(src=f"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={SITE['adsense_client']}",
                     crossorigin="anonymous", **{"async": "async"}) if SITE.get("adsense_client") else None,
            # paint the phone's browser bars in the top bar's navy, so the site looks full-screen
            t.meta(name="theme-color", content="#f3f6fc", media="(prefers-color-scheme: light)"),
            t.meta(name="theme-color", content="#071631", media="(prefers-color-scheme: dark)"),
            t.title(page_title),
            # https://aumahinay.dev is the only address: test copies on *.pages.dev and plain http jump to it
            t.script(Raw(f'if (/\\.pages\\.dev$/.test(location.hostname) || (location.protocol === "http:" && location.hostname === "{SITE["domain"]}")) location.replace("https://{SITE["domain"]}" + location.pathname + location.search + location.hash);')),
            t.link(rel="alternate", type="application/rss+xml", title=f"{SITE['short_name']}: new posts and lessons", href="/feed.xml"),
            t.link(rel="canonical", href=f"https://{SITE['domain']}{url}") if url else None,
            t.meta(name="description", content=description or SITE["tagline"]),
            t.meta(name="robots", content="noindex") if active is None else None,  # the 404 page
            t.script(Raw(person_json_ld()), type="application/ld+json") if active == "/" else None,
            # link previews on Facebook, Messenger, Viber, LinkedIn and X
            t.meta(property="og:type", content=og_type),
            t.meta(property="og:site_name", content=SITE["short_name"]),  # his name, not the domain
            t.meta(property="og:title", content=page_title),
            t.meta(property="og:description", content=description or SITE["tagline"]),
            t.meta(property="og:url", content=f"https://{SITE['domain']}{url}"),
            t.meta(property="og:image", content=f"https://{SITE['domain']}/static/share.jpg?v="
                   + hashlib.sha1((STATIC / "share.jpg").read_bytes()).hexdigest()[:8]),  # new picture = new link, so Facebook fetches it again
            t.meta(property="og:image:width", content="1200"),
            t.meta(property="og:image:height", content="630"),
            t.meta(property="og:image:alt", content=f"{SITE['short_name']}, {SITE['domain']}"),
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
                    t.button(MENU_ICON, type="button", id="menu-open", class_="menu-btn", aria_label="Open menu",
                             aria_controls="site-menu", aria_expanded="false"),
                    # the page's section name in bold beside the three bars, e.g. HOME (Butch 2026-11-10)
                    _bar_title(active),
                    t.nav(
                        [t.a(label, href=href, class_="active" if href == active else None, aria_current="page" if href == active else None)
                         for href, label in menu_items()],
                        id="site-menu", aria_label="Main menu",
                    ),
                    class_="wrap",
                ),
                class_="site",
            ),
            t.main(t.div(body, class_="wrap")),
            # small footer at the bottom of every page: "Built in Python" + Privacy Policy link (Butch 2026-11-10)
            t.footer(t.div(t.span("Built in Python", class_="built"),  # far left (Butch 2026-11-10)
                           t.a("Privacy Policy", href="/privacy/", aria_current="page" if active == "/privacy/" else None),
                           class_="wrap"), class_="legal"),
            t.script(Raw(MENU_SCRIPT)),
            t.script(Raw(SWIPE_SCRIPT % json.dumps([href for href, _ in menu_items() if href not in ("/contact/", "/privacy/")]))),
            CERT_VIEWER if 'class="cert-thumb"' in t.render(body) else None,
        ),
        lang="en",
    )
    return "<!doctype html>\n" + doc


def part(title, active, *body, description=None, url=None, og_type="website"):
    """The pieces of one page, before it is wrapped in the site layout."""
    return {"title": title, "active": active, "body": list(body), "description": description, "url": url,
            "og_type": og_type}


def tag_list(items):
    return t.div([t.span(item, class_="tag") for item in items], class_="tags") if items else None


def wordmark(word="ALTOS"):
    """ALTOS in its five letter colours, as on the book cover."""
    return [t.span(ch, class_=f"l{i}") for i, ch in enumerate(word)]


def cover_img(class_):
    return t.img(src=asset_url("altos-cover.jpg"), alt=f"Cover of {ALTOS['book']['title']}", class_=class_, width="600", height="900")


def altos_feature_card():
    return t.div(
        t.div(t.img(src=asset_url("altos-screen.jpg"), alt="The ALTOS sign-in page", class_="feature-shot", width="1600", height="1001", loading="lazy"), class_="feature-art wide"),
        t.div(
            t.p(ALTOS["where"], class_="eyebrow"),
            t.h3(t.span(wordmark(), class_="wordmark"), " ", ALTOS["full_name"]),
            tag_list(ALTOS["stack"]),
            t.div(t.a("Explore ALTOS →", href="/projects/", class_="btn white"), class_="foot"),
            class_="feature-body",
        ),
        class_="card feature",
    )


def subsystem_node(sub, summary=True):
    return t.div(
        t.div(t.span(sub["code"], class_="code"), t.span(sub["status"], class_="status" if sub["status"] == "Planned" else "status live"), class_="node-head"),
        t.p(sub["summary"]) if summary else None,
        t.div(sub["movement"], class_="forms"),
        class_="node child",
    )


def family():
    """ALTOS as the mother system with its subsystems branching below."""
    return t.div(
        t.div(
            t.div(t.span(t.span(wordmark(), class_="wordmark"), class_="code"), class_="node-head"),
            t.h3(ALTOS["full_name"]),
            t.p("Collect, Disburse and Report in one database, with the ALTOS Framework built in."),
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


def home():
    """Home: what the site offers (blog, free Python lessons, ALTOS), the newest writing first,
    then topics, lessons, the project and a short note about the author (Butch 2026-11-09:
    make Home relevant to the whole site and ready for an AdSense review)."""
    posts = sorted(live_posts(), key=post_day, reverse=True)
    lessons = [x for x in LESSONS if lesson_is_live(x)]
    topics = [(key, label, sum(b["category"] == key for b in posts)) for key, label, _ in BLOG_CATEGORIES]
    topic_text = {
        "software": "Building ALTOS, Python, and software that keeps public money accountable.",
        "finance": "Local treasury work, collections, disbursements and the rules behind them.",
        "personal": "The farm, the province, and life beyond the office.",
        "security": "A plain-language series on staying safe online: passwords, scams, home networks and ransomware.",
    }
    return part(
        "Home", "/",
        t.div(
            t.div(
                t.div(t.h1("Where public finance meets Python"), class_="hero-name"),
                t.p("Plain-language writing on local treasury work and public finance, free tutorials (Python "
                    "for treasury staff and Civil Service exam vocabulary), a free real property tax calculator, "
                    "and notes from building ALTOS, by a treasury worker who builds software.",
                    class_="lead"),
                t.div(
                    t.a("RPT Calculator", href=RPT_URL, class_="btn ghost"),
                    t.a("Tutorials", href="/tutorials/", class_="btn ghost"),
                    t.a("Blog", href="/blog/", class_="btn ghost"),
                    class_="btns",
                ),
                class_="hero-text",
            ),
            class_="hero",
        ),
        t.h2("What you'll find here"),
        t.div(
            [
                t.a(t.h3(title), t.p(text), t.span(go, class_="go"), href=href, class_="card focus")
                for title, text, go, href in (
                    ("Blog",
                     "Stories and notes on public finance, treasury work, cybersecurity and building software.",
                     "Read the blog →", "/blog/"),
                    ("Tutorials",
                     "Free, beginner-friendly lessons: Python for treasury work and Civil Service exam "
                     "vocabulary with practice questions.", "Start learning →", "/tutorials/"),
                    ("ALTOS",
                     "The Automated Local Treasury Operations System, a working treasury system for "
                     "Philippine local treasuries, written in Python.", "See the project →", "/projects/"),
                )
            ],
            class_="grid three",
        ),
        t.h2("Free tool"),
        t.div(
            t.a(t.h3("Real Property Tax Calculator"),
                t.p("Work out the basic real property tax and the Special Education Fund on any assessed value, "
                    "with the discount or interest, and see how much goes to the province, municipality, "
                    "barangay and school boards."),
                t.span("Open the calculator →", class_="go"), href=RPT_URL, class_="card focus tool"),
            class_="grid one",
        ),
        section_head("Latest posts", f"All {len(posts)} posts", "/blog/"),
        t.div([post_card(b) for b in posts[:4]], class_="post-list home-posts"),
        t.h2("Browse by topic"),
        t.div(
            [t.a(t.h3(label), t.p(topic_text.get(key, "")), t.span(f"{n} post{'s' if n != 1 else ''} →", class_="go"),
                 href=f"/blog/#cat-{key}", class_="card focus topic") for key, label, n in topics if n],
            class_="grid three",
        ),
        section_head(TUTORIAL["title"], "All lessons", "/tutorials/"),
        t.div([lesson_card(x, mini=True) for x in lessons[::-1][:3]], class_="grid three"),
        section_head("Project", "All about ALTOS", "/projects/"),
        t.div(altos_feature_card(), class_="grid one"),
        t.h2("About the author"),
        author_card(),
        description=f"{SITE['short_name']}: plain-language writing on local treasury work and public finance, "
                    "free Python lessons for treasury staff, and the ALTOS treasury system.",
    )


def author_card():
    """Short author box: on Home and at the end of every blog post. Matches the About page (Butch 2026-11-10:
    "be consistent"): same name, same violet roles line and the same facts, in third person ("he", Butch 2026-11-10) as the About intro."""
    return t.div(
        t.div(
            t.img(src=asset_url("hero-photo.jpg"), alt="", width="400", height="400", class_="hero-photo author-photo"),
            t.div(
                t.p("Ambrosio “Butch” U. Mahinay, MPA", class_="author-name"),
                t.p([t.span(r) for r in ABOUT["roles"].split(" · ")], class_="author-roles"),  # one role per line
            ),
            class_="author-top",
        ),
        t.p("He is a public administration practitioner, author, and self-taught software developer in Quezon "
            "Province, Philippines, with over 15 years in government service, more than 13 of them in local treasury "
            "work since April 2013. He has earned 7 Google Professional Certificates and 3 Specializations on Coursera. "
            "He writes, teaches and builds software in his personal capacity, outside official working hours.",
            class_="author-bio"),
        t.p(t.a("Full profile", href="/about/"), t.a("Contact", href="/contact/"),
            t.a("Privacy Policy", href="/privacy/"), class_="author-links"),
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
            t.li(t.b("The ALTOS book. "), "Requests to read the full book and feedback on the preview."),
            t.li(t.b("Talks and trainings. "), "Invitations to speak about treasury work, Python for government "
                 "offices or staying safe online."),
            class_="reasons",
        ),
        t.p("Please don't send personal data you don't want me to keep. How I handle what you send is explained "
            "in the ", t.a("Privacy Policy", href="/privacy/"), "."),
        t.p("Views on this site are my own, written in my personal capacity, and do not represent any government office.",
            class_="muted note"),
        description=f"Contact {SITE['short_name']} by email about the blog, the Python lessons, or the ALTOS book.",
        url="/contact/",
    )


def projects():
    book = ALTOS["book"]
    return part(
        "Projects", "/projects/",
        t.p("Software", class_="eyebrow"),
        photo_title("Projects"),
        t.p(
            "ALTOS is the mother system. Its two subsystems are now ready: the Treasury Collection System for collections "
            "and the Treasury Disbursement System for disbursements, each with its own reports.",
            class_="lead",
        ),
        family(),
        t.h2("ALTOS, the mother system"),
        t.div(
            t.div(
                t.p("Mother system", class_="eyebrow"),
                t.h1(wordmark(), class_="wordmark", aria_label="ALTOS"),
                t.p(ALTOS["full_name"], class_="subtitle"),
                t.p(ALTOS["summary"], class_="lead"),
                tag_list(ALTOS["stack"]),
            ),
            class_="altos-hero",
        ),
        t.blockquote(t.p(ALTOS["principle"]), t.footer("The ALTOS principle")),
        t.figure(
            t.img(src=asset_url("altos-loop.png"), alt="The ALTOS loop: Collect (OR, RCD, deposit) leads to Disburse (voucher, check, cash advance), which leads to Report (RAAF, CRAAF, RCI, BRS, SRE), which sets the targets and budgets for the next cycle of collections. At the center: 360° accountability, a named officer at every step.", width="1395", height="680", loading="lazy"),
            t.figcaption("Figure 1.1 — The ALTOS loop. The three are not a line but a loop: three movements, one accountable officer at each step."),
            class_="screenshot diagram",
        ),
        t.h2("Three movements of public money"),
        t.p("Every transaction in a local treasury belongs to one of three movements. ALTOS follows each one, with a named officer answerable at every step.", class_="muted"),
        t.div(
            [t.div(t.h3(name), t.p(desc), t.div(forms, class_="forms"), class_="card") for name, desc, forms in ALTOS["movements"]],
            class_="grid three",
        ),
        t.h2("What ALTOS does"),
        t.div([t.div(t.h3(title), t.p(desc), class_="card") for title, desc in ALTOS["features"]], class_="grid four"),
        t.h2("The ALTOS Framework"),
        t.p("Ten principles for Philippine public fiscal administration. ALTOS checks its own records against each one in a quarterly self-assessment.", class_="muted"),
        t.ol([t.li(t.b(name), t.span(desc)) for name, desc in ALTOS["principles"]], class_="principles"),
        t.h2("The book"),
        t.div(
            t.a(cover_img("book-cover"), href=BOOK_URL, aria_label="Read a preview of the ALTOS book", class_="book-link"),
            t.div(
                t.span(book["status"], class_="badge spec"),
                t.h3(book["title"]),
                t.p(book["subtitle"], t.br(), f"{book['pages']} pages", class_="muted"),
                t.p(book["blurb"]),
                t.a("Read a preview →", href=BOOK_URL, class_="btn white"),
            ),
            class_="card book",
        ),
        t.p(t.em(ALTOS["motto"]), class_="motto"),
        description=f"{ALTOS['name']}, the {ALTOS['full_name']}: software for Philippine local treasuries, built by {SITE['name']}",
    )


BOOK_PREVIEW_PAGES = 20  # cover, title, copyright, contents, Part I, Chapters 1-3 and start of Chapter 4 = PDF pp. 1-4, 9-24 (preface left out at Butch's request) (static/book/page-NN.jpg)
BOOK_URL = "/projects/altos-book/"
# visitors ask by email; Butch approves by sharing the Drive PDF with them (Viewer, no download/print/copy)
BOOK_FIRST_DAYS, BOOK_MORE_DAYS = 3, 2  # reading time per approved request (Butch, 2026-11-04)
BOOK_REQUEST_MAILTO = (f"mailto:{SITE['email']}?subject=" + quote("Request: full ALTOS book") + "&body=" + quote(
    "Hello Butch,\n\nI would like to read the full book, 360° Accountability: The ALTOS Principles.\n\n"
    "Name:\nGoogle (Gmail) address to share it with:\nOffice or school:\nWhy I want to read it:\nFirst request or more time:\n\nThank you."))

# The book reader: one page at a time, Previous/Next, arrow keys, and swipe on the page.
# Saving is made harder (no download link, no right-click or long-press save, no dragging),
# but no website can block the phone's or computer's own screenshot keys.
BOOK_SCRIPT = """
(function () {
  var r = document.getElementById("reader");
  if (!r) return;
  var pages = JSON.parse(r.getAttribute("data-pages")), i = 0;
  var img = r.querySelector(".page img"), count = r.querySelector(".count");
  var prev = r.querySelector(".prev"), next = r.querySelector(".next");
  function show(n) {
    i = Math.max(0, Math.min(pages.length - 1, n));
    img.src = pages[i];
    img.alt = "Page " + (i + 1) + " of the preview";
    count.textContent = "Page " + (i + 1) + " of " + pages.length;
    prev.disabled = i === 0; next.disabled = i === pages.length - 1;
    if (i + 1 < pages.length) (new Image()).src = pages[i + 1];  // load the next page ahead
  }
  prev.addEventListener("click", function () { show(i - 1); });
  next.addEventListener("click", function () { show(i + 1); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "ArrowRight") show(i + 1);
    if (e.key === "ArrowLeft") show(i - 1);
  });
  var x0, y0;
  var stage = r.querySelector(".page");
  stage.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
  stage.addEventListener("touchend", function (e) {
    var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
    if (Math.abs(dx) > 50 && Math.abs(dx) > 2 * Math.abs(dy)) show(i + (dx < 0 ? 1 : -1));
  }, { passive: true });
  r.addEventListener("contextmenu", function (e) { e.preventDefault(); });
  r.addEventListener("dragstart", function (e) { e.preventDefault(); });
  show(0);
})();
"""


def book_reader():
    book = ALTOS["book"]
    pages = [asset_url(f"book/page-{n:02d}.jpg") for n in range(1, BOOK_PREVIEW_PAGES + 1)]
    return part(
        "ALTOS book preview", "/projects/",
        t.a("← Back to Projects", href="/projects/", class_="crumb"),
        t.p("Book preview", class_="eyebrow"),
        t.h1(book["title"]),
        t.p(f"{book['subtitle']} · {book['status']} · {book['pages']} pages. Read the first 20 pages here: the contents, Chapters 1 to 3 and the start of Chapter 4.", class_="lead"),
        t.div(
            t.div(
                t.button("← Previous", type="button", class_="btn prev"),
                t.span(class_="count", aria_live="polite"),
                t.button("Next →", type="button", class_="btn next"),
                class_="controls",
            ),
            t.div(
                t.img(src=pages[0], alt="Page 1 of the preview", width="900", height="1350", draggable="false"),
                t.div(class_="shield"),  # sits on top of the page, so a long-press or right-click finds no picture to save
                class_="page",
            ),
            id="reader", class_="reader", data_pages=json.dumps(pages), data_noswipe="",
        ),
        t.div(
            t.h2("Want to read the whole book?"),
            t.p(f"This is a preview of the draft edition. The full book has {book['pages']} pages. To read all of it, send a request. Once I approve it, "
                "I'll share the full book with your Gmail address to read online only: no download, print or copy."),
            t.p(f"Reading time: once your request is approved, you can read the whole book for {BOOK_FIRST_DAYS} days. "
                f"Need more time? Send another request; each one after that gives you {BOOK_MORE_DAYS} more days. "
                "Access ends automatically when the time is up. There is no limit on requests."),
            t.a("Request the full book →", href=BOOK_REQUEST_MAILTO, class_="btn white"),
            class_="reader-request",
        ),
        t.script(Raw(BOOK_SCRIPT)),
        description=f"Read a preview of {book['title']} by {SITE['name']}.",
        url=BOOK_URL,
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
            t.p("✓ Last checked: " + NOTES_INFO["checked"] + " · against RA 7160 (Local Government Code) and its amendments", class_="checked"),
            [note_block(b) for b in n["body"]],
            t.div(t.h3(ex_title), t.ol([t.li(s_) for s_ in steps]), t.p(t.b("Answer: "), ex_answer), class_="card example"),
            t.h2("Practice"),
            t.p("Tap your answer. A green ✓ means you got it right; a red ✗ means try to learn the right one, shown in green."),
            practice_list(n["practice"]),
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
        url=note_url(n),  # its own address, so Share and Google point to the note, not the Study Notes page
    )


# ---- Python for Treasury Work (tutorials) ----

PH = timezone(timedelta(hours=8))  # Philippine time


def ph_today():
    return datetime.now(PH).date().isoformat()


def nice_date(iso):
    d = datetime.strptime(iso, "%Y-%m-%d")
    return f"{d:%B} {d.day}, {d.year}"


def lesson_is_live(x):
    return "publish_on" not in x or (x["publish_on"] is not None and x["publish_on"] <= ph_today())


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


def lesson_card(x, mini=False):
    open_ = SHOW_SCHEDULED or lesson_is_live(x)
    when = None if lesson_is_live(x) else t.span("Coming " + nice_date(x["publish_on"]) if x.get("publish_on") else "Coming soon", class_="badge soon")
    inner = [
        t.div(t.span(f"Lesson {x['number']}", class_="badge"), when, t.span(f"{x['level']} · {x['minutes']} min", class_="muted"), class_="meta"),
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
        t.h2("Words to know"),
        t.dl([t.div(t.dt(term), t.dd(meaning), class_="term") for term, meaning in GLOSSARY], class_="glossary"),
        t.p(
            "New lessons are added regularly. "
            "All names, receipt numbers and amounts in the examples are made up.",
            class_="muted note",
        ),
        description=f"Free, beginner-friendly Python lessons for local treasury work: collections, disbursements and reports, by {SITE['short_name']}.",
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
        t.div(t.span(f"Module {m['number']}", class_="badge"), t.span(f"{len(m['words'])} words · practice", class_="muted"), class_="meta"),
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
        description=x["summary"],
    )


def blog_block(x):
    if isinstance(x, str):
        return t.p(x)
    kind, *rest = x
    if kind == "h":
        return t.h3(rest[0])
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


def blog_post(b):
    return t.article(
        post_meta(b),
        t.h1(b["title"]),
        t.p("By ", t.a("Ambrosio “Butch” U. Mahinay", href="/about/"), class_="byline"),
        t.p(b["summary"], class_="lead") if b.get("summary") else "",
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
    if not url.startswith("/blog/") or url == "/blog/":
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
            posts,
            t.script(Raw('(function(){var m=/^#cat-(\\w+)$/.exec(location.hash);var r=m&&document.getElementById("cat-"+m[1]);if(r)r.checked=true;'
                         'var d=document.getElementById("blog-cats");if(d)d.addEventListener("change",function(){d.open=false;});})();')),
            t.p(
                "Views here are my own and do not represent any government office.",
                class_="muted note",
            ),
            class_="blog-col",
        ),
        description=f"Stories and notes by {SITE['short_name']} on local treasury work, public finance, building the ALTOS system, and life beyond the office.",
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
        t.div(
            t.a(Raw("&larr; "), "All posts", href="/blog/", class_="back"),
            blog_post(b),
            react_box(post_url(b)),
            t.h2("About the author", class_="post-section"),
            author_card(),
            related_posts(b, posts, skip=(newer, older)),  # the Newer/Older links below already show those two
            t.nav(step(newer, "Newer post", "newer"), step(older, "Older post", "older"), class_="post-steps",
                  aria_label="More posts"),
            t.p("Views here are my own and do not represent any government office.", class_="muted note"),
            class_="blog-col",
        ),
        description=b.get("summary") or post_teaser(b),
        url=post_url(b),
        og_type="article",
    )


def related_posts(b, posts, skip=()):
    """'Keep reading': up to three other live posts, same category first (newest first), then the newest others."""
    others = sorted((p for p in posts if p is not b and p not in skip), key=post_day, reverse=True)
    picks = [p for p in others if p["category"] == b["category"]][:3]
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
        photo_title("Ambrosio “Butch” U. Mahinay, MPA", photo=True, class_="name-title"),  # name beside the photo instead of "About" (Butch 2026-11-10)
        t.p(ABOUT["roles"], class_="roles"),
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
        description=f"About {SITE['name']} (Butch): public administration practitioner with 15+ years in local "
                    "government revenue operations, author, and self-taught software developer.",
    )


PRIVACY_URL = "/privacy/"


def _privacy_text(x):
    """One run of policy text: a plain string, or a list mixing strings and (label, link) pairs."""
    if isinstance(x, str):
        return x
    return [t.a(p[0], href=p[1], target="_blank", rel="noopener") if isinstance(p, tuple) else p for p in x]


def privacy():
    body = []
    for heading, blocks in PRIVACY["sections"]:
        body.append(t.h2(heading))
        for blk in blocks:
            if isinstance(blk, str):
                body.append(t.p(blk))
            elif blk[0] == "list":
                body.append(t.ul([t.li(t.b(label), " ", _privacy_text(text)) for label, text in blk[1]]))
            elif blk[0] == "contact":
                body.append(t.ul(
                    t.li(t.b("Email: "), t.a(SITE["email"], href=f"mailto:{SITE['email']}")),
                    t.li(t.b("Website: "), t.a(f"https://{SITE['domain']}", href="/")),
                    class_="plain-list"))
    return part(
        "Privacy Policy", PRIVACY_URL,
        t.p("Privacy", class_="eyebrow"),
        t.h1("Privacy Policy"),
        t.p(t.b("Effective date: "), PRIVACY["effective"], t.br(), t.b("Website: "),
            t.a(f"https://{SITE['domain']}", href="/"), class_="muted policy-meta"),
        t.p(PRIVACY["intro"], class_="lead"),
        *body,
        description=f"Privacy Policy of {SITE['domain']}: what information is collected, how it is used, "
                    "and your rights under the Philippine Data Privacy Act of 2012 (RA 10173).",
        url=PRIVACY_URL,
    )


PARTS = {"/": home, "/projects/": projects, "/study-notes/": courses, "/tutorials/": tutorials, "/blog/": blog, "/about/": about, "/contact/": contact, PRIVACY_URL: privacy, RPT_URL: rpt_page}


def _full_page(build):
    def render():
        p = build()
        return layout(p["title"], p["active"], p["body"], description=p["description"], url=p["url"],
                      og_type=p["og_type"])
    return render


ROUTES = {route: _full_page(build) for route, build in {**PARTS, **post_parts()}.items()}
ROUTES[BOOK_URL] = _full_page(book_reader)
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
