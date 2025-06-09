from ambientes import gestionar_ambientes
from automatizaciones import mostrar_automatizaciones,crear_automatizacion,eliminar_automatizacion
from configuracion import menu_configuracion
from hogares import agregar_hogar,eliminar_hogar
from dispositivos import gestionar_dispositivos

from utils import mostrar_menu

from datos import hogares_disponibles  # importá la lista de hogares

def menu_principal_usuario():
    opciones = {
        "1": {"texto": "Seleccionar hogar", "accion": menu_hogar},
        "2": {"texto": "Administrar automatizaciones del hogar", "accion": mostrar_automatizaciones},
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
    print("Nombre hogar", nombre_hogar)
    opciones = {
        "1": {"texto": "Ambientes", "accion": lambda: gestionar_ambientes(nombre_hogar)},
        "2": {"texto": "Dispositivos", "accion":   lambda: gestionar_dispositivos(nombre_hogar)},
        "3": {"texto": "Automatizaciones del hogar", "accion": lambda: menu_automatizaciones(nombre_hogar)},
        "4": {"texto": "Configuración", "accion": lambda: menu_configuracion(nombre_hogar)},
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


def menu_hogar():
    if not hogares_disponibles:
        print("No hay hogares disponibles. Por favor, agregue uno primero.")
        agregar_hogar()

    while True:
        print("\nSeleccione un hogar:")
        for i, nombre in enumerate(hogares_disponibles, start=1):
            print(f"{i}. {nombre}")
        print("0. Volver")  # <- opción para salir del menú

        opcion = input("Ingrese el número del hogar: ")

        if opcion == "0":
            break  # salir del menú y volver al anterior

        if opcion.isdigit():
            indice = int(opcion) - 1
            if 0 <= indice < len(hogares_disponibles):
                nombre_hogar = hogares_disponibles[indice]
                menu_hogar_opciones(nombre_hogar)
                return  # volver al menú principal luego de seleccionar un hogar

        print("Opción no válida.")

def menu_automatizaciones(nombre_hogar):
    while True:
        print(f"\n Automatizaciones en {nombre_hogar}")
        print("1. Mostrar automatizaciones")
        print("2. Crear automatizaciones")
        print("3. Eliminar automatizaciones")
        print("4. Volver atrás")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_automatizaciones()
        elif opcion == "2":
            crear_automatizacion()
        elif opcion == "3":
            eliminar_automatizacion()
        elif opcion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")
