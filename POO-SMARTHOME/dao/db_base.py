# dao/db_base.py
import mysql.connector
import os
from dotenv import load_dotenv
from contextlib import contextmanager

def _get_connection():
    '''
    Función simple que crea y devuelve una nueva conexión a la base de datos.
    '''
    
    load_dotenv() # Carga las variables de .env
    
    try:
        conn = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        raise # Lanza el error para que la aplicación sepa que algo falló

@contextmanager
def get_db_cursor():
    '''
    Gestor de contexto que maneja la conexión y el cursor.
    Asegura que SIEMPRE se cierren el cursor y la conexión,
    incluso si ocurre un error.
    '''
    conn = None
    cursor = None
    try:
        conn = _get_connection()
        if conn:
            # dictionary=True es clave para que los resultados sean diccionarios
            cursor = conn.cursor(dictionary=True) 
            yield conn, cursor # Entregamos la conexión Y el cursor
        else:
            raise Exception("No se pudo obtener la conexión a la base de datos.")
            
    except mysql.connector.Error as err:
        print(f"Error de base de datos, revirtiendo cambios: {err}")
        if conn:
            conn.rollback() # Revierte los cambios si algo falla
        raise
    except Exception as e:
        print(f"Error inesperado: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        # Esto se ejecuta SIEMPRE.
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()