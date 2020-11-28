from re import U
from presentacion import menu
from usuario import Usuario
from validacion import validator
from colorama import Fore

import getpass


def login():
    formlogin={}
    formlogin['mail']=input("Escriba su mail: ")
    formlogin['password']=getpass.getpass("Escriba su password: ")
    
    if validator.validar_login(formlogin) is not False:
        user=Usuario(*validator.validar_login(formlogin))
        print("Hola " + Fore.GREEN + user.get_nombrecom() + Fore.RESET + " un gusto tenerte de vuelta!" )
        menu.menuPrincipal()
        menu.ingreso()
        menu.opcion(input())

    else:
        print(Fore.RED +"           Usuario o contraseña incorrectos"+ Fore.RESET)


        exit_now = input("\n Do you like to exit now (Y)es (N)o ? ")


