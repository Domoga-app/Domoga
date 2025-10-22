from .tipo_dispositivo import TipoDispositivo

class Dispositivo:

    def __init__(self, id_dispositivo, tipo_dispositivo: TipoDispositivo, ubicacion, marca, modelo, estado):
        self.__id_dispositivo = id_dispositivo
        self.__tipo = tipo_dispositivo
        self.__ubicacion = ubicacion
        self.__marca = marca
        self.__modelo = modelo
        self.__estado = estado
        
        
    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def ubicacion(self):
        return self.__ubicacion

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def estado(self):
        return self.__estado

    def __str__(self):
        return (
            f"id: {self.__id_dispositivo}, "
            f"tipo: {self.__tipo.nombre if self.__tipo else 'N/A'}, "
            f"ubicación: {self.__ubicacion}, marca: {self.__marca}, "
            f"modelo: {self.__modelo}, estado: {self.__estado}"
        )