# from Clientes import Cliente


#En el carrito podemos agregar, listar, eliminar productos y calcular el total de la compra
class Carrito:

    #El método constructor recibe todo el objeto
    def __init__(self, objetoCliente):
        self.objetoCliente = objetoCliente
        self.productos = []
        pass
    def agregar_producto_carrito(self, producto, cantidad):
        self.productos.append({"producto": producto.nombre_producto, "cantidad": cantidad})
        print("El producto ha sido agregado con éxito")


    
    def listar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos disponibles")
        else:   
            lista_productos = []
            for item in self.productos:
                lista_productos.append(item["producto"])
                # lista_productos.append(item["cantidad"])
            return lista_productos
                
    # def calcular_total(self):
    #     for item in self.productos:
    #         total = 0
    #         producto = item["cantidad"]
    #         cantidad = item["cantidad"]
    #         total += producto * cantidad
    #     return print(total)

    def eliminar_productos(self, numero_serie):
        self.numero_serie = numero_serie
        if len(self.productos) == 0:
            print("No se puede eliminar porque no existen productos en el carrito")
        else:
            for item in self.productos:
                if self.numero_serie == item["producto"].numero_serie:
                    self.productos.remove(item)
                    print(f"El producto con número de serie: {numero_serie} ha sido eliminado")
                else: return print("El producto no existe")
    def get_lista_prod(self):
        for item in self.productos:
            producto = item["producto"]
            cantidad = item["cantidad"]
            print(f"Producto {producto.descripcion}, Clave: {producto.numero_serie} , cantidad: {cantidad}\n")


    def __str__(self):
        return f"Carrito de {self.objetoCliente} con {len(self.productos)} productos"


# nuevoCarrito.agregar_producto_carrito(producto1, 3)
# nuevoCarrito.agregar_producto_carrito(producto2, 2)
# nuevoCarrito.listar_productos()
# print("1.- Agregar producto al carrito")
# print("2.-Calcular total")
# print("3.- Listar productos")
# print("4.- Eliminar productos")
# producto1 = Impresoras3D(numero_serie=123456, tecnologia="mejor", vatios=20, velocidad_impresion=102, marca = "x", modelo= "otrox", peso=65, costo_fabrica=2100, precio_venta=1570, origen="Puebla", descripcion="El mejor" )

# opc = int(input())
# if opc == 1:
#     numero_serie = int(input("Agrega el numero de serie del producto que deseas agregar"))
#     cantidad = int(input("Ingresa la cantidad que deseas agregar"))
#     nuevoCarrito.agregar_producto_carrito(numero_serie, cantidad)
# elif opc == 2:
#     nuevoCarrito.calcular_total()
# elif opc == 3:
#     nuevoCarrito.listar_productos()
# elif opc == 4:
#     nuevoCarrito.listar_productos()
#     numero_serie = int(input("Ingresa la clave a eliminar"))
#     nuevoCarrito.eliminar_productos(numero_serie)
# elif opc==5:
#     nuevoCarrito.get_lista_prod()
# nuevoCarrito.eliminar_productos(numero_serie)
# nuevoCarrito.listar_productos()


