from typing import Optional, Dict, Any, List
from .baseDAO import BaseDAO
from models import Dispositivo


class DispositivoDAO(BaseDAO[Dispositivo]):

    def _crear_tabla(self) -> None:
        """Crea la tabla dispositivos si no existe."""
        sql = """
        CREATE TABLE IF NOT EXISTS dispositivos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            hogar INT NOT NULL,
            tipo VARCHAR(100) NOT NULL,
            ubicacion INT NOT NULL,

            marca VARCHAR(100) NOT NULL,
            modelo VARCHAR(100) NOT NULL,
            estado VARCHAR(50) NOT NULL DEFAULT 'apagado',
            fecha_creacion DATETIME,
            fecha_modificacion DATETIME,
            INDEX idx_hogar (hogar),
            INDEX idx_ubicacion (ubicacion),
            INDEX idx_tipo (tipo),
            INDEX idx_estado (estado)
        )
        """

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)

    def _nombre_tabla(self) -> str:
        """Retorna el nombre de la tabla."""
        return "dispositivos"

    def _entidad_a_dict(self, entidad: Dispositivo) -> Dict[str, Any]:
        """Convierte una entidad Dispositivo a diccionario."""
        datos = {
            'hogar': entidad.hogar,
            'tipo': entidad.tipo,
            'ubicacion': entidad.ubicacion,
            'marca': entidad.marca,
            'modelo': entidad.modelo,
            'estado': entidad.estado
        }

        # Si tiene ID y no es None, agregarlo
        if hasattr(entidad, 'id') and entidad.id:
            datos['id'] = entidad.id

        return datos

    def _row_a_entidad(self, row: Dict[str, Any]) -> Dispositivo:
        """Convierte una fila de la BD a una entidad Dispositivo."""
        dispositivo = Dispositivo(
            hogar=row['hogar'],
            tipo=row['tipo'],
            ubicacion=row['ubicacion'],
            marca=row['marca'],
            modelo=row['modelo'],
            estado=row['estado']
        )
        # Agregar el ID después de crear la instancia
        dispositivo.id = row['id']
        dispositivo.fecha_creacion = row.get('fecha_creacion')
        dispositivo.fecha_modificacion = row.get('fecha_modificacion')

        return dispositivo

    def _validar_entidad(self, entidad: Dispositivo) -> None:
        """Valida la entidad Dispositivo antes de guardarla."""
        # Validar campos obligatorios
        if not entidad.tipo:
            raise ValueError("El tipo de dispositivo es obligatorio.")
        if not entidad.hogar:
            raise ValueError("El hogar del dispositivo es obligatorio.")
        if not entidad.ubicacion:
            raise ValueError("La ubicación del dispositivo es obligatoria.")
        if not entidad.marca or len(entidad.marca) < 1:
            raise ValueError("La marca del dispositivo es obligatoria.")
        if not entidad.modelo or len(entidad.modelo) < 1:
            raise ValueError("El modelo del dispositivo es obligatorio.")

        # Validar estado
        estados_permitidos = {"encendido", "apagado", "standby", "desconocido"}
        if entidad.estado.lower() not in estados_permitidos:
            raise ValueError(
                f"El estado '{entidad.estado}' no es válido. Debe ser uno de: {', '.join(estados_permitidos)}.")

    # Métodos específicos de negocio

    def listar_por_ubicacion(self, ubicacion: int) -> List[Dispositivo]:
        """Obtiene todos los dispositivos en una ubicación específica."""
        return self.listar(filtros={'ubicacion': ubicacion})

    def listar_por_hogar(self, hogar: int) -> List[Dispositivo]:
        """Obtiene todos los dispositivos de un hogar específico."""
        return self.listar(filtros={'hogar': hogar})

    def obtener_por_tipo_y_estado(self, tipo: str, estado: str) -> List[Dispositivo]:
        """Obtiene dispositivos de un tipo específico que están en un estado particular."""
        return self.listar(filtros={'tipo': tipo, 'estado': estado})

    def cambiar_estado(self, id: str, nuevo_estado: str) -> bool:
        """
        Cambia el estado de un dispositivo.

        Args:
            id: ID del dispositivo
            nuevo_estado: Nuevo estado del dispositivo

        Returns:
            True si se cambió correctamente, False si no existe

        Raises:
            ValueError: Si el estado no es válido
        """
        # Validar que el estado sea válido
        estados_permitidos = {"encendido", "apagado", "standby", "desconocido"}
        if nuevo_estado.lower() not in estados_permitidos:
            raise ValueError(
                f"El estado '{nuevo_estado}' no es válido. Debe ser uno de: {', '.join(estados_permitidos)}.")

        return self.modificar(id, {'estado': nuevo_estado})

    def encender(self, id: str) -> bool:
        """Enciende un dispositivo."""
        return self.cambiar_estado(id, "encendido")

    def apagar(self, id: str) -> bool:
        """Apaga un dispositivo."""
        return self.cambiar_estado(id, "apagado")

    def buscar_por_marca_modelo(self, marca: str = None, modelo: str = None) -> List[Dispositivo]:
        """
        Busca dispositivos por marca y/o modelo usando LIKE.

        Args:
            marca: Marca del dispositivo (opcional)
            modelo: Modelo del dispositivo (opcional)

        Returns:
            Lista de dispositivos que coinciden
        """
        sql = f"SELECT * FROM {self._nombre_tabla()} WHERE 1=1"
        valores = []

        if marca:
            sql += " AND marca LIKE %s"
            valores.append(f"%{marca}%")

        if modelo:
            sql += " AND modelo LIKE %s"
            valores.append(f"%{modelo}%")

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            rows = cursor.fetchall()

            return [self._row_a_entidad(self._row_to_dict(cursor, row)) for row in rows]

    def listar_por_hogar_y_ubicacion(self, hogar: int, ubicacion: int) -> List[Dispositivo]:
        """Obtiene dispositivos de un hogar en una ubicación específica."""
        return self.listar(filtros={'hogar': hogar, 'ubicacion': ubicacion})

    def contar_por_estado(self, hogar: int, estado: str) -> int:
        """Cuenta dispositivos en un estado específico para un hogar."""
        return self.contar(filtros={'hogar': hogar, 'estado': estado})
