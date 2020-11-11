from usuario import Usuario
from validacion import validator
import getpass 


formusuario={}
formusuario['nombrecom']=input('Nombre completo: ')
formusuario['fechanac']=input('Fecha de Nacimiento: ')
formusuario['sexo']=input('Sexo: ')
formusuario['email']=input('Email: ')
formusuario['ciudad']=input('Ciudad: ')
formusuario['password']=getpass.getpass('Password: ')
formusuario['cpassword']=getpass.getpass('Confirmar Password: ')

print(validator.validar_usuario(formusuario))
"""if validator.validar_usuario(formusuario)=={}:
    user=Usuario(formusuario['nombrecom'],formusuario['fechanac'],formusuario['sexo'],formusuario['email'],formusuario['ciudad'],formusuario['password'],formusuario['cpassword'])
    user.save()
    print('usuario registrado exitosamente')
else:
    print(validator.validar_usuario(formusuario))"""
