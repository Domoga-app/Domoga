from conn.db_conn import get_connection
from models.usuario import Usuario
from dao.interfaces.i_usuarioDAO import IUsuarioDAO

class UsuarioDAO(IUsuarioDAO):
    def __init__(self):
        pass

    def crear(self, dni: str, nombre: str, apellido: str, contrasena: str) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            query = "INSERT INTO usuarios (dni, es_admin, nombre, apellido, contrasena) VALUES (%s, %s, %s, %s, %s)"
            params = (dni, False, nombre, apellido, contrasena)
            cursor.execute(query, params)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False
        finally:
            if conn.is_connected():
                conn.close()

    def obtener_por_dni(self, dni: str) -> Usuario | None:
        conn = get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT dni, es_admin, nombre, apellido, contrasena FROM usuarios WHERE dni = %s", (dni,))
            row = cursor.fetchone()
            if row:
                row['es_admin'] = bool(row['es_admin'])
                return Usuario(**row)
            return None
        except Exception as e:
            print(f"Error al obtener usuario por DNI: {e}")
            return None
        finally:
            if conn.is_connected():
                conn.close()
    
    def obtener_todos(self) -> list[Usuario]:
        conn = get_connection()
        usuarios = []
        if not conn: return usuarios
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT dni, es_admin, nombre, apellido, contrasena FROM usuarios")
            for row in cursor.fetchall():
                row['es_admin'] = bool(row['es_admin'])
                usuarios.append(Usuario(**row))
            return usuarios
        except Exception as e:
            print(f"Error al obtener todos los usuarios: {e}")
            return []
        finally:
            if conn.is_connected():
                conn.close()

    def actualizar(self, usuario: Usuario, dni: str) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            query = """
                UPDATE usuarios
                SET nombre = %s, apellido = %s, contrasena = %s, es_admin = %s
                WHERE dni = %s
            """
            params = (usuario._nombre, usuario._apellido, usuario._contrasena, usuario.es_admin, dni)
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False
        finally:
            if conn.is_connected():
                conn.close()

    def eliminar(self, dni: str) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE dni = %s", (dni,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            if conn.is_connected():
                conn.close()

    def cambiar_rol(self, dni: str, es_nuevo_admin: bool) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            query = "UPDATE usuarios SET es_admin = %s WHERE dni = %s"
            cursor.execute(query, (es_nuevo_admin, dni))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al cambiar rol: {e}")
            return False
        finally:
            if conn.is_connected():
                conn.close()