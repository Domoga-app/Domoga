from datos import ambientes, dispositivos

def gestionar_ambientes(hogar):
    print("\nAmbientes:")
    if hogar not in ambientes or not ambientes[hogar]:
        print("No hay ambientes creados.")
    else:
        for amb in ambientes[hogar]:
            print(f"- {amb}")
            for dispositivo in dispositivos:
                if dispositivo['hogar'] == hogar and d['ambiente'] == amb:
                    print(f"  * {d['nombre']} ({dispositivo['estado']})")
    if input("\n¿Desea crear un nuevo ambiente? (s/n): ") == "s":
        nuevo = input("Nombre del nuevo ambiente: ")
        ambientes.setdefault(hogar, []).append(nuevo)
        print(f"Ambiente '{nuevo}' agregado.")