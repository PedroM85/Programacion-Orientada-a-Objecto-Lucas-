from presentacion import menu
from usuario import Usuario
from validacion import validator
import getpass


def login():    
    formlogin={}
    formlogin['mail']=input("Escriba su mail: ")
    formlogin['password']=getpass.getpass("Escriba su password: ")


    if validator.validar_login(formlogin) is not False:
        user=Usuario(*validator.validar_login(formlogin))
        print("Hola " + user.get_nombrecom() + " un gusto tenerte de vuelta!")
        menu.menuPrincipal()
        menu.ingreso()
        menu.opcion(input())

        

    else:
        print("Usuario o contraseña incorrectos")
        

