"""Export the site as static HTML into ./dist for free HTTPS hosting
(Cloudflare Pages, GitHub Pages, Netlify). Usage:  python build.py
Upload the dist folder itself; see DEPLOY_CLOUDFLARE.md.
"""

import shutil
from pathlib import Path

from content import SITE
from pages import ROUTES, not_found

DIST = Path(__file__).parent / "dist"


def build():
    shutil.rmtree(DIST, ignore_errors=True)  # start clean so deleted pages don't linger
    for route, render in ROUTES.items():
        out = DIST / route.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(), encoding="utf-8")
        print("wrote", out.relative_to(DIST.parent))
    (DIST / "404.html").write_text(not_found(), encoding="utf-8")
    shutil.copytree(Path(__file__).parent / "static", DIST / "static", dirs_exist_ok=True)
    # GitHub Pages custom domain file
    (DIST / "CNAME").write_text(SITE["domain"] + "\n")


if __name__ == "__main__":
    build()
