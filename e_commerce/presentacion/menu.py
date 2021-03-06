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
from Validadores import delete
from colorama import Fore, init
from os import system

init()

def menuPrincipal():
    print("\n\n******************************************************************************")
    print("                         Seleccione una opción:")
    print("             1.- Agregar")
    print("             2.- Modificar")
    print("             3.- Eliminar")
    print("             0.- Salir")
    print("")
    print("******************************************************************************")

def menuAgregar():
    print("\n\n******************************************************************************")
    print("                               Seleccione una opción:")
    print("             1.- Nuevo Cliente           |         6.- Nueva Compra")
    print("             2.- Nueva Marca             |         7.- Nueva Mtd Pago")
    print("             3.- Nuevo Almacen           |         8.- Nuevo Producto")
    print("             4.- Nueva Categoria         |         9.- Nuevo Usuario")
    print("             5.- Nueva Ciudad            |         0.- Menu Principal")
    print("")
    print("******************************************************************************")

def menuModificar():
    print("\n\n******************************************************************************")
    print("                                   Seleccione una opción:")
    print("             1.- Modificar Cliente           |         5.- Modificar Ciudad")
    print("             2.- Modificar Marca             |         6.- Modificar Mtd Pago")
    print("             3.- Modificar Almacen           |         7.- Modificar Producto")
    print("             4.- Modificar Categoria         |         0.- Menu Principal ")
    print("")
    print("******************************************************************************")

def menuEliminar():
    print("\n\n******************************************************************************")
    print("                                  Seleccione una opción:")
    print("             1.- Eliminar Cliente           |         5.- Eliminar Ciudad")
    print("             2.- Eliminar Marca             |         6.- Eliminar Mtd Pago")
    print("             3.- Eliminar Almacen           |         7.- Eliminar Producto")
    print("             4.- Eliminar Categoria         |         0.- Menu Principal ")
    print("")
    print("******************************************************************************")


def ingreso():
    print("\nIngrese una opción: ")

def opcionError():
    print(Fore.LIGHTRED_EX + "\nPor favor, seleccione una opción válida..." + Fore.RESET)

def ingresoError():
    print(Fore.LIGHTRED_EX + "\nPor favor, ingrese sólo números" + Fore.RESET)

def opcion(opcion,username):
    salir = False
    while(salir != True):
        try:
            opcion= int(opcion)
        
            if opcion == 1:            
                menuAgregar()
                ingreso()                
                opcion1=int(input())
                if not isinstance(opcion1,int):
                    print("Solo Ingrese numeros")
                if int(opcion1) >= 0 and int(opcion1) <= 9:                        
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
                        newcompra.Compras("","si")
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
                else:
                    print("La opción ingresada no es valida: "+str(opcion1))
                    print("Solo ingrese numero del 0 al 9")
                    print("\n")

                        
            elif opcion == 2:
                menuModificar()
                ingreso()
                opcion2=int(input())
                if not isinstance(opcion2,int):
                    print("Solo Ingrese numeros")
                if int(opcion2) >= 0 and int(opcion2) <= 7:
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
                        edit.Edit_methpago()
                    if opcion2==7:
                        edit.Edit_Producto()
                    if opcion2==0:
                        menuPrincipal()
                        ingreso()                
                        opcion=int(input())
                    else:
                        menuPrincipal()
                        ingreso()                
                        opcion=int(input())

                
            elif opcion == 3:
                menuEliminar()
                ingreso()
                opcion3=int(input())

                if not isinstance(opcion3,int):
                    print("Solo Ingrese numeros")
                if int(opcion3) >= 0 and int(opcion3) <= 7:
                                
                    if opcion3 ==1:
                        delete.Del_Cliente()
                    if opcion3 == 2:
                        delete.Del_Marcas()
                    if opcion3 == 3:
                        delete.Del_Almacen()
                    if opcion3 == 4:
                        delete.Del_Categoria()
                    if opcion3 == 5:
                        delete.Del_Ciudad()
                    if opcion3 == 6:
                        delete.Del_methpago()
                    if opcion3 == 7:
                        delete.Del_Producto()
                    if opcion3 == 0:
                        menuPrincipal()
                        ingreso()                
                        opcion=int(input())
                    else:
                        menuPrincipal()
                        ingreso()                
                        opcion=int(input())

            elif opcion == 0:
                    salir = True
                    print("Hasta luego fue un placer: "+ str(username))
                    # system("cls")
            else:
                print("La opción ingresada no es valida: "+str(opcion))
                print("Solo ingrese numero del 0 al 9")
                print("\n")   
            

        except ValueError as identifier:
            ingresoError()
        
            
            
        
        

        
