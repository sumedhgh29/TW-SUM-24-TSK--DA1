import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='avatar',
    database='db'
)
cursor = conn.cursor()

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

cursor.close()
conn.close()

columns = ['Product ID', 'Total Quantity Sold']
top_products_df = pd.DataFrame(top_products_quantity, columns=columns)

plt.figure(figsize=(10, 6))
plt.bar(top_products_df['Product ID'].astype(str), top_products_df['Total Quantity Sold'], color='orange')
plt.title('Top-Selling Products by Quantity', fontsize=14)
plt.xlabel('Product ID', fontsize=12)
plt.ylabel('Total Quantity Sold', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
