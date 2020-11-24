from dba import dba


class validatorcate():
    def __init__(self):
        pass

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

validatorcate=validatorcate()