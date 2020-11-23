class Producto():
    def __init__(self,nombre,modelo,descripcion,precio,categoria,almacen,marca):
        self.nombre=nombre
        self.modelo=modelo
        self.descripcion=descripcion
        self.precio=precio
        self.categoria=categoria
        self.almacen=almacen
        self.marca=marca
    
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