# services/interfaces/i_dispositivo_service.py

from abc import ABC, abstractmethod
from models import Dispositivo, TipoDispositivo

class IDispositivoService(ABC):

    @abstractmethod
    def obtener_todos(self) -> list[Dispositivo]:
        pass

    @abstractmethod
    def obtener_por_id(self, id_dispositivo: int) -> Dispositivo:
        pass

    @abstractmethod
    def crear_dispositivo(
        self,
        tipo_seleccionado: TipoDispositivo,
        ubicacion: str,
        marca: str,
        modelo: str,
        estado: str
    ) -> bool:
        pass

    @abstractmethod
    def actualizar_dispositivo(
        self,
        id_a_actualizar: int,
        tipo_final: TipoDispositivo,
        ubicacion: str,
        marca: str,
        modelo: str,
        estado: str
    ) -> bool:
        pass

    @abstractmethod
    def eliminar_dispositivo(self, id_a_borrar: int) -> bool:
        pass
