import base64
from dba import dba
from validate_email import validate_email

class  validator():
    def __init__(self):
        pass

    def validar_cliente(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombrecom']=='':
            errores['nombrecom']='campo nombre vacio'
        if datosFinales['fechanac']=='':
            errores['fechanac']='campo fecha de nacimiento vacio'
        if datosFinales['sexo']=='':
            errores['sexo']='campo sexo vacio'
        if datosFinales['telefono']=='':
            errores['telefono']='campo telefono vacio'
        if datosFinales["email"]=="":
            errores["email"] = "campo email vacio"
        elif validate_email(datosFinales["email"])==False:
            errores["email"] = "El email no es un email"
        if datosFinales['ciudad']=='':
            errores['ciudad']='campo ciudad vacio'

        if errores=={}:
            sql='select id_user from tbl_clientes where email=%s'
            val=(datosFinales['email'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['mail']='el mail ya esta registrado en nuestra base'
                return errores

        return errores

    def validar_login(self, dic):        
        sql='select * from tbl_usuarios where email=%s'
        val=(dic['mail'],)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchall()
        if result == []:
            return False
        if base64.decodebytes(bytes(result[0][4].strip(),'utf-8')).decode("UTF-8")== dic['password']: 
            return result[0]
    
    def validar_marca(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombremar']=='':
            errores['nombremar']='campo marca vacio'
        
        if errores=={}:
            sql='select id_Marca from tbl_marca where nombre=%s'
            val=(datosFinales['nombremar'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['nombremar']='La marca ya se encuentra registrada en nuestra base'
                return errores

        return errores
    
    def validar_almace(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombreal']=='':
            errores['nombreal']='campo marca vacio'
        
        if errores=={}:
            sql='select id_Almacen from tbl_almacen where tipo=%s'
            val=(datosFinales['nombreal'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['nombreal']='El almacen ya se encuentra registrada en nuestra base'
                return errores

        return errores

    def validar_cate(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombrecate']=='':
            errores['nombrecate']='campo categoria vacio'
        
        if errores=={}:
            sql='select id_Categoria from tbl_categoria where tipo=%s'
            val=(datosFinales['nombrecate'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['nombrecate']='La categoria ya se encuentra registrada en nuestra base'
                return errores

        return errores
    
    def validar_ciu(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['nombreal']=='':
            errores['nombreal']='campo ciudad vacio'
        
        if errores=={}:
            sql='select id_ciudad from tbl_ciudad where nombre=%s'
            val=(datosFinales['nombreal'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['nombreal']='La ciudad ya se encuentra registrada en nuestra base'
                return errores
        return errores
    
    def validar_compra(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['id_user']=='':
            errores['id_user']='campo usuario vacio'
        if datosFinales['id_producto']=='':
            errores['id_producto']='campo producto vacio'
        if datosFinales['id_methpago']=='':
            errores['id_methpago']='campo metodo de pago vacio'
        if datosFinales['cantidad']=='':
            errores['cantidad']='campo cantidad vacio'
        if datosFinales["subtotal"]=="":
            errores["subtotal"] = "campo subtotal vacio"
        
        if errores=={}:
            sql='select * from tbl_clientes where id_user=%s'
            val=(datosFinales['id_user'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is  None:
                errores['id_user']='El usuario no esta registrado en nuestra base'
                #from presentacion.encabezado import menuAgregar
                return errores
      
        
        return errores
    
    def validar_mtd(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombreal']=='':
            errores['nombreal']='Metodo de pago vacio'
        
        if errores=={}:
            sql='select id_methpago from tbl_methpago where tipo=%s'
            val=(datosFinales['nombreal'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['nombreal']='El metodo de pago ya se encuentra registrada en nuestra base'
                return errores

        return errores
    
    def validar_pro(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombrereal']=='':
            errores['nombrereal']='campo nombre vacio'
        if datosFinales['modelo']=='':
            errores['modelo']='campo modelo vacio'
        if datosFinales['descripcion']=='':
            errores['descripcion']='campo descripcion vacio'
        if datosFinales['precio']=='':
            errores['precio']='campo precio vacio'
        if datosFinales['categoria']=='':
            errores['categoria']='campo categoria vacio'
        if datosFinales['almacen']=='':
            errores['almace']='campo almacen vacio'
        if datosFinales['marca']=='':
            errores['marca']='campo marca vacio'

        if errores=={}:
            sql='select id_Producto from tbl_producto where nombre=%s'
            val=(datosFinales['nombrereal'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['nombrereal']='El producto ya se encuentra registrada en nuestra base'
                return errores

        return errores
    
    def validar_usuario(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombrecom']=='':
            errores['nombrecom']='campo nombre vacio'        
        if datosFinales['telefono']=='':
            errores['telefono']='campo telefono vacio'
        if datosFinales["email"]=="":
            errores["email"] = "campo email vacio"
        elif validate_email(datosFinales["email"])==False:
            errores["email"] = "El email no es un email"
                
        if len(datosFinales["password"])< 6:
            errores["password"]='password debe tener mas de 6 caracteres'
        elif datosFinales["password"]=="":
            errores["password"]='campo password vacio'
        
        if datosFinales["cpassword"]=="":
            errores["cpassword"] = "Hubo error en la confirmacion de password porque esta vacia"
        elif datosFinales["cpassword"] != datosFinales["password"]:
            errores["cpassword"] = "Password no coinsiden"

        if errores=={}:
            sql='select id_user from tbl_usuarios where email=%s'
            val=(datosFinales['email'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['mail']='el mail ya esta registrado en nuestra base'
                return errores

        return errores
            

validator=validator()

# sql='select * from tbl_usuarios where email=%s'
# val=("pedrito@gmail.com",)
# dba.get_cursor().execute(sql,val)
# result=dba.get_cursor().fetchall()
# print(result[0][4].strip())
# print(base64.decodebytes(bytes(result[0][4].strip(),'utf-8')).decode("UTF-8"))

# dba.get_cursor().execute("select * from tbl_clientes")
# result=dba.get_cursor().fetchall()
# print(result)

# sql='select * from tbl_clientes where id_user=%s'
# val=(189,)
# dba.get_cursor().execute(sql,val)
# result=dba.get_cursor().fetchone()
# print(result)