#Se encarga de gestión de los productos de la tienda, inserta, elimina, lista y busca productos

class GestorProductos:
    def __init__(self):
        self.lista_productos = []


    def __str__(self):
        return f"MiObjeto: {self.nombre}"


    #Inserta los productos en una lista productos
    def insertarProducto(self, objeto_recibir):
        self.lista_productos.append(objeto_recibir)

    #Nos regresa los productos que hay disponibles
    def lista_de_productos(self):
        if not self.lista_productos:
            print("No hay productos disponibles")
        else:
            print("Lista de productos:")
            for producto in self.lista_productos:
                print(producto.numero_serie)

    #Elimina un producto de la lista de productos, pasándole el id del producto
    def eliminarProducto(self, id_producto):
        for producto in self.lista_productos:
            if producto.numero_serie == id_producto:
                self.lista_productos.remove(producto)
                return
        print("Producto no encontrado")

    #Busca un producto por su id, y nos regresa los productos
    def buscar_producto(self, id_producto):
        for p in self.lista_productos:
            print("Lista de productos:")
            if p.numero_serie == id_producto:
                print(f"Producto {p.numero_serie} , descripción: {p.descripcion}")
            else: print("El producto no se encuentra en sistema")
        return None

#Que lo retorne y quien se encarga de imprimirlo es en los objetos


# nuevoGestor = GestorProductos([])  

# nuevoGestor.insertarProducto(producto2)
# nuevoGestor.insertarProducto(producto1)
# nuevoGestor.insertarProducto(producto3)  
# nuevoGestor.listaProducto()
# nuevoGestor.eliminarProducto(producto2)
# variable = nuevoGestor.eliminarProducto(producto4)

# if not variable:
#     print("No se pudo eliminar porque el producto no existe")
# else: print("Producto eliminado")

# nuevoGestor.listaProducto()




# nuevoGestor.buscarProducto(producto1.numero_serie)
