from usuario import Usuario
from validacion import validator
import getpass

def newuser(): 
    formusuario={}
    formusuario['nombrecom']=input('Nombre completo: ')
    formusuario['telefono']=input('Telefono: ')
    formusuario['email']=input('Email: ')
    formusuario['password']=getpass.getpass('Password: ')
    formusuario['cpassword']=getpass.getpass('Confirmar Password: ')



    if validator.validar_usuario(formusuario)=={}:
        user=Usuario("",formusuario['nombrecom'],formusuario['telefono'],formusuario['email'],formusuario['password'])
        user.save()
        print('usuario registrado exitosamente')
    else:
        print(validator.validar_usuario(formusuario))

#user = Usuario("Pedro Maneiro","1985-09-10","M",1121651051,"pedromaneiro@gmail.com", 1 , "pedro1985")
#print(user.get_ciudad)
#user.save()s
#print(user)