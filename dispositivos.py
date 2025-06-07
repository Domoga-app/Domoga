
from datos import dispositivos, ambientes

def gestionar_dispositivos(hogar):
    print("\nDispositivos:")
    encontrados = [d for d in dispositivos if d['hogar'] == hogar]
    if not encontrados:
        print("No hay dispositivos creados.")
    else:
        for d in encontrados:
            print(f"- {d['nombre']} ({d['estado']}) - Ambiente: {d['ambiente']}")
    if input("\n¿Desea crear un nuevo dispositivo? (s/n): ") == "s":
        if not ambientes.get(hogar):
            print("Debe crear un ambiente primero.")
            return
        nombre = input("Nombre del dispositivo: ")
        for i, amb in enumerate(ambientes[hogar], 1):
            print(f"{i}. {amb}")
        amb_idx = int(input("Seleccione el ambiente: ")) - 1
        ambiente = ambientes[hogar][amb_idx]
        dispositivos.append({"nombre": nombre, "estado": "apagado", "hogar": hogar, "ambiente": ambiente})
        print("Dispositivo creado con éxito.")
