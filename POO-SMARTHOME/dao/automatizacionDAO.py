from conn.db_conn import get_connection
from dao.interface.i_automatizacionDAO import IAutomatizacionDAO
from models.automatizacion import Automatizacion
from models.dispositivo import Dispositivo
from models.tipo_dispositivo import TipoDispositivo

class AutomatizacionDAO(IAutomatizacionDAO):
    """Implementación DAO para la entidad Automatización."""

    def crear(self, automatizacion: Automatizacion):
        conn = get_connection()
        if not conn:
            return False

        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO automatizaciones (id_automatizacion, id_tipo_dispositivo, nombre, dias, hora, accion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                automatizacion._id_automatizacion,
                automatizacion._dispositivo._tipo._id_tipo,
                automatizacion._nombre,
                automatizacion._dias,
                automatizacion._hora,
                automatizacion._accion
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear automatización: {e}")
            return False
        finally:
            conn.close()

    def obtener_todos(self):
        conn = get_connection()
        automatizaciones = []
        if not conn:
            return automatizaciones

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM automatizaciones")
            for row in cursor.fetchall():
                tipo = TipoDispositivo(row["id_tipo_dispositivo"], "Desconocido")
                dispositivo = Dispositivo(tipo, "N/A", "N/A", "N/A", "N/A")
                automatizaciones.append(
                    Automatizacion(row["id_automatizacion"], dispositivo, row["nombre"], row["dias"], row["hora"], row["accion"])
                )
            return automatizaciones
        except Exception as e:
            print(f"Error al obtener automatizaciones: {e}")
            return []
        finally:
            conn.close()

    def obtener_por_id(self, id_automatizacion):
        conn = get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM automatizaciones WHERE id_automatizacion = %s", (id_automatizacion,))
            row = cursor.fetchone()
            if row:
                tipo = TipoDispositivo(row["id_tipo_dispositivo"], "Desconocido")
                dispositivo = Dispositivo(tipo, "N/A", "N/A", "N/A", "N/A")
                return Automatizacion(row["id_automatizacion"], dispositivo, row["nombre"], row["dias"], row["hora"], row["accion"])
            return None
        except Exception as e:
            print(f"Error al obtener automatización por ID: {e}")
            return None
        finally:
            conn.close()

    def actualizar(self, automatizacion: Automatizacion):
        conn = get_connection()
        if not conn:
            return False

        try:
            cursor = conn.cursor()
            query = """
                UPDATE automatizaciones
                SET id_tipo_dispositivo = %s, nombre = %s, dias = %s, hora = %s, accion = %s
                WHERE id_automatizacion = %s
            """
            cursor.execute(query, (
                automatizacion._dispositivo._tipo._id_tipo,
                automatizacion._nombre,
                automatizacion._dias,
                automatizacion._hora,
                automatizacion._accion,
                automatizacion._id_automatizacion
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar automatización: {e}")
            return False
        finally:
            conn.close()

    def eliminar(self, id_automatizacion):
        conn = get_connection()
        if not conn:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM automatizaciones WHERE id_automatizacion = %s", (id_automatizacion,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar automatización: {e}")
            return False
        finally:
            conn.close()
