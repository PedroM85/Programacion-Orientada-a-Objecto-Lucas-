from dba import dba


class validatorpro():
    def __init__(self):
        pass

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

validatorpro=validatorpro()