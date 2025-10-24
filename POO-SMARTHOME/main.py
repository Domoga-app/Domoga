# main.py
import os
from dotenv import load_dotenv
from services import UsuarioService, DispositivoService, TipoDispositivoService
from views import menu_principal
from dao.db_base import _get_connection

load_dotenv()

def verificar_variables_env() -> bool:
    '''
    Esta función sirve para comprobar que el archivo .env este creado
    y cuente con todas las variables necesarias
    '''
    
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    if DB_HOST is None:
        print("Falta la variable DB_HOST en el archivo .env")
        return False
    if DB_PORT is None:
        print("Falta la variable DB_PORT en el archivo .env")
        return False
    if DB_USER is None:
        print("Falta la variable DB_USER en el archivo .env")
        return False
    if DB_PASSWORD is None:
        print("Falta la variable DB_PASSWORD en el archivo .env")
        return False
    if DB_NAME is None:
        print("Falta la variable DB_NAME en el archivo .env")
        return False
    
    return True


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


def limpiar_consola():
    ''' Limpia la consola al iniciar el programa '''
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    if not verificar_variables_env():
        input("Presione Enter para salir.")
        return

    if not probar_conexion_db():
        print("La aplicación no puede iniciar sin conexión a la base de datos.")
        input("Presione Enter para salir.")
        return

    usuario_service = UsuarioService()
    dispositivo_service = DispositivoService()
    tipo_service = TipoDispositivoService()
    
    menu_principal(
        usuario_service, 
        dispositivo_service, 
        tipo_service
    )


if __name__ == "__main__":
    limpiar_consola()
    main()
