from cliente import Cliente

class Pyme(Cliente):
    def __init__(self,razons,cuit,email,password,cuenta):
        Cliente().__init__(email,password)
        self.razons = razons
        self.cuit = cuit    
    
    def get_razons(self):
        return self.razons
    def set_razons(self,razons):
        self.razons = razons

    def get_cuit(self):
        return self.cuit
    def set_cuit(self,cuit):
        self.cuit = cuit

