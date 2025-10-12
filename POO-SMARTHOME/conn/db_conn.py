from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def get_connection():
    try:
        return mysql.connector.connect(
            user= os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            host = os.getenv('DB_HOST'),
            database = os.getenv('DB_NAME'),
            port = os.getenv('DB_PORT')
        )
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None


# Probando la conexión a la base de datos
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("Conexión exitosa a la base de datos.")
        conn.close()
        print("Conexión cerrada correctamente.")
    else:
        print("No se pudo establecer la conexión.")