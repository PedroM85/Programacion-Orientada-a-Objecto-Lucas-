class Agencia():
    def __init__(self,Nombre,Direccion):
        self.Nombre = Nombre
        self.Direccion = Direccion

    
    def get_Nombre(self):
        return self.Nombre
    
    def get_Direccion(self):
        return self.Direccion
    
    def set_Nombre(self, Nombre):
        self.Nombre = Nombre
    
    def set_Direccion(self, Direccion):
        self.Direccion = Direccion