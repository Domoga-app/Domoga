# dao/interfaces/i_automatizacionDAO.py
from abc import ABC, abstractmethod
from models import Automatizacion

class IAutomatizacionDAO(ABC):

    @abstractmethod
    def crear(self, automatizacion: Automatizacion) -> int | None:
        pass

    @abstractmethod
    def obtener_por_id(self, id_automatizacion: int) -> Automatizacion | None:
        pass

    @abstractmethod
    def obtener_todos(self) -> list[Automatizacion]:
        pass

    @abstractmethod
    def actualizar(self, id_automatizacion: int, automatizacion: Automatizacion) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_automatizacion: int) -> bool:
        pass

    @abstractmethod
    def vincular_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        pass

    @abstractmethod
    def desvincular_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
        pass