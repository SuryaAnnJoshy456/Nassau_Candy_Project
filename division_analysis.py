import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Nassau Candy Distributor.csv")

# KPIs
df["Gross Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100

# Division Summary
division = df.groupby("Division").agg({
    "Sales": "sum",
    "Gross Profit": "sum",
    "Cost": "sum",
    "Gross Margin %": "mean"
}).reset_index()

print("\nDivision Performance\n")
print(division)

# Save summary
division.to_csv("division_summary.csv", index=False)

# -----------------------------
# Revenue by Division
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(division["Division"], division["Sales"])
plt.title("Revenue by Division")
plt.xlabel("Division")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("division_sales.png")
plt.show()

# -----------------------------
# Profit by Division
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(division["Division"], division["Gross Profit"])
plt.title("Profit by Division")
plt.xlabel("Division")
plt.ylabel("Gross Profit")
plt.tight_layout()
plt.savefig("division_profit.png")
plt.show()

# -----------------------------
# Margin by Division
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(division["Division"], division["Gross Margin %"])
plt.title("Average Gross Margin (%)")
plt.xlabel("Division")
plt.ylabel("Margin %")
plt.tight_layout()
plt.savefig("division_margin.png")
plt.show()

print("\nDivision analysis completed successfully!")