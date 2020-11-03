from cliente import Cliente

class Multinacional(Cliente):
    def __init__(self,razonS,cuit,nombre,email,contraseña,cuenta):
        Cliente.__init__(email,contraseña)
        self.razonS = razonS
        self.cuit = cuit

    def get_razons(self):
        return self.razons
    def set_razons(self,razons):
        self.razons = razons

    def get_cuit(self):
        return self.cuit
    def set_cuit(self,cuit):
        self.cuit = cuit
