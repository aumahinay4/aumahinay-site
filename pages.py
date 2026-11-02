"""Page builders. Each function returns a full HTML document as a string."""

from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

import tags as t
from content import ABOUT, ALTOS, BLOG, CERTIFICATES, SITE, SUBSYSTEMS, TRAININGS
from highlight import highlight
from lessons import GLOSSARY, LESSONS, TUTORIAL
from style import CSS
from tags import Raw

STATIC = Path(__file__).parent / "static"
TUTORIALS = Path(__file__).parent / "tutorials"


def asset_url(name):
    """URL of a file in static/. preview.py swaps this for inline data URLs."""
    return "/static/" + name


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
    '<svg class="enter" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5"/></svg>'
    '<svg class="exit" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4v5H4M20 9h-5V4M15 20v-5h5M4 15h5v5"/></svg>'
)

NAV = [("/", "Home"), ("/projects/", "Projects"), ("/courses/", "Courses"), ("/tutorials/", "Tutorials"), ("/blog/", "Blog"), ("/about/", "About")]


def layout(title, active, body, description=None):
    page_title = SITE["brand"] if active == "/" else f"{title} · {SITE['brand']}"
    doc = t.html(
        t.head(
            t.meta(charset="utf-8"),
            t.meta(name="viewport", content="width=device-width, initial-scale=1"),
            t.title(page_title),
            # aumahinay.dev is the only address: test copies on *.pages.dev jump to it
            t.script(Raw(f'if (/\\.pages\\.dev$/.test(location.hostname)) location.replace("https://{SITE["domain"]}" + location.pathname + location.search + location.hash);')),
            t.link(rel="canonical", href=f"https://{SITE['domain']}{active}") if active else None,
            t.meta(name="description", content=description or SITE["tagline"]),
            # link previews on Facebook, Messenger, Viber, LinkedIn and X
            t.meta(property="og:type", content="website"),
            t.meta(property="og:site_name", content=SITE["domain"]),
            t.meta(property="og:title", content=page_title),
            t.meta(property="og:description", content=description or SITE["tagline"]),
            t.meta(property="og:url", content=f"https://{SITE['domain']}{active}"),
            t.meta(property="og:image", content=f"https://{SITE['domain']}/static/share.jpg"),
            t.meta(property="og:image:width", content="1200"),
            t.meta(property="og:image:height", content="630"),
            t.meta(property="og:image:alt", content=f"{SITE['short_name']}, {SITE['domain']}"),
            t.meta(name="twitter:card", content="summary_large_image"),
            t.link(rel="icon", href="/favicon.ico", sizes="any"),
            t.link(rel="icon", type="image/png", sizes="32x32", href=asset_url("favicon-32.png")),
            t.link(rel="apple-touch-icon", href=asset_url("apple-touch-icon.png")),
            t.link(rel="preconnect", href="https://fonts.googleapis.com"),
            t.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Figtree:wght@400;500;600;700&display=swap"),
            t.style(Raw(CSS)),
        ),
        t.body(
            t.header(
                t.div(
                    t.a(t.img(src=asset_url("avatar.png"), alt="", width="34", height="34", class_="avatar"), t.span(SITE["short_name"].split()[0], " ", t.b(SITE["short_name"].split()[1])), href="/", class_="brand"),
                    t.nav([t.a(label, href=href, class_="active" if href == active else None) for href, label in NAV]),
                    t.button(FULLSCREEN_ICON, type="button", id="fs", class_="fs", title="Full screen", aria_label="Full screen", aria_pressed="false", hidden=True),
                    class_="wrap",
                ),
                class_="site",
            ),
            t.main(t.div(body, class_="wrap")),
            t.footer(
                t.div(
                    "Built in Python",
                    class_="wrap",
                ),
                class_="site",
            ),
            t.script(Raw(FULLSCREEN_SCRIPT)),
        ),
        lang="en",
    )
    return "<!doctype html>\n" + doc


def part(title, active, *body, description=None):
    """The pieces of one page, before it is wrapped in the site layout."""
    return {"title": title, "active": active, "body": list(body), "description": description}


