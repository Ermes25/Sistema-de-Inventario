from .proveedores_Modelo import Proveedores
from ..Conectores.db_connector import DBConnector


class ProveedoresControlador:
 def __init__ (self):
    pass
 
 def obtener_todos_los_proveedores(self):
   db = DBConnector ()
   Consulta= "SELECT id_proveedor, nombre_proveedor, numero_proveedor, direccion"
   db.ejecutar_consulta (Consulta)
   resultados= db.cursor.fetcha11()
   db.cerrar_conexion()

   Proveedores = [Proveedores(*fila) for fila in resultados]
   return Proveedores
 
 def buscar_proveedor_por_id(self, id_proveedor):
   db = DBConnector()
   Consulta = "SELECT id_proveedor, nombre_proveedor, numero_proveedor, direccion FROM proveedores WHERE id_proveedor = %s"
   db.ejecutar_consulta(Consulta (id_proveedor,))
   resultado = db.cursor.fetchone()
   db.cerrar_conexion()

   if resultado:
     return Proveedores(*resultado)
   else:
     print("PROVEEDOR NO ENCONTRADO")
     return None
   
   def guardar_proveedor(self, proveedor):
     db = DBConnector()
     if Proveedores.id_proveedor:
       consulta= """UPDATE proveedores
                    SET id_proveedor=%s, nombre_proveedor=%s, numero_proveedor=$s, direccion=%s
                    WHERE id_proveedores=%s"""
       
       datos = (proveedores.id_proveedores, Proveedores.nombre_proveedor, Proveedores.numero_proveedor, proveedores.direccion)

       db.ejecutar_consulta(consulta,datos)
       db.cerrar_conexion()

       def regresar_al_menu(self):
         print("REGRESANDO AL MENU PRINCIPAL")
         

       