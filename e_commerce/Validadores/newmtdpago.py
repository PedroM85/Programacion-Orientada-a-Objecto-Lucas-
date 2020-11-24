from methpago import MethPago
from validacionmtdpago import validatormtdpago

formmtdpago={}
formmtdpago['nombreal']=input('Tipo de Metodo: ')


if validatormtdpago.validar_mtd(formmtdpago)=={}:
    mtdpago=MethPago(formmtdpago['nombreal'])
    mtdpago.save()
    print('Metodo registrado exitosamente')
else:
    print(validatormtdpago.validar_mtd(formmtdpago))


