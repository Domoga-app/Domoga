# utils/probar_conexion_db.py
from dao.db_base import _get_connection


def probar_conexion_db() -> bool:
    '''
    Esta función primero se asegura de que si se pudo establecer la conexión a la base de datos
    caso contrario el programa no puede ejecutarse
    '''
    try:
        conn = _get_connection()
        if conn and conn.is_connected():
            conn.close()
            return True
        else:
            print("Error: No se pudo establecer la conexión inicial con la BD.")
            return False
    except Exception as e:
        print(f"Error fatal al conectar a la BD: {e}")
        return False