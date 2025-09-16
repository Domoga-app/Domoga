class Dispositivo:
    """Clase para manejar dispositivos del hogar inteligente."""

    def __init__(self, id_tipo, id_ubicacion, marca, modelo, estado):
        self.id_tipo = id_tipo
        self.id_ubicacion = id_ubicacion
        self.marca = marca
        self.modelo = modelo
        self.estado = estado

    @classmethod
    def crear_dispositivos(cls, id_tipo, id_ubicacion, marca, modelo, estado):
        """Método de clase para crear un nuevo dispositivo."""
        return cls(id_tipo, id_ubicacion, marca, modelo, estado)

    def gestionar_dispositivos(self, accion, datos=None):
        """Gestiona operaciones sobre el dispositivo."""
        if accion == "cambiar_estado" and datos:
            if "estado" in datos:
                self.estado = datos["estado"]
        return True

    def ver_dispositivos(self):
        """Devuelve los datos del dispositivo."""
        return {
            "id_tipo": self.id_tipo,
            "id_ubicacion": self.id_ubicacion,
            "marca": self.marca,
            "modelo": self.modelo,
            "estado": self.estado
        }

    def ejecutar_accion(self, accion):
        """Ejecuta una acción sobre el dispositivo."""
        if accion == "apagar":
            self.estado = "apagado"
        elif accion == "encender":
            self.estado = "encendido"
        return True

    def borrar_dispositivos(self):
        """Elimina el dispositivo actual."""
        return True
