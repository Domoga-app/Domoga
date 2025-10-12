# 1. Importaciones
from models import Usuario, Rol, Dispositivo

# 2. Datos iniciales
roles = [
    Rol(1, "Administrador"),
    Rol(2, "Usuario")
]

usuarios = [
    Usuario.crear_usuario("12345678", 1, "Admin", "Principal", "admin123")
]

dispositivos = [
    Dispositivo.crear_dispositivos(1, 1, "Philips", "Hue White", "encendido"),
    Dispositivo.crear_dispositivos(2, 2, "Xiaomi", "Mi Temperature", "activo")
]

# 3. Funciones de registro y login

def registrar_usuario():
    print("\n=== Registro de usuario ===")
    print("Ingrese '0' en cualquier momento para cancelar y volver al menú.")

    dni = input("DNI: ").strip()
    if dni == "0" or dni == "":
        print("❌ Registro cancelado.")
        return

    # Verificar si ya existe un usuario con el mismo DNI
    for u in usuarios:
        if u.dni == dni:
            print("❌ Ya existe un usuario con ese DNI. Intenta con otro.")
            return

    nombre = input("Nombre: ").strip()
    if nombre == "0" or nombre == "":
        print("❌ Registro cancelado.")
        return

    apellido = input("Apellido: ").strip()
    if apellido == "0" or apellido == "":
        print("❌ Registro cancelado.")
        return

    contraseña = input("Contraseña: ").strip()
    if contraseña == "0" or contraseña == "":
        print("❌ Registro cancelado.")
        return

    # Todo usuario registrado es estándar
    id_rol = 2
    nuevo_usuario = Usuario.crear_usuario(dni, id_rol, nombre, apellido, contraseña)
    usuarios.append(nuevo_usuario)
    print(f"✅ Usuario {nombre} {apellido} registrado como Usuario estándar.")

def login_usuario():
    print("\n=== Inicio de sesión ===")
    print("0 - volver")

    dni = input("DNI: ").strip()
    if dni == "0":
        print("❌ Login cancelado.")
        return None

    contraseña = input("Contraseña: ").strip()
    if contraseña == "0":
        print("❌ Login cancelado.")
        return None

    for user in usuarios:
        if user.ingresar_usuario(dni, contraseña):
            print(f"✅ Bienvenido {user.nombre} {user.apellido}")
            return user

    print("❌ Credenciales incorrectas.")
    return None

# 4. Funciones auxiliares
def ver_datos_personales(usuario):
    datos = usuario.recuperar_usuario()
    print("\n--- Datos Personales ---")
    print(f"DNI: {datos['dni']}")
    print(f"Nombre: {datos['nombre']} {datos['apellido']}")
    print(f"Rol: {'Administrador' if datos['id_rol']==1 else 'Usuario estándar'}")
    print("------------------------")

def ver_dispositivos():
    print("\n--- Dispositivos ---")
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return
    for i, d in enumerate(dispositivos, start=1):
        info = d.ver_dispositivos()
        print(f"{i}. {info['marca']} {info['modelo']} - Estado: {info['estado']}")

# 5. Funciones CRUD y gestión (admin)
def crear_dispositivo():
    print("\n=== Crear dispositivo ===")
    print("0 - volver.")

    id_tipo = input("ID tipo dispositivo: ").strip()
    if id_tipo == "0":
        print("❌ Operación cancelada.")
        return
    id_ubicacion = input("ID ubicación: ").strip()
    if id_ubicacion == "0":
        print("❌ Operación cancelada.")
        return
    marca = input("Marca: ").strip()
    if marca == "0":
        print("❌ Operación cancelada.")
        return
    modelo = input("Modelo: ").strip()
    if modelo == "0":
        print("❌ Operación cancelada.")
        return
    estado = input("Estado inicial (encendido/apagado/activo): ").strip()
    if estado == "0":
        print("❌ Operación cancelada.")
        return

    nuevo_disp = Dispositivo.crear_dispositivos(int(id_tipo), int(id_ubicacion), marca, modelo, estado)
    dispositivos.append(nuevo_disp)
    print("✅ Dispositivo creado con éxito.")

def borrar_dispositivo():
    while True:
        ver_dispositivos()
        print("0 - volver.")
        idx = input("Número de dispositivo a eliminar: ").strip()
        if idx == "0":
            print("❌ Operación cancelada.")
            return
        if not idx.isdigit():
            print("❌ Debe ingresar un número válido.")
            continue
        idx = int(idx) - 1
        if 0 <= idx < len(dispositivos):
            disp = dispositivos.pop(idx)
            print(f"✅ Dispositivo {disp.marca} {disp.modelo} eliminado.")
            return
        else:
            print("❌ Índice inválido.")

