from datos import ambientes, dispositivos

def gestionar_ambientes(hogar):
    print("\nAmbientes:")
    if hogar not in ambientes or not ambientes[hogar]:
        print("No hay ambientes creados.")
    else:
        for amb in ambientes[hogar]:
            print(f"- {amb}")
            for dispositivo in dispositivos:
                if dispositivo['hogar'] == hogar and dispositivo['ambiente'] == amb:
                    print(f"  * {dispositivo['nombre']} ({dispositivo['estado']})")
    
    if input("\n¿Desea crear un nuevo ambiente? (s/n): ") == "s":
        nuevo = input("Nombre del nuevo ambiente: ")
       
        crear_ambiente(nuevo, ambientes)
        print(f"Ambiente '{nuevo}' agregado.")


def crear_ambiente(ambiente, arr):
    nuevo_ambiente = {
        "ambiente": ambiente
    }
    arr.append(nuevo_ambiente)