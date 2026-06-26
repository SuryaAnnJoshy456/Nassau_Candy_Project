import pandas as pd

# Load dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date columns
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    dayfirst=True,
    errors="coerce"
)
# Remove rows with invalid dates
df = df.dropna(subset=["Order Date", "Ship Date"])

# Save cleaned data
df.to_csv("Cleaned_Nassau_Candy.csv", index=False)

print("\n Data cleaned successfully!")