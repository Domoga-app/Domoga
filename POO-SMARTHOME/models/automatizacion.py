from typing import Optional, List, Any
from datetime import datetime


class Automatizacion:

    def __init__(self, id_hogar: str, nombre: str, dias: List[str], hora: str, accion: str, id: Optional[str] = None):

        self.id = id
        self.fecha_creacion: Optional[datetime] = None
        self.fecha_modificacion: Optional[datetime] = None

        # Atributos del modelo
        self.id_hogar = id_hogar
        self.nombre = nombre
        self.dias = dias  # Ej: ['LUN', 'MIE', 'VIE']
        self.hora = hora  # Ej: '07:30' (formato HH:MM)
        self.accion = accion  # Ej: 'encender_luces_sala'

    @classmethod
    def crear_automatizacion(cls, id_hogar: str, nombre: str, dias: List[str], hora: str, accion: str):
        """Método de clase para crear una nueva automatización."""
        return cls(id_hogar, nombre, dias, hora, accion)

    def monitor_automatizaciones(self) -> bool:
        """Monitorea las automatizaciones activas."""
        return True

    def ejecutar_accion(self) -> bool:
        """Ejecuta la acción de la automatización."""
        # Lógica real de ejecución
        return True

    # El método 'borrar_automatizaciones' no es necesario ya que el DAO maneja 'eliminar'.

    def mostrar_automatizaciones(self) -> dict:
        """Devuelve los datos de la automatización."""
        return {
            "id": self.id,
            "id_hogar": self.id_hogar,
            "nombre": self.nombre,
            "dias": self.dias,
            "hora": self.hora,
            "accion": self.accion
        }
