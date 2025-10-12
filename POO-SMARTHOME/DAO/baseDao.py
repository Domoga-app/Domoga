from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional, Dict, Any
from datetime import datetime

T = TypeVar('T')


class BaseDAO(ABC, Generic[T]):
    def __init__(self):
        """Inicializa el DAO con almacenamiento en memoria."""
        self._storage: Dict[str, T] = {}
        self._id_counter: int = 0

    def _generar_id(self) -> str:
        """Genera un ID único para nuevos registros."""
        self._id_counter += 1
        return str(self._id_counter)

    @abstractmethod
    def _validar_entidad(self, entidad: T) -> None:
        """
        Valida la entidad antes de guardarla.
        Debe implementarse en cada DAO específico.

        Args:
            entidad: Entidad a validar

        Raises:
            ValueError: Si la validación falla
        """
        pass

    def crear(self, entidad: T) -> str:
        """
        Crea una nueva entidad en el almacenamiento.

        Args:
            entidad: Entidad a crear

        Returns:
            ID de la entidad creada

        Raises:
            ValueError: Si la validación falla
        """
        self._validar_entidad(entidad)

        # Generar ID si no existe
        if not hasattr(entidad, 'id') or not entidad.id:
            entidad.id = self._generar_id()

        # Agregar timestamps si la entidad los soporta
        if hasattr(entidad, 'fecha_creacion'):
            entidad.fecha_creacion = datetime.now()
        if hasattr(entidad, 'fecha_modificacion'):
            entidad.fecha_modificacion = datetime.now()

        self._storage[entidad.id] = entidad
        return entidad.id

    def obtener_por_id(self, id: str) -> Optional[T]:
        """
        Obtiene una entidad por su ID.

        Args:
            id: ID de la entidad

        Returns:
            Entidad encontrada o None
        """
        return self._storage.get(id)

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
        entidad = self.obtener_por_id(id)
        if not entidad:
            return False

        # Actualizar campos
        for campo, valor in datos.items():
            if hasattr(entidad, campo):
                setattr(entidad, campo, valor)

        # Actualizar timestamp de modificación
        if hasattr(entidad, 'fecha_modificacion'):
            entidad.fecha_modificacion = datetime.now()

        # Validar antes de guardar
        self._validar_entidad(entidad)

        self._storage[id] = entidad
        return True

    def eliminar(self, id: str) -> bool:
        """
        Elimina una entidad por su ID.

        Args:
            id: ID de la entidad a eliminar

        Returns:
            True si se eliminó, False si no existe
        """
        if id in self._storage:
            del self._storage[id]
            return True
        return False

    def listar(self, filtros: Optional[Dict[str, Any]] = None) -> List[T]:
        """
        Lista todas las entidades, opcionalmente filtradas.

        Args:
            filtros: Diccionario con filtros a aplicar

        Returns:
            Lista de entidades
        """
        entidades = list(self._storage.values())

        if not filtros:
            return entidades

        # Aplicar filtros
        resultado = []
        for entidad in entidades:
            cumple_filtros = True
            for campo, valor in filtros.items():
                if not hasattr(entidad, campo) or getattr(entidad, campo) != valor:
                    cumple_filtros = False
                    break
            if cumple_filtros:
                resultado.append(entidad)

        return resultado

    def contar(self, filtros: Optional[Dict[str, Any]] = None) -> int:
        """
        Cuenta las entidades que cumplen con los filtros.

        Args:
            filtros: Diccionario con filtros a aplicar

        Returns:
            Número de entidades
        """
        return len(self.listar(filtros))

    def existe(self, id: str) -> bool:
        """
        Verifica si existe una entidad con el ID dado.

        Args:
            id: ID a verificar

        Returns:
            True si existe, False en caso contrario
        """
        return id in self._storage

    def limpiar(self) -> None:
        """Elimina todos los registros (útil para testing)."""
        self._storage.clear()
        self._id_counter = 0
