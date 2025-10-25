# dao/tipo_dispositivoDAO.py
from models import TipoDispositivo
from .interfaces import ITipoDispositivoDAO
from .db_base import get_db_cursor

class TipoDispositivoDAO(ITipoDispositivoDAO):

    def crear(self, tipo_dispositivo: TipoDispositivo) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "INSERT INTO tipos_dispositivo (nombre) VALUES (%s)"
                cursor.execute(query, (tipo_dispositivo.nombre,))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error al crear tipo de dispositivo: {e}")
            return False

    def obtener_todos(self) -> list[TipoDispositivo]:
        tipos = []
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("SELECT * FROM tipos_dispositivo")
                for row in cursor.fetchall():
                    tipos.append(TipoDispositivo(row["id_tipo"], row["nombre"]))
            return tipos
        except Exception as e:
            print(f"Error al obtener tipos de dispositivos: {e}")
            return []

    def obtener_por_id(self, id_tipo: int) -> TipoDispositivo | None:
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("SELECT * FROM tipos_dispositivo WHERE id_tipo = %s", (id_tipo,))
                row = cursor.fetchone()
                if row:
                    return TipoDispositivo(row["id_tipo"], row["nombre"])
                return None
        except Exception as e:
            print(f"Error al obtener tipo de dispositivo por ID: {e}")
            return None

    def actualizar(self, id_tipo: int, tipo_dispositivo: TipoDispositivo) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "UPDATE tipos_dispositivo SET nombre = %s WHERE id_tipo = %s"
                cursor.execute(query, (tipo_dispositivo.nombre, id_tipo))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar tipo de dispositivo: {e}")
            return False

    def eliminar(self, id_tipo: int) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("DELETE FROM tipos_dispositivo WHERE id_tipo = %s", (id_tipo,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar tipo de dispositivo: {e}")
            return False