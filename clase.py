# Impresoras 3D: número de serie, tecnología de Impresión, vatios(consumo de energía),
# velocidad de impresión, marca, modelo, peso, color, costo fabrica, precio venta, origen,
# descripción de la tecnología.



#Crear la clase que se llame GestorProductos tendrá un atributo que va a ser un array o una lista de productos
#Que la clase tenga la primera función insertar productos(recibe como parámetro todo el objeto producto 1)
#Agregar la función que se llama listar_productos 

#marca, categoria cliente, gestor_productos, objetos, producto, proveedor
from Marca import Marca
from Proveedor import Proveedor
from Modelo import Modelo


marcaUno = Marca(id_marca=1, marca="Marca uno")
marcaDos = Marca(id_marca=1, marca="Marca Dos")
marcaTres = Marca(id_marca=1, marca="Marca tres")


proovedorUno = Proveedor(1, "Telcel")
proveedorDos = Proveedor(2, "Movistasr")
proveedorTres = Proveedor(3, "AT&T")

modeloUno = Modelo(1, "Modelo Uno")
modeloDos = Modelo(2, "Modelo dos")
modeloTres = Modelo(3, "Modelo tres")



class Impresoras3D:
    def __init__(self, nombre_producto, numero_serie, proovedor, vatios, velocidad_impresion, marca, modelo, peso, costo_fabrica, precio_venta, origen, descripcion):
        self.nombre_producto = nombre_producto
        self.numero_serie = numero_serie
        self.proovedor = proovedor
        self.vatios = vatios
        self.velocidad_impresion = velocidad_impresion
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.costo_fabrica = costo_fabrica
        self.precio_venta = precio_venta
        self.origen = origen
        self.descripcion = descripcion

    def __str__(self):
        return f"Numero de serie: {self.numero_serie}, proveedor: {proovedorUno.nombre_proveedor}, Vatios: {self.vatios}, Velocidad de impresion: {self.velocidad_impresion}, Marca = {marcaUno.marca}, Modelo: {modeloUno.modelo}, Peso: {self.peso}, Costo de Fábrica: {self.costo_fabrica}, Precio venta: {self.precio_venta}, Origen: {self.origen}, Descripcion: {self.descripcion} "
# Crear la función calcular_total_pagar(precio_de_venta, cantidad) Calcular el
# pago total con aumento de 16 porciento de iva

    def calular_subTotal_pagar(self, precio_venta, cantidad_venta):
        # iva = .18
        total = precio_venta * cantidad_venta
        return total
    
    def calcular_total_pagar(self, total):
        pagoPronto = total * .18 + total
        return pagoPronto

    def obtener_marca(self, marca):
        return print(f"La marca es {marca}")


#nuevoProducto = Impresoras3D(nombre_producto = "Impresora Apple", numero_serie="asd", tecnologia="mejor", vatios=20, velocidad_impresion=102, marca = "nuevaMarca", modelo= "nuevoModelo", peso=65, costo_fabrica=2100, precio_venta=1200, origen="Puebla", descripcion="El mejor" )


#producto1 = Impresoras3D(nombre_producto = "Impresora INTEL" , numero_serie="asd", tecnologia="mejor", vatios=20, velocidad_impresion=102, marca = nuevaMarca, modelo= nuevoModelo, peso=65, costo_fabrica=2100, precio_venta=1200, origen="Puebla", descripcion="El mejor" )
#roducto2 = Impresoras3D(nombre_producto = "Impresora HP", numero_serie="des", tecnologia="peor", vatios=10, velocidad_impresion=103, marca = nuevaMarca, modelo=nuevoModelo, peso=75, costo_fabrica=2100, precio_venta=1580, origen="Veracruz", descripcion="El peor" )
#producto3 = Impresoras3D(nombre_producto = "Impresora Samsung" ,numero_serie="fdg", tecnologia="mas o menos", vatios=23, velocidad_impresion=104, marca = nuevaMarca, modelo= nuevoModelo, peso=15, costo_fabrica=2100, precio_venta=720, origen="Saltillo", descripcion="El mejorcito" )
#producto4 = Impresoras3D(nombre_producto = "Impresora Lenovo", numero_serie="vcg", tecnologia="muy malo", vatios=240, velocidad_impresion=101, marca = nuevaMarca, modelo=nuevoModelo, peso=85, costo_fabrica=2100, precio_venta=15487, origen="Oaxaca", descripcion="El tremedo" )


#lista = [producto1, producto2, producto3, producto4]








# producto1.calular_total_pagar(precio_venta=20, cantidad_venta = 10)
# producto1.obtener_marca(marca= nuevaMarca.marca)
