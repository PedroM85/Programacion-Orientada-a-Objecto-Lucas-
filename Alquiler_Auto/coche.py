class Coche():
    def __init__(self,matricula,marca,modelo,color):
        self.matricula=matricula
        self.modelo=modelo
        self.marca=marca
        self.color=color

    def get_matricula(self):
        return self.matricula
    
    def get_modelo(self):
        return self.modelo

    def get_marca(self):
        return self.marca

    def get_color(self):
        return self.color

    def set_matricula(self,matricula):
        self.matricula = matricula
    
    def set_modelo(self,modelo):
        self.modelo=modelo
    
    def set_marca(self,marca):
        self.marca = marca

    def set_color(self,color):
        self.color = color