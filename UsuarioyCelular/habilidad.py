class Habilidad():
    def __init__(self,nombre,expertise):
        self.__nombre=nombre
        self.__expertise=expertise

    def get_nombre(self):
        return self.__nombre
    def get_expertise(self):
        return self.__expertise
    