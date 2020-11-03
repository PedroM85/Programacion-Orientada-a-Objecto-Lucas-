from cuenta import Cuenta

class Classic(Cuenta):
    def __init__(self,cbu):
        Cuenta.__init__(self,cbu)
    
    def debitar(self,monto,lugar):
        if lugar.upper()=="BANELCO":
            self.balance -= monto +(monto*0.05)
        elif lugar.upper()=="LINK":
            self.balance -= monto +(monto*0.10)
        else:
            self.balance -= monto
    
    def acreditar(self,monto):
        monto = monto -(monto*0.05)
        super(Classic, self).acreditar(monto)
        
    
    def comision(self):
        pass




# Cuenta1 = Classic(123124)

# print(Cuenta1.get_fecha_ult_movimiento())

# Cuenta1.acreditar(5000)
# print("Plata acredita")
# print(Cuenta1.get_balance())

# Cuenta1.debitar(800, "link")
# print(Cuenta1.get_balance())
# print(Cuenta1.get_cbu())