import mysql.connector

try:
    conn = mysql.connector.connect(
        user = 'root',
        password = '123Ho456HoinaR',
        host = 'localhost',
        port = 3306
    )
    if conn.is_connected():
        print('Connected')

except Exception as obj:
    print('Unable to Connect')

conn.close()

#1000 line of code below
#we have to close before executing 1000 line of code to free memory uses and avoid unexpeted changes in db