"""Add up one day's collections from a CSV file, per fund and in total."""

import csv
from decimal import Decimal

totals = {}            # fund name -> running total
grand_total = Decimal("0")
receipts = 0

with open("collections.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        amount = Decimal(row["amount"])          # exact peso amount, never float
        fund = row["fund"]
        totals[fund] = totals.get(fund, Decimal("0")) + amount
        grand_total += amount
        receipts += 1

print(f"Collections for the day: {receipts} official receipts")
print("-" * 44)
for fund, total in sorted(totals.items()):
    print(f"{fund:<28}{total:>16,.2f}")
print("-" * 44)
print(f"{'TOTAL':<28}{grand_total:>16,.2f}")
