from typing import Optional, List
from datetime import datetime
# Asumiendo que Usuario y Dispositivo están importados
# from usuarios import Usuario
# from dispositivos import Dispositivo


class Hogar:
    def __init__(self, direccion: str, nombre: str, id_hogar_negocio: str, id: Optional[str] = None):

        self.id = id
        self.fecha_creacion: Optional[datetime] = None
        self.fecha_modificacion: Optional[datetime] = None

        # Atributos del modelo
        self.direccion = direccion
        self.nombre = nombre
        # ID de negocio (si es necesario mantenerlo)
        self.id_hogar_negocio = id_hogar_negocio
        self._usuarios: List['Usuario'] = []  # Lista de objetos Usuario
        # Lista de objetos Dispositivo
        self._dispositivos: List['Dispositivo'] = []

    @classmethod
    def agregar_hogar(cls, direccion: str, nombre: str, id_hogar_negocio: str):
        """Método de clase para agregar un nuevo hogar."""
        return cls(direccion, nombre, id_hogar_negocio)

    # El método 'eliminar_hogar' se sustituye por la función 'eliminar' del DAO

    def ver_hogares(self) -> dict:
        """Devuelve los datos del hogar."""
        return {
            "id": self.id,
            "id_hogar_negocio": self.id_hogar_negocio,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "num_usuarios": len(self._usuarios),
            "num_dispositivos": len(self._dispositivos)
        }

    def agregar_usuario(self, usuario: 'Usuario'):
        """Agrega un objeto Usuario a la lista."""
        # NOTA: En un DAO real, esto solo guardaría el ID del usuario.
        if usuario not in self._usuarios:
            self._usuarios.append(usuario)

    def agregar_dispositivo(self, dispositivo: 'Dispositivo'):
        """Agrega un objeto Dispositivo a la lista."""
        # NOTA: En un DAO real, esto solo guardaría el ID del dispositivo.
        if dispositivo not in self._dispositivos:
            self._dispositivos.append(dispositivo)
