import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "e_commerce"
)

cursos = mydb.cursor()

cursos.execute("select * from tbl_methpago")

#print(cursos.fetchall())

for i in cursos.fetchall():
    print(i)