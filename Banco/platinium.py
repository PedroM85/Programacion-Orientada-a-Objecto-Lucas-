from cuenta import Cuenta

class Platinium(Cuenta):
    def __init__(self,cbu):
        Cuenta.__init__(self,cbu)
    
    def debitar(self,monto,lugar):
        if self.balance < 5000:
            self.balance -= monto +(monto*0.05)
        else:
            self.balance -= monto

    def acreditar(self, monto):
        super(Classic, self).acreditar(monto)

