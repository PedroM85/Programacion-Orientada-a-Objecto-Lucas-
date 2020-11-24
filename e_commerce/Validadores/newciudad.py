from ciudad import Ciudad
from validacionciu import validatorciu

formciu={}
formciu['nombreal']=input('Nombre de la Ciudad: ')


if validatorciu.validar_ciu(formciu)=={}:
    Ciudad=Ciudad(formciu['nombreal'])
    Ciudad.save()
    print('Ciudad registrado exitosamente')
else:
    print(validatorciu.validar_ciu(formciu))


