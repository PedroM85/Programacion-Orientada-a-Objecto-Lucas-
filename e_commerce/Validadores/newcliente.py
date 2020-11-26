from cliente import Cliente
from validacion import validator


def cliente():
    formcliente={}
    formcliente['dni']=input('Ingrese DNI: ')
    formcliente['nombrecom']=input('Nombre completo: ')
    formcliente['fechanac']=input('Fecha de Nacimiento AAAA-MM-DD: ')
    formcliente['sexo']=input('Sexo F o M: ')
    formcliente['telefono']=input('Telefono: ')
    formcliente['email']=input('Email: ')
    formcliente['ciudad']=input('Ciudad: ')
    formcliente['edit']="0"
    



    if validator.validar_cliente(formcliente)=={}:
        user=Cliente(formcliente['dni'],formcliente['nombrecom'],formcliente['fechanac'],formcliente['sexo'],formcliente['telefono'],formcliente['email'],formcliente['ciudad'])
        user.save()
        print('Cliente registrado exitosamente')
    else:
        print(validator.validar_cliente(formcliente))

def cliente_edit():
    formcliente={}
    formcliente['nombrecom']=input('Nombre completo: ')
    formcliente['fechanac']=input('Fecha de Nacimiento AAAA-MM-DD: ')
    formcliente['sexo']=input('Sexo F o M: ')
    formcliente['telefono']=input('Telefono: ')
    formcliente['email']=input('Email: ')
    formcliente['ciudad']=input('Ciudad: ')    



    if validator.validar_cliente(formcliente)=={}:
        user=Cliente(formcliente['nombrecom'],formcliente['fechanac'],formcliente['sexo'],formcliente['telefono'],formcliente['email'],formcliente['ciudad'])
        user.update()
        print('Cliente registrado exitosamente')
    else:
        print(validator.validar_cliente(formcliente))


#user = Usuario("Pedro Maneiro","1985-09-10","M",1121651051,"pedromaneiro@gmail.com", 1 , "pedro1985")
#print(user.get_ciudad)
#user.save()s
#print(user)
