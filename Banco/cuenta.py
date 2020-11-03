from abc import ABC, abstractmethod
from datetime import datetime

class Cuenta(ABC):
    def __init__(self, cbu):
        self.cbu = cbu
        self.balance = 0
        self.fecha_ult_movimiento = datetime.now()
    
    def get_cbu(self):
        return self.cbu
    def get_balance(self):
        return self.balance
    def get_fecha_ult_movimiento(self):
        return self.fecha_ult_movimiento
    def set_cbu(self,cbu):
        self.cbu = cbu
    def set_balance(self, balance):
        self.balance = balance
    def set_fecha_ult_movimiento(self,fecha_ult_movimiento):
        self.fecha_ult_movimiento = fecha_ult_movimiento        
    def acreditar(self,saldo):
        self.balance += saldo
        self.fecha_ult_movimiento = datetime.now()   
    def get_nombre(self):
        return self.__class__.__name__
    @abstractmethod
    def debitar(self):
        pass


