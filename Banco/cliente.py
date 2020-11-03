from abc import ABC, abstractmethod

class Cliente(ABC):
   
    def __init__(self,email,password, cuenta):
        self.email = email
        self.password = password
        self.cuenta = cuenta

    def get_email(self):
        return self.email
    def set_email(self,email):
        self.email = email

    def get_cuenta(self):
        return self.cuenta
    def set_cuenta(self, cuenta):
        self.cuenta = cuenta


    def get_password(self):
        return self.password
    def set_password(self,password):
        self.password = password


