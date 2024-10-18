import mysql.connector

class DBConector:
    def __init__(self, host='localhost', user='root',password='',database='inventario_db'):
        self.Connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.Connection.cursor()
        
    def ejecutar_consulta(self,consulta,parametros=None):
            
         if parametros:
             self.cursor.execute(consulta,parametros)

         else:
             self.cursor.execute(consulta)
             self.connection.commit()
             
    def cerrar_conexion(self):
          self.cursor.close()
          self.Connection.close()       


















