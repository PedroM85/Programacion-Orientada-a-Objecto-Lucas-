from datetime import datetime
from coche import Coche
from cliente import Cliente
from agencia import Agencia

class Reserva():
    def __init__(self,fecha_inicio,Fecha_fin,Precio_alquiler,Litros,estado,agencia, cliente,coche):
        self.fecha_inicio = fecha_inicio
        self.Fecha_fin = Fecha_fin
        self.Precio_alquiler = Precio_alquiler
        self.Litros = Litros
        self.estado = estado
        self.precio_final = 0
        self.agencia = agencia
        self.cliente = cliente
        self.coche=coche

    def get_fecha_inicio(self):
        return self.fecha_inicio
    
    def get_Fecha_fin(self):
        return self.Fecha_fin
    
    def get_Agencia(self):
        return self.Agencia
    
    def get_cliente(self):
        return self.cliente
    
    def get_coche(self):
        return self.coche
    
    def get_litros(self):
        return self.Litros
    
    def get_dias_alquilados(self):
        return abs((self.Fecha_fin - self.fecha_inicio).days)
    
    def get_descuento_nafta(self):
        descuento = self.get_dias_alquilados()*5
        self.Litros = descuento
    



   

Agencia1= Agencia("Boas","asdasd")
cliente1 = Cliente(1231412314,"Antonio","Caba",12314124)
auto = Coche("123asda","Ford","Fiesta","plata")

    
Reserva1 = Reserva(datetime.strptime('2020-09-17', "%Y-%m-%d"), datetime.strptime('2020-09-20', "%Y-%m-%d"),"2000",30,True,Agencia1,cliente1,auto)

print(Reserva1.get_coche().get_marca())