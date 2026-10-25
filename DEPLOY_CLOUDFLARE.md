# Publishing aumahinay.dev with Cloudflare Pages

The site is hosted for free on Cloudflare Pages and deploys automatically from this
GitHub repository. The finished pages are kept in the `dist/` folder, so
Cloudflare doesn't need to run any build step.

## How updates work
1. Change the Python files (`content.py` holds all the text).
2. Run `python build.py`. It regenerates `dist/`.
3. Commit and push to `main`. Cloudflare publishes the new version within a minute or two.

## One-time setup: connect Cloudflare to GitHub
A project created by uploading a zip can't be switched to GitHub, so this creates a
new project and moves the domain over to it.

1. In the Cloudflare dashboard, open **Workers & Pages → Create application**.
2. Choose **Pages → Connect to Git**, sign in to GitHub, and pick
   **aumahinay4/aumahinay-site**.
3. Use these settings:
   - Project name: `aumahinay-site`
   - Production branch: `main`
   - Framework preset: **None**
   - Build command: *(leave empty)*
   - Build output directory: `dist`
4. Click **Save and Deploy**. Check the site at `aumahinay-site.pages.dev`.
5. Move the domain: in the old **aumahinay** project, open **Custom domains** and
   remove `aumahinay.dev` and `www.aumahinay.dev`. Then in **aumahinay-site → Custom
   domains**, add both again. They turn **Active** within a few minutes.
6. Once https://aumahinay.dev shows the site, you can delete the old **aumahinay**
   project (Settings → Delete project).

## Run it on your computer
```bash
pip install -r requirements.txt
python app.py        # open http://127.0.0.1:5000
```
