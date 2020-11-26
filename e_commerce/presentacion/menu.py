from Validadores import newcliente
from Validadores import newmarca
from Validadores import newalmacen
from Validadores import newcategoria
from Validadores import newciudad
from Validadores import newcompra
from Validadores import newmtdpago
from Validadores import newproducto
from Validadores import newuser
from Validadores import edit
from colorama import Fore, init
from os import system

init()

def menuPrincipal():
    print("\n\n******************************************************************************")
    print("             1.- Agregar")
    print("             2.- Modificar")
    print("             3.- Eliminar")
    print("             0.- Salir")
    print("******************************************************************************")

def menuAgregar():
    print("\n\n******************************************************************************")
    print("             1.- Nuevo Cliente               |         6.- Nueva Compra")
    print("             2.- Nueva Marca                 |         7.- Nueva Mtd Pago")
    print("             3.- Nuevo Almacen               |         8.- Nuevo Producto")
    print("             4.- Nueva Categoria             |         9.- Nuevo Usuario")
    print("             5.- Nueva Ciudad                |         0.- Menu Principal")
    print("******************************************************************************")

def menuModificar():
    print("\n\n******************************************************************************")
    print("             1.- Modificar Cliente              |         5.- Modificar Ciudad")
    print("             2.- Modificar Marca                |         6.- Modificar Mtd Pago")
    print("             3.- Modificar Almacen              |         7.- Modificar Producto")
    print("             4.- Modificar Categoria            |         0.- Menu Principal ")
    print("******************************************************************************")

def menuEliminar():
    print("\n\n******************************************************************************")
    print("             1.- Eliminar Cliente              |         5.- Eliminar Ciudad")
    print("             2.- Eliminar Marca                |         6.- Eliminar Mtd Pago")
    print("             3.- Eliminar Almacen              |         7.- Eliminar Producto")
    print("             4.- Eliminar Categoria            |         0.- Menu Principal ")
    print("******************************************************************************")


def ingreso():
    print("\nIngrese una opción: ")

def opcionError():
    print(Fore.LIGHTRED_EX + "\nPor favor, seleccione una opción válida..." + Fore.RESET)

def ingresoError():
    print(Fore.LIGHTRED_EX + "\nPor favor, ingrese sólo números" + Fore.RESET)

def opcion(opcion):
    salir = False
    while(salir != True):
        try:
            opcion= int(opcion)
            if opcion == 1:            
                menuAgregar()
                ingreso()                
                opcion1=int(input())

                if opcion1==1:
                    newcliente.cliente()
                if opcion1==2:
                    newmarca.Marca()
                if opcion1==3:
                    newalmacen.Almacen()
                if opcion1==4:
                    newcategoria.categorias()
                if opcion1==5:
                    newciudad.ciudads()
                if opcion1==6:
                    newcompra.Compras()
                if opcion1==7:
                    newmtdpago.mtdpago()
                if opcion1==8:
                    newproducto.producto()
                if opcion1==9:
                    newuser.newuser()

                if opcion1==0:
                    menuPrincipal()
                    ingreso()                
                    opcion=int(input())
                
            elif opcion == 2:
                menuModificar()
                ingreso()
                opcion2=int(input())

                if opcion2==1:
                    edit.Edit_Cliente()
                if opcion2==2:
                    edit.Edit_Marcas()
                if opcion2==3:
                    edit.Edit_Almacen()
                if opcion2==4:
                    edit.Edit_Categoria()
                if opcion2==5:
                    edit.Edit_Ciudad()
                if opcion2==6:
                    break
                if opcion2==7:
                    break
                if opcion2==8:
                    break                
                if opcion2==0:
                    menuPrincipal()
                    ingreso()                
                    opcion=int(input())

                # import listaciudad
                # import listaruser
                # from Validadores import edituser
            elif opcion == 3:
                menuEliminar()
                ingreso()
                opcion3=int(input())
                break
            elif opcion == 0:
                salir = True
                system("cls")
            else:
                salir = True
                system("cls")

        except ValueError as identifier:
            menu.ingresoError()
                #from Validadores import newmarca
            # elif opcion ==2.1:
            #     import listarmarca
            #     from Validadores import editmarca
            # elif opcion==3:
            #     from Validadores import newalmacen
            # elif opcion==3.1:
            #     import listaalma
            # elif opcion==4:
            #     from Validadores import newcategoria
            # elif opcion==4.1:
            #     import listacate
            # elif opcion==5:
            #     from Validadores import newciudad
            # elif opcion==5.1:
            #     import listaciu
            # elif opcion==6:
            #     print("para comprar")
            #     break
            # elif opcion==7:
            #     from Validadores import newmtdpago
            # elif opcion==8:
            #     from Validadores import newproducto
            
            
        
        
