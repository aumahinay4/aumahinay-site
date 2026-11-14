"""Turn the day's receipts into a formatted Excel report with openpyxl.

Needs:  pip install openpyxl
"""

import csv
from decimal import Decimal

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font

wb = Workbook()                  # a new, empty workbook with one sheet
ws = wb.active
ws.title = "Collections"

ws.append(["OR number", "Payor", "Nature of collection", "Fund", "Amount"])
for cell in ws[1]:
    cell.font = Font(bold=True)  # make the header row bold

with open("collections.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        ws.append([int(row["or_number"]), row["payor"], row["nature"], row["fund"], Decimal(row["amount"])])

last = ws.max_row                # the last row that has data
ws.append([None, None, None, "TOTAL", f"=SUM(E2:E{last})"])
ws.cell(row=last + 1, column=4).font = Font(bold=True)
ws.cell(row=last + 1, column=5).font = Font(bold=True)

for row in ws.iter_rows(min_row=2, min_col=5, max_col=5):
    row[0].number_format = "#,##0.00"   # thousands separator and two decimals

for column, width in zip("ABCDE", [12, 20, 26, 24, 14]):
    ws.column_dimensions[column].width = width
ws.freeze_panes = "A2"           # keep the header visible while scrolling

wb.save("daily_report.xlsx")

# Open the saved file again and show what is inside
check = load_workbook("daily_report.xlsx")["Collections"]
print(f"Saved daily_report.xlsx: {check.max_row} rows, {check.max_column} columns")
for row in check.iter_rows(min_row=1, max_row=3, values_only=True):
    print(row)
print("...")
print("Last row:", next(check.iter_rows(min_row=check.max_row, values_only=True)))
print("Amount format:", check["E2"].number_format)
