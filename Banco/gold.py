from cuenta import Cuenta

class Gold(Cuenta):
    def __init__(self,cbu):
        Cuenta.__init__(self,cbu)
    
    def debitar(self,monto,lugar):
        if lugar.upper()=="LINK":
            self.balance -= monto +(monto*0.05)
        else:
            self.balance -= monto
     
    def acreditar(self,monto):
        if monto > 25000:
            super(Gold, self).acreditar(monto)
        else:
            monto = monto -(monto*0.03)
            super(Gold, self).acreditar(monto)
        
        
# Cuenta1 = Gold(123124)

# # print(Cuenta1.get_fecha_ult_movimiento())

# Cuenta1.acreditar(26000)
# print("Plata acredita")
# print(Cuenta1.get_balance())

# Cuenta1.debitar(800, "link")
# print(Cuenta1.get_balance())