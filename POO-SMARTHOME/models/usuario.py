# models/usuario.py

import re

class Usuario:
    def __init__(self, dni, nombre, apellido, contrasena, es_admin=False):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.__contrasena = contrasena  # Guarda el valor real
        self.contrasena = contrasena # Llama al setter para validación
        self.es_admin = es_admin

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if not dni or not re.match(r'^\d{7,8}$', str(dni)):
            raise ValueError("DNI inválido. Debe tener 7 u 8 dígitos.")
        self.__dni = str(dni)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 2:
            raise ValueError("El nombre no puede estar vacío o ser tan corto.")
        self.__nombre = nombre.strip()
    
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        if not apellido or len(apellido.strip()) < 2:
            raise ValueError("El apellido no puede estar vacío o ser tan corto.")
        self.__apellido = apellido.strip()

    @property
    def contrasena(self):
        return "********" # Nunca devuelvas la contraseña real

    @contrasena.setter
    def contrasena(self, contrasena_plana):
        if not contrasena_plana or len(contrasena_plana) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres.")
        self.__contrasena = contrasena_plana

    def verificar_contrasena(self, contrasena_plana):
        return self.__contrasena == contrasena_plana

    @property
    def es_admin(self):
        return self.__es_admin

    @es_admin.setter
    def es_admin(self, es_admin):
        self.__es_admin = bool(es_admin)


    def __str__(self):
        rol_str = "Administrador" if self.__es_admin else "Estandar"
        return (
            f"DNI: {self.__dni}, Rol: {rol_str}, "
            f"Nombre: {self.__nombre}, Apellido: {self.__apellido}"
        )