import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='avatar',
    database='db'
)
cursor = conn.cursor()

query_top_customers_spending = """
SELECT 
    CustomerID, 
    SUM(TotalRetailPriceforThisOrder) AS TotalSpent
FROM orders
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT 10;
"""
cursor.execute(query_top_customers_spending)
top_customers_spending = cursor.fetchall()
print("Top Customers by Total Spending:")
for row in top_customers_spending:
    print(f"CustomerID: {row[0]}, Total Spent: ${row[1]:,.2f}")

cursor.close()
conn.close()
