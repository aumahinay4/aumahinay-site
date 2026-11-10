"""Send new sitemap pages to IndexNow after a deploy (run by .github/workflows/deploy.yml).

New pages = in dist/sitemap.xml but not in live-sitemap.xml (the sitemap that was live before
publishing). A manual run (EVENT=workflow_dispatch) sends every page."""
import json, os, re, sys, time, urllib.request
from pathlib import Path
from build import INDEXNOW_KEY
from content import SITE


def locs(path):
    p = Path(path)
    return re.findall(r"<loc>(.*?)</loc>", p.read_text(encoding="utf-8")) if p.exists() else []


def main():
    host = SITE["domain"]
    new = locs("dist/sitemap.xml")
    old = set(locs("live-sitemap.xml"))
    if os.environ.get("EVENT") != "workflow_dispatch":
        if not old:
            print("No earlier sitemap to compare with; nothing sent.")
            return
        new = [u for u in new if u not in old]
    if not new:
        print("No new pages for IndexNow.")
        return
    key_url = f"https://{host}/{INDEXNOW_KEY}.txt"
    for _ in range(10):  # wait until the key file is live on Cloudflare
        try:
            if urllib.request.urlopen(key_url, timeout=20).read().decode().strip() == INDEXNOW_KEY:
                break
        except Exception:
            pass
        time.sleep(30)
    body = json.dumps({"host": host, "key": INDEXNOW_KEY, "keyLocation": key_url, "urlList": new}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow: HTTP {r.status} for {len(new)} page(s):", *new, sep="\n  ")


if __name__ == "__main__":
    sys.exit(main())
