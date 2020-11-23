from dba import dba

class Ciudad():
    #def __init__ (self,provincia,localidad):
    def __init__ (self,provincia):
        self.id=25
        self.provincia=provincia
        #self.localidad=localidad
    
    def get_provincia(self):
        return self.provincia
    def set_provincia(self,provincia):
        self.provincia=provincia
    # def get_localidad(self):
    #     return self.localidad
    # def set_localidad(self,localidad):
    #     self.localidad=localidad
    def set_id(self,id_ciudad):
        self.id=id_ciudad
    def get_id(self):
        return self.id

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
        #self.set_tipo(dic['nombrecom'])
        sql='update tbl_ciudad set nombre=%s where id_ciudad=%s '
        val=(self.get_provincia(),self.get_id(),)
        print(val)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()


Ciudad1 = Ciudad("TUCUMAN")
Ciudad1.update()
