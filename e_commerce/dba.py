import mysql.connector

dbconfig={
  "host":"localhost",
  "user":"root",
  "password":"",
  "database":"e_commerce"
}

class db():
  def __init__(self):
    self.conexion=mysql.connector.connect(**dbconfig)
    self.cursor=self.conexion.cursor()
    self.commit=self.conexion.commit()

  def get_cursor(self):
    return self.cursor
  def get_commit(self):
    return self.commit
  def get_conexion(self):
    return self.conexion
      
dba=db()

