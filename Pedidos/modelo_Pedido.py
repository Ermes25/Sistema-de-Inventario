from ..Conectores.db_connector import DBConnector

class Peticion:
    def __init__(self, id_peticion=None, id_producto=None, cantidad=0, fecha=''):
        self.id_peticion = id_peticion
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.fecha = fecha

    def __str__(self):
        return f"Petición de producto ID: {self.id_producto} - Cantidad: {self.cantidad}"
