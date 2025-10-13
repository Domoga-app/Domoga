class Usuario:
    """Clase para manejar usuarios del sistema."""

    def __init__(self, dni, id_rol, nombre, apellido, contrasena):
        self.dni = dni
        self.id_rol = id_rol
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena

    @classmethod
    def crear_usuario(cls, dni, id_rol, nombre, apellido, contrasena):
        """Método de clase para crear un nuevo usuario."""
        return cls(dni, id_rol, nombre, apellido, contrasena)

    def recuperar_usuario(self):
        """Devuelve los datos del usuario."""
        return {
            "dni": self.dni,
            "id_rol": self.id_rol,
            "nombre": self.nombre,
            "apellido": self.apellido
        }

    def ingresar_usuario(self, dni, contrasena):
        """Valida las credenciales del usuario."""
        return self.dni == dni and self.contrasena == contrasena