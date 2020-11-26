from dba import dba

class Categoria():
    def __init__(self,id,tipo):
        self.id=id
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
        sql="insert into tbl_categoria(tipo) values(%s)"
        val=(self.get_tipo(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql='delete from tbl_categoria where id_Categoria=%s'
        val=(self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update(self):
        #self.set_tipo(dic['nombrecom'])
        sql='update tbl_categoria set tipo=%s where id_Categoria=%s '
        val=(self.get_tipo(),self.get_id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def select(self):
        sql='SELECT * from tbl_categoria WHERE tipo=%s'
        val=(self.get_tipo(),)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        self.set_id(result[0])
        return result
    

# Categoria1 = Categoria("Pasta1")
# Categoria1.delete()