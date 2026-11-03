"""Answer: how many receipts are still unused in the booklet."""

import csv

BOOKLET_FIRST = 7650101
BOOKLET_LAST = 7650150

with open("receipts.csv", newline="", encoding="utf-8") as f:
    numbers = [int(row["or_number"]) for row in csv.DictReader(f)]

inside = [n for n in numbers if BOOKLET_FIRST <= n <= BOOKLET_LAST]
last_used = max(inside)
unused = BOOKLET_LAST - last_used          # numbers after the last one used

print(f"Last receipt used:  {last_used}")
print(f"Unused receipts:    {unused} ({last_used + 1} to {BOOKLET_LAST})")
