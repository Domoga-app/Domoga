# views/menu_admin.py
from services import UsuarioService, DispositivoService, TipoDispositivoService
from models import Usuario

def menu_admin(usuario: Usuario,
               usuario_service: UsuarioService, 
               dispositivo_service: DispositivoService, 
               tipo_service: TipoDispositivoService):
    while True:
        print("\n--- Menú Administrador ---")
        print(f"Usuario: {usuario.nombre} {usuario.apellido}")
        print("\n-- Gestión de Dispositivos --")
        print("1. Ver todos los dispositivos")
        print("2. Crear nuevo dispositivo")
        print("3. Actualizar un dispositivo")
        print("4. Eliminar un dispositivo")
        print("\n-- Gestión de Usuarios --")
        print("5. Cambiar rol de un usuario")
        print("6. Ver todos los usuarios")
        print("\n-- Sistema --")
        print("7. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            _ver_dispositivos(dispositivo_service)
        elif opcion == "2":
            _crear_dispositivo(dispositivo_service, tipo_service)
        elif opcion == "3":
            _actualizar_dispositivo(dispositivo_service, tipo_service)
        elif opcion == "4":
            _eliminar_dispositivo(dispositivo_service)
        elif opcion == "5":
            _cambiar_rol_usuario(usuario_service)
        elif opcion == "6":
            _ver_usuarios(usuario_service)
        elif opcion == "7":
            print("Cerrando sesión de administrador...")
            break
        else:
            print("Opción inválida.")
            
            
def _ver_dispositivos(dispositivo_service: DispositivoService):
    '''Muestra todos los dispositivos.'''
    print("\n--- Listado de Dispositivos ---")
    dispositivos = dispositivo_service.obtener_todos()
    if not dispositivos:
        print("No hay dispositivos registrados.")
    else:
        for d in dispositivos:
            print(f"- {d}")

def _crear_dispositivo(dispositivo_service: DispositivoService, tipo_service: TipoDispositivoService):
    try:
        print("\n--- Crear Nuevo Dispositivo ---")
        tipos = tipo_service.obtener_todos()
        if not tipos:
            print("Error: No hay tipos de dispositivo definidos.")
            return # Sale de la función si no hay tipos
        for t in tipos:
            print(f"ID: {t.id_tipo} - {t.nombre}")
        
        id_tipo_sel = int(input("Seleccione el ID del tipo de dispositivo: "))
        tipo_seleccionado = tipo_service.obtener_por_id(id_tipo_sel) 
        
        if not tipo_seleccionado:
            print("Error: ID de tipo inválido.")
            return

        ubicacion = input("Ubicación (ej. Sala de Estar): ")
        marca = input("Marca (Opcional): ")
        modelo = input("Modelo (Opcional): ")
        estado = input("Estado inicial (ej. apagado): ")
        
        if dispositivo_service.crear_dispositivo(tipo_seleccionado, ubicacion, marca, modelo, estado):
            print("Dispositivo creado con éxito.")
    
    except ValueError:
        print("Error: El ID del tipo debe ser un número.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def _actualizar_dispositivo(dispositivo_service: DispositivoService, tipo_service: TipoDispositivoService):
    try:
        id_a_actualizar = int(input("Ingrese el ID del dispositivo a actualizar: "))
        disp_existente = dispositivo_service.obtener_por_id(id_a_actualizar)
        
        if not disp_existente:
            print("Error: Dispositivo no encontrado.")
            return

        print(f"Actualizando: {disp_existente}")
        
        # Pide el tipo de dispositivo
        tipo_final = disp_existente.tipo
        tipos = tipo_service.obtener_todos()
        for t in tipos:
            print(f"ID: {t.id_tipo} - {t.nombre}")
        id_tipo_nuevo_str = input(f"Nuevo ID de tipo (actual: {disp_existente.tipo.id_tipo}) (deje vacío para no cambiar): ")
        
        if id_tipo_nuevo_str:
            id_tipo_nuevo = int(id_tipo_nuevo_str)
            tipo_seleccionado = tipo_service.obtener_por_id(id_tipo_nuevo)
            if tipo_seleccionado:
                tipo_final = tipo_seleccionado
            else:
                print("Advertencia: ID de tipo inválido. Se mantendrá el tipo actual.")
        
        ubicacion = input(f"Nueva ubicación (actual: {disp_existente.ubicacion}) (deje vacío para no cambiar): ") or disp_existente.ubicacion
        marca = input(f"Nueva marca (actual: {disp_existente.marca}) (deje vacío para no cambiar): ") or disp_existente.marca
        modelo = input(f"Nuevo modelo (actual: {disp_existente.modelo}) (deje vacío para no cambiar): ") or disp_existente.modelo
        estado = input(f"Nuevo estado (actual: {disp_existente.estado}) (deje vacío para no cambiar): ") or disp_existente.estado

        # Llama al servicio con los datos
        if dispositivo_service.actualizar_dispositivo(id_a_actualizar, tipo_final, ubicacion, marca, modelo, estado):
            print("Dispositivo actualizado con éxito.") 

    except ValueError:
        print("Error: El ID debe ser un número.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def _eliminar_dispositivo(dispositivo_service: DispositivoService):
    '''Pide ID y confirmación para eliminar.'''
    try:
        id_a_borrar = int(input("Ingrese el ID del dispositivo a eliminar: "))
        disp = dispositivo_service.obtener_por_id(id_a_borrar)
        if not disp:
            print("Error: Dispositivo no encontrado.")
            return
        
        confirm = input(f"¿Seguro que desea eliminar '{disp}'? (s/n): ").lower()
        if confirm == 's':
            if dispositivo_service.eliminar_dispositivo(id_a_borrar):
                print("Dispositivo eliminado con éxito.")
        else:
            print("Operación cancelada.")
    except ValueError:
        print("Error: El ID debe ser un número.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def _cambiar_rol_usuario(usuario_service: UsuarioService):
    '''Pide DNI, confirma y cambia rol.'''
    try:
        dni_a_cambiar = input("Ingrese el DNI del usuario a modificar: ")
        usuario_a_modificar = usuario_service.obtener_por_dni(dni_a_cambiar)
        
        if not usuario_a_modificar:
            print("Error: Usuario no encontrado.")
            return # Sale de la función

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
            if usuario_service.cambiar_rol_usuario(dni_a_cambiar, es_nuevo_admin):
                print("Rol actualizado con éxito.") 
        else:
            print("Operación cancelada.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def _ver_usuarios(usuario_service: UsuarioService):
    '''Muestra todos los usuarios.'''
    print("\n--- Listado de Usuarios ---")
    usuarios = usuario_service.obtener_todos_los_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for u in usuarios:
            print(f"- {u}")