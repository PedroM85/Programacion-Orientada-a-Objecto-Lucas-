from dba import dba

class MethPago():
    def __init__(self,id,tipo):
        self.__id = id
        self.tipo=tipo

    def get_tipo(self):
        return self.tipo
    def set_tipo(self,tipo):
        self.nombre=tipo
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id

    def save(self):
        sql="insert into tbl_methpago(tipo) values(%s)"
        val=(self.get_tipo(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql='delete from tbl_methpago where id_methpago=%s'
        val=(self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update(self):
        #self.set_tipo(dic['nombrecom'])
        sql='update tbl_methpago set tipo=%s where id_methpago=%s '
        val=(self.get_tipo(),self.get_id(),)
        print(val)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    def select(self):
        sql='SELECT * from tbl_methpago WHERE tipo=%s'
        val=(self.get_tipo(),)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        self.set_id(result[0])
        return result

# methpago1 = MethPago("Sony")
# methpago1.delete()