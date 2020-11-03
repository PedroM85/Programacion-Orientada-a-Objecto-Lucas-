class Compra():
    def __init__(self, usuario,producto,methpago,cantidad,subtotal):
        self.usuario=usuario
        self.producto=producto
        self.methpago=methpago
        self.cantidad=cantidad
        self.subtotal=subtotal
    
    def get_usuario(self):
        return self.usuario
    def set_usuario(self,usuario):
        self.usuario=usuario
    def get_producto(self):
        return self.producto
    def set_producto(self,producto):
        self.producto=producto
    def get_methpago(self):
        return self.methpago
    def set_methpago(self,methpago):
        self.methpago=methpago
    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self,cantidad):
        self.cantidad=cantidad
    def get_subtotal(self):
        return self.subtotal
    def set_subtotal(self,subtotal):
        self.subtotal=subtotal