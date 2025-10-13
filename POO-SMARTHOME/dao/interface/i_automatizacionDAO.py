from abc import ABC, abstractmethod

class IAutomatizacionDAO(ABC):
    """Interfaz para operaciones CRUD de Automatización."""

    @abstractmethod
    def crear(self, automatizacion):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id_automatizacion):
        pass

    @abstractmethod
    def actualizar(self, automatizacion):
        pass

    @abstractmethod
    def eliminar(self, id_automatizacion):
        pass
