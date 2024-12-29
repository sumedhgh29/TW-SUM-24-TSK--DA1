
import mysql.connector

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
print("Top-Selling Products by Quantity:")
for row in top_products_quantity:
    print(f"ProductID: {row[0]}, Total Quantity Sold: {row[1]}")

# Close the connection
cursor.close()
conn.close()
