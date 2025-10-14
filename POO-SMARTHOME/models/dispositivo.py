from .tipo_dispositivo import TipoDispositivo

class Dispositivo:

    def __init__(self, id_dispositivo, tipo_dispositivo: TipoDispositivo, ubicacion, marca, modelo, estado):
        self._id_dispositivo = id_dispositivo
        self._tipo = tipo_dispositivo
        self._ubicacion = ubicacion
        self._marca = marca
        self._modelo = modelo
        self._estado = estado
        
        
    @property
    def id_dispositivo(self):
        return self._id_dispositivo

    @property
    def tipo(self):
        return self._tipo

    @property
    def ubicacion(self):
        return self._ubicacion

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def estado(self):
        return self._estado

    def __str__(self):
        return (
            f"id: {self._id_dispositivo}, "
            f"tipo: {self._tipo.nombre if self._tipo else 'N/A'}, "
            f"ubicación: {self._ubicacion}, marca: {self._marca}, "
            f"modelo: {self._modelo}, estado: {self._estado}"
        )