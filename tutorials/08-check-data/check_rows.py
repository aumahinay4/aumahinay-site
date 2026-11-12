"""Check every row of a collections file before adding it up, and list each problem found."""

import csv
from datetime import date
from decimal import Decimal, InvalidOperation

FUNDS = {"General Fund", "Special Education Fund", "Trust Fund"}


def check(row: dict) -> list:
    """Return a list of problems in one row. An empty list means the row is good."""
    problems = []

    number = row["or_number"].strip()
    if not (number.isdigit() and len(number) == 7):
        problems.append(f"OR number {number!r} must be 7 digits")

    try:
        date.fromisoformat(row["date"])
    except ValueError:
        problems.append(f"date {row['date']!r} is not a real date (YYYY-MM-DD)")

    if not row["payor"].strip():
        problems.append("payor is blank")

    if row["fund"] not in FUNDS:
        problems.append(f"fund {row['fund']!r} is not one of {sorted(FUNDS)}")

    try:
        amount = Decimal(row["amount"])
    except InvalidOperation:
        problems.append(f"amount {row['amount']!r} is not a number (no commas)")
    else:  # runs only when the amount was read without error
        if amount <= 0:
            problems.append(f"amount {amount} must be more than zero")
        elif amount != amount.quantize(Decimal("0.01")):
            problems.append(f"amount {amount} has more than two decimal places")

    return problems


good, bad = [], []
with open("collections.csv", newline="", encoding="utf-8") as f:
    for line, row in enumerate(csv.DictReader(f), start=2):   # line 1 is the header
        problems = check(row)
        if problems:
            bad.append((line, problems))
        else:
            good.append(row)

for line, problems in bad:
    print(f"Line {line}:")
    for problem in problems:
        print(f"  - {problem}")

total = sum(Decimal(row["amount"]) for row in good)
print(f"\n{len(good)} rows passed, {len(bad)} need fixing.")
print(f"Total of the rows that passed: {total:,.2f}")
print("Fix the file and run the check again before preparing the report.")
