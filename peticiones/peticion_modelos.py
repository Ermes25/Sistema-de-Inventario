import mysql.connector
from ..Conectores.db_connctor import DBConnector

class peticion: 
   def __init__ (self,id_pedido=None,nombre_cliente=None,fecha_pedido='',cantidad_pedido=None):
       self.id_pedido = id_pedido
       self.nombre_cliente =  nombre_cliente
       self.fecha_pedido = fecha_pedido
       self.cantidad_pedido = cantidad_pedido
    
    def __str__(self):
         return f"peticion "