import threading
from usuarios import ingresar_usuario, crear_usuario, recuperar_usuario
from automatizaciones import monitor_automatizaciones

def menu_principal():
    while True:
        print("\n¡Bienvenido a Domóga!")
        print("1. Ingresar usuario")
        print("2. ¿Aún no tienes cuenta? Crear nuevo usuario")
        print("3. Recuperar usuario y/o contraseña")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            recuperar_usuario()
        elif opcion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    threading.Thread(target=monitor_automatizaciones, daemon=True).start()
    menu_principal()
