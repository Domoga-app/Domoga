from typing import Optional, Dict, Any, List
import hashlib
from .baseDAO import BaseDAO
from models import Usuario


class UsuarioDAO(BaseDAO[Usuario]):

    def _crear_tabla(self) -> None:
        """Crea la tabla usuarios si no existe."""
        sql = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            dni VARCHAR(20) NOT NULL UNIQUE,
            id_rol INT NOT NULL,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            contraseña VARCHAR(255) NOT NULL,
            fecha_creacion DATETIME,
            fecha_modificacion DATETIME,
            INDEX idx_dni (dni),
            INDEX idx_rol (id_rol),
            INDEX idx_nombre_apellido (nombre, apellido)
        )
        """

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)

    def _nombre_tabla(self) -> str:
        """Retorna el nombre de la tabla."""
        return "usuarios"

    def _hash_contraseña(self, contraseña: str) -> str:
        """
        Genera un hash SHA-256 de la contraseña.
        NOTA: En producción se recomienda usar bcrypt o argon2.
        """
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def _entidad_a_dict(self, entidad: Usuario) -> Dict[str, Any]:
        """Convierte una entidad Usuario a diccionario."""
        datos = {
            'dni': entidad.dni,
            'id_rol': entidad.id_rol,
            'nombre': entidad.nombre,
            'apellido': entidad.apellido,
            'contraseña': self._hash_contraseña(entidad.contraseña)
        }

        # Si tiene ID y no es None, agregarlo
        if hasattr(entidad, 'id') and entidad.id:
            datos['id'] = entidad.id

        return datos

    def _row_a_entidad(self, row: Dict[str, Any]) -> Usuario:
        """Convierte una fila de la BD a una entidad Usuario."""
        usuario = Usuario(
            dni=row['dni'],
            id_rol=str(row['id_rol']),
            nombre=row['nombre'],
            apellido=row['apellido'],
            contraseña=row['contraseña'],  # Ya está hasheada
            id=str(row['id'])
        )

        usuario.fecha_creacion = row.get('fecha_creacion')
        usuario.fecha_modificacion = row.get('fecha_modificacion')

        return usuario

    def _validar_entidad(self, entidad: Usuario) -> None:
        """
        Valida la entidad Usuario antes de guardarla.
        Reglas: todos los campos requeridos deben estar presentes y ser válidos.
        """
        if not entidad.dni:
            raise ValueError("El DNI del usuario es obligatorio.")

        # Validar formato de DNI (ajustar según tu país)
        if not entidad.dni.isdigit() or len(entidad.dni) < 7:
            raise ValueError(
                "El DNI debe ser numérico y tener al menos 7 dígitos.")

        if not entidad.nombre or len(entidad.nombre) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")

        if not entidad.apellido or len(entidad.apellido) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")

        if not entidad.id_rol:
            raise ValueError("El rol del usuario (id_rol) es obligatorio.")

        # Validar si el DNI ya existe, excepto si es una modificación del mismo registro
        dni_existente = self.buscar_por_dni(entidad.dni)
        if dni_existente and str(dni_existente.id) != str(entidad.id):
            raise ValueError(
                f"Ya existe un usuario con el DNI: {entidad.dni}.")

        # Validación de contraseña
        if not hasattr(entidad, 'contraseña') or not entidad.contraseña:
            raise ValueError("La contraseña es obligatoria.")

        # Validar fortaleza de contraseña (solo si no está hasheada)
        if len(entidad.contraseña) < 64:  # Si no es un hash (SHA-256 = 64 chars)
            if len(entidad.contraseña) < 6:
                raise ValueError(
                    "La contraseña debe tener al menos 6 caracteres.")

    def buscar_por_dni(self, dni: str) -> Optional[Usuario]:
        """
        Busca un usuario utilizando su DNI, que es único.

        Args:
            dni: DNI del usuario

        Returns:
            Usuario encontrado o None
        """
        resultados = self.listar(filtros={'dni': dni})
        return resultados[0] if resultados else None

    def autenticar_usuario(self, dni: str, contraseña: str) -> Optional[Usuario]:
        """
        Busca el usuario por DNI y verifica la contraseña.

        Args:
            dni: DNI del usuario
            contrasena: Contraseña en texto plano

        Returns:
            Usuario autenticado o None si las credenciales son inválidas
        """
        usuario = self.buscar_por_dni(dni)
        if usuario:
            # Comparar el hash de la contraseña ingresada con el almacenado
            contraseña_hash = self._hash_contraseña(contraseña)
            if usuario.contraseña == contraseña_hash:
                return usuario
        return None

    def cambiar_contraseña(self, id: str, contraseña_actual: str, contraseña_nueva: str) -> bool:
        """
        Cambia la contraseña de un usuario.

        Args:
            id: ID del usuario
            contrasena_actual: Contraseña actual para verificación
            contrasena_nueva: Nueva contraseña

        Returns:
            True si se cambió correctamente, False si la contraseña actual es incorrecta

        Raises:
            ValueError: Si la nueva contraseña no cumple los requisitos
        """
        usuario = self.obtener_por_id(id)
        if not usuario:
            return False

        # Verificar contraseña actual
        if usuario.contraseña != self._hash_contraseña(contraseña_actual):
            return False

        # Validar nueva contraseña
        if len(contraseña_nueva) < 6:
            raise ValueError(
                "La nueva contraseña debe tener al menos 6 caracteres.")

        # Actualizar contraseña
        return self.modificar(id, {'contraseña': self._hash_contraseña(contraseña_nueva)})

    def listar_por_rol(self, id_rol: str) -> List[Usuario]:
        """Obtiene todos los usuarios con un rol específico."""
        return self.listar(filtros={'id_rol': id_rol})

    def buscar_por_nombre(self, nombre: str = None, apellido: str = None) -> List[Usuario]:
        """
        Busca usuarios por nombre y/o apellido usando LIKE.

        Args:
            nombre: Nombre del usuario (opcional)
            apellido: Apellido del usuario (opcional)

        Returns:
            Lista de usuarios que coinciden
        """
        sql = f"SELECT * FROM {self._nombre_tabla()} WHERE 1=1"
        valores = []

        if nombre:
            sql += " AND nombre LIKE %s"
            valores.append(f"%{nombre}%")

        if apellido:
            sql += " AND apellido LIKE %s"
            valores.append(f"%{apellido}%")

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            rows = cursor.fetchall()

            return [self._row_a_entidad(self._row_to_dict(cursor, row)) for row in rows]

    def actualizar_perfil(self, id: str, nombre: str, apellido: str) -> bool:
        """
        Actualiza el nombre y apellido de un usuario.

        Args:
            id: ID del usuario
            nombre: Nuevo nombre
            apellido: Nuevo apellido

        Returns:
            True si se actualizó correctamente
        """
        return self.modificar(id, {'nombre': nombre, 'apellido': apellido})

    def existe_dni(self, dni: str) -> bool:
        """
        Verifica si existe un usuario con el DNI dado.

        Args:
            dni: DNI a verificar

        Returns:
            True si existe, False en caso contrario
        """
        return self.buscar_por_dni(dni) is not None

    def contar_por_rol(self, id_rol: str) -> int:
        """Cuenta usuarios por rol."""
        return self.contar(filtros={'id_rol': id_rol})
