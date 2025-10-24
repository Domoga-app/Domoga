# dao/usuarioDAO.py
from models.usuario import Usuario
from .interfaces.i_usuarioDAO import IUsuarioDAO
from .db_base import get_db_cursor 

class UsuarioDAO(IUsuarioDAO):
    
    def crear(self, usuario: Usuario) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "INSERT INTO usuarios (dni, es_admin, nombre, apellido, contrasena) VALUES (%s, %s, %s, %s, %s)"
                params = (usuario.dni, usuario.es_admin, usuario.nombre, usuario.apellido, usuario._Usuario__contrasena)
                cursor.execute(query, params)
                conn.commit() 
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    def obtener_por_dni(self, dni: str) -> Usuario | None:
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("SELECT dni, es_admin, nombre, apellido, contrasena FROM usuarios WHERE dni = %s", (dni,))
                row = cursor.fetchone()
                if row:
                    row['es_admin'] = bool(row['es_admin'])
                    return Usuario(**row)
                return None
        except Exception as e:
            print(f"Error al obtener usuario por DNI: {e}")
            return None

    def cambiar_rol(self, dni: str, es_nuevo_admin: bool) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "UPDATE usuarios SET es_admin = %s WHERE dni = %s"
                cursor.execute(query, (es_nuevo_admin, dni))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al cambiar rol: {e}")
            return False
            
    def obtener_todos(self) -> list[Usuario]:
        usuarios = []
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("SELECT dni, es_admin, nombre, apellido, contrasena FROM usuarios")
                for row in cursor.fetchall():
                    row['es_admin'] = bool(row['es_admin'])
                    usuarios.append(Usuario(**row))
            return usuarios
        except Exception as e:
            print(f"Error al obtener todos los usuarios: {e}")
            return []

    def actualizar(self, dni: str, usuario: Usuario) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = """
                    UPDATE usuarios SET 
                        nombre = %s, apellido = %s, contrasena = %s, es_admin = %s 
                    WHERE dni = %s
                """
                params = (
                    usuario.nombre, 
                    usuario.apellido, 
                    usuario._Usuario__contrasena, 
                    usuario.es_admin,
                    dni
                )
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    def eliminar(self, dni: str) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("DELETE FROM usuarios WHERE dni = %s", (dni,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False