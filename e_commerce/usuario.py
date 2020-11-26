from dba import dba
import base64

class Usuario():
    def __init__(self,id, nombrecom, telefono, email, password ):
        self.__id=id
        self.nombrecom=nombrecom        
        self.telefono=telefono
        self.email=email        
        self.password=self.encriptar_pass(password)


    def get_id_user(self):
        return self.__id
    def set_id_user(self,id):
        self.__id=id
    def get_nombrecom(self):
        return self.nombrecom
    def set_nombrecom(self, nombrecom):
        self.nombrecom=nombrecom
    
    def get_password(self):
        return self.desencriptar_pass(self.password)
    def set_password(self, password):
        self.password =  self.encriptar_pass(password)
    def encriptar_pass(self, password):
        return base64.encodebytes(bytes(password, 'utf-8'))
    def desencriptar_pass(self, password):
        return base64.decodebytes(password).decode("UTF-8")
    def get_telefono(self):
        return self.telefono
    def set_telefono(self, telefono):
        self.telefono=telefono
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email=email
    

    def save(self):
        sql="insert into tbl_usuarios(nombrecom,telefono,email,password) values(%s,%s,%s,%s)"
        val=(self.get_nombrecom(),self.get_telefono(),self.get_email(),self.encriptar_pass(self.get_password()),)
        dba.get_cursor().execute(sql,val)        
        dba.get_conexion().commit()
        self.set_id_user(dba.get_cursor().lastrowid)

    def delete(self):
        sql='delete from tbl_usuarios where id=%s'
        val=(self.id_user(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update(self):     
        sql='update tbl_usuarios set nombrecom=%s, telefono=%s, email=%s, where id_user=%s '
        val=(self.get_nombrecom(),self.get_telefono(),self.get_email(),self.get_id_user())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

