# models/automatizacion.py
from .dispositivo import Dispositivo
from datetime import time, datetime

class Automatizacion:
    def __init__(self, id_automatizacion: int = None, nombre: str = None, dias: list[str] | str = None, hora: time = None, accion: str = None):
        self.__id_automatizacion = id_automatizacion
        self.__nombre = nombre
        self.__dias = dias
        self.__hora = hora
        self.__accion = accion
        self.__dispositivos_afectados = []

    # ID
    @property
    def id_automatizacion(self):
        return self.__id_automatizacion

    # Nombre
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not nombre or not (2 <= len(nombre.strip()) <= 30):
            raise ValueError("El nombre debe tener entre 2 y 30 caracteres.")
        self.__nombre = nombre.strip()
        
    # Días
    @property
    def dias(self):
        if not self.__dias:
            return ""
        
        mapping = {"L": "Lunes", "M": "Martes", "X": "Miércoles", "J": "Jueves",
               "V": "Viernes", "S": "Sábado", "D": "Domingo"}
        return ", ".join(mapping[d] for d in self.__dias)
        
    def _dias_str(self) -> str:
        return "".join(self.__dias)
    
    @dias.setter
    def dias(self, dias):
        '''Permite asignar días como string (ej: 'LMX' o 'L, M, X') y también como una lista (['L','M','X']).'''
        if dias is None:
            self.__dias = []
            return

        if isinstance(dias, str):
            # Elimina comas y espacios, convierte a mayúsculas
            dias = dias.replace(",", "").replace(" ", "").upper()
            self.__dias = [d for d in dias if d in "LMXJVSD"]
        elif isinstance(dias, list):
            self.__dias = [d.upper() for d in dias if d.upper() in "LMXJVSD"]
        else:
            raise ValueError("Dias debe ser string o lista con iniciales válidas")

    # Hora
    @property
    def hora(self):
        return self.__hora

    def _hora_str(self):
        if self.__hora:
            return self.__hora.strftime("%H:%M")
        return None

    @hora.setter
    def hora(self, hora):
        if hora is None:
            self.__hora = None
            return

        if isinstance(hora, str):
            try:
                dt = datetime.strptime(hora, "%H:%M")
                hora = dt.time()
            except ValueError:
                raise ValueError("La hora debe estar en formato HH:MM")
        elif not isinstance(hora, time):
            raise ValueError("La hora debe ser un objeto time o string HH:MM")

        self.__hora = hora
        
    # Acción
    @property
    def accion(self):
        return self.__accion

    @accion.setter
    def accion(self, accion):
        if not accion or not (2 <= len(accion.strip()) <= 30):
            raise ValueError("La acción debe tener entre 2 y 30 caracteres.")
        self.__accion = accion

    # Lista de dispositivos
    @property
    def dispositivos_afectados(self):
        return self.__dispositivos_afectados

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        if dispositivo not in self.__dispositivos_afectados:
            self.__dispositivos_afectados.append(dispositivo)

    # print(Automatizacion())
    def __str__(self):
        num_disp = len(self.dispositivos_afectados)
        return (f"ID: {self.id_automatizacion}, Nombre: {self.nombre}, "
                f"Día(s): {self.dias}, Hora: {self.hora}, "
                f"Acción: {self.accion}, Afecta a {num_disp} dispositivo(s)")