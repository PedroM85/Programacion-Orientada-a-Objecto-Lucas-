class Cliente():
    def __init__(self, DNI,Nombre,Direccion,Telefeno):
        self.DNI= DNI
        self.Nombre= Nombre
        self.Direccion=Direccion
        self.Telefono=Telefeno

    def get_DNI(self):
        return self.DNI
    
    def get_Nombre(self):
        return self.Nombre
    
    def get_Direccion(self):
        return self.Direccion
    
    def get_Telefono(self):
        return self.Telefono
    
    def set_DNI(self,DNI):
        self.DNI = DNI
    
    def set_Nombre(self,Nombre):
        self.Nombre = Nombre
    
    def set_Direccion(self, Direccion):
        self.Direccion = Direccion
    
    def  set_Telefono(self,Telefono):
        self.Telefono=Telefono