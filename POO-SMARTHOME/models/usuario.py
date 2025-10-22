class Usuario:
    def __init__(self, dni, nombre, apellido, contrasena, es_admin=False):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contrasena = contrasena
        self.__es_admin = es_admin

    @property
    def dni(self):
        return self.__dni

    @property
    def es_admin(self):
        return self.__es_admin

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}" 

    @property
    def contrasena(self):
        return self.__contrasena
    
    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena

    def __str__(self):
        rol_str = "Administrador" if self.__es_admin else "Estandar"
        return (
            f"dni: {self.__dni}, rol: {rol_str}, "
            f"nombre: {self.__nombre}, apellido: {self.__apellido}"
        )