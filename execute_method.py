import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='123Ho456HoinaR',
        host='localhost',
        port=3306
    )
    if conn.is_connected():
        print('Connected')
except:
    print('Unable to connect')

cur = conn.cursor()
cur.execute('CREATE DATABASE Shree')
cur.close()
conn.close()