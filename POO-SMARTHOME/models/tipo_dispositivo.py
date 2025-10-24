# models/tipo_dispositivo.py
class TipoDispositivo:
    def __init__(self, id_tipo, nombre):
        self.__id_tipo = id_tipo
        self.nombre = nombre

    @property
    def id_tipo(self):
        return self.__id_tipo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 3:
            raise ValueError("El nombre del tipo no puede estar vacío o ser tan corto.")
        self.__nombre = nombre.strip()

    def __str__(self):
        return f"{self.__nombre}"