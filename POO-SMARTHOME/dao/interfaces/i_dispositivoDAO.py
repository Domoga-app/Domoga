# dao/interfaces/i_dispositivoDAO.py
from abc import ABC, abstractmethod
from models import Dispositivo

class IDispositivoDAO(ABC):

    @abstractmethod
    def crear(self, dispositivo: Dispositivo) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> list[Dispositivo]:
        pass

    @abstractmethod
    def obtener_por_id(self, id_dispositivo: int) -> Dispositivo | None:
        pass

    @abstractmethod
    def actualizar(self, id_dispositivo: int, dispositivo: Dispositivo) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo: int) -> bool:
        pass