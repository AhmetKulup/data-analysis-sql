

import pandas as pd
import matplotlib.pyplot as plt

# Simulated sales data (same structure as in basic_analysis.py)
data = [
    {"date": "2024-01-01", "product": "Heater A", "category": "Industrial", "quantity": 3, "price": 1200},
    {"date": "2024-01-02", "product": "Heater B", "category": "Industrial", "quantity": 1, "price": 900},
    {"date": "2024-01-03", "product": "Heater A", "category": "Industrial", "quantity": 2, "price": 1200},
    {"date": "2024-01-04", "product": "Heater C", "category": "Home",       "quantity": 5, "price": 600},
    {"date": "2024-01-05", "product": "Heater C", "category": "Home",       "quantity": 3, "price": 600},
]

df = pd.DataFrame(data)
# Convert date and calculate revenue
df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["date"].dt.to_period("M").astype(str)

print("📊 Sales data used for visualization:")
print(df)

# 1) Monthly revenue line chart
monthly_revenue = df.groupby("month")["revenue"].sum()

plt.figure(figsize=(6, 4))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

# 2) Top products bar chart (by quantity)
product_quantity = df.groupby("product")["quantity"].sum().sort_values(ascending=False)

plt.figure(figsize=(6, 4))
product_quantity.plot(kind="bar")
plt.title("Top Selling Products (by Quantity)")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

# 3) Revenue by category bar chart
category_revenue = df.groupby("category")["revenue"].sum()

plt.figure(figsize=(6, 4))
category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.close()

print("\n✅ Charts generated:")
print("- monthly_revenue.png")
print("- top_products.png")
print("- revenue_by_category.png")
