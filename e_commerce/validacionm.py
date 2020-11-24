from dba import dba


class validatormar():
    def __init__(self):
        pass

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

validatormar=validatormar()