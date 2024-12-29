import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='avatar',
    database='db'
)

### Visualization 1: Top-Selling Products by Quantity ###
query_top_products = """
SELECT ProductID, SUM(QuantityOrdered) AS TotalQuantity
FROM orders
GROUP BY ProductID
ORDER BY TotalQuantity DESC
LIMIT 10;
"""
top_products_df = pd.read_sql(query_top_products, conn)

plt.figure(figsize=(8, 5))
plt.bar(top_products_df['ProductID'].astype(str), top_products_df['TotalQuantity'], color='skyblue')
plt.title('Top-Selling Products by Quantity')
plt.xlabel('Product ID')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Visualization 2: Top-Selling Products by Revenue ###
query_top_revenue_products = """
SELECT ProductID, SUM(QuantityOrdered * TotalRetailPriceforThisOrder) AS TotalRevenue
FROM orders
GROUP BY ProductID
ORDER BY TotalRevenue DESC
LIMIT 10;
"""
top_revenue_df = pd.read_sql(query_top_revenue_products, conn)

plt.figure(figsize=(8, 5))
plt.bar(top_revenue_df['ProductID'].astype(str), top_revenue_df['TotalRevenue'], color='orange')
plt.title('Top-Selling Products by Revenue')
plt.xlabel('Product ID')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Visualization 3: Monthly Sales Trends ###
query_monthly_sales = """
SELECT 
    YEAR(`Date Order was placed`) AS Year,
    MONTH(`Date Order was placed`) AS Month,
    SUM(TotalRetailPriceforThisOrder) AS TotalSales
FROM orders
GROUP BY Year, Month
ORDER BY Year, Month;
"""
monthly_sales_df = pd.read_sql(query_monthly_sales, conn)
monthly_sales_df['Date'] = pd.to_datetime(monthly_sales_df[['Year', 'Month']].assign(Day=1))

plt.figure(figsize=(10, 6))
plt.plot(monthly_sales_df['Date'], monthly_sales_df['TotalSales'], marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

### Visualization 4: Product Counts by Category ###
query_product_counts = """
SELECT `Product Category`, COUNT(*) AS ProductCount
FROM products
GROUP BY `Product Category`
ORDER BY ProductCount DESC;
"""
product_counts_df = pd.read_sql(query_product_counts, conn)

plt.figure(figsize=(8, 5))
plt.bar(product_counts_df['Product Category'], product_counts_df['ProductCount'], color='purple')
plt.title('Product Counts by Category')
plt.xlabel('Product Category')
plt.ylabel('Count of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Visualization 5: Top Customers by Total Purchases ###
query_top_customers = """
SELECT CustomerID, SUM(TotalRetailPriceforThisOrder) AS TotalPurchase
FROM orders
GROUP BY CustomerID
ORDER BY TotalPurchase DESC
LIMIT 10;
"""
top_customers_df = pd.read_sql(query_top_customers, conn)

plt.figure(figsize=(8, 5))
plt.bar(top_customers_df['CustomerID'].astype(str), top_customers_df['TotalPurchase'], color='red')
plt.title('Top Customers by Total Purchases')
plt.xlabel('Customer ID')
plt.ylabel('Total Purchase Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Close the database connection
conn.close()
