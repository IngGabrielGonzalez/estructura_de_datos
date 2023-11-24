from Carrito import Carrito
from Pagos import Pagos
from datetime import datetime
from OrdenCompra import OrdenCompra
from clase import Impresoras3D
from GestorProductos import GestorProductos
from Factura import Factura


class Cliente:
    def __init__(self, id_cliente, nombre, estado, rfc, ):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.estado =estado
        # self.lista_ordenes_compra = lista_ordenes_compra
        self.rfc = rfc

#  eNTRA COMO PARÁMETRO EL OBJETO EL PAGO DEL CLIENTE
    def agregar_pago(self, nPagos):
        lista_pagos = []
        fecha = datetime.now()
        self.nPagos = nPagos
        lista_pagos.append(nPagos)
        for item in lista_pagos:
            print(f"{item.id} {item.metodo_pago} {item.monto} {item.referencia} {fecha}")
            # id, cliente, lista_productos, fecha
    def datos_orden(self, orden):
            print(f"{orden.id} {orden.cliente} {orden.lista_productos} {orden.fecha} {orden.totalPagar}")     


    def agregar_orden_compra(self, orden):
        self.lista_ordenes_compra = []
        self.orden = orden
        self.lista_ordenes_compra.append(orden)
        for i in self.lista_ordenes_compra:
            print(f"{i.id}")
            
    def listar_facturas(self, precio_venta, cantidad, importe):
        print(f"{self.nombre} {precio_venta} {cantidad} {importe}")






#Se crea el producto para agregar al gestor de productos
nuevoProducto = Impresoras3D(nombre_producto = "Impresora Lenovo", numero_serie="vcg", tecnologia="muy malo", vatios=240, velocidad_impresion=101, marca = "Lenovo", modelo="104l-g234", peso=85, costo_fabrica=2100, precio_venta=1000, origen="Oaxaca", descripcion="El tremedo")


nuevoGestor = GestorProductos()  

#***** Lista los productos del GESTOR PRODUCTOS *****
nuevoGestor.insertarProducto(nuevoProducto)



#Se crea el cliente para utilizarlo en el carrito ✓
nuevoCliente = Cliente(1, "Gabriel", "Oaxaca", "SAD1234AS")



#Se crea el cliente ✓
nuevoCliente = Cliente(1,"Pedro","Puebla", "MUAS98344")


#Se crea el carrito para que el cliente ingrese los productos a comprar ✓
nuevoCarrito = Carrito(nuevoCliente) 

#Se manda a llamar los productos existentes ✓
# nuevoGestor.lista_de_productos()

#Se agrega el producto al carrito ✓
nuevoCarrito.agregar_producto_carrito(nuevoProducto, 1)
nuevoCarrito.agregar_producto_carrito(nuevoProducto, 1)

print("Xxcxx")
nuevoCarrito.listar_productos()
print("Xxcxx")
#Listar productos del carrito ✓
# nuevoCarrito.listar_productos()

# nuevoProducto.calular_total_pagar(nuevoProducto.precio_venta, 2)

#Crear la orden compra
fecha = datetime.now()
nuevaOrdenCompra = OrdenCompra(1, nuevoCliente.nombre, nuevoCarrito.listar_productos(), nuevoProducto.calular_subTotal_pagar(nuevoProducto.precio_venta, 2), 1, fecha)


#Crear la factura de la compra
# num_factura, fecha, cliente, orden_compra, subtotal, total
nuevaFactura = Factura(1, fecha, nuevoCliente.nombre, nuevaOrdenCompra, nuevoProducto.calular_subTotal_pagar(nuevoProducto.precio_venta, 2), nuevoProducto.calcular_total_pagar(nuevoProducto.calular_subTotal_pagar(nuevoProducto.precio_venta, 2)))



#Mostramos la factura
nuevaFactura.mostrar_factura()








