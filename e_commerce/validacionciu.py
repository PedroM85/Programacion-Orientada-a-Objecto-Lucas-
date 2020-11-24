from dba import dba


class validatorciu():
    def __init__(self):
        pass

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

validatorciu=validatorciu()