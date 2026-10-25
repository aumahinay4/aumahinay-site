# aumahinay.dev — Portfolio of Ambrosio "Butch" U. Mahinay

A personal portfolio website written entirely in Python. There are no HTML template
or CSS files: pages are built with a small Python HTML helper (`tags.py`), and the
stylesheet lives in `style.py`.

## Files
| File | What it does |
|---|---|
| `content.py` | **All the text on the site.** Edit this to update projects, courses, About me. Search for `TODO` to find placeholders. |
| `pages.py` | Builds the Home, Projects, Courses and About pages. |
| `style.py` | Colours, fonts and layout (light and dark mode). |
| `tags.py` | Tiny helper that turns Python calls into HTML. |
| `app.py` | Runs the site locally with Flask. |
| `build.py` | Exports the site as static HTML into `dist/` for hosting. |

## Run it on your computer
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows   (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
python app.py                   # open http://127.0.0.1:5000
```

## Publish (Cloudflare Pages)
The site is served from `dist/` by Cloudflare Pages, which redeploys on every push to `main`.
After changing content, run `python build.py`, then commit and push. Setup details are in
**DEPLOY_CLOUDFLARE.md**.
