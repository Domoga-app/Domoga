# models/dispositivo.py
from .tipo_dispositivo import TipoDispositivo

class Dispositivo:
    def __init__(self, id_dispositivo, tipo_dispositivo: TipoDispositivo, ubicacion, marca, modelo, estado):
        self.__id_dispositivo = id_dispositivo
        self.tipo = tipo_dispositivo # Llama al setter
        self.ubicacion = ubicacion
        self.marca = marca
        self.modelo = modelo
        self.estado = estado
        
    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo_dispositivo):
        # Esta es la validación de "referencia a instancia de clase"
        if not isinstance(tipo_dispositivo, TipoDispositivo):
            raise ValueError("El tipo de dispositivo debe ser un objeto TipoDispositivo válido.")
        self.__tipo = tipo_dispositivo

    @property
    def ubicacion(self):
        return self.__ubicacion
    
    @ubicacion.setter
    def ubicacion(self, ubicacion):
        if not ubicacion or len(ubicacion.strip()) < 3:
            raise ValueError("La ubicación no puede estar vacía y/o debe tener más de 3 cacteres")
        self.__ubicacion = ubicacion.strip()

    # ... (puedes añadir setters para marca, modelo y estado si lo deseas) ...
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return (
            f"ID: {self.__id_dispositivo}, "
            f"Tipo: {self.__tipo.nombre}, "
            f"Ubicación: {self.__ubicacion}, Marca: {self.__marca}, "
            f"Modelo: {self.__modelo}, Estado: {self.__estado}"
        )