# Publishing aumahinay.dev

The site is hosted for free on the Cloudflare Pages project **aumahinay**, which serves
aumahinay.dev. A GitHub Actions workflow (`.github/workflows/deploy.yml`) builds the
site and publishes `dist/` to that project on every push to `main`.

## How updates work
1. Change the Python files (`content.py` holds all the text).
2. Run `python build.py` to regenerate `dist/`, and commit both.
3. Push to `main`. The site updates within a minute or two
   (progress shows in the repository's **Actions** tab).

## One-time setup: the Cloudflare API token
The workflow needs one repository secret, `CLOUDFLARE_API_TOKEN`.

1. In Cloudflare, click the person icon (top right) → **Profile → API Tokens →
   Create Token → Custom token: Get started**.
2. Name it `GitHub deploy`. Under **Permissions** choose **Account**,
   **Cloudflare Pages**, **Edit**. Click **Continue to summary → Create Token**,
   then copy the token (it is shown only once).
3. In GitHub, open the repository → **Settings → Secrets and variables → Actions →
   New repository secret**. Name: `CLOUDFLARE_API_TOKEN`, Secret: paste the token.
   Click **Add secret**.
4. Open the **Actions** tab → **Deploy to Cloudflare Pages → Run workflow**.

Never paste the token anywhere else, including chats.

## Run it on your computer
```bash
pip install -r requirements.txt
python app.py        # open http://127.0.0.1:5000
```
