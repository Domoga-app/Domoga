# views/menu_principal.py
from .menu_usuario import menu_usuario
from .menu_admin import menu_admin
from services import UsuarioService, DispositivoService, TipoDispositivoService

def menu_principal(usuario_service: UsuarioService, 
                   dispositivo_service: DispositivoService, 
                   tipo_service: TipoDispositivoService):

    while True:
        print("\n--- Bienvenido a Domoga ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            _iniciar_sesion(usuario_service, dispositivo_service, tipo_service)
        elif opcion == "2":
            _registrar_usuario(usuario_service)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
      
            
def _iniciar_sesion(usuario_service: UsuarioService, dispositivo_service: DispositivoService, tipo_service: TipoDispositivoService):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    usuario = usuario_service.iniciar_sesion(nombre_usuario, contrasena) 
    
    if usuario:
        if usuario.es_admin:
            menu_admin(usuario, usuario_service, dispositivo_service, tipo_service)
        else:
            menu_usuario(usuario, dispositivo_service)
            
def _registrar_usuario(usuario_service: UsuarioService):
    try:
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        dni = input("Ingrese su DNI (7 u 8 dígitos): ")
        contrasena = input("La contraseña debe tener minimo 8 caracteres y debe contener al menos una mayúscula, una minúscula, un número y un simbolo. \nIngrese su contraseña: ")
        usuario_service.registrar_usuario(nombre_usuario, nombre, apellido, dni, contrasena)
    
    except Exception as e:
        print(f"Ocurrió un error en el registro: {e}")