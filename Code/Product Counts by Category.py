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


query_monthly_sales_trend = """
SELECT 
    YEAR(`Date Order was placed`) AS Year,
    MONTH(`Date Order was placed`) AS Month,
    SUM(TotalRetailPriceforThisOrder) AS TotalSales
FROM orders
GROUP BY Year, Month
ORDER BY Year, Month;
"""
cursor.execute(query_monthly_sales_trend)
monthly_sales_trend = cursor.fetchall()


cursor.close()
conn.close()


columns = ['Year', 'Month', 'Total Sales']
monthly_sales_df = pd.DataFrame(monthly_sales_trend, columns=columns)


monthly_sales_df['Date'] = pd.to_datetime(monthly_sales_df[['Year', 'Month']].assign(Day=1))
monthly_sales_df.sort_values('Date', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales_df['Date'], monthly_sales_df['Total Sales'], marker='o', color='green')
plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
