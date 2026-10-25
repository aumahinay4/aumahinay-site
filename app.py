"""Run the portfolio locally:  python app.py  then open http://127.0.0.1:5000"""

from flask import Flask, abort

from pages import ROUTES

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def page(path):
    key = "/" + path.strip("/") + "/" if path.strip("/") else "/"
    if key not in ROUTES:
        abort(404)
    return ROUTES[key]()


if __name__ == "__main__":
    app.run(debug=True)
