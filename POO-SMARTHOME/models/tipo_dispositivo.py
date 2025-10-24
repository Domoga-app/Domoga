# models/tipo_dispositivo.py
class TipoDispositivo:
    def __init__(self, id_tipo: int = None, nombre: str = None):
        self.__id_tipo = id_tipo
        self.__nombre = nombre

    # ID
    @property
    def id_tipo(self):
        return self.__id_tipo

    # Nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 3:
            raise ValueError("El nombre del tipo no puede estar vacío o ser tan corto.")
        self.__nombre = nombre.strip()
        
        
    # print(TipoDispositivo())
    def __str__(self):
        return f"ID: {self.id_tipo}, Nombre: {self.nombre}"