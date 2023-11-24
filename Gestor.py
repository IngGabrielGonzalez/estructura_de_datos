from GestorProductos import GestorProductos
from clase import producto1, producto2, producto3


nuevoGestor = GestorProductos([])  

nuevoGestor.insertarProducto(producto2)
nuevoGestor.insertarProducto(producto1)
nuevoGestor.insertarProducto(producto3)  
nuevoGestor.listaProducto()
nuevoGestor.eliminarProducto(producto2)
variable  = nuevoGestor.buscarProducto(producto2.numero_serie)

if variable:
    print(variable)
else: print("No se encontró el producto")