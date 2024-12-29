import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='avatar',
    database='db'
)
cursor = conn.cursor()

# Query for top-selling products by revenue
query_top_products_revenue = """
SELECT 
    ProductID, 
    SUM(TotalRetailPriceforThisOrder) AS TotalRevenue
FROM orders
GROUP BY ProductID
ORDER BY TotalRevenue DESC
LIMIT 10;
"""
cursor.execute(query_top_products_revenue)
top_products_revenue = cursor.fetchall()
print("Top-Selling Products by Revenue:")
for row in top_products_revenue:
    print(f"ProductID: {row[0]}, Total Revenue: ${row[1]:,.2f}")

# Close the connection
cursor.close()
conn.close()
