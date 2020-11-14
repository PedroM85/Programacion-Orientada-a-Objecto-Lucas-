from usuario import Usuario
from celular import Celular
from habilidad import Habilidad

cel1=Celular("Apple","Redmi","Claro","123456798")
user1 = Usuario("Jesus","asdadasd","Pedro1985,",cel1)
habilidad1=Habilidad("comer",10)
habilidad2=Habilidad("correr",5)
habilidad3=Habilidad("saltar",7)
cel2=Celular("Xiaomi","Redmi 9","Claro","1234654452")
user2 = Usuario("Marco","asdadasffasdsd","pedro1985",cel2)


user1.agregar_habilidad(habilidad1)
user1.agregar_habilidad(habilidad2)
user1.agregar_habilidad(habilidad3)

print(user1.get_password())
print(user1.encriptar_pass(user1.get_password()))