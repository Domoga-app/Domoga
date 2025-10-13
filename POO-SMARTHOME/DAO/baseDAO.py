from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional, Dict, Any
from datetime import datetime
from contextlib import contextmanager
import mysql.connector
from conn.db_conn import get_connection

T = TypeVar('T')


class BaseDAO(ABC, Generic[T]):
    def __init__(self):
        """Inicializa el DAO y crea la tabla si no existe."""
        self._crear_tabla()

    @contextmanager
    def _get_connection(self):
        """Context manager para manejo de conexiones MySQL."""
        conn = None
        try:
            conn = get_connection()
            if conn is None:
                raise Exception(
                    "No se pudo establecer conexión con la base de datos")
            yield conn
            conn.commit()
        except mysql.connector.Error as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn and conn.is_connected():
                conn.close()

    @abstractmethod
    def _crear_tabla(self) -> None:
        """
        Crea la tabla en la base de datos si no existe.
        Debe implementarse en cada DAO específico con el schema correspondiente.
        """
        pass

    @abstractmethod
    def _nombre_tabla(self) -> str:
        """
        Retorna el nombre de la tabla para esta entidad.

        Returns:
            Nombre de la tabla
        """
        pass

    @abstractmethod
    def _entidad_a_dict(self, entidad: T) -> Dict[str, Any]:
        """
        Convierte una entidad a diccionario para insertar en BD.

        Args:
            entidad: Entidad a convertir

        Returns:
            Diccionario con los campos de la entidad (sin id si es auto-increment)
        """
        pass

    @abstractmethod
    def _row_a_entidad(self, row: Dict[str, Any]) -> T:
        """
        Convierte una fila de la BD a una entidad.

        Args:
            row: Diccionario con los datos de la fila

        Returns:
            Entidad del tipo correspondiente
        """
        pass

    @abstractmethod
    def _validar_entidad(self, entidad: T) -> None:
        """
        Valida la entidad antes de guardarla.

        Args:
            entidad: Entidad a validar

        Raises:
            ValueError: Si la validación falla
        """
        pass

    def _row_to_dict(self, cursor, row) -> Dict[str, Any]:
        """Convierte una fila de MySQL a diccionario."""
        if row is None:
            return None
        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, row))

    def crear(self, entidad: T) -> str:
        """
        Crea una nueva entidad en la base de datos.

        Args:
            entidad: Entidad a crear

        Returns:
            ID de la entidad creada

        Raises:
            ValueError: Si la validación falla
        """
        self._validar_entidad(entidad)

        datos = self._entidad_a_dict(entidad)

        # Agregar timestamps
        datos['fecha_creacion'] = datetime.now()
        datos['fecha_modificacion'] = datetime.now()

        # Preparar la consulta SQL
        columnas = ', '.join(datos.keys())
        placeholders = ', '.join(['%s' for _ in datos])
        valores = tuple(datos.values())

        sql = f"INSERT INTO {self._nombre_tabla()} ({columnas}) VALUES ({placeholders})"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores)

            # Obtener el ID generado
            if 'id' in datos and datos['id']:
                return str(datos['id'])
            else:
                return str(cursor.lastrowid)

    def obtener_por_id(self, id: str) -> Optional[T]:
        """
        Obtiene una entidad por su ID.

        Args:
            id: ID de la entidad

        Returns:
            Entidad encontrada o None
        """
        sql = f"SELECT * FROM {self._nombre_tabla()} WHERE id = %s"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
            row = cursor.fetchone()

            if row:
                row_dict = self._row_to_dict(cursor, row)
                return self._row_a_entidad(row_dict)
            return None

    def modificar(self, id: str, datos: Dict[str, Any]) -> bool:
        """
        Modifica una entidad existente.

        Args:
            id: ID de la entidad a modificar
            datos: Diccionario con los campos a modificar

        Returns:
            True si se modificó, False si no existe

        Raises:
            ValueError: Si la validación falla
        """
        # Verificar que existe
        entidad = self.obtener_por_id(id)
        if not entidad:
            return False

        # Actualizar timestamp
        datos['fecha_modificacion'] = datetime.now()

        # Construir la consulta UPDATE
        set_clause = ', '.join([f"{campo} = %s" for campo in datos.keys()])
        valores = list(datos.values()) + [id]

        sql = f"UPDATE {self._nombre_tabla()} SET {set_clause} WHERE id = %s"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores)

            # Obtener la entidad actualizada para validar
            if cursor.rowcount > 0:
                entidad_actualizada = self.obtener_por_id(id)
                if entidad_actualizada:
                    self._validar_entidad(entidad_actualizada)

            return cursor.rowcount > 0

    def eliminar(self, id: str) -> bool:
        """
        Elimina una entidad por su ID.

        Args:
            id: ID de la entidad a eliminar

        Returns:
            True si se eliminó, False si no existe
        """
        sql = f"DELETE FROM {self._nombre_tabla()} WHERE id = %s"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
            return cursor.rowcount > 0

    def listar(self, filtros: Optional[Dict[str, Any]] = None) -> List[T]:
        """
        Lista todas las entidades, opcionalmente filtradas.

        Args:
            filtros: Diccionario con filtros a aplicar

        Returns:
            Lista de entidades
        """
        sql = f"SELECT * FROM {self._nombre_tabla()}"
        valores = []

        if filtros:
            condiciones = []
            for campo, valor in filtros.items():
                condiciones.append(f"{campo} = %s")
                valores.append(valor)
            sql += " WHERE " + " AND ".join(condiciones)

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            rows = cursor.fetchall()

            return [self._row_a_entidad(self._row_to_dict(cursor, row)) for row in rows]

    def contar(self, filtros: Optional[Dict[str, Any]] = None) -> int:
        """
        Cuenta las entidades que cumplen con los filtros.

        Args:
            filtros: Diccionario con filtros a aplicar

        Returns:
            Número de entidades
        """
        sql = f"SELECT COUNT(*) as total FROM {self._nombre_tabla()}"
        valores = []

        if filtros:
            condiciones = []
            for campo, valor in filtros.items():
                condiciones.append(f"{campo} = %s")
                valores.append(valor)
            sql += " WHERE " + " AND ".join(condiciones)

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0

    def existe(self, id: str) -> bool:
        """
        Verifica si existe una entidad con el ID dado.

        Args:
            id: ID a verificar

        Returns:
            True si existe, False en caso contrario
        """
        sql = f"SELECT 1 FROM {self._nombre_tabla()} WHERE id = %s LIMIT 1"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
            return cursor.fetchone() is not None

    def limpiar(self) -> None:
        """Elimina todos los registros (útil para testing)."""
        sql = f"DELETE FROM {self._nombre_tabla()}"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
