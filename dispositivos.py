from datos import dispositivos

def gestionar_dispositivos(hogar):
    print("\nDispositivos:")
    encontrados = [d for d in dispositivos if d['hogar'] == hogar]

    if not encontrados:
        print("No hay dispositivos creados.")
    else:
        for d in encontrados:
            print(f"- {d['nombre']} ({d['estado']})")

    if input("\n¿Desea crear un nuevo dispositivo? (s/n): ").strip().lower() == "s":
        nombre = input("Nombre del dispositivo: ")
        dispositivos.append({"nombre": nombre, "estado": "apagado", "hogar": hogar})
        print("Dispositivo creado con éxito.")
