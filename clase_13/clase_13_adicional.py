"""
CLASE 13 - Programación Orientada a objetos II
"""

class Producto:

    def __init__(self, codigo, precio, detalle, unid_med, promo_desc):
        self.codigo = codigo
        self.precio = precio
        self.detalle = detalle
        self.unid_med = unid_med
        self.promo_desc = promo_desc
    
    def __str__(self):
        return f"{self.detalle} - {self.unid_med}: $ {self.precio}"


class Pedido:
    
    __cantidad_de_pedidos = 0

    def __init__(self):
        self.lista_pedido = []
        Pedido.__cantidad_de_pedidos += 1

    def agregar_producto(self, producto):
        self.lista_pedido.append(producto)

    def obtener_total(self):
        suma = 0.0
        for producto in self.lista_pedido:
            suma += producto.precio
        return suma
    
    def devuelve_cantidad_pedidos(self):
        return Pedido.__cantidad_de_pedidos
    
    def __len__(self):
        return len(self.lista_pedido)

