# services/tipo_dispositivo_service.py
from dao import TipoDispositivoDAO

class TipoDispositivoService:
    def __init__(self):
        self.tipo_dao = TipoDispositivoDAO()

    def obtener_todos(self):
        return self.tipo_dao.obtener_todos()

    def obtener_por_id(self, id_tipo):
        return self.tipo_dao.obtener_por_id(id_tipo)