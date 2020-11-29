
from dba import dba

class Producto():
    def __init__(self,id,nombre,modelo,descripcion,precio,categoria,almacen,marca):
        self.__id=id
        self.nombre=nombre
        self.modelo=modelo
        self.descripcion=descripcion
        self.precio=precio
        self.categoria=categoria
        self.almacen=almacen
        self.marca=marca
    
    def get_id(self):
        return  self.__id
    def set_id(self,id):
        self.__id=id
    def get_nombre(self):
        return  self.nombre
    def set_nombre(self,nombre):
        self.nombre=nombre
    def get_modelo(self):
        return  self.modelo
    def set_modelo(self,modelo):
        self.modelo=modelo
    def get_descripcion(self):
        return  self.descripcion
    def set_descripcion(self,descripcion):
        self.descripcion=descripcion
    def get_precio(self):
        return  self.precio
    def set_precio(self,precio):
        self.precio=precio
    def get_categoria(self):
        return  self.categoria
    def set_categoria(self,categoria):
        self.categoria=categoria
    def get_almacen(self):
        return  self.almacen
    def set_almacen(self,almacen):
        self.almacen=almacen
    def get_marca(self):
        return  self.marca
    def set_marca(self,marca):
        self.marca=marca

    def save(self):
        sql="insert into tbl_producto(nombre,modelo,descripcion,precio,idCategoria,idAlmacen,idMarca) values(%s,%s,%s,%s,%s,%s,%s)"
        val=(self.get_nombre(),self.get_modelo(),self.get_descripcion(),self.get_precio(),self.get_categoria(),self.get_almacen(),self.get_marca())
        dba.get_cursor().execute(sql,val)        
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
    
    def update(self):
        sql="update tbl_producto set nombre=%s,modelo=%s,descripcion=%s,precio=%s,idcategoria=%s,idalmacen=%s,idmarca=%s where id_producto=%s "
        val=(self.get_nombre(),self.get_modelo(),self.get_descripcion(),self.get_precio(),self.get_categoria(),self.get_almacen(),self.get_marca(),self.get_id())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        
    
    def select(self):
        sql='SELECT * from tbl_producto WHERE nombre=%s and modelo=%s'
        val=(self.get_nombre(),self.get_modelo())
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        self.set_id(result[0])
        return result
    
    def delete(self):
        sql='UPDATE tbl_producto SET activo=%s WHERE id_Producto=%s '
        val=("1",self.get_id())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()