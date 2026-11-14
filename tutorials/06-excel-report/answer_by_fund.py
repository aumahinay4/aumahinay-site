"""Answer: add a "By fund" sheet that totals daily_report.xlsx with SUMIF formulas.

Run make_report.py first; this opens the file it saved.
"""

from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook("daily_report.xlsx")
data = wb["Collections"]
last = data.max_row - 1          # the row above TOTAL

funds = sorted({data.cell(row=r, column=4).value for r in range(2, last + 1)})

ws = wb.create_sheet("By fund")
ws.append(["Fund", "Amount"])
for cell in ws[1]:
    cell.font = Font(bold=True)
for fund in funds:
    ws.append([fund, f"=SUMIF(Collections!D2:D{last},A{ws.max_row + 1},Collections!E2:E{last})"])
ws.append(["TOTAL", f"=SUM(B2:B{ws.max_row})"])
for row in ws.iter_rows(min_row=2, min_col=2, max_col=2):
    row[0].number_format = "#,##0.00"
ws.column_dimensions["A"].width = 24
ws.column_dimensions["B"].width = 14

wb.save("daily_report.xlsx")
print("Sheets:", wb.sheetnames)
for row in ws.iter_rows(values_only=True):
    print(row)
