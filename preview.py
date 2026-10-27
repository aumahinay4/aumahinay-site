"""Render the whole site as one self-contained page (each page becomes a tab).
Used to share a quick preview. Usage:  python preview.py  -> preview.html
"""

import base64
from pathlib import Path

import pages
import tags as t
from content import SITE
from pages import NAV, PARTS
from style import CSS
from tags import Raw, render

SLUG = {"/": "home", "/projects/": "projects", "/courses/": "courses", "/news/": "news", "/blog/": "blog", "/about/": "about"}

SCRIPT = """
function show() {
  var id = (location.hash || "#home").slice(1);
  if (!document.getElementById("view-" + id)) id = "home";
  document.querySelectorAll("section.view").forEach(function (s) { s.hidden = s.id !== "view-" + id; });
  document.querySelectorAll("nav a").forEach(function (a) {
    a.classList.toggle("active", a.getAttribute("href") === "#" + id);
  });
  window.scrollTo(0, 0);
}
window.addEventListener("hashchange", show);
show();
"""


def inline_asset(name):
    data = (Path(__file__).parent / "static" / name).read_bytes()
    kind = "jpeg" if name.endswith(".jpg") else name.rsplit(".", 1)[-1]
    return f"data:image/{kind};base64," + base64.b64encode(data).decode()


def build():
    pages.asset_url = inline_asset  # one self-contained file, no separate images
    views = []
    for route, make in PARTS.items():
        p = make()
        views.append(t.section(p["body"], class_="view", id="view-" + SLUG[route], hidden=route != "/"))
    html = render([
        t.title(SITE["brand"]),
        t.link(rel="icon", type="image/png", href=inline_asset("favicon-32.png")),
        t.meta(name="claude:viewport-fit-sides", content="cover"),
        t.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Figtree:wght@400;500;600;700&display=swap"),
        t.style(Raw(CSS + "body{background:var(--bg)}")),
        t.header(
            t.div(
                t.a(t.img(src=inline_asset("avatar.png"), alt="", width="34", height="34", class_="avatar"), t.span(SITE["short_name"].split()[0], " ", t.b(SITE["short_name"].split()[1])), href="#home", class_="brand"),
                t.nav([t.a(label, href="#" + SLUG[href]) for href, label in NAV]),
                class_="wrap",
            ),
            class_="site",
        ),
        t.main(t.div(views, class_="wrap"), lang="en"),
        t.footer(t.div("Built in Python", class_="wrap"), class_="site"),
        t.script(Raw(SCRIPT)),
    ])
    # Internal links point at tabs instead of separate pages
    for route, slug in SLUG.items():
        html = html.replace(f'href="{route}"', f'href="#{slug}"')
    out = Path(__file__).parent / "preview.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out.name)


if __name__ == "__main__":
    build()
