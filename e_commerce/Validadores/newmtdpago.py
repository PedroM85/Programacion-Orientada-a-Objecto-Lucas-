from methpago import MethPago
from validacion import validator

def mtdpago():
    formmtdpago={}
    formmtdpago['nombreal']=input('Tipo de Metodo: ')


    if validator.validar_mtd(formmtdpago)=={}:
        mtdpago=MethPago(formmtdpago['nombreal'])
        mtdpago.save()
        print('Metodo de pago registrado exitosamente')
    else:
        print(validator.validar_mtd(formmtdpago))


