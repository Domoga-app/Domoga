from hogar import Hogar
class Usuario:
    """Clase para manejar usuarios del sistema."""

    def __init__(self, dni, id_rol, nombre, apellido, contraseña):
        self.dni = dni
        self.id_rol = id_rol
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self._hogares = []

    @classmethod
    def crear_usuario(cls, dni, id_rol, nombre, apellido, contraseña):
        """Método de clase para crear un nuevo usuario."""
        return cls(dni, id_rol, nombre, apellido, contraseña)

    def recuperar_usuario(self):
        """Devuelve los datos del usuario."""
        return {
            "dni": self.dni,
            "id_rol": self.id_rol,
            "nombre": self.nombre,
            "apellido": self.apellido
        }

    def ingresar_usuario(self, dni, contraseña):
        """Valida las credenciales del usuario."""
        return self.dni == dni and self.contraseña == contraseña

    def agregar_hogar(self, hogar: Hogar):
        if hogar not in self._hogares:
            self._hogares.append(hogar)