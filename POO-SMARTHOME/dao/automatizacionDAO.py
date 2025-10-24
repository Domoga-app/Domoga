from models import Automatizacion, Dispositivo, TipoDispositivo
from .interfaces.i_automatizacionDAO import IAutomatizacionDAO
from .db_base import get_db_cursor

class AutomatizacionDAO(IAutomatizacionDAO):

    def crear(self, automatizacion: Automatizacion) -> int | None:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "INSERT INTO automatizaciones (nombre, dias, hora, accion) VALUES (%s, %s, %s, %s)"
                params = (automatizacion.nombre, automatizacion._dias_str(), automatizacion._hora_str(), automatizacion.accion)
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid # Devuelve el ID de la automatización creada
        except Exception as e:
            print(f"Error al crear automatización: {e}")
            return None

    def obtener_por_id(self, id_automatizacion: int) -> Automatizacion | None:
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("SELECT * FROM automatizaciones WHERE id_automatizacion = %s", (id_automatizacion,))
                row = cursor.fetchone()
                if not row: 
                    return None
                
                auto = Automatizacion(**row)
                
                # Buscamos los dispositivos vinculados
                dispositivos = self._obtener_dispositivos_vinculados(cursor, id_automatizacion)
                for d in dispositivos:
                    auto.agregar_dispositivo(d)
                
                return auto
        except Exception as e:
            print(f"Error al obtener automatización por ID: {e}")
            return None

    def _obtener_dispositivos_vinculados(self, cursor, id_automatizacion: int) -> list[Dispositivo]:
        ''' 
        Función interna para obtener los dispositivos vinculados a una automatización.
        La hicimos por separada para que la función obtener_por_id() quede mas limpia a la vista.
        '''
        query = """
            SELECT d.id_dispositivo, d.ubicacion, d.marca, d.modelo, d.estado,
                   t.id_tipo, t.nombre as tipo_nombre
            FROM dispositivos d
            JOIN tipos_dispositivo t ON d.id_tipo = t.id_tipo
            JOIN automatizacion_dispositivo ad ON d.id_dispositivo = ad.dispositivo_id
            WHERE ad.automatizacion_id = %s
        """
        cursor.execute(query, (id_automatizacion,))
        dispositivos = []
        for row in cursor.fetchall():
            tipo = TipoDispositivo(id_tipo=row['id_tipo'], nombre=row['tipo_nombre'])
            disp = Dispositivo(
                id_dispositivo=row['id_dispositivo'],
                tipo_dispositivo=tipo,
                ubicacion=row['ubicacion'],
                marca=row['marca'],
                modelo=row['modelo'],
                estado=row['estado']
            )
            dispositivos.append(disp)
        return dispositivos

    def obtener_todos(self) -> list[Automatizacion]:
        automatizaciones = []
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("SELECT * FROM automatizaciones")
                rows = cursor.fetchall()
                for row in rows:
                    auto = Automatizacion(**row)
                    automatizaciones.append(auto)
            return automatizaciones
        except Exception as e:
            print(f"Error al obtener todas las automatizaciones: {e}")
            return []

    def actualizar(self, id_automatizacion: int, automatizacion: Automatizacion) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "UPDATE automatizaciones SET nombre = %s, dias = %s, hora = %s, accion = %s WHERE id_automatizacion = %s"
                params = (
                    automatizacion.nombre, 
                    automatizacion.dias, 
                    automatizacion.hora, 
                    automatizacion.accion,
                    id_automatizacion
                )
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar automatización: {e}")
            return False

    def eliminar(self, id_automatizacion: int) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                cursor.execute("DELETE FROM automatizacion_dispositivo WHERE automatizacion_id = %s", (id_automatizacion,))
                cursor.execute("DELETE FROM automatizaciones WHERE id_automatizacion = %s", (id_automatizacion,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar automatización: {e}")
            return False

    def vincular_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "INSERT INTO automatizacion_dispositivo (automatizacion_id, dispositivo_id) VALUES (%s, %s)"
                cursor.execute(query, (id_automatizacion, id_dispositivo))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error al vincular dispositivo: {e}")
            return False

    def desvincular_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "DELETE FROM automatizacion_dispositivo WHERE automatizacion_id = %s AND dispositivo_id = %s"
                cursor.execute(query, (id_automatizacion, id_dispositivo))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al desvincular dispositivo: {e}")
            return False