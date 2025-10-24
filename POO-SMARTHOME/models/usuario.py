# models/usuario.py

import re
import string

class Usuario:
    def __init__(self, id_usuario: int = None, dni: str = None, nombre: str = None, apellido: str = None, contrasena:str = None, es_admin: bool = False):
        self.__id_usuario = id_usuario
        self.__dni = str(dni) # Le puse el str porque si bien el DNI son números en Argentina, no hacemos calculos u otra operación con esos números
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contrasena = contrasena
        self.__es_admin = bool(es_admin)

    # ID
    @property
    def id(self):
        return self.__id_usuario    
    
    
    # DNI
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if not dni or not re.match(r'^\d{7,8}$', str(dni)):
            raise ValueError("DNI inválido. Debe tener 7 u 8 dígitos.")
        self.__dni = str(dni)

    # Nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 2:
            raise ValueError("El nombre no puede estar vacío o ser tan corto.")
        self.__nombre = nombre.strip()
    
    # Apellido
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        if not apellido or len(apellido.strip()) < 2:
            raise ValueError("El apellido no puede estar vacío o ser tan corto.")
        self.__apellido = apellido.strip()

    # Contraseña
    @property
    def contrasena(self):
        return "********"
    
    def _contrasena_real(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, nueva_contrasena: str):
        if len(nueva_contrasena) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        if not re.search(r"[A-Z]", nueva_contrasena):
            raise ValueError("Debe contener al menos una mayúscula")
        if not re.search(r"[a-z]",nueva_contrasena):
            raise ValueError("Debe contener al menos una minúscula")
        if not re.search(r"[0-9]",nueva_contrasena):
            raise ValueError("Debe contener al menos un número")
        if not any(caracter in string.punctuation for caracter in nueva_contrasena):
            raise ValueError("Debe contener al menos un carácter especial")
        
        self.__contrasena = nueva_contrasena

    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena

    # Rol
    @property
    def es_admin(self):
        return self.__es_admin

    @es_admin.setter
    def es_admin(self, es_admin):
        self.__es_admin = bool(es_admin)

    # print(Usuario())
    def __str__(self):
        rol_str = "Administrador" if self.__es_admin else "Estandar"
        return (
            f"DNI: {self.__dni}, Rol: {rol_str}, "
            f"Nombre: {self.__nombre}, Apellido: {self.__apellido}"
        )