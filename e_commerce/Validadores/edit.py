from Validadores.newcategoria import categorias
from cliente import Cliente
from marca import Marcas
from almacen import Almacenes
from validacion import validator
from categoria import Categoria
from ciudad import Ciudad

#region Cliente
def Edit_Cliente():

    formcliente={}
    formcliente['dni']=input("Ingrese DNI: ")
 
    if validator.edit_cliente(formcliente)=={}:
        user=Cliente(formcliente['dni'],"","","","","","")
        user.select()
        print("\nUsuario encontrado")
        formeditcliente={}
        formeditcliente['dni']=formcliente['dni']
        formeditcliente['nombrecom']=input('Nombre completo: ')
        formeditcliente['fechanac']=input('Fecha de Nacimiento AAAA-MM-DD: ')
        formeditcliente['sexo']=(input('Sexo F o M: ').capitalize())
        formeditcliente['telefono']=input('Telefono: ')
        formeditcliente['email']=input('Email: ')
        formeditcliente['ciudad']=input('Ciudad: ')
        formeditcliente['edit']="1"
        
        if validator.validar_cliente(formeditcliente)=={}:
            
            user=Cliente(formeditcliente['dni'],formeditcliente['nombrecom'],formeditcliente['fechanac'],formeditcliente['sexo'],formeditcliente['telefono'],formeditcliente['email'],formeditcliente['ciudad'])
            user.update()
            print('usuario Actualizado exitosamente')
        else:
            print(validator.validar_cliente(formeditcliente))


    else:
        print(validator.edit_cliente(formcliente))

#endregion

#region Marca
def Edit_Marcas():

    formMarca={}
    formMarca['nombre']=(input("Ingrese Marca: ").capitalize())
    
    if validator.edit_Marca(formMarca)=={}:
        user=Marcas("",formMarca['nombre'])
        user.select()
        print(user.select())
        a=user.select()
        # print(a[0])
        print("\nMarca encontrada")
        
        
        formeditmarca={}
        formeditmarca['id']=str(a[0])
        formeditmarca['nombremar']=(input("Ingrese nueva Marca: ").capitalize())
        formeditmarca['edit']="1"

        if validator.validar_marca(formeditmarca)=={}:
            user=Marcas(formeditmarca['id'],formeditmarca['nombremar'])
            user.update()
            print("Marca Actualizada exitosamente")
        else:
            print(validator.validar_marca(formeditmarca))
    else:
        print(validator.edit_Marca(formMarca))

#endregion

#region Almacen
def Edit_Almacen():

    formAlmacen={}
    formAlmacen['nombre']=(input("Ingrese nombre del Almacen: ").capitalize())
    
    if validator.edit_Almacen(formAlmacen)=={}:
        user=Almacenes("",formAlmacen['nombre'])
        user.select()
        print(user.select())
        a=user.select()
        # print(a[0])
        print("\nAlmacen encontrada")
        
        
        formeditAlmacen={}
        formeditAlmacen['id']=str(a[0])
        formeditAlmacen['nombreal']=(input("Ingrese nuevo Almacen: ").capitalize())
        formeditAlmacen['edit']="1"

        if validator.validar_almace(formeditAlmacen)=={}:
            user=Almacenes(formeditAlmacen['id'],formeditAlmacen['nombreal'])
            user.update()
            print("Almacen Actualizada exitosamente")
        else:
            print(validator.validar_almace(formeditAlmacen))
    else:
        print(validator.edit_Almacen(formAlmacen))

#endregion

#region Categoria
def Edit_Categoria():

    formCategoria={}
    formCategoria['nombre']=(input("Ingrese nombre de la Categoria: ").capitalize())
    
    if validator.edit_Categoria(formCategoria)=={}:
        user=Categoria("",formCategoria['nombre'])
        user.select()
        print(user.select())
        a=user.select()
        # print(a[0])
        print("\n Categoria encontrada")
        
        
        formeditCategoria={}
        formeditCategoria['id']=str(a[0])
        formeditCategoria['nombrecate']=(input("Ingrese nueva Categoria: ").capitalize())
        formeditCategoria['edit']="1"

        if validator.validar_cate(formeditCategoria)=={}:
            user=Categoria(formeditCategoria['id'],formeditCategoria['nombrecate'])
            user.update()
            print("Almacen Actualizada exitosamente")
        else:
            print(validator.validar_cate(formeditCategoria))
    else:
        print(validator.edit_Categoria(formCategoria))

#endregion

#region Categoria
def Edit_Ciudad():

    formCiudad={}
    formCiudad['nombre']=(input("Ingrese nombre de la Ciudad: ").capitalize())
    
    if validator.edit_Ciudad(formCiudad)=={}:
        user=Ciudad("",formCiudad['nombre'])
        user.select()
        print(user.select())
        a=user.select()
        # print(a[0])
        print("\n Cuidad encontrada")
        
        
        formeditCategoria={}
        formeditCategoria['id']=str(a[0])
        formeditCategoria['nombreal']=(input("Ingrese nueva Ciudad: ").capitalize())
        formeditCategoria['edit']="1"

        if validator.validar_ciu(formeditCategoria)=={}:
            user=Ciudad(formeditCategoria['id'],formeditCategoria['nombreal'])
            user.update()
            print("Ciudad Actualizada exitosamente")
        else:
            print(validator.validar_ciu(formeditCategoria))
    else:
        print(validator.edit_Ciudad(formCiudad))

#endregion
