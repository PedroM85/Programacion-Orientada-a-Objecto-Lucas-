from colorama import Fore, init
init()

def menuPrincipal():
    print("\n\n************************************************************************")
    print("       1. Tirar dados!")
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

def resultados(dado1, dado2):
    sumaDados = int(dado1) + int(dado2)
    print("\n\n************************************************************************")
    print("\n       Resultados:\n\n       Dado 1: ", dado1, "\n       Dado 2: ", dado2, "\n       La sumatoria total es: ", sumaDados )