class TipoDispositivo:

    def __init__(self, id_tipo, nombre):
        self.__id_tipo = id_tipo
        self.__nombre = nombre

    @property
    def id_tipo(self):
        return self.__id_tipo

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return f"{self.__nombre}"