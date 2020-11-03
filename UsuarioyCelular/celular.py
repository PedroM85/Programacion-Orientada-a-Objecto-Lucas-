class Celular():
    def __init__(self, marca,modelo,proveedor, numero):
        self.__marca=marca
        self.__modelo=modelo
        self.__proveedor=proveedor
        self.__numero=numero

    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_proveedor(self):
        return self.__proveedor
    def get_numero(self):
        return self.__numero
    def set_marca(self, marca):
        self.__marca=marca
    def set_modelo(self,modelo):
        self.__modelo=modelo
    def set_proveedor(self,proveedor):
        self.__proveedor=proveedor
    def set_numero(self,numero):
        self.__numero=numero

    def mostrar_telefono(self):
        if self.get_marca().lower()=="apple":
            print(f'la marca es {self.get_marca()}, el modelo es: {self.get_modelo()}, el proveedor es {self.get_proveedor()}, el numero es: {self.get_numero()} y soy fan de Apple')
        else:
            print(f'la marca es {self.get_marca()}, el modelo es: {self.get_modelo()}, el proveedor es {self.get_proveedor()} y el numero es: {self.get_numero()} ')

