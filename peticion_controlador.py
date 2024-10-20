from .peticion_modelos import peticion
from..Conectores.db_connector import DBConnector 

class peticionesControlador:
    def __init__(self):
        pass
    def obtener_todas_peticiones(self):
        db = DBConnector()
        consulta = "SELECT id_peticion, id_producto,cantidad, fecha FROM peticiones"
        db.ejecutar_consulta(consulta)
        resultados = db.cursor.fetchall()
        db.cerrar_conexion()
        
        peticiones = [peticion(*fila)for fila in resultados]
        return peticiones
    def buscar_peticion_por_id(self,id_peticion):
        db = DBConnector()
        consulta ="SELECT id_peticion,id_producto,cantidad,fecha FROM peticiones WHRE id_peticion = %s"
        db.ejecutar_consulta(consulta,(id_peticion))
        resultado = db.cursor.fetchone()
        db.cerrar_conexion()
        
        if resultado:
            return peticion(*resultado)
        else: 
            print("peticion no encontrada ")
            return None
        
        def guardar_peticion(self,peticion):
            db = DBConnector()
            if peticion.id_peticion:
                consulta = """ UPDATE peticiones
                           SET id_producto=%s,cantidad=%s,fecha=%s
                           WHERE id_peticion=%s"""
                datos = (peticion.id_producto,peticion.cantidad,peticion.fecha,peticion.id_peticion)
            
            else:
             consulta ="""INSER INTO peticiones(id_producto,cantidad,fecha ) VALUES(%S,%S,%S)"""     
             
             datos = (peticion.id_producto,peticion.cantidad,peticion.fecha)
             
        db.ejecutar_consulta(consulta , datos)
        db.cerrar_conexion()     
            
                           
            