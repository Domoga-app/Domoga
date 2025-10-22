from .menu_usuario import menu_usuario
from .menu_admin import menu_admin

def menu_principal(usuario_dao, dispositivo_dao, tipo_dispositivo_dao):
    while True:
        print("\n--- Bienvenido a Domoga ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = iniciar_sesion(usuario_dao)
            if usuario:
                if usuario.es_admin:
                    menu_admin(usuario_dao, dispositivo_dao, tipo_dispositivo_dao)
                else:
                    menu_usuario(usuario, dispositivo_dao)
        elif opcion == "2":
            registrarse(usuario_dao)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
            
def iniciar_sesion(usuario_dao):
    dni = input("Ingrese su DNI: ")
    contrasena = input("Ingrese su contraseña: ")
    usuario = usuario_dao.obtener_por_dni(dni)
    
    if usuario and usuario._contrasena == contrasena:
        rol_str = "Administrador" if usuario.es_admin else "Estandar"
        print(f"\n¡Bienvenido {usuario.nombre_completo}! (Rol: {rol_str})")
        return usuario
    else:
        print("DNI o contraseña incorrectos.")
        return None

def registrarse(usuario_dao):
    dni = input("Ingrese su DNI: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if usuario_dao.crear(dni, nombre, apellido, contrasena):
        print("Usuario registrado correctamente.")
        return
    else:
        print("Error: No se pudo registrar (el DNI puede que ya exista).")
        return None