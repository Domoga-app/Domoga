# dao/interfaces/i_tipo_dispositivoDAO.py
from abc import ABC, abstractmethod
from models import TipoDispositivo

class ITipoDispositivoDAO(ABC):

    @abstractmethod
    def crear(self, tipo_dispositivo: TipoDispositivo) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> list[TipoDispositivo]:
        pass

    @abstractmethod
    def obtener_por_id(self, id_tipo: int) -> TipoDispositivo | None:
        pass

    @abstractmethod
    def actualizar(self, id_tipo: int, tipo_dispositivo: TipoDispositivo) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_tipo: int) -> bool:
        pass