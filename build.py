"""Export the site as static HTML into ./dist for free HTTPS hosting
(Cloudflare Pages, GitHub Pages, Netlify). Usage:  python build.py
Upload the dist folder itself; see DEPLOY_CLOUDFLARE.md.
"""

import shutil
from pathlib import Path

from content import SITE
from lessons import LESSONS
from datetime import datetime
from email.utils import format_datetime
from html import escape

from pages import ROUTES, live_notes, TUTORIALS, lesson_is_live, lesson_url, live_posts, not_found, post_teaser, post_url, PH, TUTORIAL

DIST = Path(__file__).parent / "dist"


def sitemap(site):
    """Every live page (scheduled posts and lessons appear on their date, with the nightly build)."""
    # Study Notes stays out of the sitemap until its first note is live (no empty hub pages for AdSense)
    urls = "".join(f"  <url><loc>{site}{route}</loc></url>\n" for route in ROUTES
                   if route != "/study-notes/" or live_notes())
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")


# Lesson 0 has no publish date; the Tutorials page went live on this day.
FIRST_LESSON_DATE = "2026-11-02"


def feed_items():
    """Every live blog post and lesson, newest first, as (date, title, url, summary)."""
    items = []
    for p in live_posts():
        day = p.get("publish_on") or datetime.strptime(p["date"], "%B %d, %Y").date().isoformat()
        items.append((day, p["title"], post_url(p), p.get("summary") or post_teaser(p)))
    for x in LESSONS:
        if lesson_is_live(x):
            items.append((x.get("publish_on") or FIRST_LESSON_DATE, f"Lesson {x['number']}: {x['title']}",
                          lesson_url(x), x["summary"]))
    return sorted(items, key=lambda i: i[0], reverse=True)


def feed(site):
    """RSS news feed of new posts and lessons, for reading apps and follow-by-email services."""
    def when(day):
        fmt = "%Y-%m-%d %H:%M" if len(day) > 10 else "%Y-%m-%d"  # posts may go live at a set time
        return format_datetime(datetime.strptime(day, fmt).replace(tzinfo=PH))
    items = feed_items()
    rows = "".join(
        f"    <item>\n      <title>{escape(title)}</title>\n      <link>{site}{url}</link>\n"
        f"      <guid isPermaLink=\"true\">{site}{url}</guid>\n      <pubDate>{when(day)}</pubDate>\n"
        f"      <description>{escape(summary)}</description>\n    </item>\n"
        for day, title, url, summary in items)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n  <channel>\n'
            f"    <title>{escape(SITE['short_name'])}</title>\n    <link>{site}/</link>\n"
            f'    <atom:link href="{site}/feed.xml" rel="self" type="application/rss+xml"/>\n'
            f"    <description>New blog posts and {escape(TUTORIAL['title'])} lessons by {escape(SITE['short_name'])}</description>\n"
            "    <language>en</language>\n"
            + (f"    <lastBuildDate>{when(items[0][0])}</lastBuildDate>\n" if items else "")
            + rows + "  </channel>\n</rss>\n")


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
    (DIST / "_redirects").write_text("/news/ /tutorials/ 301\n/news /tutorials/ 301\n/courses/ /study-notes/ 301\n/courses /study-notes/ 301\n")
    # help search engines find every page
    site = f"https://{SITE['domain']}"
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {site}/sitemap.xml\n")
    if SITE.get("adsense_client"):  # ads.txt names Google as the site's only authorised ad seller
        pub = SITE["adsense_client"].removeprefix("ca-")
        (DIST / "ads.txt").write_text(f"google.com, {pub}, DIRECT, f08c47fec0942fa0\n")
    (DIST / "sitemap.xml").write_text(sitemap(site), encoding="utf-8")
    (DIST / "feed.xml").write_text(feed(site), encoding="utf-8")
    # GitHub Pages custom domain file
    (DIST / "CNAME").write_text(SITE["domain"] + "\n")


if __name__ == "__main__":
    build()
