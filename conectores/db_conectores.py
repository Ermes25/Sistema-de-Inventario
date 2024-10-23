import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=" ",
            database="sistema_inventario"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def authenticate_user(username, password):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM usuarios WHERE nombre_usuario = %s AND contrasena = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result is not None
        except Exception as e:
            print(f"Error: {e}")
            return False
    return False
