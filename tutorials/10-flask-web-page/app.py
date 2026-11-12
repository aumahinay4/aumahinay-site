"""A small web page that shows the day's collections, made with Flask.

Needs:  pip install flask
Run:    py app.py   (Mac: python3 app.py), then open http://127.0.0.1:5000 in a browser
"""

import csv
from decimal import Decimal

from flask import Flask, abort, render_template_string

app = Flask(__name__)

PAGE = """<!doctype html>
<title>Collections for {{ day }}</title>
<h1>Collections for {{ day }}</h1>
<table border="1" cellpadding="6">
  <tr><th>Fund</th><th>Amount</th></tr>
  {% for fund, total in totals %}
  <tr><td>{{ fund }}</td><td align="right">{{ "{:,.2f}".format(total) }}</td></tr>
  {% endfor %}
  <tr><th>TOTAL</th><th align="right">{{ "{:,.2f}".format(grand_total) }}</th></tr>
</table>
<p>{{ count }} official receipts. Open /receipt/7650101 to see one receipt.</p>
"""

RECEIPT = """<!doctype html>
<title>OR {{ r.or_number }}</title>
<h1>Official receipt {{ r.or_number }}</h1>
<p>{{ r.date }} · {{ r.payor }} · {{ r.nature }} · {{ r.fund }} · {{ r.amount }}</p>
<p><a href="/">Back to the totals</a></p>
"""


def load_receipts():
    with open("collections.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@app.route("/")
def totals_page():
    rows = load_receipts()
    totals = {}
    for row in rows:
        totals[row["fund"]] = totals.get(row["fund"], Decimal("0")) + Decimal(row["amount"])
    return render_template_string(
        PAGE, day=rows[0]["date"], totals=sorted(totals.items()),
        grand_total=sum(totals.values()), count=len(rows))


@app.route("/receipt/<int:or_number>")
def receipt_page(or_number):
    for row in load_receipts():
        if int(row["or_number"]) == or_number:
            return render_template_string(RECEIPT, r=row)
    abort(404)               # no such receipt: the browser gets "404 Not Found"


if __name__ == "__main__":
    app.run()                # only on your own computer; see the note on safety
