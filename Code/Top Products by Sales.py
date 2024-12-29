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
cursor = conn.cursor()

# Query for top-selling products by quantity
query_top_products_quantity = """
SELECT 
    ProductID, 
    SUM(QuantityOrdered) AS TotalQuantitySold
FROM orders
GROUP BY ProductID
ORDER BY TotalQuantitySold DESC
LIMIT 10;
"""
cursor.execute(query_top_products_quantity)
top_products_quantity = cursor.fetchall()

# Close the connection
cursor.close()
conn.close()

# Convert results to a DataFrame
columns = ['Product ID', 'Total Quantity Sold']
top_products_df = pd.DataFrame(top_products_quantity, columns=columns)

# Visualization: Top-selling products by quantity
plt.figure(figsize=(10, 6))
plt.bar(top_products_df['Product ID'].astype(str), top_products_df['Total Quantity Sold'], color='orange')
plt.title('Top-Selling Products by Quantity', fontsize=14)
plt.xlabel('Product ID', fontsize=12)
plt.ylabel('Total Quantity Sold', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
