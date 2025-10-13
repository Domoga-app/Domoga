class TipoDispositivo:
    """Clase para manejar tipos de dispositivos."""

    def __init__(self, id_tipo, nombre):
        self._id_tipo = id_tipo
        self._nombre = nombre

    @property
    def id_tipo(self):
        return self._id_tipo

    @property
    def nombre(self):
        return self._nombre

    def __str__(self):
        return f"{self._nombre}"