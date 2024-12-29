import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='avatar',
    database='db'
)
cursor = conn.cursor()

# Query to fetch product details
query_product_details = """
SELECT 
    `Product ID`, `Product Name`, `Product Line`, `Product Category`
FROM products;
"""
cursor.execute(query_product_details)
product_details = cursor.fetchall()
print("Product Details:")
for row in product_details:
    print(f"Product ID: {row[0]}, Name: {row[1]}, Line: {row[2]}, Category: {row[3]}")

# Close the connection
cursor.close()
conn.close()
