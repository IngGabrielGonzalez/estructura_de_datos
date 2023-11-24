from clase import *
from Pilas import *
from Cola import * 

miPila = Stack()
miCola = Cola()
producto1 = Impresoras3D(nombre_producto = "Impresora INTEL" , numero_serie="asd", proovedor= proovedorUno.nombre_proveedor, vatios=20, velocidad_impresion=102, marca = marcaUno, modelo= modeloUno, peso=65, costo_fabrica=2100, precio_venta=1200, origen="Puebla", descripcion="El mejor" )
miPila.apilar(producto1)


producto2 = Impresoras3D(nombre_producto = "Impresora CANON" , numero_serie="asd", proovedor=proveedorDos.nombre_proveedor, vatios=20, velocidad_impresion=102, marca = marcaDos, modelo= modeloDos, peso=65, costo_fabrica=2100, precio_venta=1200, origen="Puebla", descripcion="El mejor" )
miPila.apilar(producto2)


producto3 = Impresoras3D(nombre_producto = "Monitor DELL" , numero_serie="asd", proovedor= proveedorTres.nombre_proveedor, vatios=20, velocidad_impresion=102, marca = marcaTres, modelo= modeloTres, peso=65, costo_fabrica=2100, precio_venta=1200, origen="Puebla", descripcion="El mejor" )
miPila.apilar(producto3)


producto4 = Impresoras3D(nombre_producto = "Computadora HP" , numero_serie="asd", proovedor=proovedorUno.nombre_proveedor, vatios=20, velocidad_impresion=102, marca = marcaUno, modelo= modeloUno, peso=65, costo_fabrica=2100, precio_venta=1200, origen="Puebla", descripcion="El mejor" )
miPila.apilar(producto4)


# print(len(miPila))
# for ele in miPila:
#     print(ele)
#     print('Pila después de desapilar')
# miPila.desapilar()
# for ele in miPila:
#     print(ele)

miCola.agregarCola(producto1)
miCola.agregarCola(producto2)
miCola.agregarCola(producto3)
miCola.agregarCola(producto4)


for ele in miCola:
    print(ele)
print("Pila después de entregar el primero de la fila")
miCola.extrarDeLaCola()
for ele in miCola:
    print(ele)