def tag_list(items):
    return t.div([t.span(item, class_="tag") for item in items], class_="tags") if items else None


def ring(size_class=""):
    """The ALTOS emblem: a 360° colour ring."""
    return t.div(t.span("360°"), t.small("ALTOS"), class_=f"ring {size_class}".strip(), aria_hidden="true")


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
            t.div(t.a("Explore ALTOS →", href="/projects/", class_="btn primary"), class_="foot"),
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


def cert_card(c):
    return t.div(
        t.div(t.span(c["kind"], class_="badge" if c["kind"].startswith("Prof") else "badge spec"), class_="meta"),
        t.h3(c["name"]),
        t.div(f"Completed {c['date']} · {c['courses']} courses · Coursera", class_="meta"),
        t.details(t.summary("Show courses"), t.ul([t.li(x) for x in c["course_list"]])),
        t.div(t.a("Verify on Coursera →", href=c["verify"], target="_blank", rel="noopener"), class_="foot"),
        class_="card",
    )


def section_head(title, link_text, href):
    return t.div(t.h2(title), t.a(f"{link_text} →", href=href, class_="more"), class_="section-head")


def home():
    pro = [c for c in CERTIFICATES if c["kind"].startswith("Prof")]
    return part(
        "Home", "/",
        t.div(
            t.div(
                t.h1(SITE["title"]),
                t.div(class_="rule"),
                t.p(SITE["tagline"] + " My tools make treasury work faster, more accurate, and easier to audit.", class_="lead"),
                t.div(
                    t.a("See ALTOS", href="/projects/", class_="btn primary"),
                    t.a("Certificates", href="/courses/", class_="btn ghost"),
                    t.a("Contact me", href=f"mailto:{SITE['email']}", class_="btn ghost"),
                    class_="btns",
                ),
                class_="hero-text",
            ),
            t.div(cover_img("hero-cover"), class_="hero-art"),
            class_="hero",
        ),
        t.div(
            t.div(t.b("15", t.small("+")), t.span("Years in government service"), class_="stat"),
            t.div(t.b("13", t.small("+")), t.span("Years in public finance"), class_="stat"),
            t.div(t.b(len(pro)), t.span("Google Professional Certificates"), class_="stat"),
            t.div(t.b(sum(c["courses"] for c in CERTIFICATES)), t.span("Coursera courses completed"), class_="stat"),
            class_="stats",
        ),
        t.h2("What I do"),
        t.div(
            [
                t.div(t.h3(title), t.p(text), class_="card focus")
                for title, text in (
                    ("Treasury operations",
                     "More than 13 years in local government fiscal administration: collections, "
                     "disbursements, deposits and the reports that keep them accountable."),
                    ("Software for local treasuries",
                     "I design and build ALTOS in Python, with tamper-evident audit logs and encrypted "
                     "backups, to bring automation to treasury offices."),
                    ("Continuous learning",
                     f"{len(pro)} Google Professional Certificates and {len(CERTIFICATES) - len(pro)} Specializations "
                     "in data analytics, AI, cybersecurity, IT support and project management."),
                )
            ],
            class_="grid three",
        ),
        section_head("Projects", "All about ALTOS", "/projects/"),
        t.div(altos_feature_card(), class_="grid one"),
        t.div([subsystem_node(sub, summary=False) for sub in SUBSYSTEMS], class_="children compact"),
        section_head("Latest certificates", f"All {len(CERTIFICATES)} credentials", "/courses/"),
        t.div([cert_card(c) for c in CERTIFICATES[:3]], class_="grid"),
        section_head(TUTORIAL["title"], "All lessons", "/tutorials/"),
        t.div([lesson_card(x, mini=True) for x in home_lessons()], class_="grid three"),
    )


