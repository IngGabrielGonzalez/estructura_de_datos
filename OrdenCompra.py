

#Después de que se crea el carrito, se manda a hacer la OrdenCompra
class OrdenCompra():
    def __init__(self, id, cliente, lista_productos, subTotal, totalPagar, fecha):
        self.id = id
        self.cliente = cliente
        self.lista_productos = lista_productos
        self.subTotal = subTotal
        self.totalPagar = totalPagar
        self.fecha = fecha
    def __str__(self):
        return f"Orden de Compra:\nID: {self.id}\nCliente: {self.cliente}\nLista de Productos: {self.lista_productos}\nSubtotal: ${self.subTotal:.2f}\nFecha: {self.fecha}"

    def mostrarList(self):
        print(self.lista_productos)

# nuevoCliente = Cliente(1,"Pedro","Puebla")

