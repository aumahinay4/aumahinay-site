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
| `lessons.py`, `tutorials/` | The Python for Treasury Work lessons, and the code each one runs. |
| `highlight.py` | Colours the lesson code, using Python's own tokenizer. |
| `run_lessons.py` | Runs every lesson script and saves its printed output. |
| `tags.py` | Tiny helper that turns Python calls into HTML. |
| `app.py` | Runs the site locally with Flask. |
| `build.py` | Exports the site as static HTML into `dist/` for hosting. |

## How to edit your site on GitHub (no software needed)
1. Open https://github.com/aumahinay4/aumahinay-site and click **content.py**.
2. Click the pencil icon (**Edit this file**) at the top right of the file.
3. Change the words you want. Only edit the text inside the quotation marks `"like this"`,
   and leave the commas, brackets and quotation marks in place.
4. Click **Commit changes…**, then **Commit changes** again.
5. aumahinay.dev updates by itself in about a minute. If it doesn't, open the **Actions** tab:
   a red ✗ means something in the edit broke the file. Open the file's **History** to undo it,
   or ask Claude to fix it.

`content.py` holds all the text: About me, experience, education, ALTOS, courses, trainings and blog posts.
The Python tutorials live in `lessons.py` (the lesson text) and `tutorials/` (each lesson's scripts and data).

**To add a Python tutorial lesson:** make a folder under `tutorials/` with the lesson's scripts
and data files, run `python run_lessons.py` (it runs every script and saves its real output
as a `.out` file), then add the lesson to `LESSONS` in `lessons.py`. A lesson with
`publish_on` stays hidden until that date (Philippine time). `python run_lessons.py --check`
confirms the saved outputs still match the code.

## Run it on your computer
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows   (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
python app.py                   # open http://127.0.0.1:5000
```

## Publish (Cloudflare Pages)
Every push to `main` is published to aumahinay.dev by the GitHub Actions workflow in
`.github/workflows/deploy.yml`. After changing content, run `python build.py`, then
commit and push. Setup details are in **DEPLOY_CLOUDFLARE.md**.

## Adding a blog post
Open `content.py`, find `BLOG = []`, and add a post at the top of the list
(newest first), following the example in the comment just above it. Each post
needs a date, title, slug (short, lowercase, with hyphens), an optional
one-line summary, and its paragraphs. Then run `python build.py`, commit and push.

### Scheduling or hiding a post
Add `"publish_on": "2026-11-03"` to a post to keep it hidden until that date
(Philippine time). `"publish_on": None` keeps it hidden until a date is set.
The deploy workflow runs daily, so scheduled posts appear on their date once the
Cloudflare token is set up.
