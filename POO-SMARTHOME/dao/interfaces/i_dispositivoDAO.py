from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
    """Interfaz para operaciones CRUD de la entidad Dispositivo."""

    @abstractmethod
    def crear(self, dispositivo):
        """
        Guarda un nuevo dispositivo en la base de datos.
        """
        pass

    @abstractmethod
    def obtener_todos(self):
        """
        Devuelve una lista con todos los dispositivos de la base de datos.
        """
        pass

    @abstractmethod
    def obtener_por_id(self, id_dispositivo):
        """
        Busca y devuelve un dispositivo por su ID.
        """
        pass

    @abstractmethod
    def actualizar(self, dispositivo, id_dispositivo):
        """
        Actualiza los datos de un dispositivo existente en la base de datos.
        """
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo):
        """
        Elimina un dispositivo de la base de datos por su ID.
        """
        pass