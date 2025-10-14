from dao.usuarioDAO import UsuarioDAO
from dao.dispositivoDAO import DispositivoDAO
from models.usuario import Usuario
from models.dispositivo import Dispositivo
from models.tipo_dispositivo import TipoDispositivo
from dao.tipo_dispositivoDAO import TipoDispositivoDAO

def iniciar_sesion(usuario_dao: UsuarioDAO):
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

def registrarse(usuario_dao: UsuarioDAO):
    dni = input("Ingrese su DNI: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    contrasena = input("Ingrese su contraseña: ")
    nuevo_usuario = Usuario(dni, False, nombre, apellido, contrasena)
    
    if usuario_dao.crear(nuevo_usuario):
        print("Usuario registrado correctamente.")
        return nuevo_usuario
    else:
        print("Error: No se pudo registrar (el DNI puede que ya exista).")
        return None

def menu_usuario(usuario: Usuario, dispositivo_dao: DispositivoDAO):
    while True:
        print("\n--- Menú Usuario Estandar ---")
        print("1. Consultar mis datos personales")
        print("2. Consultar dispositivos de la casa")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"\n--- Tus Datos --- \n{usuario}")
        elif opcion == "2":
            print("\n--- Dispositivos de la Casa ---")
            dispositivos = dispositivo_dao.obtener_todos()
            if not dispositivos:
                print("No hay dispositivos registrados en la casa.")
            for d in dispositivos:
                print(f"- {d}")
        elif opcion == "3":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")

def menu_admin(usuario_dao: UsuarioDAO, dispositivo_dao: DispositivoDAO, tipo_dispositivo_dao: TipoDispositivoDAO):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Gestionar dispositivos (CRUD)")
        print("2. Cambiar rol de un usuario")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_dispositivos_admin(dispositivo_dao, tipo_dispositivo_dao)
        elif opcion == "2":
            dni_a_cambiar = input("Ingrese el DNI del usuario a modificar: ")
            usuario_a_modificar = usuario_dao.obtener_por_dni(dni_a_cambiar)
            
            if not usuario_a_modificar:
                print("Error: Usuario no encontrado.")
                continue

            
            if usuario_a_modificar.es_admin:
                rol_actual_str = "Administrador"
                accion_propuesta = "¿Desea cambiarlo a Estandar? (s/n): "
                es_nuevo_admin = False
            else:
                rol_actual_str = "Estandar"
                accion_propuesta = "¿Desea hacerlo Administrador? (s/n): "
                es_nuevo_admin = True
            
            print(f"El rol actual del usuario {dni_a_cambiar} es: {rol_actual_str}")
            confirmacion = input(accion_propuesta).lower()
            
            if confirmacion == 's':
                if usuario_dao.cambiar_rol(dni_a_cambiar, es_nuevo_admin):
                    print("Rol actualizado correctamente.")
                else:
                    print("Error: No se pudo actualizar el rol.")
            else:
                print("Operación cancelada.")
        elif opcion == "3":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")

def gestionar_dispositivos_admin(dispositivo_dao: DispositivoDAO, tipo_dispositivo_dao: TipoDispositivoDAO):
    while True:
        print("\n--- Gestión de Dispositivos (CRUD) ---")
        print("1. Crear dispositivo")
        print("2. Listar todos los dispositivos")
        print("3. Actualizar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver al menú de Administrador")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n--- Crear Nuevo Dispositivo ---")
            tipos = tipo_dispositivo_dao.obtener_todos()
            for t in tipos:
                print(f"ID: {t.id_tipo} - Nombre: {t.nombre}")
            id_tipo = int(input("Seleccione el ID del tipo de dispositivo: "))
            tipo_seleccionado = next((t for t in tipos if t.id_tipo == id_tipo), None)
            
            if not tipo_seleccionado:
                print("ID de tipo inválido.")
                continue
            
            ubicacion = input("Ubicación (ej. Living): ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            estado = input("Estado inicial (ej. apagado): ")

            nuevo_disp = Dispositivo(None, tipo_seleccionado, ubicacion, marca, modelo, estado)
            if dispositivo_dao.crear(nuevo_disp):
                print("Dispositivo creado con éxito.")
            else:
                print("Error al crear dispositivo.")
        
        elif opcion == '2':
            print("\n--- Listado de Todos los Dispositivos ---")
            todos_los_dispositivos = dispositivo_dao.obtener_todos()
            if not todos_los_dispositivos:
                print("No hay ningún dispositivo en el sistema.")
            for d in todos_los_dispositivos:
                print(f"- {d}")
        
        elif opcion == '3':
            print("\n--- Actualizar Dispositivo ---")
            try:
                id_a_actualizar = int(input("Ingrese el ID del dispositivo que desea actualizar: "))
                disp_existente = dispositivo_dao.obtener_por_id(id_a_actualizar)

                if not disp_existente:
                    print("Error: Dispositivo no encontrado.")
                    continue

                print(f"Datos actuales: {disp_existente}")
                print("--- Ingrese los nuevos datos (deje en blanco para no cambiar) ---")
                
                tipos = tipo_dispositivo_dao.obtener_todos()
                for t in tipos:
                    print(f"ID: {t.id_tipo} - Nombre: {t.nombre}")
                id_tipo_nuevo_str = input(f"Nuevo ID de tipo (actual: {disp_existente.tipo.id_tipo}): ")
                
                tipo_final = disp_existente.tipo
                if id_tipo_nuevo_str:
                    tipo_seleccionado = next((t for t in tipos if t.id_tipo == int(id_tipo_nuevo_str)), None)
                    if tipo_seleccionado:
                        tipo_final = tipo_seleccionado
                    else:
                        print("Advertencia: ID de tipo inválido. Se mantendrá el tipo actual.")
                        
                ubicacion = input(f"Nueva ubicación (actual: {disp_existente.ubicacion}): ") or disp_existente.ubicacion
                marca = input(f"Nueva marca (actual: {disp_existente.marca}): ") or disp_existente.marca
                modelo = input(f"Nuevo modelo (actual: {disp_existente.modelo}): ") or disp_existente.modelo
                estado = input(f"Nuevo estado (actual: {disp_existente.estado}): ") or disp_existente.estado

                disp_actualizado = Dispositivo(None, tipo_final, ubicacion, marca, modelo, estado)
                
                if dispositivo_dao.actualizar(disp_actualizado, id_a_actualizar):
                    print("Dispositivo actualizado con éxito.")
                else:
                    print("Error al actualizar el dispositivo.")

            except ValueError:
                print("Error: El ID debe ser un número.")
        
        elif opcion == '4':
            id_a_borrar = int(input("Ingrese el ID del dispositivo a eliminar: "))
            if dispositivo_dao.eliminar(id_a_borrar):
                print("Dispositivo eliminado con éxito.")
            else:
                print("Error al eliminar (verifique el ID).")
        
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

def main():
    usuario_dao = UsuarioDAO()
    dispositivo_dao = DispositivoDAO()
    tipo_dispositivo_dao = TipoDispositivoDAO()

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

if __name__ == "__main__":
    main()