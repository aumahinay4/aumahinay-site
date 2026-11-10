"""Check the official receipts used today against the booklet issued to the collector."""

import csv
from collections import Counter

BOOKLET_FIRST = 7650101      # Accountable Form No. 51, one booklet of 50 receipts
BOOKLET_LAST = 7650150

with open("receipts.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

numbers = [int(row["or_number"]) for row in rows]
cancelled = [int(row["or_number"]) for row in rows if row["status"] == "Cancelled"]

# 1. Numbers that appear more than once
counts = Counter(numbers)
duplicates = sorted(n for n, times in counts.items() if times > 1)

# 2. Numbers that do not belong to the booklet
outside = sorted(n for n in set(numbers) if not BOOKLET_FIRST <= n <= BOOKLET_LAST)

# 3. Gaps: every number from the first to the last one used should be accounted for
inside = {n for n in numbers if BOOKLET_FIRST <= n <= BOOKLET_LAST}
expected = set(range(min(inside), max(inside) + 1))
gaps = sorted(expected - inside)

print(f"Receipts recorded: {len(numbers)}")
print(f"Series used:       {min(inside)} to {max(inside)}")
print(f"Cancelled:         {cancelled or 'none'}")
print(f"Duplicates:        {duplicates or 'none'}")
print(f"Outside booklet:   {outside or 'none'}")
print(f"Missing numbers:   {gaps or 'none'}")

if duplicates or outside or gaps:
    print("\nStatus: NOT BALANCED. Explain each item above before preparing the report.")
else:
    print("\nStatus: series is complete.")
