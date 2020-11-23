from presentacion import encabezado
from presentacion import menu

encabezado.autor()
salir = False
while(salir != True):
    menu.menuPrincipal()
    menu.ingreso()
    opcion = input()
    try:
        opcion= int(opcion)
        if opcion == 1:
            from Validadores import newuser


        else:
            salir = True
        #print("\nDeseas tirar los dados nuevamente?, ingresa la opción 1 para lanzar")
    
    except ValueError as identifier:
        menu.ingresoError()
