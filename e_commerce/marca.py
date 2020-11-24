from dba import dba



class Marca():
    def __init__(self,nombre):
        self.id = id
        self.nombre=nombre

    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_id(self,id):
        self.id=id
    def get_id(self):
        return self.id

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
        #self.set_tipo(dic['nombrecom'])
        sql='update tbl_marca set nombre=%s where id_Marca=%s '
        val=(self.get_nombre(),self.get_id(),)
        print(val)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

# marca1 = Marca("")
# marca1.delete()