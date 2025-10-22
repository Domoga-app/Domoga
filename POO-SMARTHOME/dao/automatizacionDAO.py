from conn.db_conn import get_connection
from dao.interfaces.i_automatizacionDAO import IAutomatizacionDAO
from models.automatizacion import Automatizacion
from models.dispositivo import Dispositivo
from models.tipo_dispositivo import TipoDispositivo

class AutomatizacionDAO(IAutomatizacionDAO):

    def crear(self, automatizacion: Automatizacion) -> int | None:
        conn = get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor()
            query = "INSERT INTO automatizaciones (nombre, dias, hora, accion) VALUES (%s, %s, %s, %s)"
            params = (automatizacion._nombre, automatizacion._dias, automatizacion._hora, automatizacion._accion)
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al crear automatización: {e}")
            return None
        finally:
            if conn.is_connected(): conn.close()

    def obtener_por_id(self, id_automatizacion: int) -> Automatizacion | None:
        conn = get_connection()
        if not conn: return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM automatizaciones WHERE id_automatizacion = %s", (id_automatizacion,))
            row = cursor.fetchone()
            if not row: return None
            
            automatizacion = Automatizacion(row['id_automatizacion'], row['nombre'], row['dias'], row['hora'], row['accion'])

            query_disp = """
                SELECT d.*, td.nombre as nombre_tipo FROM dispositivos d
                JOIN tipos_dispositivo td ON d.id_tipo = td.id_tipo
                JOIN automatizacion_dispositivo ad ON d.id_dispositivo = ad.dispositivo_id
                WHERE ad.automatizacion_id = %s
            """
            cursor.execute(query_disp, (id_automatizacion,))
            for disp_row in cursor.fetchall():
                tipo = TipoDispositivo(disp_row['id_tipo'], disp_row['nombre_tipo'])
                dispositivo = Dispositivo(
                    id_dispositivo=disp_row['id_dispositivo'], tipo_dispositivo=tipo, ubicacion=disp_row['ubicacion'],
                    marca=disp_row['marca'], modelo=disp_row['modelo'], estado=disp_row['estado']
                )
                automatizacion.agregar_dispositivo(dispositivo)
            return automatizacion
        except Exception as e:
            print(f"Error al obtener automatización por ID: {e}")
            return None
        finally:
            if conn.is_connected(): conn.close()

    def obtener_todos(self) -> list[Automatizacion]:
        conn = get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id_automatizacion FROM automatizaciones")
            ids_automatizaciones = [row['id_automatizacion'] for row in cursor.fetchall()]
            
            automatizaciones_completas = []
            for id_auto in ids_automatizaciones:
                auto = self.obtener_por_id(id_auto)
                if auto:
                    automatizaciones_completas.append(auto)
            return automatizaciones_completas
        except Exception as e:
            print(f"Error al obtener todas las automatizaciones: {e}")
            return []
        finally:
            if conn.is_connected(): conn.close()

    def actualizar(self, automatizacion: Automatizacion) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            query = "UPDATE automatizaciones SET nombre = %s, dias = %s, hora = %s, accion = %s WHERE id_automatizacion = %s"
            params = (
                automatizacion._nombre, automatizacion._dias, 
                automatizacion._hora, automatizacion._accion, automatizacion.id_automatizacion
            )
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar automatización: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()

    def eliminar(self, id_automatizacion: int) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM automatizaciones WHERE id_automatizacion = %s", (id_automatizacion,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar automatización: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()

    def vincular_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        conn = get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            query = "INSERT INTO automatizacion_dispositivo (automatizacion_id, dispositivo_id) VALUES (%s, %s)"
            cursor.execute(query, (id_automatizacion, id_dispositivo))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al vincular dispositivo: {e}")
            return False
        finally:
            if conn.is_connected(): conn.close()