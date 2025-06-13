from ambientes import gestionar_ambientes
from automatizaciones import mostrar_automatizaciones,crear_automatizacion,eliminar_automatizacion
from hogares import agregar_hogar,eliminar_hogar
from dispositivos import gestionar_dispositivos
from configuracion import eliminar_ambiente,eliminar_automatizacion,eliminar_dispositivo,eliminar_hogar
from utils import mostrar_menu

from datos import hogares_disponibles 

# Refactorizar funcion de ejecutar_menu

def mostrar_menu_para(usuario):
    rol = usuario.get("rol")
    funcion_menu = menus_por_rol.get(rol)
    if funcion_menu:
        funcion_menu()
    else:
        print(f"Rol desconocido: {rol}")

def menu_admin():
    menu_principal_usuario("admin")

def menu_usuario():
    menu_principal_usuario("usuario")


menus_por_rol = {
    "admin": menu_admin,
    "usuario": menu_usuario,
}


def menu_principal_usuario(rol):
  # Opciones generales para todos
    opciones = {}

    if rol in ["admin", "usuario"]:
        opciones["1"] = {"texto": "Seleccionar hogar", "accion": menu_hogar}
        opciones["2"] = {"texto": "Administrar automatizaciones del hogar", "accion": mostrar_automatizaciones}

    if rol == "admin":
        opciones["3"] = {"texto": "Agregar nuevo hogar", "accion": agregar_hogar}
        opciones["4"] = {"texto": "Eliminar hogar", "accion": eliminar_hogar}

    opciones["5"] = {"texto": "Cerrar sesión", "accion": None}

    while True:
        opcion = mostrar_menu("Menú principal", opciones)
        if opcion == "5":
            break
        elif opcion in opciones:
            accion = opciones[opcion]["accion"]
            if accion:
                accion()
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
    opciones = {
        "1": {
            "texto": "Mostrar automatizaciones",
            "accion": mostrar_automatizaciones
        },
        "2": {
            "texto": "Crear automatizaciones",
            "accion": crear_automatizacion
        },
        "3": {
            "texto": "Eliminar automatizaciones",
            "accion": eliminar_automatizacion
        },
        "4": {
            "texto": "Volver atrás",
            "accion": lambda: None
        }
    }
    while True:
        resultado = mostrar_menu(f"Automatizaciones en {nombre_hogar}", opciones)
        if resultado is None or resultado == "4":
            break
        elif resultado in opciones and opciones[resultado]["accion"]:
            opciones[resultado]["accion"]()
        else:
            print("Opción no válida.")
        

def menu_configuracion(hogar):
    opciones = {
        "1": {
            "texto": "Eliminar dispositivos",
            "accion": lambda: eliminar_dispositivo(hogar)
        },
        "2": {
            "texto": "Eliminar ambiente",
            "accion": lambda: eliminar_ambiente(hogar)
        },
        "3": {
            "texto": "Eliminar hogar",
            "accion": lambda: (eliminar_hogar(hogar), None)[1]
        },
        "4": {
            "texto": "Eliminar automatización",
            "accion": eliminar_automatizacion
        },
        "5": {"texto": "Cerrar sesión", "accion": None},
        "6": {"texto": "Volver", "accion": None}
    }
    while True:
        resultado = mostrar_menu("Configuración:", opciones)
        if resultado in ("5", "6", None):
            break
        elif resultado in opciones and opciones[resultado]["accion"]:
            opciones[resultado]["accion"]()
        else:
            print("Opción no válida.")


