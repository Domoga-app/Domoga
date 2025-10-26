# dao/dispositivoDAO.py
from models import Dispositivo, TipoDispositivo
from .interfaces import IDispositivoDAO
from .db_base import get_db_cursor

class DispositivoDAO(IDispositivoDAO):

    def crear(self, dispositivo: Dispositivo) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = """
                    INSERT INTO dispositivos (id_tipo, ubicacion, marca, modelo, estado)
                    VALUES (%s, %s, %s, %s, %s)
                """
                params = (
                    dispositivo.tipo.id_tipo, dispositivo.ubicacion, dispositivo.marca,
                    dispositivo.modelo, dispositivo.estado
                )
                cursor.execute(query, params)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error al crear dispositivo: {e}")
            return False

    def obtener_todos(self) -> list[Dispositivo]:
        dispositivos = []
        try:
            with get_db_cursor() as (conn, cursor):
                query = """
                    SELECT d.id_dispositivo, d.ubicacion, d.marca, d.modelo, d.estado,
                           t.id_tipo, t.nombre as tipo_nombre
                    FROM dispositivos d
                    JOIN tipos_dispositivo t ON d.id_tipo = t.id_tipo
                """
                cursor.execute(query)
                for row in cursor.fetchall():
                    tipo = TipoDispositivo(id_tipo=row['id_tipo'])
                    tipo.nombre=row['tipo_nombre']
                    
                    disp = Dispositivo(id_dispositivo=row['id_dispositivo'])
                    disp.tipo=tipo
                    disp.ubicacion=row['ubicacion']
                    disp.marca=row['marca']
                    disp.modelo=row['modelo']
                    disp.estado=row['estado']
                    
                    dispositivos.append(disp)
            return dispositivos
        except Exception as e:
            print(f"Error al obtener todos los dispositivos: {e}")
            return []

    def obtener_por_id(self, id_dispositivo: int) -> Dispositivo | None:
        try:
            with get_db_cursor() as (conn, cursor):
                query = """
                    SELECT d.id_dispositivo, d.ubicacion, d.marca, d.modelo, d.estado,
                           t.id_tipo, t.nombre as tipo_nombre
                    FROM dispositivos d
                    JOIN tipos_dispositivo t ON d.id_tipo = t.id_tipo
                    WHERE d.id_dispositivo = %s
                """
                cursor.execute(query, (id_dispositivo,))
                row = cursor.fetchone()
                if row:
                    tipo = TipoDispositivo(id_tipo=row['id_tipo'])
                    tipo.nombre=row['tipo_nombre']
                    
                    disp = Dispositivo(id_dispositivo=row['id_dispositivo'])
                    disp.tipo=tipo
                    disp.ubicacion=row['ubicacion']
                    disp.marca=row['marca']
                    disp.modelo=row['modelo']
                    disp.estado=row['estado']
                    
                    return disp
                return None
        except Exception as e:
            print(f"Error al obtener dispositivo por ID: {e}")
            return None

    def actualizar(self, id_dispositivo: int, dispositivo: Dispositivo) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = """
                    UPDATE dispositivos 
                    SET id_tipo = %s, ubicacion = %s, marca = %s,
                        modelo = %s, estado = %s
                    WHERE id_dispositivo = %s
                """
                params = (
                    dispositivo.tipo.id_tipo, dispositivo.ubicacion, dispositivo.marca,
                    dispositivo.modelo, dispositivo.estado, id_dispositivo
                )
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar dispositivo: {e}")
            return False

    def eliminar(self, id_dispositivo: int) -> bool:
        try:
            with get_db_cursor() as (conn, cursor):
                query = "DELETE FROM dispositivos WHERE id_dispositivo = %s"
                cursor.execute(query, (id_dispositivo,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar dispositivo: {e}")
            return False