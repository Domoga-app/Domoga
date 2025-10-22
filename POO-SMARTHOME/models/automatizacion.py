from .dispositivo import Dispositivo

class Automatizacion:
    def __init__(self, id_automatizacion: int, nombre: str, dias: str, hora, accion: str):
        self.__id_automatizacion = id_automatizacion
        self.__nombre = nombre
        self.__dias = dias
        self.__hora = hora
        self.__accion = accion
        self.__dispositivos_afectados = []

    @property
    def id_automatizacion(self):
        return self.__id_automatizacion

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def dias(self):
        return self.__dias
    
    @property
    def hora(self):
        return self.__hora

    @property
    def dispositivos_afectados(self):
        return self.__dispositivos_afectados

    def agregar_dispositivo(self, dispositivo):
        if dispositivo not in self.__dispositivos_afectados:
            self.__dispositivos_afectados.append(dispositivo)

    def __str__(self):
        num_disp = len(self.__dispositivos_afectados)
        return (f"ID: {self.__id_automatizacion}, Nombre: {self.__nombre}, "
                f"Acción: {self.__accion}, Afecta a {num_disp} dispositivo(s)")
