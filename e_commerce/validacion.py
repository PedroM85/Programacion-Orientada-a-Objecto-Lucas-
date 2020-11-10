from dba import dba
from validate_email import validate_email

class validator():
    def __init__(self):
        pass


    def validar_usuario(self,dic):
        datosFinales={}
        errores={}
        SpecialSym=['$','@','#','%']
        for x,y in dic.items():
            datosFinales[x]=y.strip()

        if datosFinales['nombrecom']=='':
            errores['nombrecom']='campo nombre vacio'
        if datosFinales['email']=='':
            errores['email']='campo email vacio'
        
        if len(datosFinales["password"])< 6:
            errores["password"]='password debe tener mas de 6 caracteres'
        elif datosFinales["password"]=="":
            errores["password"]='campo password vacio'
        elif not any(char.isdigit() for char in datosFinales["password"]):
            errores["password"]='Password debe tener un caracter numeral'
        elif not any(char.isupper() for char in datosFinales["password"]):
            errores["password"]='Password debe tener una palabra mayuscula'
        elif not any(char.islower() for char in datosFinales["password"]):
            errores["password"]='Password debe tener minusculas'
        elif not any(char in SpecialSym for char in datosFinales["password"]):
            errores["password"]='Password debe tener al menos un caracter especial $@#'

        if datosFinales["cpassword"]=="":
            errores["cpassword"] = "Hubo error en la confirmacion de contrasenia porque esta vacia"
        elif datosFinales["cpassword"] != datosFinales["password"]:
            errores["cpassword"] = "Password no verifica"
        
        if datosFinales["email"]=="":
            errores["email"] = "campo email vacio"
        elif validate_email(datosFinales["email"])==False:
            errores["email"] = "El email no es un email"

        if errores=={}:
            sql='select id_user from tbl_usuarios where email=%s'
            val=(datosFinales['email'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['mail']='el mail ya esta registrado en nuestra base'
                return errores
        
        return errores