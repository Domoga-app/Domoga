from data.datos import ambientes

def gestionar_dispositivos(hogar):
    print("\nDispositivos:")
    ambientes_hogar = [a for a in ambientes if a['hogar'] == hogar]
    if not ambientes_hogar:
        print("Debe crear un ambiente primero.")
        return

    for amb in ambientes_hogar:
        for d in amb['dispositivos']:
            print(f"-Nombre: {d['nombre']} ({d['estado']}) -Marca: {d['marca']} -Modelo: {d['modelo']} -> Ambiente: {amb['ambiente']}")

    if input("\n¿Desea crear un nuevo dispositivo? (s/n): ") == "s":
        for i, amb in enumerate(ambientes_hogar, 1):
            print(f"{i}. {amb['ambiente']}")
        # amb_idx = int(input("Seleccione el ambiente: ")) - 1
        amb_idx = input("Seleccione el ambiente (número): ")
        if not amb_idx.isdigit():
            print("Debes ingresar el número correspondiente al ambiente en el listado.")   
            return
            
        amb_idx = int(amb_idx) - 1
        
        if 0 <= amb_idx <=len(ambientes_hogar):
            ambiente_obj = ambientes_hogar[amb_idx]
        else:
            print("Ambiente inexistente.")
            return
        nombre = input("Nombre del dispositivo: ")
        tipo = input("Tipo del dispositivo: ")
        marca = input("Marca del dispositivo: ")
        modelo = input("Modelo del dispositivo: ")

        nuevo_dispositivo = {
            "nombre": nombre,
            "tipo": tipo,
            "marca": marca,
            "modelo": modelo,
            "estado": "apagado"
        }

        ambiente_obj["dispositivos"].append(nuevo_dispositivo)
        print("Dispositivo creado con éxito.")
