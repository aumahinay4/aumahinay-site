"""Answer: also flag rows whose date is not the date of the report being prepared."""

import csv
from datetime import date

REPORT_DATE = date(2026, 11, 3)

with open("collections.csv", newline="", encoding="utf-8") as f:
    for line, row in enumerate(csv.DictReader(f), start=2):
        try:
            day = date.fromisoformat(row["date"])
        except ValueError:
            print(f"Line {line}: date {row['date']!r} is not a real date")
            continue                     # skip to the next row
        if day != REPORT_DATE:
            print(f"Line {line}: dated {day}, but this report is for {REPORT_DATE}")

print("Date check done.")
