from usuario import Usuario
from validacionuedit import validatoredit


formusuario={}
formusuario['id']=input("Indique id de usuario: ")
formusuario['nombrecom']=input('Nombre completo: ')
formusuario['fechanac']=input('Fecha de Nacimiento AAAA-MM-DD: ')
formusuario['sexo']=input('Sexo F o M: ')
formusuario['telefono']=input('Telefono: ')
formusuario['email']=input('Email: ')
formusuario['ciudad']=input('Ciudad: ')
#formusuario['password']=getpass.getpass('Password: ')
#formusuario['cpassword']=getpass.getpass('Confirmar Password: ')



if validatoredit.validar_usuario_edit(formusuario)=={}:
    user=Usuario(formusuario['id'],formusuario['nombrecom'],formusuario['fechanac'],formusuario['sexo'],formusuario['telefono'],formusuario['email'],formusuario['ciudad'])
    user.update()
    print('usuario Actualizado exitosamente')
else:
    print(validatoredit.validar_usuario_edit(formusuario))

# user = Usuario("32","Pedro Maneiro","1985-09-10","M",1121651051,"pedromaneiro@gmail.com", 1)
# print(user.get_nombrecom())
# #user.save()
# #print(user.get_nombre())
