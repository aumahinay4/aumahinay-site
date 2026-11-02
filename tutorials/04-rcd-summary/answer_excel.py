"""Answer: save the summary tables to one Excel file, one sheet each.

Needs:  pip install pandas openpyxl
"""

import pandas as pd

collections = pd.read_csv("collections.csv")
deposits = pd.read_csv("deposits.csv")

receipts = collections.groupby("collector").agg(
    first_or=("or_number", "min"), last_or=("or_number", "max"),
    receipts=("or_number", "count"), amount=("amount", "sum"),
)
by_fund = collections.pivot_table(index="fund", columns="collector", values="amount",
                                  aggfunc="sum", fill_value=0, margins=True, margins_name="Total")
summary = collections.groupby("fund")["amount"].sum().to_frame("collected")
summary = summary.join(deposits.set_index("fund"))
summary["undeposited"] = (summary["collected"] - summary["deposited"]).round(2)

with pd.ExcelWriter("rcd_summary.xlsx") as excel:
    receipts.to_excel(excel, sheet_name="Receipts used")
    by_fund.to_excel(excel, sheet_name="By fund")
    summary.to_excel(excel, sheet_name="Deposits")

# Open the file again to confirm what was saved
print("Saved rcd_summary.xlsx with sheets:", pd.ExcelFile("rcd_summary.xlsx").sheet_names)
