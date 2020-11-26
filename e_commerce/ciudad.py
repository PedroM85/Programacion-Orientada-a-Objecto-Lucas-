from dba import dba

class Ciudad():
    def __init__ (self,id,provincia):
        self.__id=id
        self.provincia=provincia
       
    
    def get_provincia(self):
        return self.provincia
    def set_provincia(self,provincia):
        self.provincia=provincia
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id

    def save(self):
        sql="insert into tbl_ciudad(nombre) values(%s)"
        val=(self.get_provincia(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql='delete from tbl_ciudad where id_ciudad=%s'
        val=(self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update(self):
        sql='update tbl_ciudad set nombre=%s where id_ciudad=%s '
        val=(self.get_provincia(),self.get_id(),)
        print(val)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def select(self):
        sql='SELECT * from tbl_ciudad WHERE nombre=%s'
        val=(self.get_provincia(),)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        self.set_id(result[0])
        return result