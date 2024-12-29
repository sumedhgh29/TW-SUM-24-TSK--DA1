import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='avatar',
    database='db'
)
cursor = conn.cursor()

query_top_customers_purchases = """
SELECT 
    CustomerID, 
    COUNT(OrderID) AS TotalOrders
FROM orders
GROUP BY CustomerID
ORDER BY TotalOrders DESC
LIMIT 10;
"""
cursor.execute(query_top_customers_purchases)
top_customers_purchases = cursor.fetchall()
print("Top Customers by Number of Purchases:")
for row in top_customers_purchases:
    print(f"CustomerID: {row[0]}, Total Orders: {row[1]}")
    
cursor.close()
conn.close()
