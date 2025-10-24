# models/dispositivo.py
from .tipo_dispositivo import TipoDispositivo

class Dispositivo:
    def __init__(self, id_dispositivo: int = None, tipo_dispositivo: TipoDispositivo = None, ubicacion: str = None, marca: str = None, modelo: str = None, estado: str = None):
        self.__id_dispositivo = id_dispositivo
        self.__tipo = tipo_dispositivo
        self.__ubicacion = ubicacion
        self.__marca = marca
        self.__modelo = modelo
        self.__estado = estado
    
    # ID (Solo getter porque no se puede modificar) 
    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    # Tipo de Producto
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo_dispositivo):
        # Valida que el tipo ingresado sea un objeto de Tipo Dispositivo
        if not isinstance(tipo_dispositivo, TipoDispositivo):
            raise ValueError("El tipo de dispositivo debe ser un objeto TipoDispositivo válido.")
        self.__tipo = tipo_dispositivo

    # Ubicación
    @property
    def ubicacion(self):
        return self.__ubicacion
    
    @ubicacion.setter
    def ubicacion(self, ubicacion):
        if not ubicacion or len(ubicacion.strip()) < 3:
            raise ValueError("La ubicación no puede estar vacía y/o necesita tener más de 3 carácteres")
        self.__ubicacion = ubicacion.strip()

    # Marca
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    # Modelo
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):        
        self.__modelo = modelo

    # Estado
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        if not estado or len(estado.strip()) < 3:
            raise ValueError("El estado no puede estar vacío y/o necesita tener más de 3 carácteres")
        self.__estado = estado

    # print(Dispositivo())
    def __str__(self):
        return (
            f"ID: {self.id_dispositivo}, "
            f"Tipo: {self.tipo.nombre}, "
            f"Ubicación: {self.ubicacion}, Marca: {self.marca}, "
            f"Modelo: {self.modelo}, Estado: {self.estado}"
        )