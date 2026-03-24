import pandas as pd

# Load data
df = pd.read_csv('../data/sales_data.csv')

# Data Cleaning
df.drop_duplicates(inplace=True)
df['date'] = pd.to_datetime(df['date'])

# Feature Engineering
df['revenue'] = df['quantity'] * df['price']

# KPIs
total_revenue = df['revenue'].sum()
top_product = df.groupby('product')['revenue'].sum().idxmax()
region_sales = df.groupby('region')['revenue'].sum()

print("Total Revenue:", total_revenue)
print("Top Product:", top_product)
print("\nSales by Region:\n", region_sales)

# Save processed data
df.to_csv('../data/processed_sales_data.csv', index=False)
