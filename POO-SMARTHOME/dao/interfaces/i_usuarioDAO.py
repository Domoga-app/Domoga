from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
    """Interfaz para operaciones CRUD y de gestión de roles de Usuario."""

    @abstractmethod
    def crear(self, dni: str, nombre: str, apellido: str, contrasena: str):
        """Guarda un nuevo usuario en la base de datos."""
        pass

    @abstractmethod
    def obtener_por_dni(self, dni: str):
        """Busca y devuelve un usuario por su DNI."""
        pass

    @abstractmethod
    def obtener_todos(self):
        """Devuelve una lista de todos los usuarios."""
        pass

    @abstractmethod
    def actualizar(self, usuario, dni):
        """Actualiza los datos de un usuario existente."""
        pass

    @abstractmethod
    def eliminar(self, dni):
        """Elimina un usuario de la base de datos por su DNI."""
        pass

    @abstractmethod
    def cambiar_rol(self, dni, es_nuevo_admin):
        """Modifica el rol de un usuario (admin o estándar)."""
        pass