from presentacion import encabezado
from presentacion import menu
  

encabezado.autor()
salir = False
while(salir != True):
    menu.menuPrincipal()
    menu.ingreso()
    opcion = input()
    try:
        opcion= float(opcion)
        if opcion == 1:
            
            from Validadores import newuser
        elif opcion ==1.2:
            import listaciudad
            import listaruser
            from Validadores import edituser
        elif opcion ==2:
            from Validadores import newmarca
        elif opcion ==2.1:
            import listarmarca
            from Validadores import editmarca
        elif opcion==3:
            from Validadores import newalmacen
        elif opcion==3.1:
            import listaalma
        elif opcion==4:
            from Validadores import newcategoria
        elif opcion==4.1:
            import listacate
        elif opcion==5:
            from Validadores import newciudad
        elif opcion==5.1:
            import listaciu
        elif opcion==6:
            print("para comprar")
        elif opcion==7:
            from Validadores import newmtdpago
        elif opcion==8:
            from Validadores import newproducto
        
        else:
            salir = True
        
    
    except ValueError as identifier:
        menu.ingresoError()