def actualizar_dispositivo():
    while True:
        ver_dispositivos()
        print("0 - volver.")
        idx = input("Número de dispositivo a actualizar: ").strip()
        if idx == "0":
            print("❌ Operación cancelada.")
            return
        if not idx.isdigit():
            print("❌ Debe ingresar un número válido.")
            continue
        idx = int(idx) - 1
        if 0 <= idx < len(dispositivos):
            disp = dispositivos[idx]
            nuevo_estado = input(f"Nuevo estado para {disp.marca} {disp.modelo} 0 - para cancelar): ").strip()
            if nuevo_estado == "0":
                print("❌ Operación cancelada.")
                return
            disp.gestionar_dispositivos("cambiar_estado", {"estado": nuevo_estado})
            print("✅ Dispositivo actualizado.")
            return
        else:
            print("❌ Índice inválido.")

def cambiar_rol_usuario(usuario_actual):
    print("\n=== Cambiar rol de usuario ===")
    print("0 - volver.")

    # Usuario estándar → solo puede subir a admin (su propio rol)
    if usuario_actual.id_rol == 2:
        confirm = input("¿Deseas cambiar tu rol a Administrador? (s/n): ").strip().lower()
        if confirm == "0" or confirm == "n":
            print("❌ Cambio cancelado.")
            return
        elif confirm == "s":
            usuario_actual.id_rol = 1
            print("✅ Ahora tienes rol de Administrador.")
            print("⚠️ Se cerrará la sesión para aplicar el cambio.")
            return "cerrar_sesion"
        else:
            print("❌ Opción no válida.")
        return

    # Admin predefinido → puede cambiar todos excepto a sí mismo
    if usuario_actual.dni == "12345678":
        for i, u in enumerate(usuarios, start=1):
            rol_str = "Administrador" if u.id_rol == 1 else "Usuario estándar"
            print(f"{i}. {u.dni} - {u.nombre} {u.apellido} - Rol actual: {rol_str}")

        idx = input("Selecciona el número del usuario (o '0' para cancelar): ").strip()
        if idx == "0":
            print("❌ Operación cancelada.")
            return
        if not idx.isdigit():
            print("❌ Opción inválida.")
            return

        idx = int(idx) - 1
        if 0 <= idx < len(usuarios):
            u = usuarios[idx]
            if u.dni == "12345678":
                print("⚠️ No podés cambiar tu propio rol (admin predefinido).")
                return
            nuevo_rol = 1 if u.id_rol == 2 else 2
            u.id_rol = nuevo_rol
            print(f"✅ Rol de {u.dni} - {u.nombre} {u.apellido} cambiado a {'Administrador' if nuevo_rol==1 else 'Usuario estándar'}.")
        else:
            print("❌ Índice inválido.")
        return

    # Admin común → solo puede bajarse a estándar
    if usuario_actual.id_rol == 1:
        confirmar = input("¿Querés cambiar tu rol? (s/n/0 para cancelar): ").strip().lower()
        if confirmar == "0" or confirmar == "n":
            print("❌ Cambio cancelado.")
            return
        elif confirmar == "s":
            usuario_actual.id_rol = 2
            print("✅ Tu rol ahora es: Usuario estándar.")
            print("⚠️ Se cerrará la sesión para aplicar el cambio.")
            return "cerrar_sesion"
        else:
            print("❌ Opción no válida.")
        return


# 6. Menú usuario estándar
def menu_usuario_estandar(usuario):
    while True:
        print("\n=== Menú Usuario Estándar ===")
        print("1 - Ver mis datos personales")
        print("2 - Ver dispositivos")
        print("3 - Cerrar sesión")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            ver_datos_personales(usuario)
        elif opcion == "2":
            ver_dispositivos()
        elif opcion == "3":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

# 7. Menú admin
def menu_admin(usuario):
    while True:
        print("\n=== Menú Administrador ===")
        print("1 - Ver mis datos personales")       # opción común
        print("2 - Ver dispositivos")              # opción común
        print("3 - Crear dispositivo")             # admin exclusivo
        print("4 - Actualizar dispositivo")        # admin exclusivo
        print("5 - Eliminar dispositivo")          # admin exclusivo
        print("6 - Cambiar rol de usuario")        # admin exclusivo
        print("7 - Cerrar sesión")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            ver_datos_personales(usuario)          
        elif opcion == "2":
            ver_dispositivos()                     
        elif opcion == "3":
            crear_dispositivo()
        elif opcion == "4":
            actualizar_dispositivo()
        elif opcion == "5":
            borrar_dispositivo()
        elif opcion == "6":
            # ⚡ Aquí detectamos si el cambio de rol requiere cerrar sesión
            resultado = cambiar_rol_usuario(usuario)
            if resultado == "cerrar_sesion":
                print("🔐 Cerrando sesión...")
                break  # rompe el while y vuelve al login o menú principal
        elif opcion == "7":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

# 8. Menú principal + punto de entrada
def menu_principal():
    while True:
        print("\n=== Sistema Domótica Smart Home ===")
        print("1 - Registrarse")
        print("2 - Iniciar sesión")
        print("3 - Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = login_usuario()
            if usuario:
                if usuario.id_rol == 1:
                    menu_admin(usuario)
                else:
                    menu_usuario_estandar(usuario)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# 9. Ejecutar el programa
if __name__ == "__main__":
    menu_principal()
