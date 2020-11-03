class bazaar():
    def __init__(self):
        self.empleados=[]
        self.articulos=[]
        self.caja = 0


    def agregar_empleado(self,empleado):
        self.empleados.append(empleado)
    def sacar_empleado(self,empleado):
        self.empleados.remove(empleado)
    def agregar_articulo(self,articulo):
        self.empleados.append(articulo)
    def sacar_articulo(self,articulo):
        self.empleados.remove(articulo)
    def liquidar_sueldo(self):
        resultado = 0
        for empleado in self.empleados:
            resultado += empleado.get_sueldo() + empleado.get_comision()
        return resultado


