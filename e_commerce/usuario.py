
class Usuario():
    def __init__(self, nombrecom, fechanac, sexo, telefono, email,cuidad):
    self.nombrecom=nombrecom
    self.fechanac=fechanac
    self.sexo=sexo
    self.telefono=telefono
    self.email=email
    self.cuidad=cuidad

    def get_nombrecom(self):
        return self.nombrecom
    def set_nombrecom(self, nombrecom):
        self.nombrecom=nombrecom
    def get_fechanac(self):
        return self.fechanac
    def set_fechanac(self, fechanac):
        self.fechanac=fechanac
    def get_sexo(self):
        return self.sexo
    def set_sexo(self, sexo):
        self.sexo=sexo
    def get_telefono(self):
        return self.telefono
    def set_telefono(self, telefono):
        self.telefono=telefono
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email=email
    def get_cuidad(self):
        return self.cuidad
    def set_cuidad(self, cuidad):
        self.cuidad=cuidad
    