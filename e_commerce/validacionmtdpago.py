from dba import dba


class validatormtdpago():
    def __init__(self):
        pass

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

validatormtdpago=validatormtdpago()