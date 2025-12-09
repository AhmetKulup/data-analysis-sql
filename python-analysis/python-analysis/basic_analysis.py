import pandas as pd

# Example dataset (simulated sales data)
data = [
    {"date": "2024-01-01", "product": "Heater A", "category": "Industrial", "quantity": 3, "price": 1200},
    {"date": "2024-01-02", "product": "Heater B", "category": "Industrial", "quantity": 1, "price": 900},
    {"date": "2024-01-03", "product": "Heater A", "category": "Industrial", "quantity": 2, "price": 1200},
    {"date": "2024-01-04", "product": "Heater C", "category": "Home", "quantity": 5, "price": 600},
    {"date": "2024-01-05", "product": "Heater C", "category": "Home", "quantity": 3, "price": 600},
]

df = pd.DataFrame(data)

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Create revenue column
df["revenue"] = df["quantity"] * df["price"]

print("📊 Raw Sales Data:")
print(df)

# 1) Monthly revenue summary
df["month"] = df["date"].dt.to_period("M")
monthly_revenue = df.groupby("month")["revenue"].sum()

print("\n💰 Monthly Revenue:")
print(monthly_revenue)

# 2) Top selling products
top_products = df.groupby("product")["quantity"].sum().sort_values(ascending=False)

print("\n🔥 Top Selling Products:")
print(top_products)

# 3) Revenue by category
category_revenue = df.groupby("category")["revenue"].sum()

print("\n🏷️ Revenue by Category:")
print(category_revenue)
