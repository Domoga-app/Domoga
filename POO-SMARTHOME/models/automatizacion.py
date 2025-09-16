class Automatizacion:
    """Clase para manejar automatizaciones del hogar."""

    def __init__(self, id_automatizacion, id_hogar, nombre, dias, hora, accion):
        self.id_automatizacion = id_automatizacion
        self.id_hogar = id_hogar
        self.nombre = nombre
        self.dias = dias
        self.hora = hora
        self.accion = accion

    @classmethod
    def crear_automatizacion(cls, id_automatizacion, id_hogar, nombre, dias, hora, accion):
        """Método de clase para crear una nueva automatización."""
        return cls(id_automatizacion, id_hogar, nombre, dias, hora, accion)

    def monitor_automatizaciones(self):
        """Monitorea las automatizaciones activas."""
        # En una implementación real, aquí se verificarían las condiciones
        return True

    def ejecutar_accion(self):
        """Ejecuta la acción de la automatización."""
        # En una implementación real, aquí se ejecutaría la acción específica
        return True

    def borrar_automatizaciones(self):
        """Elimina la automatización actual."""
        return True

    def mostrar_automatizaciones(self):
        """Devuelve los datos de la automatización."""
        return {
            "id_automatizacion": self.id_automatizacion,
            "id_hogar": self.id_hogar,
            "nombre": self.nombre,
            "dias": self.dias,
            "hora": self.hora,
            "accion": self.accion
        }
