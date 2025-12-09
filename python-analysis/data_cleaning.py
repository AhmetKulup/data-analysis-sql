import pandas as pd

# Example raw data (in a real project this would come from a CSV or database)
data = [
    {"order_id": 1, "date": "2024-01-01", "product": "Heater A", "category": "Industrial", "quantity": 5, "price": 1200},
    {"order_id": 2, "date": "2024-01-02", "product": "Heater B", "category": "Industrial", "quantity": 2, "price": None},
    {"order_id": 3, "date": "2024-01-03", "product": "Heater A ", "category": "Industrial", "quantity": 1, "price": 1200},
    {"order_id": 4, "date": "2024-01-03", "product": "heater a", "category": "Industrial", "quantity": 3, "price": 1200},
]

df = pd.DataFrame(data)

print("🔹 Raw data:")
print(df)

# 1) Remove duplicates
df = df.drop_duplicates(subset=["order_id"])

# 2) Fix missing prices (use average price)
df["price"] = df["price"].fillna(df["price"].mean())

# 3) Standardize product names
df["product"] = df["product"].str.strip().str.lower()

# 4) Calculate total value
df["total_amount"] = df["quantity"] * df["price"]

print("\n✅ Cleaned data:")
print(df)

# KPI: Total revenue
total_revenue = df["total_amount"].sum()
print(f"\n💡 Total revenue in this sample: {total_revenue:.2f}")