def projects():
    book = ALTOS["book"]
    return part(
        "Projects", "/projects/",
        t.p("Software", class_="eyebrow"),
        t.h1("Projects"),
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
            ring(),
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
            cover_img("book-cover"),
            t.div(
                t.span(book["status"], class_="badge spec"),
                t.h3(book["title"]),
                t.p(book["subtitle"], class_="muted"),
                t.p(book["blurb"]),
            ),
            class_="card book",
        ),
        t.p(t.em(ALTOS["motto"]), class_="motto"),
        description=f"{ALTOS['name']}, the {ALTOS['full_name']}, built by {SITE['name']}",
    )


def courses():
    pro = [c for c in CERTIFICATES if c["kind"].startswith("Prof")]
    spec = [c for c in CERTIFICATES if not c["kind"].startswith("Prof")]
    return part(
        "Courses", "/courses/",
        t.p("Learning", class_="eyebrow"),
        t.h1("Completed courses"),
        t.p(
            "I began learning on Coursera through Google Career Certificates (GCC) in 2020, during the pandemic, "
            "while serving as Acting Municipal Treasurer of Mulanay, Quezon. In 2024 I committed to the GCC "
            "program fully, and I have since earned "
            f"{len(pro)} Google Professional Certificates and {len(spec)} Specializations, "
            f"{sum(c['courses'] for c in CERTIFICATES)} courses in total. "
            "Every credential links to its Coursera verification page.",
            class_="lead",
        ),
        t.h2("Google Professional Certificates"),
        t.div([cert_card(c) for c in pro], class_="grid"),
        t.h2("Google Specializations"),
        t.div([cert_card(c) for c in spec], class_="grid"),
        t.h2("Government & professional training"),
        t.p("A selection of the government and professional trainings I have completed over the years. The full list is longer than what is shown here.", class_="muted"),
        t.table([t.tr(t.td(t.b(name), t.br(), t.span(org, class_="muted")), t.td(when)) for name, org, when in TRAININGS]),
        description="Coursera and Google certificates completed by " + SITE["name"],
    )


# ---- Python for Treasury Work (tutorials) ----

def ph_today():
    return datetime.now(timezone(timedelta(hours=8))).date().isoformat()


def nice_date(iso):
    d = datetime.strptime(iso, "%Y-%m-%d")
    return f"{d:%B} {d.day}, {d.year}"


def lesson_is_live(x):
    return "publish_on" not in x or (x["publish_on"] is not None and x["publish_on"] <= ph_today())


# preview.py sets SHOW_SCHEDULED so lessons can be reviewed before their date,
# and turns DOWNLOADS off because the one-file preview has no files to download
SHOW_SCHEDULED = False
DOWNLOADS = True


def lesson_url(x):
    return f"/tutorials/{x['slug']}/"


def visible_lessons():
    return [x for x in LESSONS if SHOW_SCHEDULED or lesson_is_live(x)]


