from categoria import Categoria
from validacioncate import validatorcate

formcate={}
formcate['nombrecate']=input('Nombre Categoria: ')


if validatorcate.validar_cate(formcate)=={}:
    Cate=Categoria(formcate['nombrecate'])
    Cate.save()
    print('Categoria registrado exitosamente')
else:
    print(validatorcate.validar_cate(formcate))

