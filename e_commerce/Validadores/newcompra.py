import re
from compra import Compra
from presentacion import menu
from validacion import validator

       
comprando = "si"
user1=""
id_producto = validator.ID_Ultimo_Producto()

def Compras(user1,comprando):

    if comprando == "si":  
        formcom={}
        formcom['id']= str(id_producto)
        print("-"*35)
        validator.listar_cliente()
        print("-"*35)
        user1= input('Numero de usuario: ')
        formcom['id_user']= str(user1)
        print("-"*35)
        validator.listar_producto()
        print("-"*35)
        formcom['id_producto']=input('Numero de producto: ')
        print("-"*35)
        validator.listar_methpago()
        print("-"*35)
        formcom['id_methpago']=input('Numero de metodo de pago: ')
        formcom['cantidad']=input('Cantidad de producto a vender: ')
        formcom['subtotal']=input('Precio del producto: ')
        

        if validator.validar_compra(formcom)=={}:        
            Compra1=Compra(formcom['id'],formcom['id_user'],formcom['id_producto'],formcom['id_methpago'],formcom['cantidad'],formcom['subtotal'])        
            Compra1.save()
            print("Desea agregar otra compra? (S)i o (N)o")
            addcompra=(str(input())).upper()
            if (addcompra == "S" or addcompra == "SI"):
                formcom={}
                formcom['id']= str(id_producto)
                formcom['id_user']= str(user1)
                print("-"*35)
                validator.listar_producto()
                print("-"*35)
                formcom['id_producto']=input('Numero de producto: ')
                print("-"*35)
                validator.listar_methpago()
                print("-"*35)
                formcom['id_methpago']=input('Numero de metodo de pago: ')
                formcom['cantidad']=input('Cantidad de producto a vender: ')
                formcom['subtotal']=input('Precio del producto: ')
                formcom['new']="si"
                validator.validar_compra(formcom)
                Compra1=Compra(formcom['id'],formcom['id_user'],formcom['id_producto'],formcom['id_methpago'],formcom['cantidad'],formcom['subtotal'])         
                Compra1.save()
               
                print("Desea agregar otra compra? (S)i o (N)o")
                addcompra1=(str(input())).upper()
                if (addcompra1 == "S" or addcompra1 == "SI"):
                    comprando="si"
                    Compras(user1,comprando)
                else:
                    comprando="no"
                    Compras(user1,comprando)
                
                print('Compra registrada exitosamente')
                
            else:
                pass
        
                    
        else:        
            print(validator.validar_compra(formcom))
    
        
