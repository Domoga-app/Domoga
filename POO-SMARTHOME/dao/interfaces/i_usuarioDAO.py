# dao/interfaces/i_usuarioDAO.py
from abc import ABC, abstractmethod
from models import Usuario

class IUsuarioDAO(ABC):
    
    @abstractmethod
    def crear(self, usuario: Usuario) -> bool:
        pass

    @abstractmethod
    def obtener_por_dni(self, dni: str) -> Usuario | None:
        pass

    @abstractmethod
    def obtener_todos(self) -> list[Usuario]:
        pass
    
    @abstractmethod
    def actualizar(self, dni: str, usuario: Usuario) -> bool:
        pass

    @abstractmethod
    def eliminar(self, dni: str) -> bool:
        pass

    @abstractmethod
    def cambiar_rol(self, dni: str, es_nuevo_admin: bool) -> bool:
        pass