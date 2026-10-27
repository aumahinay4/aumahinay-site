"""Page builders. Each function returns a full HTML document as a string."""

from pathlib import Path

import tags as t
from content import ABOUT, ALTOS, BLOG, CERTIFICATES, NEWS, SITE, SUBSYSTEMS, TRAININGS
from style import CSS
from tags import Raw

STATIC = Path(__file__).parent / "static"


def asset_url(name):
    """URL of a file in static/. preview.py swaps this for inline data URLs."""
    return "/static/" + name


NAV = [("/", "Home"), ("/projects/", "Projects"), ("/courses/", "Courses"), ("/news/", "IT News"), ("/blog/", "Blog"), ("/about/", "About")]


def layout(title, active, body, description=None):
    page_title = SITE["brand"] if active == "/" else f"{title} · {SITE['brand']}"
    doc = t.html(
        t.head(
            t.meta(charset="utf-8"),
            t.meta(name="viewport", content="width=device-width, initial-scale=1"),
            t.title(page_title),
            t.meta(name="description", content=description or SITE["tagline"]),
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
            t.div(t.b("15+"), t.span("years in government service"), class_="stat"),
            t.div(t.b("13+"), t.span("years in public finance"), class_="stat"),
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
        section_head("Latest IT news", "More IT news", "/news/"),
        t.div(
            [
                t.a(
                    t.div(t.span(n["topic"], class_="badge"), t.span(n["date"], class_="muted"), class_="meta"),
                    t.h3(n["title"]),
                    t.span(f"{n['source']} →", class_="muted"),
                    href="/news/",
                    class_=f"card news-mini {NEWS_TOPIC_COLOR.get(n['topic'], 'gold')}",
                )
                for n in NEWS[:3]
            ],
            class_="grid three",
        ),
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


NEWS_TOPIC_COLOR = {
    "Cybersecurity": "coral",
    "Digital ID": "blue",
    "E-government": "green",
    "AI in government": "violet",
}


def news_card(n, latest=False):
    return t.article(
        t.div(
            t.span(n["topic"], class_="badge"),
            t.span("Latest", class_="badge latest") if latest else "",
            t.span(n["date"], class_="muted"),
            class_="meta",
        ),
        t.h3(n["title"]),
        t.p(n["summary"]),
        t.p(t.b("Why it matters: "), n["why"], class_="why") if n.get("why") else "",
        t.div(
            t.span(f"Source: {n['source']}", class_="muted"),
            t.a("Read the full story →", href=n["url"], target="_blank", rel="noopener"),
            class_="foot source",
        ),
        class_=f"card news {NEWS_TOPIC_COLOR.get(n['topic'], 'gold')}" + (" latest" if latest else ""),
    )


def news():
    return part(
        "IT News", "/news/",
        t.p("Updates", class_="eyebrow"),
        t.h1("IT News"),
        t.p(
            "Selected technology news on digital government, cybersecurity and AI in the Philippines, "
            "summarized briefly in my own words. Each item links to the original article.",
            class_="lead",
        ),
        t.p(f"Last updated {NEWS[0]['date']} · {len(NEWS)} stories", class_="muted news-updated"),
        t.div([news_card(n, latest=(i == 0)) for i, n in enumerate(NEWS)], class_="news-list"),
        t.p(
            "Summaries of published news, each linked to its original source. "
            "This is a personal website and not an official publication of any government office.",
            class_="muted note",
        ),
        description="Selected IT news for Philippine public service",
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


def blog():
    if BLOG:
        posts = [
            t.div(
                t.p("Posts", class_="eyebrow"),
                t.ul([t.li(t.a(b["title"], href=f"#{b['slug']}"), " ", t.span(b["date"], class_="muted")) for b in BLOG]),
                class_="card post-index",
            ) if len(BLOG) > 1 else "",
            [blog_post(b) for b in BLOG],
        ]
    else:
        posts = t.div(
            t.h3("First posts coming soon"),
            t.p("I'll share notes here on treasury work, building ALTOS, and what I learn along the way."),
            class_="card empty",
        )
    return part(
        "Blog", "/blog/",
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


PARTS = {"/": home, "/projects/": projects, "/courses/": courses, "/news/": news, "/blog/": blog, "/about/": about}


def _full_page(build):
    def render():
        p = build()
        return layout(p["title"], p["active"], p["body"], description=p["description"])
    return render


ROUTES = {route: _full_page(build) for route, build in PARTS.items()}


def not_found():
    """Shown by static hosts (Cloudflare Pages) for any address that doesn't exist."""
    return layout("Page not found", None, [
        t.p("404", class_="eyebrow"),
        t.h1("Page not found"),
        t.p("The page you are looking for doesn't exist or has moved.", class_="lead"),
        t.a("Back to home", href="/", class_="btn primary"),
    ])
