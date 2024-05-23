import mysql.connector

config = {
   'user':'root',
   'password':'123Ho456HoinaR',
   'host':'localhost',
   'port':3306
}

try:
   conn = mysql.connector.connect(**config)
except Exception as obj:
   print('cant connect')
else:
   print('connected')