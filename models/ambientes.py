from data.datos import ambientes

def gestionar_ambientes(hogar, rol):
    print("\nAmbientes:")
    ambientes_hogar = [a for a in ambientes if a['hogar'] == hogar]
    
    if not ambientes_hogar:
        print("No hay ambientes creados.")
    else:
        for amb in ambientes_hogar:
            print(f"- {amb['ambiente']}")
            if amb['dispositivos']:
                for dispositivo in amb['dispositivos']:
                    print(f"  * {dispositivo['nombre']} ({dispositivo['estado']})")
            else:
                print("  (Sin dispositivos)")

    if rol == "admin":        
        if input("\n¿Desea crear un nuevo ambiente? (s/n): ") == "s":
            nuevo = input("Nombre del nuevo ambiente: ")
            crear_ambiente(hogar, nuevo)
            print(f"Ambiente '{nuevo}' agregado.")
    else: 
        print("El administrador no ha creado ningún ambiente por el momento.")


def crear_ambiente(hogar, nombre_ambiente):
    nuevo_ambiente = {
        "hogar": hogar,
        "ambiente": nombre_ambiente,
        "dispositivos": []
    }
    ambientes.append(nuevo_ambiente)
