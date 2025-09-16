class Permiso:
    """Clase para manejar permisos (relación M:N entre Usuarios y Roles)."""

    def __init__(self, dni, id_rol):
        self.dni = dni
        self.id_rol = id_rol
