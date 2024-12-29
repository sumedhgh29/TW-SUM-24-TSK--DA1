import mysql.connector
conn = mysql.connector.connect(host='localhost', password='avatar', user='root', database='db')
if conn.is_connected():
    print("Connection successful")
    conn.close()
else:
    print("Connection failed")
