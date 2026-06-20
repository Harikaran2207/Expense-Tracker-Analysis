import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("expense.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create additional columns
df["Month"] = df["Date"].dt.month_name()
df["Day"] = df["Date"].dt.day_name()

# -------------------------
# BASIC SUMMARY
# -------------------------
print("\n========== EXPENSE ANALYSIS REPORT ==========\n")

total_spending = df["Amount"].sum()
average_expense = df["Amount"].mean()
max_expense = df["Amount"].max()
min_expense = df["Amount"].min()

print(f"Total Spending      : ₹{total_spending:.2f}")
print(f"Average Expense     : ₹{average_expense:.2f}")
print(f"Highest Expense     : ₹{max_expense:.2f}")
print(f"Lowest Expense      : ₹{min_expense:.2f}")

# -------------------------
# CATEGORY ANALYSIS
# -------------------------
category_spend = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n----- Spending by Category -----")
print(category_spend)

top_category = category_spend.idxmax()

print(
    f"\nMost Money Spent On: {top_category}"
)

# -------------------------
# PAYMENT MODE ANALYSIS
# -------------------------
mode_spend = (
    df.groupby("Mode")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n----- Payment Mode Analysis -----")
print(mode_spend)

# -------------------------
# DAILY TREND
# -------------------------
daily_spend = (
    df.groupby("Date")["Amount"]
    .sum()
)

# -------------------------
# WEEKDAY ANALYSIS
# -------------------------
weekday_spend = (
    df.groupby("Day")["Amount"]
    .sum()
)

print("\n----- Spending by Day -----")
print(weekday_spend)

# -------------------------
# TOP 5 EXPENSIVE TRANSACTIONS
# -------------------------
print("\n----- Top 5 Transactions -----")

top_transactions = (
    df.sort_values(
        by="Amount",
        ascending=False
    )
    .head(5)
)

print(top_transactions)

# -------------------------
# GRAPH 1
# -------------------------
plt.figure(figsize=(8, 5))

category_spend.plot(
    kind="bar"
)

plt.title(
    "Total Spending by Category"
)

plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.tight_layout()

plt.savefig(
    "category_spending.png"
)

plt.show()

# -------------------------
# GRAPH 2
# -------------------------
plt.figure(figsize=(7, 7))

category_spend.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title(
    "Expense Distribution"
)

plt.ylabel("")

plt.tight_layout()

plt.savefig(
    "expense_distribution.png"
)

plt.show()

# -------------------------
# GRAPH 3
# -------------------------
plt.figure(figsize=(10, 5))

daily_spend.plot(
    marker="o"
)

plt.title(
    "Daily Spending Trend"
)

plt.xlabel("Date")
plt.ylabel("Amount (₹)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "daily_spending_trend.png"
)

plt.show()

# -------------------------
# FINAL INSIGHTS
# -------------------------
print("\n========== INSIGHTS ==========")

print(
    f"• Total money spent: ₹{total_spending:.2f}"
)

print(
    f"• Highest spending category: {top_category}"
)

print(
    f"• Average transaction value: ₹{average_expense:.2f}"
)

print(
    f"• Number of transactions: {len(df)}"
)

print(
    "\nGraphs saved successfully."
)

print(
    "\n========== END OF REPORT =========="
)
