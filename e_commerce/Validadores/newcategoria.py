from categoria import Categoria
from validacion import validator

def categorias():
    formcate={}
    formcate['nombrecate']=input('Nombre Categoria: ')
    formcate['edit']="0"

    if validator.validar_cate(formcate)=={}:
        Cate=Categoria("",formcate['nombrecate'])
        Cate.save()
        print('Categoria registrado exitosamente')
    else:
        print(validator.validar_cate(formcate))

