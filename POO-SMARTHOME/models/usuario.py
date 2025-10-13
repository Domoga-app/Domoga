class Usuario:
    """Clase para manejar usuarios del sistema."""

    def __init__(self, dni, nombre, apellido, contrasena, es_admin=False):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._contrasena = contrasena
        self._es_admin = es_admin

    @property
    def dni(self):
        return self._dni

    @property
    def es_admin(self):
        return self._es_admin

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def contrasena(self):
        return self._contrasena

    def __str__(self):
        rol_str = "Administrador" if self._es_admin else "Estandar"
        return (
            f"dni: {self._dni}, rol: {rol_str}, "
            f"nombre: {self._nombre}, apellido: {self._apellido}"
        )