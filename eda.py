import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load Cleaned Dataset
# -------------------------------
df = pd.read_csv("Cleaned_Nassau_Candy.csv")

print("Dataset Shape:", df.shape)

# -------------------------------
# Basic Statistics
# -------------------------------
print("\nSummary Statistics")
print(df.describe())

# -------------------------------
# Sales by Division
# -------------------------------
plt.figure(figsize=(8,5))

sales_division = df.groupby("Division")["Sales"].sum().sort_values()

sales_division.plot(kind="barh")

plt.title("Sales by Division")
plt.xlabel("Sales")
plt.ylabel("Division")
plt.tight_layout()

plt.savefig("sales_by_division.png")
plt.show()

# -------------------------------
# Profit by Division
# -------------------------------
plt.figure(figsize=(8,5))

profit_division = df.groupby("Division")["Gross Profit"].sum().sort_values()

profit_division.plot(kind="barh", color="green")

plt.title("Gross Profit by Division")
plt.xlabel("Gross Profit")
plt.ylabel("Division")
plt.tight_layout()

plt.savefig("profit_by_division.png")
plt.show()

# -------------------------------
# Top 10 Products by Sales
# -------------------------------
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))

top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("top10_products.png")
plt.show()

# -------------------------------
# Correlation Heatmap
# -------------------------------
plt.figure(figsize=(6,4))

sns.heatmap(
    df[["Sales","Cost","Gross Profit","Units"]].corr(),
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("correlation_heatmap.png")
plt.show()

print("\nEDA Completed Successfully!")