from abc import ABC, abstractmethod

class ITipoDispositivoDAO(ABC):
    """Interfaz para operaciones CRUD de la entidad TipoDispositivo."""

    @abstractmethod
    def crear(self, tipo_dispositivo):
        """
        Guarda un nuevo tipo de dispositivo en la base de datos.
        """
        pass

    @abstractmethod
    def obtener_todos(self):
        """
        Devuelve una lista con todos los tipos de dispositivo.
        """
        pass

    @abstractmethod
    def obtener_por_id(self, id_tipo):
        """
        Busca y devuelve un tipo de dispositivo por su ID.
        """
        pass

    @abstractmethod
    def actualizar(self, tipo_dispositivo, id_tipo):
        """
        Actualiza el nombre de un tipo de dispositivo existente.
        """
        pass

    @abstractmethod
    def eliminar(self, id_tipo):
        """
        Elimina un tipo de dispositivo de la base de datos por su ID.
        """
        pass