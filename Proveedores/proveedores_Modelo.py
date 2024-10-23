import mysql.connector

from ..Conectores.db_connector import DBConnector

class Proveedores:
    def __init__(self,id_proveedor=None, nombre_proveedor=None, numero_proveedor=None, direccion=None):
        self.id_proveedor = id_proveedor
        self.nombre_proveedor = nombre_proveedor
        self.numero_proveedor = numero_proveedor
        self.direccion = direccion
        
    def __str__(self):
        return 
           