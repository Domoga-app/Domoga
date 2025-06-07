from datos import ambientes

def gestionar_ambientes(hogar):
    print("\nAmbientes:")
    
    # Verifica si existe el hogar y si tiene ambientes
    if hogar not in ambientes or not ambientes[hogar]:
        print("No hay ambientes creados.")
    else:
        for amb in ambientes[hogar]:
            print(f"- {amb}")
    
    # Pregunta al usuario si desea crear un nuevo ambiente
    if input("\n¿Desea crear un nuevo ambiente? (s/n): ").lower() == "s":
        nuevo = input("Nombre del nuevo ambiente: ")
        # Verifica si el hogar ya tiene una lista de ambientes
        if hogar in ambientes:
            ambientes[hogar].append(nuevo)
        else:
            ambientes[hogar] = [nuevo]  # Crea una nueva lista para el hogar
        print(f"Ambiente '{nuevo}' agregado.")
