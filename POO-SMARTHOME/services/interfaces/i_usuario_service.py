# services/interfaces/i_usuario_service.py
from abc import ABC, abstractmethod
from models import Usuario


class IUsuarioService(ABC):

    @abstractmethod
    def iniciar_sesion(self, nombre_usuario: str, contrasena: str) -> Usuario:
        pass

    @abstractmethod
    def registrar_usuario(self, nombre_usuario: str, nombre: str, apellido: str, dni: str, contrasena: str) -> bool:
        pass

    @abstractmethod
    def cambiar_rol_usuario(self, nombre_usuario: str) -> bool:
        pass

    @abstractmethod
    def obtener_todos_los_usuarios(self) -> list[Usuario]:
        pass
