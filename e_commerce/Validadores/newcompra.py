from compra import Compra
from validacion import validator

def Compras():
    formcom={}
    formcom['id_user']=input('Numero de usuario: ')
    formcom['id_producto']=input('Numero de producto: ')
    formcom['id_methpago']=input('Numero de metodo de pago: ')
    formcom['cantidad']=input('Cantidad de producto a vender: ')
    formcom['subtotal']=input('Precio del producto: ')
    
    if validator.validar_compra(formcom)=={}:
        Compra1=Compra(formcom['id_user'],formcom['id_producto'],formcom['id_methpago'],formcom['cantidad'],formcom['subtotal'])
        Compra1.save()
        print('Compra registrado exitosamente')
    else:        
        print(validator.validar_compra(formcom))



# asd = Compra(3,3,2,1,45)
# asd.save()

