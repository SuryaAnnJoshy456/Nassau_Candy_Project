import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/Nassau Candy Distributor.csv")

# -------------------------
# Create KPIs
# -------------------------

# Gross Margin %
df["Gross Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100

# Profit Per Unit
df["Profit Per Unit"] = df["Gross Profit"] / df["Units"]

# Revenue Contribution
total_sales = df["Sales"].sum()
df["Revenue Contribution %"] = (df["Sales"] / total_sales) * 100

# Profit Contribution
total_profit = df["Gross Profit"].sum()
df["Profit Contribution %"] = (df["Gross Profit"] / total_profit) * 100

# -------------------------
# Product Summary
# -------------------------

product_summary = df.groupby("Product Name").agg({
    "Sales":"sum",
    "Gross Profit":"sum",
    "Cost":"sum",
    "Units":"sum",
    "Gross Margin %":"mean",
    "Profit Per Unit":"mean"
}).reset_index()

print("\nTop 10 Products by Profit\n")
print(product_summary.sort_values(
    by="Gross Profit",
    ascending=False
).head(10))

print("\nTop 10 Products by Margin\n")
print(product_summary.sort_values(
    by="Gross Margin %",
    ascending=False
).head(10))

# Save file
product_summary.to_csv("product_summary.csv", index=False)

print("\nProduct summary saved successfully!")
