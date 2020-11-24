from producto import Producto
from validacionpro import validatorpro


formpro={}
formpro['nombrereal']=input('Nombre: ')
formpro['modelo']=input('Modelo: ')
formpro['descripcion']=input('Descripcion: ')
formpro['precio']=input('Precio: ')
formpro['categoria']=input('Categoria: ')
formpro['almacen']=input('Almacen: ')
formpro['marca']=input('Marca: ')




if validatorpro.validar_pro(formpro)=={}:
    producto=Producto(formpro['nombrereal'],formpro['modelo'],formpro['descripcion'],formpro['precio'],formpro['categoria'],formpro['almacen'],formpro['marca'])
    producto.save()
    print('Producto registrado exitosamente')
else:
    print(validatorpro.validar_pro(formpro))

#user = Usuario("Pedro Maneiro","1985-09-10","M",1121651051,"pedromaneiro@gmail.com", 1 , "pedro1985")
#print(user.get_ciudad)
#user.save()s
#print(user)
