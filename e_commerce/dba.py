import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="e_commerce"
)

mycursor = mydb.cursor()

