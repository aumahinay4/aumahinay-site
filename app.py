"""Run the portfolio locally:  python app.py  then open http://127.0.0.1:5000"""

from flask import Flask, abort, jsonify, send_from_directory

from lessons import LESSONS
from pages import MANIFEST, ROUTES, TUTORIALS, lesson_is_live

app = Flask(__name__)


@app.route("/tutorials/<slug>/<name>")
def lesson_file(slug, name):
    """The Download buttons on a lesson page."""
    for x in LESSONS:
        if x["slug"] == slug and lesson_is_live(x) and not name.endswith(".out"):
            return send_from_directory(TUTORIALS / x["folder"], name, as_attachment=True)
    abort(404)


@app.route("/manifest.webmanifest")
def manifest():
    """Home-screen app settings."""
    response = jsonify(MANIFEST)
    response.mimetype = "application/manifest+json"
    return response


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def page(path):
    key = "/" + path.strip("/") + "/" if path.strip("/") else "/"
    if key not in ROUTES:
        abort(404)
    return ROUTES[key]()


if __name__ == "__main__":
    app.run(debug=True)
