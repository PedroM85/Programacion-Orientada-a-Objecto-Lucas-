import base64
class Usuario():
    def __init__(self, nombre, mail, password,celular):
        self.nombre = nombre
        self.mail = mail
        self.password = self.encriptar_pass(password)
        self.celular=celular
        self.habilidades=[]

    def saludar(self):
        print(f"Hola {self.nombre}")
    
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_mail(self):
        return self.mail
    def set_mail(self,mail):
        self.mail = mail
    def get_password(self):
        return self.desencriptar_pass(self.password)
    def set_password(self, password):
        self.password =  self.encriptar_pass(password)
    def encriptar_pass(self, password):
        return base64.encodebytes(bytes(password, 'utf-8'))
    def desencriptar_pass(self, password):
        return base64.decodebytes(password).decode("UTF-8")
    def get_celular(self):
        return self.celular
    def set_celular(self,celular):
        self.celular=celular
    def get_habilidades(self):
        return self.habilidades

    def llamar(self,usuario,tiempo):
        if self.get_celular().get_proveedor()== usuario.get_celular().get_proveedor():
            return 0
        else:
            return tiempo*10

    def agregar_habilidad(self,habilidad):
        if len(self.get_habilidades())<3:
            self.get_habilidades().append(habilidad)

    def sabeHacer(self,habilidad,puntaje):
        for i in self.get_habilidades():
            if i.get_nombre()==habilidad.lower() and i.get_expertise()>puntaje:
                return True
            else:
                return False