from dba import dba
from validate_email import validate_email

class validator():
    def __init__(self):
        pass


    def validar_usuario(self,dic):
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

        
        if len(datosFinales["password"])< 6:
            errores["password"]='password debe tener mas de 6 caracteres'
        elif datosFinales["password"]=="":
            errores["password"]='campo password vacio'
        
        if datosFinales["cpassword"]=="":
            errores["cpassword"] = "Hubo error en la confirmacion de password porque esta vacia"
        elif datosFinales["cpassword"] != datosFinales["password"]:
            errores["cpassword"] = "Password no verifica"

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
