from dba import dba

class Compra():
    def __init__(self, usuario,producto,methpago,cantidad,subtotal):
        self.__id = id
        self.usuario=usuario
        self.producto=producto
        self.methpago=methpago
        self.cantidad=cantidad
        self.subtotal=subtotal
    
    def get_usuario(self):
        return self.usuario
    def set_usuario(self,usuario):
        self.usuario=usuario
    def get_producto(self):
        return self.producto
    def set_producto(self,producto):
        self.producto=producto
    def get_methpago(self):
        return self.methpago
    def set_methpago(self,methpago):
        self.methpago=methpago
    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self,cantidad):
        self.cantidad=cantidad
    def get_subtotal(self):
        return self.subtotal
    def set_subtotal(self,subtotal):
        self.subtotal=subtotal
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return id
    
    def save(self):
        sql="insert into tbl_compra(id_user,id_producto,id_methpago,cantidad,subtotal) values(%s,%s,%s,%s,%s)"
        val=(self.get_usuario(),self.get_producto(),self.get_methpago(),self.get_cantidad(),self.get_subtotal())
        dba.get_cursor().execute(sql,val)        
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql='delete from tbl_compra where id=%s'
        val=(self.id(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update(self):     
        sql='update tbl_compra set id_user=%s,id_producto=%s, id_methpago=%s, cantidad=%s, subtotal=%s where id_compra=%s '
        val=(self.get_usuario(),self.get_producto(),self.get_methpago(),self.get_cantidad(),self.get_subtotal(),self.get_id())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

