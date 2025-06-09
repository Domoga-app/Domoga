from datos import ambientes

def gestionar_dispositivos(hogar):
    print("\nDispositivos:")
    ambientes_hogar = [a for a in ambientes if a['hogar'] == hogar]
    if not ambientes_hogar:
        print("Debe crear un ambiente primero.")
        return

    for amb in ambientes_hogar:
        for d in amb['dispositivos']:
            print(f"- {d['nombre']} ({d['estado']}) - Ambiente: {amb['ambiente']}")

    if input("\n¿Desea crear un nuevo dispositivo? (s/n): ") == "s":
        for i, amb in enumerate(ambientes_hogar, 1):
            print(f"{i}. {amb['ambiente']}")
        amb_idx = int(input("Seleccione el ambiente: ")) - 1
        ambiente_obj = ambientes_hogar[amb_idx]
        nombre = input("Nombre del dispositivo: ")

        nuevo_dispositivo = {
            "nombre": nombre,
            "estado": "apagado"
        }

        ambiente_obj["dispositivos"].append(nuevo_dispositivo)
        print("Dispositivo creado con éxito.")
