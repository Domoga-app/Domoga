# services/usuario_service.py
from models import Usuario
from dao import UsuarioDAO

class UsuarioService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def iniciar_sesion(self, dni, contrasena):
        if not dni or not contrasena:
            print("Error: DNI y contraseña son obligatorios.")
            return None
            
        try:
            usuario = self.usuario_dao.obtener_por_dni(dni)
            if usuario and usuario.verificar_contrasena(contrasena):
                return usuario
            else:
                print("Error: DNI o contraseña incorrectos.")
                return None
        except Exception as e:
            print(f"Error en servicio de inicio de sesión: {e}")
            return None

    def registrar_usuario(self, dni, nombre, apellido, contrasena):
        try:
            if self.usuario_dao.obtener_por_dni(dni):
                print("Error: El DNI ya está registrado.")
                return False

            nuevo_usuario = Usuario(dni, nombre, apellido, contrasena, es_admin=False)
            
            if self.usuario_dao.crear(nuevo_usuario):
                print("¡Usuario registrado con éxito! Por favor, inicie sesión.")
                return True
            else:
                return False
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return False
        except Exception as e:
            print(f"Error inesperado en servicio de registro: {e}")
            return False

    def cambiar_rol_usuario(self, dni_a_cambiar):
        try:
            usuario = self.usuario_dao.obtener_por_dni(dni_a_cambiar)
            if not usuario:
                print("Error: Usuario no encontrado.")
                return
            
            if usuario.es_admin:
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
                if self.usuario_dao.cambiar_rol(dni_a_cambiar, es_nuevo_admin):
                    print("Rol actualizado con éxito.")
                else:
                    print("No se pudo actualizar el rol.")
            else:
                print("Operación cancelada.")
        except Exception as e:
            print(f"Error en servicio de cambio de rol: {e}")

    def obtener_todos_los_usuarios(self):
        return self.usuario_dao.obtener_todos()