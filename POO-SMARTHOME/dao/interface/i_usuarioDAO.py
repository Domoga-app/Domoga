from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
    """Interfaz para operaciones CRUD de Usuario."""

    @abstractmethod
    def crear(self, usuario):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_dni(self, dni):
        pass

    @abstractmethod
    def actualizar(self, usuario, dni):
        pass

    @abstractmethod
    def eliminar(self, dni):
        pass

    @abstractmethod
    def cambiar_rol(self, dni, es_admin):
        pass