def home_lessons():
    """Newest live lessons first, then the next ones coming; three in all."""
    live = [x for x in LESSONS if lesson_is_live(x)]
    soon = [x for x in LESSONS if not lesson_is_live(x)]
    return (live[::-1] + soon)[:3]


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
        t.h1(TUTORIAL["title"]),
        t.p(TUTORIAL["intro"], class_="lead"),
        t.div(t.p(t.b("Where to begin. "), TUTORIAL["setup"]), class_="card setup"),
        t.div([lesson_card(x) for x in LESSONS], class_="lesson-list"),
        t.h2("Words to know"),
        t.dl([t.div(t.dt(term), t.dd(meaning), class_="term") for term, meaning in GLOSSARY], class_="glossary"),
        t.p(
            f"{len(shown)} of {len(LESSONS)} lessons published. New lessons are added regularly. "
            "All names, receipt numbers and amounts in the examples are made up.",
            class_="muted note",
        ),
        description="Python lessons for local treasury work, by " + SITE["short_name"],
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
            tag_list(x["topics"]),
            t.div(t.p("In this lesson", class_="eyebrow"), t.ul([t.li(item) for item in x["learn"]]), class_="card learn"),
            [lesson_block(x, b) for b in x["body"]],
            t.div(
                t.a("← Lesson " + str(prev["number"]), href=lesson_url(prev)) if prev else t.span(),
                (t.a("Lesson " + str(nxt["number"]) + " →", href=lesson_url(nxt)) if nxt_open
                 else t.span(f"Lesson {nxt['number']} comes out {nice_date(nxt['publish_on'])}", class_="muted") if nxt else t.span()),
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
    if kind == "ask":
        return t.p(rest[0], " ", t.a("Email me", href=f"mailto:{SITE['email']}"), ".", class_="ask")
    raise ValueError(f"unknown blog block {kind!r}")


def blog_post(b):
    return t.article(
        t.div(t.span(b["date"], class_="muted"), class_="meta"),
        t.h2(b["title"]),
        t.p(b["summary"], class_="lead") if b.get("summary") else "",
        [blog_block(x) for x in b["body"]],
        class_="post",
        id=b["slug"],
    )


def live_posts():
    """Posts without publish_on, or whose publish_on date has arrived (Philippine time)."""
    today = datetime.now(timezone(timedelta(hours=8))).date().isoformat()
    return [b for b in BLOG if "publish_on" not in b or (b["publish_on"] and b["publish_on"] <= today)]


def blog():
    posts_live = live_posts()
    if posts_live:
        posts = [
            t.div(
                t.p("Posts", class_="eyebrow"),
                t.ul([t.li(t.a(b["title"], href=f"#{b['slug']}"), " ", t.span(b["date"], class_="muted")) for b in posts_live]),
                class_="card post-index",
            ) if len(posts_live) > 1 else "",
            [blog_post(b) for b in posts_live],
        ]
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
            t.h1("Blog"),
            t.p(
                "My own stories and thoughts, from treasury work and building software to life beyond the office.",
                class_="lead",
            ),
            posts,
            t.p(
                "Views here are my own and do not represent any government office.",
                class_="muted note",
            ),
            class_="blog-col",
        ),
        description="Blog by " + SITE["short_name"],
    )


def about():
    return part(
        "About", "/about/",
        t.p("About me", class_="eyebrow"),
        t.h1("Hello, I'm Butch."),
        t.p(ABOUT["intro"], class_="lead"),
        [t.p(p) for p in ABOUT["paragraphs"]],
        t.h2("Experience"),
        t.div(
            [
                t.div(
                    t.h3(e["role"]),
                    t.div(f"{e['org']} · {e['period']}", class_="muted"),
                    t.ul([t.li(x) for x in e["points"]]),
                    class_="item",
                )
                for e in ABOUT["experience"]
            ],
            class_="timeline",
        ),
        t.div(
            t.div(
                t.h2("Education"),
                t.table([t.tr(t.td(t.b(d), t.br(), t.span(s, class_="muted")), t.td(y)) for d, s, y in ABOUT["education"]]),
            ),
            t.div(
                t.h2("Eligibilities"),
                t.ul([t.li(x) for x in ABOUT["eligibilities"]]),
            ),
            class_="two",
        ),
        t.h2("Skills"),
        tag_list(ABOUT["skills"]),
        t.h2("Get in touch"),
        t.p("Email me at ", t.a(SITE["email"], href=f"mailto:{SITE['email']}"), "."),
        description="About " + SITE["name"],
    )


PARTS = {"/": home, "/projects/": projects, "/courses/": courses, "/tutorials/": tutorials, "/blog/": blog, "/about/": about}


def _full_page(build):
    def render():
        p = build()
        return layout(p["title"], p["active"], p["body"], description=p["description"])
    return render


ROUTES = {route: _full_page(build) for route, build in PARTS.items()}
# one page per published lesson; scheduled lessons appear on their publish_on date
ROUTES.update({lesson_url(x): _full_page(lambda x=x: lesson_page(x)) for x in LESSONS if lesson_is_live(x)})


def not_found():
    """Shown by static hosts (Cloudflare Pages) for any address that doesn't exist."""
    return layout("Page not found", None, [
        t.p("404", class_="eyebrow"),
        t.h1("Page not found"),
        t.p("The page you are looking for doesn't exist or has moved.", class_="lead"),
        t.a("Back to home", href="/", class_="btn primary"),
    ])
