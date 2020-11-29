from validacion import validator
from cliente import Cliente
from producto import Producto


def eliminar():
    print("\n Desea eliminar registro (S)i o (N)o")

#region Cliente
def Del_Cliente():

    formcliente={}
    formcliente['dni']=input("Ingrese DNI de cliente a eliminar: ")
 
    if validator.edit_cliente(formcliente)=={}:
        user=Cliente(formcliente['dni'],"","","","","","")
        #user.select()
        a=user.select()
        print("ID: "+str(a[0])+ " DNI: " +str(a[1]) + " Nombre: " +str(a[2]) + " Fecha Nac.: " +str(a[3]) + " Sexo: " +str(a[4]) + " Celuar: " +str(a[5]) + " Email: " +str(a[6]) + " Ciudad: "+str(a[7]))

        print("\nUsuario encontrado")
        
        eliminar()
        confir=(input().upper())
        
        if confir=="S":
            formdeletecliente={}
            formdeletecliente['dni']=str(a[1])

            if validator.eliminar_cliente(formdeletecliente)=={}:
                cliente=Cliente(formcliente['dni'],"","","","","","")
                cliente.delete()

                print("\n Cliente Eliminado")
            
            else:
                print(validator.eliminar_cliente(formdeletecliente))

        elif confir=="N":
            print("Volviendo al menu principal")
        else:
            eliminar()
        


    else:
        print(validator.edit_cliente(formcliente))

#endregion

#region Producto
def Del_Producto():

    formProducto={}
    formProducto['nombrereal']=input("Ingrese Nombre del producto: ")
    formProducto['modelo']=input("Ingrese Modelo: ")
 
    if validator.edit_pro(formProducto)=={}:
        user=Producto("",formProducto['nombrereal'],formProducto['modelo'],"","","","","",)
        #user.select()
        a=user.select()

        if (str(a[8])=="0"):
            print("ID: "+str(a[0])+ " DNI: " +str(a[1]) + " Nombre: " +str(a[2]) + " Fecha Nac.: " +str(a[3]) + " Sexo: " +str(a[4]) + " Celuar: " +str(a[5]) + " Email: " +str(a[6]) + " Ciudad: "+str(a[7]))
            print("\nProducto encontrado")
        
            eliminar()
            confir=(input().upper())
            
            if confir=="S":
                formdeleteProducto={}
                formdeleteProducto['ID']=str(a[0])

                if validator.eliminar_Producto(formdeleteProducto)=={}:
                    user=Producto(formdeleteProducto['ID'],formProducto['nombrereal'],formProducto['modelo'],"","","","","",)
                    user.delete()

                    print("\n Producto Eliminado")
                
                else:
                    print(validator.eliminar_Producto(formdeleteProducto))

            elif confir=="N":
                print("Volviendo al menu principal")
            else:
                eliminar()
        else:
            print("\n Producto no existe")
        


    else:
        print(validator.edit_pro(formProducto))

#endregion
