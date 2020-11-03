from abc import ABC, abstractmethod

class Articulo(ABC):
    def __init__(self,nombre,precio):
        self.nombre= nombre
        self.precio = precio
    
    @abstractmethod
    def get_nombre(self):
        pass
    def get_precio(Self):
        pass
    def set_nombre(self):
        pass
    def set_precio(self):
        pass

class ArticuloVajilla(Articulo):
    def __init__(self, nombre,precio,material):
        super().__init__(nombre,precio)
        self.material=material

    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return  self.precio
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_precio(self,precio):
        self.precio = precio
    def get_material(self):
        return self.material
    def set_material(self,material):
        self.material = material

class ArticuloJuguete(Articulo):
    def __init__(self, nombre, precio, edad):
        super().__init__(nombre, precio)
        self.edad =edad

    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return  self.precio
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_precio(self,precio):
        self.precio = precio
    def get_edad(self):
        return self.edad
    def set_edad(self,edad):
        self.edad = edad

class ArticuloJardin(Articulo):
    def __init__(self, nombre, precio, uso):
        super().__init__(nombre, precio)
        self.uso =uso

    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return  self.precio
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_precio(self,precio):
        self.precio = precio
    def get_uso(self):
        return self.uso
    def set_uso(self,uso):
        self.uso = uso

