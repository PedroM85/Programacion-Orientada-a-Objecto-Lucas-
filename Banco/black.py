from cuenta import Cuenta

class Black(Cuenta):
    def __init__(self,cbu):
        Cuenta.__init__(self,cbu)
    
    def debitar(self,monto,lugar):
        self.balance -= monto
    
    def acreditar(self,monto):
        if monto < 100000:
            super(Black, self).acreditar(monto)
        else:
            monto = monto -(monto*0.04)
            super(Black, self).acreditar(monto)

