<<<<<<< HEAD

from datos import dispositivos, ambientes
=======
from datos import ambientes
>>>>>>> 3d5df8de5daa321b2225278f9190539033d93804

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
<<<<<<< HEAD
        ambiente = ambientes[hogar][amb_idx]
        dispositivos.append({"nombre": nombre, "estado": "apagado", "hogar": hogar, "ambiente": ambiente})
=======
        ambiente_obj = ambientes_hogar[amb_idx]
        nombre = input("Nombre del dispositivo: ")

        nuevo_dispositivo = {
            "nombre": nombre,
            "estado": "apagado"
        }

        ambiente_obj["dispositivos"].append(nuevo_dispositivo)
>>>>>>> 3d5df8de5daa321b2225278f9190539033d93804
        print("Dispositivo creado con éxito.")
