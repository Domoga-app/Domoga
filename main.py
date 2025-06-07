from usuarios import ingresar_usuario, crear_usuario, recuperar_usuario



def menu_principal():
    opciones = {
            "1": lambda: ingresar_usuario,
            "2": lambda: crear_usuario,
            "3": lambda: recuperar_usuario,
        }
       
    while True:
        print("\n¡Bienvenido a Domóga!")
        print("1. Ingresar usuario")
        print("2. ¿Aún no tienes cuenta? Crear nuevo usuario")
        print("3. Recuperar usuario y/o contraseña")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
      

        if opcion == "4":
            break 
        elif opcion in opciones:
            opciones[opcion]()   
        else:
              print("Opción no válida.")
         
        

if __name__ == "__main__":
    menu_principal()