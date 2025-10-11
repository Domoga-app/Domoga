from usuarios import Usuario
from dispositivos import Dispositivo

class Hogar:
    """Clase para manejar hogares."""

    def __init__(self, direccion, nombre, id_hogar):
        self.direccion = direccion
        self.nombre = nombre
        self.id_hogar = id_hogar
        self._usuarios = []
        self._dispositivos = []

    @classmethod
    def agregar_hogar(cls, direccion, nombre, id_hogar):
        """Método de clase para agregar un nuevo hogar."""
        return cls(direccion, nombre, id_hogar)

    def eliminar_hogar(self):
        """Elimina el hogar actual."""
        # En una implementación real, aquí se eliminaría de la base de datos
        return True

    def ver_hogares(self):
        """Devuelve los datos del hogar."""
        return {
            "id_hogar": self.id_hogar,
            "nombre": self.nombre,
            "direccion": self.direccion
        }

    def agregar_usuario(self, usuario: Usuario):
        if usuario not in self._usuarios:
            self._usuarios.append(usuario)

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        if dispositivo not in self._dispositivos:
            self._dispositivos.append(dispositivo)