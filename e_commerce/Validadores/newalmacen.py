from almacen import Almacen
from validacional import validatoral

formalma={}
formalma['nombreal']=input('Nombre de Almacen: ')


if validatoral.validar_almace(formalma)=={}:
    Almacen=Almacen(formalma['nombreal'])
    Almacen.save()
    print('Almacen registrado exitosamente')
else:
    print(validatoral.validar_almace(formalma))


