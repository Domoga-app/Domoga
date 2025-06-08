from datos import ambientes, automatizaciones

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
            eliminar_hogar(hogar)
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
    dispositivos_en_hogar = []
    for ambiente in ambientes:
        if ambiente["hogar"] == hogar:
            for dispositivo in ambiente["dispositivos"]:
                dispositivos_en_hogar.append((ambiente, dispositivo))
    
    if not dispositivos_en_hogar:
        print("No hay dispositivos en este hogar.")
        return

    for i, (ambiente, dispositivo) in enumerate(dispositivos_en_hogar, 1):
        print(f"{i}. {dispositivo['nombre']} (Ambiente: {ambiente['ambiente']})")
    
    idx = int(input("Seleccione el número del dispositivo a eliminar: ")) - 1
    if 0 <= idx < len(dispositivos_en_hogar):
        ambiente, dispositivo = dispositivos_en_hogar[idx]
        ambiente["dispositivos"].remove(dispositivo)
        print(f"Dispositivo '{dispositivo['nombre']}' eliminado.")
    else:
        print("Selección inválida.")

def eliminar_ambiente(hogar):
    ambientes_del_hogar = [amb for amb in ambientes if amb["hogar"] == hogar]
    
    if not ambientes_del_hogar:
        print("No hay ambientes en este hogar.")
        return

    for i, amb in enumerate(ambientes_del_hogar, 1):
        print(f"{i}. {amb['ambiente']}")
    
    idx = int(input("Seleccione el ambiente a eliminar: ")) - 1
    if 0 <= idx < len(ambientes_del_hogar):
        ambiente_a_eliminar = ambientes_del_hogar[idx]
        ambientes.remove(ambiente_a_eliminar)
        print(f"Ambiente '{ambiente_a_eliminar['ambiente']}' eliminado.")
    else:
        print("Selección inválida.")

def eliminar_hogar(hogar):
    global ambientes
    ambientes = [amb for amb in ambientes if amb["hogar"] != hogar]
    print(f"Hogar '{hogar}' eliminado.")

def eliminar_automatizacion():
    if not automatizaciones:
        print("No hay automatizaciones.")
        return

    for i, a in enumerate(automatizaciones, 1):
        print(f"{i}. {a['nombre']}")
    
    idx = int(input("Seleccione la automatización a eliminar: ")) - 1
    if 0 <= idx < len(automatizaciones):
        auto = automatizaciones.pop(idx)
        print(f"Automatización '{auto['nombre']}' eliminada.")
    else:
        print("Selección inválida.")
