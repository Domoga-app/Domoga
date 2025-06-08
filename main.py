import threading
from usuarios import ingresar_usuario, crear_usuario, recuperar_usuario
from automatizaciones import monitor_automatizaciones

from utils import mostrar_menu

def menu_principal():
    opciones = {
        "1": {"texto": "Ingresar usuario", "accion": ingresar_usuario},
        "2": {"texto": "¿Aún no tienes cuenta? Crear nuevo usuario", "accion": crear_usuario},
        "3": {"texto": "Recuperar usuario y/o contraseña", "accion": recuperar_usuario},
        "4": {"texto": "Salir", "accion": None}
    }
       
    while True:
        opcion = mostrar_menu("¡Bienvenido a Domóga!", opciones)
        if opcion == "4":
            break
        elif opcion in opciones:
            opciones[opcion]["accion"]()
        else:
            print("Opción no válida.")
         
        

if __name__ == "__main__":
    threading.Thread(target=monitor_automatizaciones, daemon=True).start()
    menu_principal()