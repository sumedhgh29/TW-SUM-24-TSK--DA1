import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='avatar',
    database='db'
)
cursor = conn.cursor()

# Query for sales trends by month
query_monthly_sales_trend = """
SELECT 
    YEAR(`Date Order was placed`) AS Year,
    MONTH(`Date Order was placed`) AS Month,
    SUM(TotalRetailPriceforThisOrder) AS TotalSales
FROM orders
GROUP BY Year, Month
ORDER BY Year DESC, Month DESC;
"""
cursor.execute(query_monthly_sales_trend)
monthly_sales_trend = cursor.fetchall()
print("Monthly Sales Trend:")
for row in monthly_sales_trend:
    print(f"Total Sales: ${row[2]:,.2f}")

# Close the connection
cursor.close()
conn.close()
