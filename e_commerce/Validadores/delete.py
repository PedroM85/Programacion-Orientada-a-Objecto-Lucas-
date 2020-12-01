from validacion import validator
from cliente import Cliente
from producto import Producto
from marca import Marcas
from methpago import MethPago
from ciudad import Ciudad
from almacen import Almacenes
from categoria import Categoria

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

#region Marca

def Del_Marcas():

    formMarca={}
    formMarca['nombre']=(input("Ingrese Marca: ").capitalize())
 
    if validator.edit_Marca(formMarca)=={}:
        user=Marcas("",formMarca['nombre'])
        a=user.select()
        print("ID: "+str(a[0])+" - Nombre: "+str(a[1]))
        print("\nMarca encontrada")

        eliminar()
        confir=(input().upper())

        if confir=="S":
            formdeleteMarca={}
            formdeleteMarca['ID']=str(a[0])

            if validator.eliminar_Marca(formdeleteMarca)=={}:
                user=Marcas(formdeleteMarca['ID'],formMarca['nombre'])
                user.delete()

                print("\n Marca Eliminada")
                
            else:
                print(validator.eliminar_Marca(formdeleteMarca))

        elif confir=="N":
            print("Volviendo al menu principal")
        else:
            eliminar()
        
    else:
        print(validator.edit_Marca(formMarca))


#endregion

#region Metodo pago

def Del_methpago():

    formmethpago={}
    formmethpago['nombre']=(input("Ingrese Metodo de pago: ").capitalize())
    
    if validator.edit_Methpago(formmethpago)=={}:
        user=MethPago("",formmethpago['nombre'])
        a=user.select()
        print("ID: "+str(a[0])+" - Nombre: "+str(a[1]))
        print("\n Metodo de pago encontrado")
        
        eliminar()
        confir=(input().upper())

        if confir=="S":
            formdeleteMethpago={}
            formdeleteMethpago['ID']=str(a[0])

            if validator.eliminar_MethPago(formdeleteMethpago)=={}:
                user=MethPago(formdeleteMethpago['ID'],formmethpago['nombre'])
                user.delete()

                print("\n Metodo de pago Eliminado")
            
            else:
                print(validator.eliminar_MethPago(formdeleteMethpago))

        elif confir=="N":
            print("Volviendo al menu principal")
        else:
            eliminar()

    else:
        print(validator.edit_Methpago(formmethpago))

#endregion

#region Ciudad
def Del_Ciudad():

    formCiudad={}
    formCiudad['nombre']=(input("Ingrese nombre de la Ciudad: ").capitalize())
 
    if validator.edit_Ciudad(formCiudad)=={}:
        user=Ciudad("",formCiudad['nombre'])
        a=user.select()
        print("ID: "+str(a[0])+" - Nombre: "+str(a[1]))
        print("\n ciudad encontrada")
        

        eliminar()
        confir=(input().upper())
        
        if confir=="S":
            formdeleteCiudad={}
            formdeleteCiudad['ID']=str(a[0])

            if validator.eliminar_ciudad(formdeleteCiudad)=={}:
                user=Ciudad(formdeleteCiudad['ID'],formCiudad['nombre'])
                user.delete()

                print("\n Ciudad Eliminada")
            
            else:
                print(validator.eliminar_ciudad(formdeleteCiudad))

        elif confir=="N":
            print("Volviendo al menu principal")
        else:
            eliminar()
        


    else:
        print(validator.edit_Ciudad(formCiudad))

#endregion

#region Almacen

def Del_Almacen():

    formAlmacen={}
    formAlmacen['nombre']=input("Ingrese nombre del almacen a eliminar: ")
 
    if validator.edit_Almacen(formAlmacen)=={}:
        user=Almacenes("",formAlmacen['nombre'])
        a=user.select()
        print("ID: "+str(a[0])+" - Nombre: "+str(a[1]))
        print("\n Almacen encontrado")
        
        eliminar()
        confir=(input().upper())
        
        if confir=="S":
            formdeleteAlmacen={}
            formdeleteAlmacen['ID']=str(a[0])

            if validator.eliminar_Almacen(formdeleteAlmacen)=={}:
                user=Almacenes(formdeleteAlmacen['ID'],formAlmacen['nombre'])
                user.delete()

                print("\n Almacen Eliminado")
            
            else:
                print(validator.eliminar_Almacen(formdeleteAlmacen))

        elif confir=="N":
            print("Volviendo al menu principal")
        else:
            eliminar()
        


    else:
        print(validator.edit_Almacen(formAlmacen))

#endregion

#region Categoria
def Del_Categoria():

    formCategoria={}
    formCategoria['nombre']=(input("Ingrese categoria: ").capitalize())
    
    if validator.edit_Categoria(formCategoria)=={}:
        user=Categoria("",formCategoria['nombre'])
        a=user.select()
        print("ID: "+str(a[0])+" - Nombre: "+str(a[1]))
        print("\n Categoria encontrada")
        
        eliminar()
        confir=(input().upper())

        if confir=="S":
            formdeleteCategoria={}
            formdeleteCategoria['ID']=str(a[0])

            if validator.eliminar_Categoria(formdeleteCategoria)=={}:
                user=Categoria(formdeleteCategoria['ID'],formCategoria['nombre'])
                user.delete()

                print("\n Categoria Eliminada")
            
            else:
                print(validator.eliminar_Categoria(formdeleteCategoria))

        elif confir=="N":
            print("Volviendo al menu principal")
        else:
            eliminar()

    else:
        print(validator.edit_Categoria(formCategoria))

#endregion

