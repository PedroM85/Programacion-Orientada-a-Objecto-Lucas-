from colorama import Fore, init
init()

def menuPrincipal():
    print("\n\n************************************************************************")
    print("       1. Nuevo Usuario!")
    print("       2. Resultados")
    print("       3. Créditos")
    print("       4. Salir")
    print("************************************************************************")

def ingreso():
    print("\ningrese la opción: ")

def opcionError():
    print(Fore.LIGHTRED_EX + "\nPor favor, seleccione una opción válida..." + Fore.RESET)

def ingresoError():
    print(Fore.LIGHTRED_EX + "\nPor favor, ingrese sólo números" + Fore.RESET)
