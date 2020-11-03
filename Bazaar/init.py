from articulo import ArticuloVajilla, ArticuloJuguete, ArticuloJardin
from empleado import Empleado, EmpleadoCoordinador, EmpleadoMostrador, EmpleadoRepositor
from bazaar import bazaar

bazaar = bazaar()

Empleado1 = EmpleadoMostrador("federico","Paredes","99884",30000,0,10000)
Empleado2 = EmpleadoRepositor("jose","martinez","212333",20000,8000)
Articulo1 = ArticuloVajilla("asdasd",200,"acero")
Articulo2 = ArticuloJuguete("asdasd",800,12)
Articulo3 = ArticuloJardin("asfasf",1500,True)
articulos=[Articulo1,Articulo2,Articulo3]

bazaar.agregar_empleado(Empleado1)
bazaar.agregar_empleado(Empleado2)
# print(bazaar.liquidar_sueldo())

print(Empleado1.get_comision())
Empleado1.vender(articulos)
print(Empleado1.get_comision())



