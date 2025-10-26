# main.py
import os
from dotenv import load_dotenv
from services import UsuarioService, DispositivoService, TipoDispositivoService
from views import menu_principal
from dao.db_base import _get_connection


def verificar_variables_env() -> bool:
    """
    Esta función verifica que exista el archivo .env
    y que contenga todas las variables necesarias para la conexión.
    """
    if not os.path.exists(".env"):
        print("No se encontró el archivo .env en el directorio actual.")
        return False

    load_dotenv()

    # Lista de variables requeridas
    variables_requeridas = ["DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME"]

    # Verificamos cada variable con for para evitar repetición de código
    for var in variables_requeridas:
        if os.getenv(var) is None:
            print(f"Falta la variable {var} en el archivo .env")
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
