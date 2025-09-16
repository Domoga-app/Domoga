import data.datos as datos


from data.datos import hogares_disponibles  # importá la lista de hogares
        
def agregar_hogar():
    nuevo_hogar = input("Ingrese el nombre del nuevo hogar: ")
    if nuevo_hogar and nuevo_hogar not in hogares_disponibles:
        hogares_disponibles.append(nuevo_hogar)
        print(f"Hogar '{nuevo_hogar}' agregado.")
    else:
        print("Nombre inválido o ya existe.")

def eliminar_hogar():
    if not datos.hogares_disponibles:
        print("No hay hogares para eliminar.")
        return

    print("\nSeleccione el hogar que desea eliminar:")
    for i, nombre in enumerate(hogares_disponibles, start=1):
        print(f"{i}. {nombre}")

    opcion = input("Ingrese el número del hogar a eliminar: ")
    
    if opcion.isdigit():
        indice = int(opcion) - 1
        if 0 <= indice < len(hogares_disponibles):
            nombre_hogar = hogares_disponibles[indice]
            confirmacion = input(f"¿Está seguro que desea eliminar el hogar '{nombre_hogar}'? (s/n): ").lower()
            if confirmacion == 's':
                eliminado = hogares_disponibles.pop(indice)
                print(f"Hogar '{eliminado}' eliminado.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Número fuera de rango.")
    else:
        print("Opción no válida.")

