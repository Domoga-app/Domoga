# utils/verificar_variables_env.py
import os
from dotenv import load_dotenv

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