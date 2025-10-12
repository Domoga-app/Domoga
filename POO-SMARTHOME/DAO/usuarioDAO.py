from typing import Optional, Dict, Any, List
from datetime import datetime


from .baseDao import BaseDAO, T
from .models import Usuario


class UsuarioDAO(BaseDAO[Usuario]):

    def _validar_entidad(self, entidad: Usuario) -> None:
        """
        Valida la entidad Usuario antes de guardarla.
        Reglas: todos los campos requeridos deben estar presentes y ser válidos.
        """
        if not entidad.dni:
            raise ValueError("El DNI del usuario es obligatorio.")
        if not entidad.nombre or len(entidad.nombre) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        if not entidad.apellido or len(entidad.apellido) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")
        if not entidad.id_rol:
            raise ValueError("El rol del usuario (id_rol) es obligatorio.")

        # Validar si el DNI ya existe, excepto si es una modificación del mismo registro
        dni_existente = self.buscar_por_dni(entidad.dni)
        if dni_existente and dni_existente.id != entidad.id:
            raise ValueError(
                f"Ya existe un usuario con el DNI: {entidad.dni}.")

        # Validación de contraseña simple
        if not hasattr(entidad, 'contraseña') or not entidad.contraseña:
            raise ValueError("La contraseña es obligatoria.")
        # Nota: En un sistema real, la contraseña nunca debería guardarse en texto plano
        # y esta validación se centraría en su fortaleza, no solo su existencia.

    # Método de acceso específico de negocio (no CRUD estándar)

    def buscar_por_dni(self, dni: str) -> Optional[Usuario]:
        """
        Busca un usuario utilizando su DNI, que es único.
        """
        # Utiliza el método listar del BaseDAO, filtrando por el campo 'dni'
        resultados = self.listar(filtros={'dni': dni})
        return resultados[0] if resultados else None

    # Método específico para autenticación (usando la lógica del modelo)
    def autenticar_usuario(self, dni: str, contraseña: str) -> Optional[Usuario]:
        """
        Busca el usuario por DNI y verifica la contraseña.
        """
        usuario = self.buscar_por_dni(dni)
        if usuario and usuario.ingresar_usuario(dni, contraseña):
            # En un sistema real, aquí devolverías un objeto sin la contraseña o un token.
            return usuario
        return None
