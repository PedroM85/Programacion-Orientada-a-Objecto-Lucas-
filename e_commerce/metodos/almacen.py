from dba import dba

class Almacen():
    def __init__(self,tipo):
        self.id=4
        self.tipo=tipo

    def get_tipo(self):
        return self.tipo
    def set_tipo(self,tipo):
        self.tipo=tipo
    def set_id(self,id_almacen):
        self.id=id_almacen
    def get_id(self):
        return self.id

    def save(self):
        sql="insert into tbl_almacen(tipo) values(%s)"
        val=(self.get_tipo(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql='delete from tbl_almacen where id_Almacen=%s'
        val=(self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update(self):
        #self.set_tipo(dic['nombrecom'])
        sql='update tbl_almacen set tipo=%s where id_Almacen=%s '
        val=(self.get_tipo(),self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    # def buscarexistencia(self,tipo):
    #     sql = "select id_almacen from tbl_almacen where tipo=%s"
    #     val = (self.get_tipo(),)
    #     dba.get_cursor().execute(sql,val)
    #     id_almacen = dba.get_cursor().fetchone()
    #     self.set_id(id_almacen[0])
    




almacen1 = Almacen("Deposito 18")
almacen1.delete()