from datos import dispositivos, ambientes, automatizaciones

def menu_configuracion(hogar):
    while True:
        print("\nConfiguración:")
        print("1. Eliminar dispositivos")
        print("2. Eliminar ambiente")
        print("3. Eliminar hogar")
        print("4. Eliminar automatización")
        print("5. Cerrar sesión")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            eliminar_dispositivo(hogar)
        elif opcion == "2":
            eliminar_ambiente(hogar)
        elif opcion == "3":
            ambientes.pop(hogar, None)
            dispositivos[:] = [d for d in dispositivos if d['hogar'] != hogar]
            print(f"Hogar '{hogar}' eliminado.")
            break
        elif opcion == "4":
            eliminar_automatizacion()
        elif opcion == "5":
            break
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

def eliminar_dispositivo(hogar):
    dispositivos_hogar = [d for d in dispositivos if d['hogar'] == hogar]
    for i, d in enumerate(dispositivos_hogar, 1):
        print(f"{i}. {d['nombre']}")
    idx = int(input("Seleccione el número del dispositivo a eliminar: ")) - 1
    if 0 <= idx < len(dispositivos_hogar):
        dispositivos.remove(dispositivos_hogar[idx])
        print("Dispositivo eliminado.")

def eliminar_ambiente(hogar):
    if hogar in ambientes:
        for i, amb in enumerate(ambientes[hogar], 1):
            print(f"{i}. {amb}")
        idx = int(input("Seleccione el ambiente a eliminar: ")) - 1
        if 0 <= idx < len(ambientes[hogar]):
            amb = ambientes[hogar].pop(idx)
            dispositivos[:] = [d for d in dispositivos if d['ambiente'] != amb or d['hogar'] != hogar]
            print(f"Ambiente '{amb}' eliminado.")

def eliminar_automatizacion():
    for i, a in enumerate(automatizaciones, 1):
        print(f"{i}. {a['nombre']}")
    idx = int(input("Seleccione la automatización a eliminar: ")) - 1
    if 0 <= idx < len(automatizaciones):
        auto = automatizaciones.pop(idx)
        print(f"Automatización '{auto['nombre']}' eliminada.")