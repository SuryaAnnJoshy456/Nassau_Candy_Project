import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Nassau Candy Distributor.csv")

# Product-wise Sales
pareto = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

pareto_df = pareto.reset_index()
pareto_df.columns = ["Product Name", "Sales"]

# Cumulative %
pareto_df["Cumulative Sales"] = pareto_df["Sales"].cumsum()
pareto_df["Cumulative %"] = (
    pareto_df["Cumulative Sales"] / pareto_df["Sales"].sum()
) * 100

print(pareto_df)

# Save
pareto_df.to_csv("pareto_analysis.csv", index=False)

# Plot
plt.figure(figsize=(12,6))

plt.bar(pareto_df["Product Name"], pareto_df["Sales"])

plt.plot(
    pareto_df["Product Name"],
    pareto_df["Cumulative %"],
    color="red",
    marker="o"
)

plt.axhline(80, color="green", linestyle="--")

plt.xticks(rotation=90)
plt.ylabel("Sales / Cumulative %")
plt.title("Pareto Analysis (80/20 Rule)")
plt.tight_layout()

plt.savefig("pareto_chart.png")
plt.show()

print("\nPareto analysis completed successfully!")