from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
    """Interfaz para operaciones CRUD de Dispositivo."""

    @abstractmethod
    def crear(self, dispositivo):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id_dispositivo):
        pass

    @abstractmethod
    def actualizar(self, dispositivo):
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo):
        pass
