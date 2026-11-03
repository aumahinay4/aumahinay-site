"""A simple Report of Collections and Deposits (RCD) summary with pandas."""

import pandas as pd

pd.set_option("display.float_format", "{:,.2f}".format)

collections = pd.read_csv("collections.csv")
deposits = pd.read_csv("deposits.csv")

# A. Receipts used by each collector
receipts = collections.groupby("collector").agg(
    first_or=("or_number", "min"),
    last_or=("or_number", "max"),
    receipts=("or_number", "count"),
    amount=("amount", "sum"),
)
print("A. Official receipts used")
print(receipts, end="\n\n")

# B. Collections per fund, one column per collector
by_fund = collections.pivot_table(
    index="fund", columns="collector", values="amount",
    aggfunc="sum", fill_value=0, margins=True, margins_name="Total",
)
print("B. Collections by fund")
print(by_fund, end="\n\n")

# C. Deposits against collections
summary = collections.groupby("fund")["amount"].sum().to_frame("collected")
summary = summary.join(deposits.set_index("fund"))
summary["undeposited"] = (summary["collected"] - summary["deposited"]).round(2)
print("C. Collections and deposits")
print(summary)
