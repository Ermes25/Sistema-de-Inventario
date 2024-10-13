from .modelo_Pedido import Peticion
from ..Connectores import DBConnector

class PeticionesControlador:
    def __init__(self):
        pass

    def obtener_todas_peticiones(self):
        db = DBConnector()
        consulta = "SELECT id_peticion, id_producto, cantidad, fecha FROM peticiones"
        db.ejecutar_consulta(consulta)
        resultados = db.cursor.fetchall()
        db.cerrar_conexion()

        peticiones = [Peticion(*fila) for fila in resultados]
        return peticiones

    def buscar_peticion_por_id(self, id_peticion):
        db = DBConnector()
        consulta = "SELECT id_peticion, id_producto, cantidad, fecha FROM peticiones WHERE id_peticion = %s"
        db.ejecutar_consulta(consulta, (id_peticion,))
        resultado = db.cursor.fetchone()
        db.cerrar_conexion()

        if resultado:
            return Peticion(*resultado)
        else:
            print("Petición no encontrada")
            return None

    def guardar_peticion(self, peticion):
        db = DBConnector()
        if peticion.id_peticion:
            consulta = """UPDATE peticiones 
                          SET id_producto=%s, cantidad=%s, fecha=%s 
                          WHERE id_peticion=%s"""
            datos = (peticion.id_producto, peticion.cantidad, peticion.fecha, peticion.id_peticion)
        else:
            consulta = """INSERT INTO peticiones (id_producto, cantidad, fecha) 
                          VALUES (%s, %s, %s)"""
            datos = (peticion.id_producto, peticion.cantidad, peticion.fecha)

        db.ejecutar_consulta(consulta, datos)
        db.cerrar_conexion()

    def regresar_al_menu(self):
        print("Regresando al menú principal...")
        # Lógica para volver a la vista del menú principal en la interfaz gráfica
