from datos import usuarios, usuario_actual
import hogares

def crear_usuario():
    nombre = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    nuevo_usuario = { 
        "nombre":  nombre,
        "contra": contrasena
    }
    usuarios.append(nuevo_usuario)
    print("Usuario creado con éxito.")

def recuperar_usuario():
    print("Funcionalidad de recuperación de usuario a implementar.")

def ingresar_usuario():
    global usuario_actual
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    for usuario in usuarios:
        print("usuarios", usuario)
        if usuario["nombre"] == nombre and usuario["contra"] == contrasena:
         print(f"Hola {nombre}! Bienvenido a casa")
         hogares.menu_principal_usuario()
        else:
         print("Usuario o contraseña incorrectos.")