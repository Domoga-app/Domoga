# 1. Importaciones
from models import Usuario, Rol, Dispositivo
from DAO import UsuarioDAO, DispositivoDAO


# 2. Inicializar DAOs
usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()

# 3. Datos iniciales (solo si no existen en BD)


def inicializar_datos():
    """Carga datos iniciales si la BD está vacía."""
    # Verificar si existe el admin predefinido
    admin_existente = usuario_dao.buscar_por_dni("12345678")
    if not admin_existente:
        try:
            admin = Usuario.crear_usuario(
                "12345678", "1", "Admin", "Principal", "admin123")
            usuario_dao.crear(admin)
            print("✅ Usuario administrador creado.")
        except Exception as e:
            print(f"⚠️ Error al crear admin: {e}")

    # Verificar si hay dispositivos
    if dispositivo_dao.contar() == 0:
        try:
            disp1 = Dispositivo(1, "luz", 1, "Philips",
                                "Hue White", "encendido")
            disp2 = Dispositivo(1, "sensor", 2, "Xiaomi",
                                "Mi Temperature", "apagado")
            dispositivo_dao.crear(disp1)
            dispositivo_dao.crear(disp2)
            print("✅ Dispositivos iniciales creados.")
        except Exception as e:
            print(f"⚠️ Error al crear dispositivos: {e}")

# 4. Funciones auxiliares para entrada de datos


def pedir_numero(mensaje):
    """
    Solicita un número entero al usuario.
    Devuelve el número ingresado o None si el usuario ingresa '0' para cancelar.
    """
    while True:
        valor = input(mensaje).strip()
        if valor == "0":
            return None  # indica cancelación
        if valor.isdigit():
            return int(valor)
        print("❌ Debe ingresar un número válido. Intente nuevamente o ingrese 0 para cancelar.")


def pedir_estado():
    """
    Permite al usuario seleccionar un estado de la lista de opciones.
    Devuelve el estado seleccionado como string o None si ingresa 0 para cancelar.
    """
    opciones = ["encendido", "apagado", "standby", "desconocido"]
    while True:
        print("Seleccione el estado:")
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i} - {opcion}")
        print("0 - volver")
        eleccion = input("Opción: ").strip()
        if eleccion == "0":
            return None
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
            return opciones[int(eleccion)-1]
        print("❌ Opción inválida, intente nuevamente.")

# 5. Funciones de registro y login


