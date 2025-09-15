from models.ambientes import gestionar_ambientes
from models.automatizaciones import mostrar_automatizaciones,crear_automatizacion,eliminar_automatizacion
from models.hogares import agregar_hogar,eliminar_hogar
from models.dispositivos import gestionar_dispositivos, ver_dispositivos
from utils.configuracion import eliminar_ambiente,eliminar_automatizacion,eliminar_dispositivo,eliminar_hogar
from utils.utils import mostrar_menu

from data.datos import hogares_disponibles, usuarios

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


def menu_principal_usuario(rol, dni):
  # Opciones generales para todos
    opciones = {}

    if rol in ["admin", "usuario"]:        
        opciones["1"] = {"texto": "Mostrar información personal", "accion": lambda: informacion_personal(dni)}        
        opciones["2"] = {"texto": "Seleccionar hogar", "accion": lambda: menu_hogar(rol)}
        opciones["3"] = {"texto": "Mostrar automatizaciones activas", "accion": mostrar_automatizaciones}

    if rol == "usuario":
        opciones["4"] = {"texto": "Cerrar sesión", "accion": None}
        
    if rol == "admin":
        opciones["4"] = {"texto": "Agregar nuevo hogar", "accion": agregar_hogar}
        opciones["5"] = {"texto": "Eliminar hogar", "accion": menu_eliminar_hogar}
        opciones["6"] = {"texto": "Cambiar rol usuario", "accion": cambiar_rol_usuario}
        opciones["7"] = {"texto": "Cerrar sesión", "accion": None}


    while True:
        opcion = mostrar_menu("Menú principal", opciones)
        if opcion == "4" and rol == "usuario":
            break
        elif opcion == "7" and rol == "admin":
            break
        elif opcion in opciones:
            accion = opciones[opcion]["accion"]
            if accion:
                accion()
        else:
            print("Opción no válida.")

            
def menu_hogar_opciones(nombre_hogar, rol):
    print("Nombre hogar", nombre_hogar)
    if rol == "admin":
        opciones = {
            "1": {"texto": "Ambientes", "accion": lambda: gestionar_ambientes(nombre_hogar, rol)},
            "2": {"texto": "Dispositivos", "accion":   lambda: gestionar_dispositivos(nombre_hogar)},
            "3": {"texto": "Automatizaciones del hogar", "accion": lambda: menu_automatizaciones(nombre_hogar)},
            "4": {"texto": "Configuración", "accion": lambda: menu_configuracion(nombre_hogar)},
            "5": {"texto": "Volver", "accion": None}
        }
    else: 
        opciones = {
            "1": {"texto": "Dispositivos", "accion":   lambda: ver_dispositivos(nombre_hogar)},
            "2": {"texto": "Automatizaciones del hogar", "accion": lambda: menu_automatizaciones(nombre_hogar)},
            "3": {"texto": "Volver", "accion": None}
        }
    
 
    while True:
        opcion = mostrar_menu(f"Menú de {nombre_hogar}", opciones)
        if opcion == "5" and rol == "admin":
            break
        elif opcion == "3" and rol == "usuario":
            break
        elif opcion in opciones:
            opciones[opcion]["accion"]()
        else:
            print("Opción no válida.")


def menu_hogar(rol):
    if not hogares_disponibles:
        if rol == "admin":
            print("No hay hogares disponibles. Por favor, agregue uno primero.")
            agregar_hogar()
        
        print("El administrador no ha agregado ningun hogar por el momento.")
        

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
                menu_hogar_opciones(nombre_hogar, rol)
                return  # volver al menú principal luego de seleccionar un hogar

        print("Opción no válida.")

def menu_eliminar_hogar():
    if not hogares_disponibles:
        print("No hay hogares disponibles para eliminar.")
        return

    while True:
        print("\nSeleccione un hogar para eliminar:")
        for i, nombre in enumerate(hogares_disponibles, start=1):
            print(f"{i}. {nombre}")
        print("0. Cancelar")

        opcion = input("Ingrese el número del hogar a eliminar: ")

        if opcion == "0":
            break  # volver atrás

        if opcion.isdigit():
            indice = int(opcion) - 1
            if 0 <= indice < len(hogares_disponibles):
                nombre_hogar = hogares_disponibles[indice]

                confirmar = input(f"¿Está seguro de eliminar el hogar '{nombre_hogar}'? (s/n): ").lower()
                if confirmar == "s":
                    eliminar_hogar(nombre_hogar)
                return  # salir después de eliminar (si querés, podés sacar este return para seguir borrando más)

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
            "texto": "Eliminar automatización",
            "accion": eliminar_automatizacion
        },
        "4": {"texto": "Volver", "accion": None}
    }
    while True:
        resultado = mostrar_menu("Configuración:", opciones)
        if resultado in ("4", None):
            break
        elif resultado in opciones and opciones[resultado]["accion"]:
            opciones[resultado]["accion"]()
        else:
            print("Opción no válida.")

def cambiar_rol_usuario():
    cambiar_rol = input("Deseas cambiar el rol de un usuario? (s/n): ")
    if cambiar_rol == "s":
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario["nombre"]} ({usuario["rol"]})")
        print("0. Cancelar")
        
        id_usuario = input("Seleccione el id del usuario: ")
        
        if not id_usuario.isdigit():
            print("ERROR: El id debe ser númerico.")
            return
        
        id_usuario = int(id_usuario) - 1
        
        if 0 <= id_usuario <= len(usuarios):
            usuario = usuarios[id_usuario]
            nuevo_rol = input("Ingrese el nuevo rol (admin/usuario): ")
            if nuevo_rol in ["admin", "usuario"]:
                usuario["rol"] = nuevo_rol
                return
            else:
                print("ERROR: Rol inexistente.")        
        else:
            print("ERROR: Usuario inexistente.")        
            
            
def informacion_personal(dni):
    for usuario in usuarios:
        if usuario["dni"] == dni:
            print("\n--- Información Personal ---")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Apellido: {usuario['apellido']}")
            print(f"DNI: {usuario['dni']}")
            print(f"Rol: {usuario['rol']}")
            return
        
    print("No se encontró un usuario con ese DNI.")
    return