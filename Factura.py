# Crea la Clase
# Factura. Atributos: Num_factura, fecha, cliente, orden_compra, subtotal,
# total(con iva)
from Carrito import Carrito

class Factura:
    def __init__(self, num_factura, fecha, cliente, orden_compra, subtotal, total):
        self.num_factura = num_factura
        self.fecha = fecha
        self.cliente = cliente
        self.orden_compra = orden_compra
        self.subtotal = subtotal
        self.total = total
        
        #imprimir
#     Num_factura,
#     fecha, rfc del cliente, nombre del cliente, orden_de_compra,



    def mostrar_factura(self):
        
        print("******************** FACTURA ELECTRÓNICA ********************")
        print(f"**     Número de Factura: {self.num_factura}                **")
        print("***********************************************************")
        print(f"** Fecha: {self.fecha}")
        print(f"** Cliente: {self.cliente}")
        print(f"** {(str(self.orden_compra))}")
        print(f"** Subtotal: ${self.subtotal}")
        print(f"** Total: ${self.total}")
        print("***********************************************************")



        