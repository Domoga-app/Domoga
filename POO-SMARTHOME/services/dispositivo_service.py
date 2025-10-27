# services/dispositivo_service.py
from dao import DispositivoDAO
from models import Dispositivo, TipoDispositivo
from .interfaces import IDispositivoService

class DispositivoService(IDispositivoService):
    def __init__(self):
        self.dispositivo_dao = DispositivoDAO()

    def obtener_todos(self):
        try:
            return self.dispositivo_dao.obtener_todos()
        except Exception as e:
            print(f"Error en servicio al obtener todos los dispositivos: {e}")
            return [] # Devuelve una lista vacía en caso de error

    def obtener_por_id(self, id_dispositivo: int):
        try:
            return self.dispositivo_dao.obtener_por_id(id_dispositivo)
        except Exception as e:
            print(f"Error en servicio al obtener dispositivo por ID: {e}")
            return None

    def crear_dispositivo(self, tipo_seleccionado: TipoDispositivo, ubicacion: str, marca: str, modelo: str, estado: str) -> bool:
        try:
            
            nuevo_dispositivo = Dispositivo()
            nuevo_dispositivo.tipo = tipo_seleccionado
            nuevo_dispositivo.ubicacion = ubicacion
            nuevo_dispositivo.marca = marca
            nuevo_dispositivo.modelo = modelo
            nuevo_dispositivo.estado = estado
            
            if self.dispositivo_dao.crear(nuevo_dispositivo):
                return True
            else:
                return False
        
        except ValueError as ve: 
            print(f"Error de validación al crear dispositivo: {ve}")
            return False
        except Exception as e:
            print(f"Error inesperado en servicio al crear dispositivo: {e}")
            return False

    def actualizar_dispositivo(self, id_a_actualizar: int, tipo_final: TipoDispositivo, 
                               ubicacion, marca, modelo, estado) -> bool:
        try:
            disp_actualizado = Dispositivo(
                id_dispositivo=id_a_actualizar,
                tipo=tipo_final,
                ubicacion=ubicacion,
                marca=marca,
                modelo=modelo,
                estado=estado
            )
            
            if self.dispositivo_dao.actualizar(id_a_actualizar, disp_actualizado):
                return True
            else:
                return False
        except ValueError as ve:
            print(f"Error de validación al actualizar dispositivo: {ve}")
            return False
        except Exception as e:
            print(f"Error inesperado en servicio al actualizar dispositivo: {e}")
            return False

    def eliminar_dispositivo(self, id_a_borrar: int) -> bool:
        try:
            if self.dispositivo_dao.eliminar(id_a_borrar):
                return True
            else:
                return False
        except Exception as e:
            print(f"Error inesperado en servicio al eliminar dispositivo: {e}")
            return False