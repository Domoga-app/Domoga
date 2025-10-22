from dao import DispositivoDAO
from models import Usuario

def menu_usuario(usuario: Usuario, dispositivo_dao: DispositivoDAO):
    while True:
        print("\n--- Menú Usuario Estandar ---")
        print("1. Consultar mis datos personales")
        print("2. Consultar dispositivos de la casa")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"\n--- Tus Datos --- \n{usuario}")
        elif opcion == "2":
            print("\n--- Dispositivos de la Casa ---")
            dispositivos = dispositivo_dao.obtener_todos()
            if not dispositivos:
                print("No hay dispositivos registrados en la casa.")
            for d in dispositivos:
                print(f"- {d}")
        elif opcion == "3":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")