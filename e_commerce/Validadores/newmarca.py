from marca import Marca
from validacionm import validatormar

formarca={}
formarca['nombremar']=input('Nombre Marca: ')


if validatormar.validar_marca(formarca)=={}:
    marca=Marca(formarca['nombremar'])
    marca.save()
    print('Marca registrado exitosamente')
else:
    print(validatormar.validar_marca(formarca))

