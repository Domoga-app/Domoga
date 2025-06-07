from usuarios import ingresar_usuario, crear_usuario, recuperar_usuario



def menu_principal():
    opciones = {
            "1": ingresar_usuario,
            "2": crear_usuario,
            "3": recuperar_usuario,
            "4": print("Hasta luego!"),
        }
       
    while True:
        print("\n¡Bienvenido a Domóga!")
        print("1. Ingresar usuario")
        print("2. ¿Aún no tienes cuenta? Crear nuevo usuario")
        print("3. Recuperar usuario y/o contraseña")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
      
        accion = opciones.get(opcion)

        if accion:
            accion()
            if opcion == "4":
                break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()