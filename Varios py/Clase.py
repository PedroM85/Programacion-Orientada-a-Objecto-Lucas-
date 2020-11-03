class Perro():

    def __init__(self,nombre,edad,Duenio):
        self.Nombre=nombre
        self.edad=edad
        self.Duenio=Duenio

    def ladrar(self):
        print("Wau Wau Wau")

    def correr(self):
        print("anda libre")    


print("ingrese nombre, edad y dueño del perro")
Nombrep=input()
Anios=input()
dueño=input()

Scooby=Perro(Nombrep,Anios,dueño)

#Scooby=Perro("Scooby",2,"Francisco")


Scooby.ladrar()

print(F"mi perro {Scooby.Nombre} tiene {Scooby.edad} años y su dueño es {Scooby.Duenio}")