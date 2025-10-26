# models/usuario.py

import hashlib
import re
import string

class Usuario:
    def __init__(self, id_usuario: int = None, nombre_usuario: str = None, nombre: str = None, apellido: str = None, dni: str = None, es_admin: bool = False, contrasena:str = None):
        self.__id_usuario = id_usuario
        self.__nombre_usuario = nombre_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = str(dni) # Le puse el str porque si bien el DNI son números en Argentina, no hacemos calculos u otra operación con esos números
        self.__es_admin = bool(es_admin)
        self.__contrasena = contrasena

    # ID
    @property
    def id(self):
        return self.__id_usuario    
      
    # Nombre de usuario
    @property
    def nombre_usuario(self):
        return self.__nombre_usuario

    @nombre_usuario.setter
    def nombre_usuario(self, nombre_usuario):
        if not nombre_usuario or not (4 <= len(nombre_usuario.strip()) <= 30):
            raise ValueError("El nombre de usuario debe tener entre 4 y 30 caracteres.")
        self.__nombre_usuario = str(nombre_usuario)

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
        if not nombre or not (2 <= len(nombre.strip()) <= 30):
            raise ValueError("El nombre debe tener entre 2 y 30 caracteres.")
        self.__nombre = nombre.strip()
    
    # Apellido
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        if not apellido or not (2 <= len(apellido.strip()) <= 30):
            raise ValueError("El apellido debe tener entre 2 y 30 caracteres.")
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
        
        self.__contrasena = hashlib.sha256(nueva_contrasena.encode()).hexdigest()

    def verificar_contrasena(self, contrasena):
        return self.__contrasena == hashlib.sha256(contrasena.encode()).hexdigest()

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
            f"Usuario: {self.__nombre_usuario}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, "
            f"DNI: {self.__dni}, Rol: {rol_str}"
        )