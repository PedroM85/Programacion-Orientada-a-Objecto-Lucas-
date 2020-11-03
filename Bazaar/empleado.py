class Empleado():
    def __init__(self, nombre, apellido,dni,sueldo,comision):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.sueldo = sueldo
        self.comision = comision

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido
        
    def set_apellido(self, apellido):
        self.apellido = apellido
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        self.dni = dni

    def get_sueldo(self):
        return self.sueldo
    
    def set_sueldo(self, sueldo):
        self.sueldo = sueldo

    def get_comision(self):
        return self.comision
    
    def set_comision(self, comision):
        self.comision = comision

    def get_caja(self):
        return self.caja
    
    def vender(self,articulos):
        resultado=0
        for articulo in articulos:
            resultado += articulo.get_precio()*0.10
        self.comision += resultado
                
class EmpleadoMostrador(Empleado):
    def __init__(self,nombre, apellido,dni,sueldo,comision,caja):
        Empleado.__init__(self,nombre,apellido,dni,sueldo,comision)
        self.caja=caja
    
    def cobrar(self, dinero):
        self.caja+= dinero

class EmpleadoCoordinador(Empleado):
    def __init__(self,nombre, apellido,dni,sueldo,comision):
        Empleado.__init__(self,nombre,apellido,dni,sueldo,comision)
    
    def Coordinar(self):
        # print("Estoy coordinando")
        return ("Estoy Coordinando")

class EmpleadoRepositor(Empleado):
    def __init__(self,nombre, apellido,dni,sueldo,comision):
        Empleado.__init__(self,nombre,apellido,dni,sueldo,comision)
    
    def AbrirDeposito(self):
        print("Abriendo Deposito")


# Empleado2 = EmpleadoRepositor("asdas","asdasd",5424,3000,0)

# Empleado3 = EmpleadoCoordinador("asdas","asdasd",5424,3000,0)

# Empleado1 = EmpleadoMostrador("asd","asdm",234234,30000,0,0)

# Empleado1.cobrar(499)

# print(Empleado1.get_caja())
# Empleado2.AbrirDeposito()
# print(Empleado3.Coordinar())