def registrar_usuario():
    print("\n=== Registro de usuario ===")
    print("0 - volver.")

    dni = input("DNI: ").strip()
    if dni == "0" or dni == "":
        print("❌ Registro cancelado.")
        return

    # Verificar si ya existe un usuario con el mismo DNI
    if usuario_dao.existe_dni(dni):
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
    try:
        nuevo_usuario = Usuario.crear_usuario(
            dni, "2", nombre, apellido, contraseña)
        usuario_dao.crear(nuevo_usuario)
        print(
            f"✅ Usuario {nombre} {apellido} registrado como Usuario estándar.")
    except ValueError as e:
        print(f"❌ Error al registrar: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


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

    try:
        usuario = usuario_dao.autenticar_usuario(dni, contraseña)
        if usuario:
            print(f"✅ Bienvenido {usuario.nombre} {usuario.apellido}")
            return usuario
        else:
            print("❌ Credenciales incorrectas.")
            return None
    except Exception as e:
        print(f"❌ Error al iniciar sesión: {e}")
        return None

# 6. Funciones comunes (ambos roles)


def ver_datos_personales(usuario):
    datos = usuario.recuperar_usuario()
    print("\n--- Datos Personales ---")
    print(f"DNI: {datos['dni']}")
    print(f"Nombre: {datos['nombre']} {datos['apellido']}")
    print(
        f"Rol: {'Administrador' if datos['id_rol'] == '1' else 'Usuario estándar'}")
    print("------------------------")


def ver_dispositivos():
    print("\n--- Dispositivos ---")
    try:
        dispositivos = dispositivo_dao.listar()
        if not dispositivos:
            print("No hay dispositivos registrados.")
            return
        for i, d in enumerate(dispositivos, start=1):
            info = d.ver_dispositivos()
            print(
                f"{i}. ID: {d.id} | {info['marca']} {info['modelo']} - Estado: {info['estado']}")
    except Exception as e:
        print(f"❌ Error al listar dispositivos: {e}")

# 7. Funciones exclusivas de admin


def crear_dispositivo():
    print("\n=== Crear dispositivo ===")
    print("0 - volver")

    id_hogar = pedir_numero("ID hogar: ")
    if id_hogar is None:
        print("❌ Operación cancelada.")
        return

    tipo = input("Tipo de dispositivo: ").strip()
    if tipo == "0":
        print("❌ Operación cancelada.")
        return

    id_ubicacion = pedir_numero("ID ubicación: ")
    if id_ubicacion is None:
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

    estado = pedir_estado()
    if estado is None:
        print("❌ Operación cancelada.")
        return

    try:
        nuevo_disp = Dispositivo(
            id_hogar, tipo, id_ubicacion, marca, modelo, estado)
        dispositivo_dao.crear(nuevo_disp)
        print("✅ Dispositivo creado con éxito.")
    except ValueError as e:
        print(f"❌ Error al crear dispositivo: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def borrar_dispositivo():
    while True:
        ver_dispositivos()
        print("0 - volver.")

        dispositivos = dispositivo_dao.listar()
        if not dispositivos:
            print("No hay dispositivos para eliminar.")
            return

        id_disp = input("ID del dispositivo a eliminar: ").strip()
        if id_disp == "0":
            print("❌ Operación cancelada.")
            return

        try:
            if dispositivo_dao.eliminar(id_disp):
                print(f"✅ Dispositivo eliminado.")
                return
            else:
                print("❌ Dispositivo no encontrado.")
        except Exception as e:
            print(f"❌ Error al eliminar: {e}")


def actualizar_dispositivo():
    while True:
        ver_dispositivos()
        print("0 - volver")

        dispositivos = dispositivo_dao.listar()
        if not dispositivos:
            print("No hay dispositivos para actualizar.")
            return

        id_disp = input("ID del dispositivo a actualizar: ").strip()
        if id_disp == "0":
            print("❌ Operación cancelada.")
            return

        disp = dispositivo_dao.obtener_por_id(id_disp)
        if not disp:
            print("❌ Dispositivo no encontrado.")
            continue

        # Elegir nuevo estado con menú numerado
        nuevo_estado = pedir_estado()
        if nuevo_estado is None:
            print("❌ Operación cancelada.")
            return

        try:
            if dispositivo_dao.cambiar_estado(id_disp, nuevo_estado):
                print(
                    f"✅ Dispositivo {disp.marca} {disp.modelo} actualizado a {nuevo_estado}.")
                return
            else:
                print("❌ No se pudo actualizar el dispositivo.")
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")


def cambiar_rol_usuario(usuario_actual):
    print("\n=== Cambiar rol de usuario ===")
    print("0 - volver.")

    # Usuario estándar solo puede subir a admin (su propio rol)
    if usuario_actual.id_rol == "2":
        confirm = input(
            "¿Deseas cambiar tu rol a Administrador? (s/n): ").strip().lower()
        if confirm == "0" or confirm == "n":
            print("❌ Cambio cancelado.")
            return
        elif confirm == "s":
            try:
                if usuario_dao.modificar(usuario_actual.id, {'id_rol': 1}):
                    usuario_actual.id_rol = "1"
                    print("✅ Ahora tienes rol de Administrador.")
                    print("⚠️ Se cerrará la sesión para aplicar el cambio.")
                    return "cerrar_sesion"
            except Exception as e:
                print(f"❌ Error al cambiar rol: {e}")
        else:
            print("❌ Opción no válida.")
        return

    # Admin predefinido puede cambiar todos excepto a sí mismo
    if usuario_actual.dni == "12345678":
        try:
            usuarios = usuario_dao.listar()
            for i, u in enumerate(usuarios, start=1):
                rol_str = "Administrador" if u.id_rol == "1" else "Usuario estándar"
                print(
                    f"{i}. {u.dni} - {u.nombre} {u.apellido} - Rol actual: {rol_str}")

            idx = input(
                "Selecciona el número del usuario (o '0' para cancelar): ").strip()
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
                nuevo_rol = 1 if u.id_rol == "2" else 2
                if usuario_dao.modificar(u.id, {'id_rol': nuevo_rol}):
                    print(
                        f"✅ Rol de {u.dni} - {u.nombre} {u.apellido} cambiado a {'Administrador' if nuevo_rol == 1 else 'Usuario estándar'}.")
                else:
                    print("❌ No se pudo cambiar el rol.")
            else:
                print("❌ Índice inválido.")
        except Exception as e:
            print(f"❌ Error: {e}")
        return

    # Admin común solo puede bajarse a estándar
    if usuario_actual.id_rol == "1":
        confirmar = input(
            "¿Querés cambiar tu rol? (s/n/0 para cancelar): ").strip().lower()
        if confirmar == "0" or confirmar == "n":
            print("❌ Cambio cancelado.")
            return
        elif confirmar == "s":
            try:
                if usuario_dao.modificar(usuario_actual.id, {'id_rol': 2}):
                    usuario_actual.id_rol = "2"
                    print("✅ Tu rol ahora es: Usuario estándar.")
                    print("⚠️ Se cerrará la sesión para aplicar el cambio.")
                    return "cerrar_sesion"
            except Exception as e:
                print(f"❌ Error al cambiar rol: {e}")
        else:
            print("❌ Opción no válida.")
        return

# 8. Menú usuario estándar


def menu_usuario_estandar(usuario):
    while True:
        print("\n=== Menú Usuario Estándar ===")
        print("1 - Ver mis datos personales")
        print("2 - Ver dispositivos")
        print("3 - Cambiar rol a Administrador")
        print("4 - Cerrar sesión")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            ver_datos_personales(usuario)
        elif opcion == "2":
            ver_dispositivos()
        elif opcion == "3":
            resultado = cambiar_rol_usuario(usuario)
            if resultado == "cerrar_sesion":
                print("🔐 Cerrando sesión...")
                break
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

# 9. Menú administrador


def menu_admin(usuario):
    while True:
        print("\n=== Menú Administrador ===")
        print("1 - Ver mis datos personales")
        print("2 - Ver dispositivos")
        print("3 - Crear dispositivo")
        print("4 - Actualizar dispositivo")
        print("5 - Eliminar dispositivo")
        print("6 - Cambiar rol de usuario")
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
            resultado = cambiar_rol_usuario(usuario)
            if resultado == "cerrar_sesion":
                print("🔐 Cerrando sesión...")
                break
        elif opcion == "7":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

# 10. Menú principal


def menu_principal():
    print("\n🏠 Inicializando sistema...")
    inicializar_datos()

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
                if usuario.id_rol == "1":
                    menu_admin(usuario)
                else:
                    menu_usuario_estandar(usuario)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


# 11. Ejecutar el programa
if __name__ == "__main__":
    menu_principal()
