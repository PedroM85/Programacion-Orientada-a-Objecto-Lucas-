import base64
from dba import dba
from validate_email import validate_email

class  validator():
    def __init__(self):
        pass

#region Cliente
    def validar_cliente(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['dni']=='':
            errores['dni']='campo dni vacio'
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
        if datosFinales['edit'] == "":
            errores['edit']='campo edit vacio'

        if errores=={}:
            if datosFinales['edit']=="1":
                 print("\n")
            else:          
                sql='select id_user from tbl_clientes where email=%s or dni=%s'
                val=(datosFinales['email'],datosFinales['dni'])
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is not None:
                    errores['mail']='El DNI o mail ya esta registrado en nuestra base'
                    return errores

        return errores
#endregion

#region ClienteBusqueda
    def edit_cliente(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['dni']=='':
            errores['dni']='campo dni vacio'
        
        if errores=={}:
            sql='SELECT * from tbl_clientes WHERE dni=%s'
            val=(datosFinales['dni'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is  None:
                errores['dni']='el usuario no esta registrado en nuestra base'
                return errores

        return errores
#endregion

#region login    
    def validar_login(self, dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['mail']=="":
            errores['mail']='campo email vacio'
        if datosFinales['password']=='':
            errores['password']='campo password vacio'
        
        if errores=={}:

            sql='select * from tbl_usuarios where email=%s'
            val=(dic['mail'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchall()
            if result == []:
                return False
            if base64.decodebytes(bytes(result[0][4].strip(),'utf-8')).decode("UTF-8")== dic['password']: 
                return result[0]
            else:
                return False
        
        return errores
#endregion
    
#region Marca
    def validar_marca(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()
        
        # if datosFinales['id']=="":
        #     errores['id']='campo id vacio'
        if datosFinales['nombremar']=='':
            errores['nombremar']='campo marca vacio'

        
        if errores=={}:
            if datosFinales['edit']=="1":
                print("\n")
            else:           
                sql='select id_Marca from tbl_marca where nombre=%s'
                val=(datosFinales['nombremar'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is not None:
                    errores['nombremar']='La marca ya se encuentra registrada en nuestra base'
                    return errores

        return errores
#endregion

#region Edit Marca
    def edit_Marca(self,dic):
        datosFinales={}
        errores={}

        for x,y in dic.items():
            datosFinales[x]=y.strip()

            if datosFinales['nombre']=='':
                errores['nombre']='campo nombre vacio'
            
            if errores=={}:
                sql='SELECT * from tbl_marca WHERE nombre=%s'
                val=(datosFinales['nombre'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is None:
                    errores['nombre']='La marca no esta registrada en nuestra base'
                    return errores

            return errores
#endregion

#region Almacen
    def validar_almace(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        # if datosFinales['id']=="":
        #     errores['id']='campo id vacio'
        if datosFinales['nombreal']=='':
            errores['nombreal']='campo marca vacio'
        
        if errores=={}:
            if datosFinales['edit']=="1":
                print("\n")
            else:    
                sql='select id_Almacen from tbl_almacen where tipo=%s'
                val=(datosFinales['nombreal'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is not None:
                    errores['nombreal']='El almacen ya se encuentra registrada en nuestra base'
                    return errores

        return errores
#endregion 

#region Edit Almacen
    def edit_Almacen(self,dic):
        datosFinales={}
        errores={}

        for x,y in dic.items():
            datosFinales[x]=y.strip()

            if datosFinales['nombre']=='':
                errores['nombre']='campo nombre vacio'
            
            if errores=={}:
                sql='SELECT * from tbl_almacen WHERE tipo=%s'
                val=(datosFinales['nombre'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is None:
                    errores['nombre']='El Almance no esta registrada en nuestra base'
                    return errores

            return errores
#endregion

#region Categoria
    def validar_cate(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        # if datosFinales['id']=="":
        #     errores['id']='campo id vacio'
        if datosFinales['nombrecate']=='':
            errores['nombrecate']='campo categoria vacio'
        
        if errores=={}:
            if datosFinales['edit']=="1":
                print("\n")
            else:    
                sql='select id_Categoria from tbl_categoria where tipo=%s'
                val=(datosFinales['nombrecate'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is not None:
                    errores['nombrecate']='La categoria ya se encuentra registrada en nuestra base'
                    return errores

        return errores
#endregion 

#region Edit Categoria
    def edit_Categoria(self,dic):
        datosFinales={}
        errores={}

        for x,y in dic.items():
            datosFinales[x]=y.strip()

            if datosFinales['nombre']=='':
                errores['nombre']='campo nombre vacio'
            
            if errores=={}:
                sql='SELECT * from tbl_categoria WHERE tipo=%s'
                val=(datosFinales['nombre'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is None:
                    errores['nombre']='La Categoria no esta registrada en nuestra base'
                    return errores

            return errores

#endregion

#region Cuidad
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
#endregion

#region Edit Ciudad
    def edit_Ciudad(self,dic):
        datosFinales={}
        errores={}

        for x,y in dic.items():
            datosFinales[x]=y.strip()

            if datosFinales['nombre']=='':
                errores['nombre']='campo ciudad vacio'
            
            if errores=={}:
                sql='SELECT * from tbl_ciudad WHERE nombre=%s'
                val=(datosFinales['nombre'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is None:
                    errores['nombre']='La ciudad no esta registrada en nuestra base'
                    return errores

            return errores
#endregion

#region Compra
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
#endregion

#region Metodo_Pago    
    def validar_mtd(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombreal']=='':
            errores['nombreal']='Metodo de pago vacio'
        
        if errores=={}:
            if datosFinales['edit']=="1":
                print("\n")
            else:    
                sql='select id_methpago from tbl_methpago where tipo=%s'
                val=(datosFinales['nombreal'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is not None:
                    errores['nombreal']='El metodo de pago ya se encuentra registrada en nuestra base'
                    return errores

        return errores
#endregion

#region Edit methpago
    def edit_Methpago(self,dic):
        datosFinales={}
        errores={}

        for x,y in dic.items():
            datosFinales[x]=y.strip()

            if datosFinales['nombre']=='':
                errores['nombre']='campo Metodo de pago vacio'
            
            if errores=={}:
                sql='SELECT * from tbl_methpago WHERE tipo=%s'
                val=(datosFinales['nombre'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is None:
                    errores['nombre']='El metodo de pago no esta registrada en nuestra base'
                    return errores

            return errores
#endregion

#region Producto    
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
            if datosFinales['edit']=="1":
                print("\n")
            else:
                sql='select id_Producto from tbl_producto where nombre=%s'
                val=(datosFinales['nombrereal'],)
                dba.get_cursor().execute(sql,val)
                result=dba.get_cursor().fetchone()
                if result is not None:
                    errores['nombrereal']='El producto ya se encuentra registrada en nuestra base'
                    return errores

        return errores
#endregion

#region Edit Producto    
    def edit_pro(self,dic):
        datosFinales={}
        errores={}
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombrereal']=='':
            errores['nombrereal']='campo nombre vacio'
        if datosFinales['modelo']=='':
            errores['modelo']='campo modelo vacio'
        # if datosFinales['descripcion']=='':
        #     errores['descripcion']='campo descripcion vacio'
        # if datosFinales['precio']=='':
        #     errores['precio']='campo precio vacio'
        # if datosFinales['categoria']=='':
        #     errores['categoria']='campo categoria vacio'
        # if datosFinales['almacen']=='':
        #     errores['almace']='campo almacen vacio'
        # if datosFinales['marca']=='':
        #     errores['marca']='campo marca vacio'

        if errores=={}:
            sql='select id_Producto from tbl_producto where nombre=%s and modelo=%s'
            val=(datosFinales['nombrereal'],datosFinales['modelo'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is  None:
                errores['nombrereal']='El producto no esta registrada en nuestra base'
                return errores

        return errores
#endregion

#region Usuario
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
                errores['mail']='El mail ya esta registrado en nuestra base'
                return errores

        return errores
#endregion
            

validator=validator()

# sql='select * from tbl_usuarios where email=%s'
# val=("pedritqo@gmail.com",)
# dba.get_cursor().execute(sql,val)
# result=dba.get_cursor().fetchall()
# #print(type(result))
# print(result)
#print(result[0][4].strip())
#print(base64.decodebytes(bytes(result[0][4].strip(),'utf-8')).decode("UTF-8"))

# dba.get_cursor().execute("select * from tbl_clientes")
# result=dba.get_cursor().fetchall()
# print(result)

# sql='SELECT * from tbl_producto WHERE nombre=%s and modelo=%s'
# val=("Cerveza","rubia")
# dba.get_cursor().execute(sql,val)
# result=dba.get_cursor().fetchone()
# print(result)


# sql="insert into tbl_clientes(dni,nombrecom,fechanac,sexo,telefono,email,ciudad) values(%s,%s,%s,%s,%s,%s,%s)"
# val=(95896376,"asdasdsad","2020-11-23","F",11231212414,"adasdmasd@aad.com",2)
# dba.get_cursor().execute(sql,val)        
# dba.get_conexion().commit()
# self.set_id_user(dba.get_cursor().lastrowid)
