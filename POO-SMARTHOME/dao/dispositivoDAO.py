# dao/dispositivoDAO.py
from conn.db_conn import get_connection
from dao.interface.i_dispositivoDAO import IDispositivoDAO
from models.dispositivo import Dispositivo
from models.tipo_dispositivo import TipoDispositivo

class DispositivoDAO(IDispositivoDAO):
    """
    Implementación DAO para la entidad Dispositivo, corregida para
    funcionar con el modelo simplificado y la nueva base de datos.
    """

    def crear(self, dispositivo: Dispositivo) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            # CORRECCIÓN: Se usa id_tipo y se añade dni_usuario
            query = """
                INSERT INTO dispositivos (id_tipo, ubicacion, marca, modelo, estado, dni_usuario)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            params = (
                dispositivo._tipo.id_tipo, dispositivo._ubicacion, dispositivo._marca,
                dispositivo._modelo, dispositivo._estado, dispositivo._dni_usuario
            )
            cursor.execute(query, params)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear dispositivo: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()

    def obtener_todos(self) -> list[Dispositivo]:
        conn = get_connection()
        dispositivos = []
        if not conn: return dispositivos
        try:
            cursor = conn.cursor(dictionary=True)
            # CORRECCIÓN: Se usa JOIN para obtener el nombre real del tipo
            query = """
                SELECT d.*, td.nombre as nombre_tipo FROM dispositivos d
                JOIN tipos_dispositivo td ON d.id_tipo = td.id_tipo
            """
            cursor.execute(query)
            for row in cursor.fetchall():
                tipo = TipoDispositivo(row['id_tipo'], row['nombre_tipo'])
                # CORRECCIÓN: Se construye el objeto Dispositivo completo
                dispositivo = Dispositivo(
                    id_dispositivo=row['id_dispositivo'], tipo=tipo, ubicacion=row['ubicacion'],
                    marca=row['marca'], modelo=row['modelo'], estado=row['estado'],
                    dni_usuario=row['dni_usuario']
                )
                dispositivos.append(dispositivo)
            return dispositivos
        except Exception as e:
            print(f"Error al obtener todos los dispositivos: {e}")
            return []
        finally:
            if conn.is_connected(): conn.close()

    def obtener_por_id(self, id_dispositivo: int) -> Dispositivo | None:
        conn = get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT d.*, td.nombre as nombre_tipo FROM dispositivos d
                JOIN tipos_dispositivo td ON d.id_tipo = td.id_tipo
                WHERE d.id_dispositivo = %s
            """
            cursor.execute(query, (id_dispositivo,))
            row = cursor.fetchone()
            if row:
                tipo = TipoDispositivo(row['id_tipo'], row['nombre_tipo'])
                return Dispositivo(
                    id_dispositivo=row['id_dispositivo'], tipo=tipo, ubicacion=row['ubicacion'],
                    marca=row['marca'], modelo=row['modelo'], estado=row['estado'],
                    dni_usuario=row['dni_usuario']
                )
            return None
        except Exception as e:
            print(f"Error al obtener dispositivo por ID: {e}")
            return None
        finally:
            if conn.is_connected(): conn.close()

    def actualizar(self, dispositivo: Dispositivo, id_dispositivo: int) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            # CORRECCIÓN: La consulta se adapta a las columnas correctas
            query = """
                UPDATE dispositivos SET id_tipo = %s, ubicacion = %s, marca = %s, 
                                     modelo = %s, estado = %s, dni_usuario = %s
                WHERE id_dispositivo = %s
            """
            params = (
                dispositivo._tipo.id_tipo, dispositivo._ubicacion, dispositivo._marca,
                dispositivo._modelo, dispositivo._estado, dispositivo._dni_usuario,
                id_dispositivo
            )
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar dispositivo: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()

    def eliminar(self, id_dispositivo: int) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            query = "DELETE FROM dispositivos WHERE id_dispositivo = %s"
            cursor.execute(query, (id_dispositivo,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar dispositivo: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()

    # --- MÉTODO NUEVO: Requerido por el menú de Usuario Estándar ---
    def obtener_por_usuario(self, dni_usuario: str) -> list[Dispositivo]:
        conn = get_connection()
        dispositivos = []
        if not conn: return dispositivos
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT d.*, td.nombre as nombre_tipo FROM dispositivos d
                JOIN tipos_dispositivo td ON d.id_tipo = td.id_tipo
                WHERE d.dni_usuario = %s
            """
            cursor.execute(query, (dni_usuario,))
            for row in cursor.fetchall():
                tipo = TipoDispositivo(row['id_tipo'], row['nombre_tipo'])
                dispositivo = Dispositivo(
                    id_dispositivo=row['id_dispositivo'], tipo=tipo, ubicacion=row['ubicacion'],
                    marca=row['marca'], modelo=row['modelo'], estado=row['estado'],
                    dni_usuario=row['dni_usuario']
                )
                dispositivos.append(dispositivo)
            return dispositivos
        except Exception as e:
            print(f"Error al obtener dispositivos del usuario: {e}")
            return []
        finally:
            if conn.is_connected(): conn.close()