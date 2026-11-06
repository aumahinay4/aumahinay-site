"""Answer: totals per fund AND per nature of collection, in one pass over the file."""

import csv
from decimal import Decimal

by_fund = {}
by_nature = {}          # the second dictionary

with open("collections.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        amount = Decimal(row["amount"])
        by_fund[row["fund"]] = by_fund.get(row["fund"], Decimal("0")) + amount
        by_nature[row["nature"]] = by_nature.get(row["nature"], Decimal("0")) + amount

print("By fund")
for fund, total in sorted(by_fund.items()):
    print(f"  {fund:<30}{total:>12,.2f}")

print("\nBy nature of collection")
for nature, total in sorted(by_nature.items()):
    print(f"  {nature:<30}{total:>12,.2f}")
print(f"  {'TOTAL':<30}{sum(by_nature.values()):>12,.2f}")
