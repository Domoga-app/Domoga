# services/usuario_service.py
from models import Usuario
from dao import UsuarioDAO
from .interfaces import IUsuarioService

class UsuarioService(IUsuarioService):
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def iniciar_sesion(self, nombre_usuario: str, contrasena: str):
        if not nombre_usuario or not contrasena:
            print("Error: Nombre de usuario y contraseña son obligatorios.")
            return None
            
        try:
            usuario = self.usuario_dao.obtener_por_nombre_usuario(nombre_usuario)
            if usuario and usuario.verificar_contrasena(contrasena):
                return usuario
            else:
                print("Error: Nombre de usuario o contraseña incorrectos.")
                return None
        except Exception as e:
            print(f"Error en servicio de inicio de sesión: {e}")
            return None

    def registrar_usuario(self, nombre_usuario: str, nombre: str, apellido: str, dni: str, contrasena: str):
        try:
            if self.usuario_dao.obtener_por_nombre_usuario(nombre_usuario):
                print("Error: El usuario ya está registrado.")
                return False

            nuevo_usuario = Usuario()
            nuevo_usuario.nombre_usuario = nombre_usuario
            nuevo_usuario.nombre = nombre
            nuevo_usuario.apellido = apellido
            nuevo_usuario.dni = dni
            nuevo_usuario.contrasena = contrasena
            
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

    def cambiar_rol_usuario(self, nombre_usuario: str):
        try:
            usuario = self.usuario_dao.obtener_por_nombre_usuario(nombre_usuario)
            if not usuario:
                print("Error: Usuario no encontrado.")
                return False  

            if usuario.es_admin:
                rol_actual_str = "Administrador"
                accion_propuesta = "¿Desea cambiarlo a Estandar? (s/n): "
                es_nuevo_admin = False
            else:
                rol_actual_str = "Estandar"
                accion_propuesta = "¿Desea hacerlo Administrador? (s/n): "
                es_nuevo_admin = True

            print(f"El rol actual del usuario {nombre_usuario} es: {rol_actual_str}")
            confirmacion = input(accion_propuesta).lower()

            if confirmacion == 's':
                if self.usuario_dao.cambiar_rol(nombre_usuario, es_nuevo_admin):
                    print("Rol actualizado con éxito.")
                    return True
                else:
                    print("No se pudo actualizar el rol.")
                    return False
            else:
                print("Operación cancelada.")
                return False
        except Exception as e:
            print(f"Error en servicio de cambio de rol: {e}")
            return False

    def obtener_todos_los_usuarios(self):
        return self.usuario_dao.obtener_todos()