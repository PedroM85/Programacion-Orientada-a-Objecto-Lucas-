from presentacion import menu
from usuario import Usuario
from validacion import validator
from colorama import Fore

import getpass

debug = 0


def login():
    salir = False
    while (salir != True):

        formlogin={}
        if debug == 1:
            formlogin['mail']="admin@admin.com"
            formlogin['password']="pedro123"
        else:
            formlogin['mail']=input("Escriba su mail: ")
            formlogin['password']=getpass.getpass("Escriba su password: ")
        
        if validator.validar_login(formlogin) is not False:
            user=Usuario(*validator.validar_login(formlogin))
            print("Hola " + Fore.GREEN + user.get_nombrecom() + Fore.RESET + " un gusto tenerte de vuelta!" )
            menu.menuPrincipal()
            menu.ingreso()
            username= user.get_nombrecom()
            valor=int(input())
            if not isinstance(valor,int):
                print("solo ingrese numero")
            if int(valor) >= 0 and  int(valor) <= 3:                
                menu.opcion(valor,username)
                salir = True
            else:
                print("La opción ingresada no es valida: "+str(valor))
                print("Solo ingrese numero del 0 al 3")
                print("\n")

        else:
            print(Fore.RED +"           Usuario o contraseña incorrectos"+ Fore.RESET)
            salir = False



