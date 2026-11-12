"""Answer: add a /api/totals address that returns the totals as JSON for other programs.

The route is added to the same app from app.py, then visited with the test client.
"""

from decimal import Decimal

from app import app, load_receipts


@app.route("/api/totals")
def totals_json():
    totals = {}
    for row in load_receipts():
        totals[row["fund"]] = totals.get(row["fund"], Decimal("0")) + Decimal(row["amount"])
    # JSON has no Decimal type, so send each amount as text with two decimals
    return {fund: f"{total:.2f}" for fund, total in sorted(totals.items())}


response = app.test_client().get("/api/totals")
print(response.status, response.content_type)
print(response.get_data(as_text=True))
