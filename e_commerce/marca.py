import re
from dba import dba

class Marcas():
    def __init__(self,id,nombre):
        self.__id = id
        self.nombre=nombre

    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id

    def save(self):
        sql="insert into tbl_marca(nombre) values(%s)"
        val=(self.get_nombre(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql='delete from tbl_marca where id_Marca=%s'
        val=(self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update(self):       
        sql='update tbl_marca set nombre=%s where id_Marca=%s '
        val=(self.get_nombre(),self.get_id())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        
    
    def select(self):
        sql='SELECT * from tbl_marca WHERE nombre=%s'
        val=(self.get_nombre(),)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        self.set_id(result[0])
        # print(result)
        # print(self.get_id())
        return result

#marca1 = Marca("")
# marca1.delete()
# marca1=Marca("Xiaomi")
# marca1.save()
# sql='SELECT * from tbl_marca WHERE nombre=%s'
# val=("hp",)
# dba.get_cursor().execute(sql,val)
# result=dba.get_cursor().fetchone()
# print(result)

#print(self.get_id())
