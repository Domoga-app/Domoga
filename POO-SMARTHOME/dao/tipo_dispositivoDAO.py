from conn.db_conn import get_connection
from dao.interfaces.i_tipo_dispositivoDAO import ITipoDispositivoDAO
from models.tipo_dispositivo import TipoDispositivo

class TipoDispositivoDAO(ITipoDispositivoDAO):

    def crear(self, tipo_dispositivo: TipoDispositivo):
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            query = "INSERT INTO tipos_dispositivo (nombre) VALUES (%s)"
            cursor.execute(query, (tipo_dispositivo._nombre,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear tipo de dispositivo: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()

    def obtener_todos(self) -> list[TipoDispositivo]:
        conn = get_connection()
        tipos = []
        if not conn: return tipos
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tipos_dispositivo")
            for row in cursor.fetchall():
                tipos.append(TipoDispositivo(row["id_tipo"], row["nombre"]))
            return tipos
        except Exception as e:
            print(f"Error al obtener tipos de dispositivos: {e}")
            return []
        finally:
            if conn.is_connected(): conn.close()

    def obtener_por_id(self, id_tipo: int) -> TipoDispositivo | None:
        conn = get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tipos_dispositivo WHERE id_tipo = %s", (id_tipo,))
            row = cursor.fetchone()
            if row:
                return TipoDispositivo(row["id_tipo"], row["nombre"])
            return None
        except Exception as e:
            print(f"Error al obtener tipo de dispositivo por ID: {e}")
            return None
        finally:
            if conn.is_connected(): conn.close()

    def actualizar(self, tipo_dispositivo: TipoDispositivo, id_tipo: int) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            query = "UPDATE tipos_dispositivo SET nombre = %s WHERE id_tipo = %s"
            cursor.execute(query, (tipo_dispositivo._nombre, id_tipo))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar tipo de dispositivo: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()

    def eliminar(self, id_tipo: int) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tipos_dispositivo WHERE id_tipo = %s", (id_tipo,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar tipo de dispositivo: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()