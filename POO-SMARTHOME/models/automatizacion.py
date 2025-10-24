# models/automatizacion.py
from .dispositivo import Dispositivo
import re

class Automatizacion:
    def __init__(self, id_automatizacion: int, nombre: str, dias: str, hora, accion: str):
        self.__id_automatizacion = id_automatizacion
        self.nombre = nombre
        self.dias = dias
        self.hora = hora
        self.accion = accion
        self.__dispositivos_afectados = []

    @property
    def id_automatizacion(self):
        return self.__id_automatizacion

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 3:
            raise ValueError("El nombre de la automatización no puede estar vacío.")
        self.__nombre = nombre.strip()
    
    @property
    def dias(self):
        return self.__dias
    
    @dias.setter
    def dias(self, dias):
        # Simple validación de ejemplo
        if not dias or len(dias.strip()) == 0:
            raise ValueError("Debe especificar los días.")
        self.__dias = dias

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        # Validación de formato HH:MM
        if not hora or not re.match(r'^\d{2}:\d{2}$', str(hora)):
            raise ValueError("La hora debe estar en formato HH:MM.")
        self.__hora = hora
        
    @property
    def accion(self):
        return self.__accion

    @accion.setter
    def accion(self, accion):
        if not accion or len(accion.strip()) < 3:
            raise ValueError("La acción no puede estar vacía.")
        self.__accion = accion

    @property
    def dispositivos_afectados(self):
        return self.__dispositivos_afectados

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        if dispositivo not in self.__dispositivos_afectados:
            self.__dispositivos_afectados.append(dispositivo)

    def __str__(self):
        num_disp = len(self.__dispositivos_afectados)
        return (f"ID: {self.__id_automatizacion}, Nombre: {self.__nombre}, "
                f"Días: {self.__dias}, Hora: {self.__hora}, "
                f"Acción: {self.__accion}, Afecta a {num_disp} dispositivo(s)")