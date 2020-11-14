from dba import dba

class Almacen():
    def __init__(self,tipo):
        self.id=0
        self.tipo=tipo

    def get_tipo(self):
        return self.tipo
    def set_tipo(self,tipo):
        self.tipo=tipo
    def set_id(self,id):
        self.id=id
    def get_id(self):
        return self.id

    def save(self):
        sql="insert into tbl_almacen(tipo) values(%s)"
        val=(self.get_tipo(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

# almacen1 = Almacen("Vitrina")
# print(almacen1.get_id())
# almacen1.save()
# print(almacen1.get_id())