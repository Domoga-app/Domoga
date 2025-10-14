from .dispositivo import Dispositivo

class Automatizacion:
    def __init__(self, id_automatizacion: int, nombre: str, dias: str, hora, accion: str):
        self._id_automatizacion = id_automatizacion
        self._nombre = nombre
        self._dias = dias
        self._hora = hora
        self._accion = accion
        self._dispositivos_afectados = []

    @property
    def id_automatizacion(self):
        return self._id_automatizacion

    @property
    def nombre(self):
        return self._nombre

    @property
    def dispositivos_afectados(self):
        return self._dispositivos_afectados

    def agregar_dispositivo(self, dispositivo):
        if dispositivo not in self._dispositivos_afectados:
            self._dispositivos_afectados.append(dispositivo)

    def __str__(self):
        num_disp = len(self._dispositivos_afectados)
        return (f"ID: {self._id_automatizacion}, Nombre: {self._nombre}, "
                f"Acción: {self._accion}, Afecta a {num_disp} dispositivo(s)")
