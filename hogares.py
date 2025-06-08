import ambientes
import dispositivos as disp
import automatizaciones as auto
import configuracion
import datos

def menu_principal_usuario():
    while True:
        print("\n1. Seleccionar hogar")
        print("2. Administrar automatizaciones del hogar")
        print("3. Agregar nuevo hogar")
        print("4. Eliminar hogar")
        print("5. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_hogar()
        elif opcion == "2":
            auto.mostrar_automatizaciones()
        elif opcion == "3":
            agregar_hogar()
        elif opcion == "4":
            eliminar_hogar()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

from datos import hogares_disponibles  # importá la lista de hogares

def menu_hogar():
    if not datos.hogares_disponibles:
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
        
def agregar_hogar():
    nuevo_hogar = input("Ingrese el nombre del nuevo hogar: ")
    if nuevo_hogar and nuevo_hogar not in hogares_disponibles:
        hogares_disponibles.append(nuevo_hogar)
        print(f"Hogar '{nuevo_hogar}' agregado.")
    else:
        print("Nombre inválido o ya existe.")

def eliminar_hogar():
    if not datos.hogares_disponibles:
        print("No hay hogares para eliminar.")
        return

    print("\nSeleccione el hogar que desea eliminar:")
    for i, nombre in enumerate(hogares_disponibles, start=1):
        print(f"{i}. {nombre}")

    opcion = input("Ingrese el número del hogar a eliminar: ")
    
    if opcion.isdigit():
        indice = int(opcion) - 1
        if 0 <= indice < len(hogares_disponibles):
            nombre_hogar = hogares_disponibles[indice]
            confirmacion = input(f"¿Está seguro que desea eliminar el hogar '{nombre_hogar}'? (s/n): ").lower()
            if confirmacion == 's':
                eliminado = hogares_disponibles.pop(indice)
                print(f"Hogar '{eliminado}' eliminado.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Número fuera de rango.")
    else:
        print("Opción no válida.")

def menu_hogar_opciones(nombre_hogar):
    while True:
        print(f"\nMenú de {nombre_hogar}:")
        print("1. Ambientes")
        print("2. Dispositivos")
        print("3. Automatizaciones del hogar")
        print("4. Configuración")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ambientes.gestionar_ambientes(nombre_hogar)
        elif opcion == "2":
            disp.gestionar_dispositivos(nombre_hogar)
        elif opcion == "3":
            auto.mostrar_automatizaciones()
        elif opcion == "4":
            configuracion.menu_configuracion(nombre_hogar)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")