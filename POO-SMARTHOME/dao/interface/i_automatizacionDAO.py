from abc import ABC, abstractmethod

class IAutomatizacionDAO(ABC):
    """Interfaz para operaciones de la entidad Automatización."""

    @abstractmethod
    def crear(self, automatizacion):
        """
        Crea una nueva automatización en la base de datos.
        Devuelve el ID de la nueva automatización creada.
        """
        pass

    @abstractmethod
    def obtener_por_id(self, id_automatizacion):
        """
        Busca y devuelve una automatización por su ID, incluyendo
        la lista de dispositivos que afecta.
        """
        pass

    @abstractmethod
    def obtener_todos(self):
        """Devuelve una lista de todas las automatizaciones."""
        pass

    @abstractmethod
    def actualizar(self, automatizacion):
        """
        Actualiza los datos base de una automatización existente
        (nombre, días, hora, acción).
        """
        pass

    @abstractmethod
    def eliminar(self, id_automatizacion):
        """Elimina una automatización de la base de datos por su ID."""
        pass

    @abstractmethod
    def vincular_dispositivo(self, id_automatizacion, id_dispositivo):
        """
        Crea una relación entre una automatización y un dispositivo
        en la tabla intermedia.
        """
        pass

    @abstractmethod
    def desvincular_dispositivo(self, id_automatizacion, id_dispositivo):
        """
        Elimina la relación entre una automatización y un dispositivo.
        """
        pass