# services/interfaces/i_tipo_dispositivo_service.py
from abc import ABC, abstractmethod
from models import TipoDispositivo


class ITipoDispositivoService(ABC):

    @abstractmethod
    def obtener_todos(self) -> list[TipoDispositivo]:
        pass

    @abstractmethod
    def obtener_por_id(self, id_tipo: int) -> TipoDispositivo:
        pass
