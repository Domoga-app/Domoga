# dao/usuarioDAO.py
from models import Usuario
from .interfaces import IUsuarioDAO
from .db_base import get_db_cursor 

class UsuarioDAO(IUsuarioDAO):
    
    def crear(self, usuario: Usuario) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "INSERT INTO usuarios (nombre_usuario, nombre, apellido, dni, es_admin, contrasena) VALUES (%s, %s, %s, %s, %s)"
                params = (usuario.nombre_usuario, usuario.nombre, usuario.apellido, usuario.dni, usuario.es_admin, usuario._contrasena_real())
                cursor.execute(query, params)
                conn.commit() 
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    def obtener_por_nombre_usuario(self, nombre_usuario: str) -> Usuario | None:
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("SELECT id_usuario, nombre_usuario, nombre, apellido, dni, es_admin, contrasena FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
                row = cursor.fetchone()
                if row:
                    usuario = Usuario(row['id_usuario'])
                    usuario.nombre_usuario = row['nombre_usuario']
                    usuario.nombre = row['nombre']
                    usuario.apellido = row['apellido']
                    usuario.dni = str(row['dni'])
                    usuario.es_admin = bool(row['es_admin'])
                    usuario.contrasena = row['contrasena']
                    return usuario
                return None
        except Exception as e:
            print(f"Error al obtener usuario por nombre de usuario: {e}")
            return None

    def cambiar_rol(self, nombre_usuario: str, es_nuevo_admin: bool) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "UPDATE usuarios SET es_admin = %s WHERE nombre_usuario = %s"
                cursor.execute(query, (es_nuevo_admin, nombre_usuario))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al cambiar rol: {e}")
            return False
            
    def obtener_todos(self) -> list[Usuario]:
        usuarios = []
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("SELECT id_usuario, nombre_usuario, nombre, apellido, dni, es_admin, contrasena FROM usuarios")
                for row in cursor.fetchall():
                    usuario = Usuario(row['id_usuario'])
                    usuario.nombre_usuario = row['nombre_usuario']
                    usuario.nombre = row['nombre']
                    usuario.apellido = row['apellido']
                    usuario.dni = str(row['dni'])
                    usuario.es_admin = bool(row['es_admin'])
                    usuario.contrasena = row['contrasena']
                    
                    usuarios.append(usuario)
            return usuarios
        except Exception as e:
            print(f"Error al obtener todos los usuarios: {e}")
            return []

    def actualizar(self, nombre_usuario: str, usuario: Usuario) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = """
                    UPDATE usuarios SET 
                        nombre = %s, apellido = %s, dni = %s, contrasena = %s, es_admin = %s 
                    WHERE nombre_usuario = %s
                """
                params = (
                    usuario.nombre, 
                    usuario.apellido, 
                    usuario.dni,
                    usuario.contrasena, 
                    usuario.es_admin,
                    nombre_usuario
                )
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    def eliminar(self, nombre_usuario: str) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("DELETE FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False