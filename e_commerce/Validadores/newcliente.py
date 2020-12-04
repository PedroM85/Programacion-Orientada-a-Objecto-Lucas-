from cliente import Cliente
from validacion import validator


def cliente():
    formcliente={}
    formcliente['dni']=input('Ingrese su DNI: ')
    formcliente['nombrecom']=input('Ingrese su nombre completo: ')
    formcliente['fechanac']=input('Ingrese su fecha de Nacimiento AAAA-MM-DD: ')
    formcliente['sexo']=input('Ingrese su sexo F o M: ')
    formcliente['telefono']=input('Ingrese su telefono: ')
    formcliente['email']=input('Ingrese su email: ')
    print("-"*35)
    validator.listar_ciudad()
    print("-"*35)
    formcliente['ciudad']=input('Ingrese el numero de la ciudad: ')
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
