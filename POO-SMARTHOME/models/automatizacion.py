from .dispositivo import Dispositivo

class Automatizacion:

    def __init__(self, id_automatizacion, dispositivo: Dispositivo, nombre, dias, hora, accion):
        self._id_automatizacion = id_automatizacion
        self._dispositivo = dispositivo
        self._nombre = nombre
        self._dias = dias
        self._hora = hora
        self._accion = accion

    @property
    def id_automatizacion(self):
        return self._id_automatizacion

    @property
    def dispositivo(self):
        return self._dispositivo

    @property
    def nombre(self):
        return self._nombre

    @property
    def dias(self):
        return self._dias

    @property
    def hora(self):
        return self._hora

    @property
    def accion(self):
        return self._accion

    def __str__(self):
        return (
            f"id_automatizacion: {self._id_automatizacion}, "
            f"dispositivo: {self._dispositivo.tipo if self._dispositivo else 'N/A'}, "
            f"nombre: {self._nombre}, dias: {self._dias}, hora: {self._hora}, accion: {self._accion}"
        )