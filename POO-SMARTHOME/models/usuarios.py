from typing import Optional


class Usuario:
    def __init__(self, dni: str, id_rol: str, nombre: str, apellido: str, contraseña: str, id: Optional[str] = None):
        self.id = id
        self.dni = dni
        self.id_rol = id_rol
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        # Campos de timestamp para compatibilidad con BaseDAO
        self.fecha_creacion: Optional[datetime] = None
        self.fecha_modificacion: Optional[datetime] = None
        self._hogares = []

    @classmethod
    def crear_usuario(cls, dni: str, id_rol: str, nombre: str, apellido: str, contraseña: str):
        return cls(dni, id_rol, nombre, apellido, contraseña)

    def recuperar_usuario(self):
        return {
            "id": self.id,
            "dni": self.dni,
            "id_rol": self.id_rol,
            "nombre": self.nombre,
            "apellido": self.apellido
        }

    def ingresar_usuario(self, dni: str, contraseña: str) -> bool:
        """Valida las credenciales del usuario."""
        return self.dni == dni and self.contraseña == contraseña
