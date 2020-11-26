from ciudad import Ciudad
from validacion import validator

def ciudads():
    formciu={}
    formciu['nombreal']=input('Nombre de la Ciudad: ')


    if validator.validar_ciu(formciu)=={}:
        Ciudad1=Ciudad(formciu['nombreal'])
        Ciudad1.save()
        print('Ciudad registrado exitosamente')
    else:
        print(validator.validar_ciu(formciu))


