from abc import ABC, abstractmethod

class ITipoDispositivoDAO(ABC):
    """Interfaz para operaciones CRUD de TipoDispositivo."""

    @abstractmethod
    def crear(self, tipo_dispositivo):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id_tipo):
        pass

    @abstractmethod
    def actualizar(self, tipo_dispositivo, id_tipo):
        pass

    @abstractmethod
    def eliminar(self, id_tipo):
        pass
