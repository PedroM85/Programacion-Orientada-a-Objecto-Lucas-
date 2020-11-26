from almacen import Almacenes
from validacion import validator

def Almacen():

    formalma={}
    formalma['nombreal']=input('Nombre de Almacen: ')


    if validator.validar_almace(formalma)=={}:
        Almacen=Almacenes(formalma['nombreal'])
        Almacen.save()
        print('Almacen registrado exitosamente')
    else:
        print(validator.validar_almace(formalma))


