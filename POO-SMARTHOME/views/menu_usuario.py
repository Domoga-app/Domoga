# views/menu_usuario.py
from models import Usuario
from services import DispositivoService

def menu_usuario(usuario: Usuario, dispositivo_service: DispositivoService):
    while True:
        print("\n--- Menú Usuario Estandar ---")
        print(f"Usuario: {usuario.nombre} {usuario.apellido}")
        print("1. Consultar mis datos personales")
        print("2. Consultar dispositivos de la casa")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            _mostrar_datos_personales(usuario)
        elif opcion == "2":
            _ver_dispositivos(dispositivo_service)
        elif opcion == "3":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")
            
def _mostrar_datos_personales(usuario: Usuario):
    print(f"\n--- Tus Datos ---")
    print(usuario)
    
    
def _ver_dispositivos(dispositivo_service: DispositivoService):
    '''Muestra todos los dispositivos.'''
    print("\n--- Dispositivos de la Casa ---")
    dispositivos = dispositivo_service.obtener_todos()
    if not dispositivos:
        print("No hay dispositivos registrados.")
    else:
        for d in dispositivos:
            print(f"- {d}")