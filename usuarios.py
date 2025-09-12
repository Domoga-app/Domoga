from datos import usuarios
from utils import verificar_contra, verificar_usuario
from ui import menu_principal_usuario

def crear_usuario():
    nombre = input("Ingrese un nombre de usuario: ")
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print(f"El usuario '{nombre}' ya existe. Intente con otro nombre.")
            return      
        
    contrasena = input("Ingrese una contraseña: ")

    rol = input("Ingrese un rol (admin / usuario): ").strip().lower()
    if rol not in ["admin", "usuario"]:
        print("Rol inválido. Se asignará 'usuario' por defecto.")
        rol = "usuario"

    nuevo_usuario = {
        "nombre": nombre,
        "contra": contrasena,
        "rol": rol
    }
    usuarios.append(nuevo_usuario)
    print(f"Usuario '{nombre}' creado con rol '{rol}'.")

def recuperar_usuario():
    print("Funcionalidad de recuperación de usuario a implementar.")

def ingresar_usuario():
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    for usuario in usuarios:
        if verificar_usuario(usuario["nombre"],nombre) and verificar_contra(usuario["contra"], contrasena):
         print(f"Hola {nombre}! Bienvenido a casa")
         menu_principal_usuario(usuario["rol"])
        else:
         print("Usuario o contraseña incorrectos.")
