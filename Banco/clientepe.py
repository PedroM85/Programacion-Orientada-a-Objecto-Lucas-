from cliente import Cliente

class Persona(Cliente):
    def __init__(self,nombre,apellido,dni,email,password,cuenta):
        super().__init__(email,password,cuenta)
        self.nombre = nombre
        self.apellido = apellido
        self.dni =dni
        
    def get_nombre(self):
        return self.nombre    
    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido        
    def set_apellido(self,apellido):
        self.apellido = apellido

    def get_dni(self):
        return self.dni
    def set_dni(self,dni):
        self.dni = dni

    def cobrar_servicios(self):
        if self.cuenta.get_cuenta() == "Classic":
            resultado=self.cuenta.get_balance()-100
            self.cuenta.set_balance(resultado)
        elif self.cuenta.get_cuenta() == "Gold":
            resultado=self.cuenta.get_balance()-len(self.get_apellido())*10
            self.cuenta.set_balance(resultado)
        elif self.cuenta.get_cuenta() == "Platinium":
            resultado=self.cuenta.get_balance()-(self.cuenta.get_balance()*0.10)
            self.cuenta.set_balance(resultado)
        else:
            resultado=self.cuenta.get_balance()-500-100*self.cuenta.get_fecha_ult_movimiento().weekday()
            self.cuenta.set_balance(resultado)
        



