from data.datos import usuarios
from utils.utils import verificar_contra, verificar_usuario
from ui.ui import menu_principal_usuario

def crear_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su DNI: ")    
    for usuario in usuarios:
        if usuario["dni"] == dni:
            print(f"Ya existe un usuario registrado con ese DNI. Intente con otro nombre.")
            return      
        
    contrasena = input("Ingrese una contraseña: ")

    rol = input("Ingrese un rol (admin / usuario): ").strip().lower()
    if rol not in ["admin", "usuario"]:
        print("Rol inválido. Se asignará 'usuario' por defecto.")
        rol = "usuario"

    nuevo_usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "contra": contrasena,
        "rol": rol,
        
    }
    usuarios.append(nuevo_usuario)
    print(f"Usuario '{nombre}' creado con rol '{rol}'.")

def recuperar_usuario():
    print("Funcionalidad de recuperación de usuario a implementar.")

def ingresar_usuario():
    dni = input("Ingrese su número de DNI: ")
    contrasena = input("Ingrese su contraseña: ")

    for usuario in usuarios:
        if verificar_usuario(usuario["dni"],dni) and verificar_contra(usuario["contra"], contrasena):
         print(f"Hola {usuario["nombre"]} {usuario["apellido"]}! Bienvenido a casa")
         menu_principal_usuario(usuario["rol"], usuario["dni"])
        else:
         print("Usuario o contraseña incorrectos.")
