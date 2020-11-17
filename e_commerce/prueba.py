from usuario import Usuario
from validacion import validator
import getpass 


formusuario={}
formusuario['nombrecom']=input('Nombre completo: ')
formusuario['fechanac']=input('Fecha de Nacimiento AAAA-MM-DD: ')
formusuario['sexo']=input('Sexo F o M: ')
formusuario['telefono']=input('Telefono: ')
formusuario['email']=input('Email: ')
formusuario['ciudad']=input('Ciudad: ')
formusuario['password']=getpass.getpass('Password: ')
formusuario['cpassword']=getpass.getpass('Confirmar Password: ')


if validator.validar_usuario(formusuario)=={}:
    user=Usuario(formusuario['nombrecom'],formusuario['fechanac'],formusuario['sexo'],formusuario['telefono'],formusuario['email'],formusuario['ciudad'],formusuario['password'])
    user.save()
    print('usuario registrado exitosamente')
else:
    print(validator.validar_usuario(formusuario))

#user = Usuario("Pedro Maneiro","1985-09-10","M",1121651051,"pedromaneiro@gmail.com", 1 , "pedro1985")
#print(user.get_ciudad)
#user.save()s
#print(user)
