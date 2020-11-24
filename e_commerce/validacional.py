from dba import dba


class validatoral():
    def __init__(self):
        pass

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

validatoral=validatoral()