from marca import Marcas
from validacion import validator

def Marca():
    formarca={}
    formarca['nombremar']=input('Nombre Marca: ')


    if validator.validar_marca(formarca)=={}:
        marcas=Marcas(formarca['nombremar'])
        marcas.save()
        print('Marca registrado exitosamente')
    else:
        print(validator.validar_marca(formarca))


#Marca()
