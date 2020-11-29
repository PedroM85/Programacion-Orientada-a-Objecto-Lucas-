from ciudad import Ciudad
from dba import dba

class Cliente():
    def __init__(self,dni,nombrecom, fechanac, sexo, telefono, email, ciudad ):
        self.__id=id
        self.dni=dni
        self.nombrecom=nombrecom
        self.fechanac=fechanac
        self.sexo=sexo
        self.telefono=telefono
        self.email=email
        self.ciudad=ciudad
       

    def get_id_user(self):
        return self.__id
    def set_id_user(self,id):
        self.__id=id
    def get_dni(self):
        return self.dni
    def set_dni(self,dni):
        self.dni=dni
    def get_nombrecom(self):
        return self.nombrecom
    def set_nombrecom(self, nombrecom):
        self.nombrecom=nombrecom
    def get_fechanac(self):
        return self.fechanac
    def set_fechanac(self, fechanac):
        self.fechanac=fechanac
    def get_sexo(self):
        return self.sexo
    def set_sexo(self, sexo):
        self.sexo=sexo    
    def get_telefono(self):
        return self.telefono
    def set_telefono(self, telefono):
        self.telefono=telefono
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email=email
    def get_ciudad(self):
        return self.ciudad
    def set_ciudad(self, ciudad):
        self.ciudad=ciudad


    def save(self):
        sql="insert into tbl_clientes(dni,nombrecom,fechanac,sexo,telefono,email,ciudad) values(%s,%s,%s,%s,%s,%s,%s)"
        val=(self.get_dni(),self.get_nombrecom(),self.get_fechanac(),self.get_sexo(),self.get_telefono(),self.get_email(),self.get_ciudad())
        dba.get_cursor().execute(sql,val)        
        dba.get_conexion().commit()
        self.set_id_user(dba.get_cursor().lastrowid)

    def delete(self):
        sql='delete from tbl_clientes where dni=%s'
        val=(self.get_dni(),)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update(self):     
        sql='update tbl_clientes set nombrecom=%s,fechanac=%s, sexo=%s, telefono=%s, email=%s, ciudad=%s where dni=%s '
        val=(self.get_nombrecom(),self.get_fechanac(),self.get_sexo(),self.get_telefono(),self.get_email(),self.get_ciudad(),self.get_dni())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    def select(self):
        sql='SELECT * from tbl_clientes WHERE dni=%s'
        val=(self.get_dni(),)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        return result



