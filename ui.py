import ambientes
import dispositivos as disp
import automatizaciones as auto
import configuracion
from hogares import menu_hogar, agregar_hogar,eliminar_hogar

from utils import mostrar_menu

def menu_principal_usuario():
    opciones = {
        "1": {"texto": "Seleccionar hogar", "accion": menu_hogar},
        "2": {"texto": "Administrar automatizaciones del hogar", "accion": auto.mostrar_automatizaciones},
        "3": {"texto": "Agregar nuevo hogar", "accion": agregar_hogar},
        "4": {"texto": "Eliminar hogar", "accion": eliminar_hogar},
        "5": {"texto": "Cerrar sesión", "accion": None}
     }
    while True:
        opcion = mostrar_menu("Menú principal", opciones)
        if opcion == "5":
            break
        elif opcion in opciones:
            opciones[opcion]["accion"]()
        else:
            print("Opción no válida.")

            
def menu_hogar_opciones(nombre_hogar):
    opciones = {
        "1": {"texto": "Ambientes", "accion": lambda: ambientes.gestionar_ambientes(nombre_hogar)},
        "2": {"texto": "Dispositivos", "accion": lambda: disp.gestionar_dispositivos(nombre_hogar)},
        "3": {"texto": "Automatizaciones del hogar", "accion": auto.mostrar_automatizaciones},
        "4": {"texto": "Configuración", "accion": lambda: configuracion.menu_configuracion(nombre_hogar)},
        "5": {"texto": "Volver", "accion": None}
     }
 
    while True:
        opcion = mostrar_menu(f"Menú de {nombre_hogar}", opciones)
        if opcion == "5":
            break
        elif opcion in opciones:
            opciones[opcion]["accion"]()
        else:
            print("Opción no válida.")