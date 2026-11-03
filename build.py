"""Export the site as static HTML into ./dist for free HTTPS hosting
(Cloudflare Pages, GitHub Pages, Netlify). Usage:  python build.py
Upload the dist folder itself; see DEPLOY_CLOUDFLARE.md.
"""

import shutil
from pathlib import Path

from content import SITE
from lessons import LESSONS
from pages import ROUTES, TUTORIALS, lesson_is_live, lesson_url, not_found

DIST = Path(__file__).parent / "dist"


def sitemap(site):
    """Every live page (scheduled posts and lessons appear on their date, with the nightly build)."""
    urls = "".join(f"  <url><loc>{site}{route}</loc></url>\n" for route in ROUTES)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")


def build():
    shutil.rmtree(DIST, ignore_errors=True)  # start clean so deleted pages don't linger
    for route, render in ROUTES.items():
        out = DIST / route.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(), encoding="utf-8")
        print("wrote", out.relative_to(DIST.parent))
    (DIST / "404.html").write_text(not_found(), encoding="utf-8")
    shutil.copytree(Path(__file__).parent / "static", DIST / "static", dirs_exist_ok=True)
    shutil.copy(DIST / "static" / "favicon.ico", DIST / "favicon.ico")  # browsers look for it at the root
    # each published lesson's scripts and data files, for the Download buttons
    for x in LESSONS:
        if lesson_is_live(x):
            for f in (TUTORIALS / x["folder"]).iterdir():
                if f.suffix in (".py", ".csv"):
                    shutil.copy(f, DIST / lesson_url(x).strip("/") / f.name)
    # the old IT News page now points to the tutorials (Cloudflare Pages reads this file)
    (DIST / "_redirects").write_text("/news/ /tutorials/ 301\n/news /tutorials/ 301\n")
    # help search engines find every page
    site = f"https://{SITE['domain']}"
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {site}/sitemap.xml\n")
    (DIST / "sitemap.xml").write_text(sitemap(site), encoding="utf-8")
    # GitHub Pages custom domain file
    (DIST / "CNAME").write_text(SITE["domain"] + "\n")


if __name__ == "__main__":
    build()
