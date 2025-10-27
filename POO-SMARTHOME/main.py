# main.py
import os
from services import UsuarioService, DispositivoService, TipoDispositivoService
from views import menu_principal
from utils import ejecutar_con_cierre_controlado, verificar_variables_env, probar_conexion_db

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
    ejecutar_con_cierre_controlado(main)
