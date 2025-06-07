import ambientes
import dispositivos as disp
import automatizaciones as auto
import configuracion

def menu_principal_usuario():
    while True:
        print("\n1. Seleccionar hogar")
        print("2. Administrar automatizaciones del hogar")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_hogar()
        elif opcion == "2":
            auto.mostrar_automatizaciones()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

def menu_hogar():
    print("\n1. hogar")
    print("2. casa campo")
    opcion = input("Seleccione un hogar: ")
    nombre_hogar = "hogar" if opcion == "1" else "casa campo" if opcion == "2" else None
    if nombre_hogar:
        menu_hogar_opciones(nombre_hogar)
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