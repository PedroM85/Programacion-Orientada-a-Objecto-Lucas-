from colorama import Fore, init
init()

def menuPrincipal():
    print("\n\n******************************************************************************")
    print("       1   - Nuevo Usuario!               |         5   - Nueva Ciudad")
    print("       1.2 - Modificar Usuario            |         5.1 - Modificar Ciudad")       
    print("       2   - Nueva Marca                  |         6   - Nueva Compra")
    print("       2.1 - Modificar Marca              |         7   - Nuevo Mtd Pago")
    print("       3   - Nuevo Almacen                |         7.1 - Modificar Mtd Pago")
    print("       3.1 - Modificar Almacen            |         8   - Nuevo Producto")
    print("       4   - Nueva Categoria              |         8.1 - Modificar Producto")
    print("       4.1 - Modificar Categoria          |         0   - Salir")
    print("******************************************************************************")

def ingreso():
    print("\nIngrese una opción: ")

def opcionError():
    print(Fore.LIGHTRED_EX + "\nPor favor, seleccione una opción válida..." + Fore.RESET)

def ingresoError():
    print(Fore.LIGHTRED_EX + "\nPor favor, ingrese sólo números" + Fore.RESET)
