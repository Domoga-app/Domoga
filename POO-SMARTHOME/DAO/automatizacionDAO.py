from typing import Optional, Dict, Any, List
import json
from .baseDAO import BaseDAO
from models import Automatizacion


class AutomatizacionDAO(BaseDAO[Automatizacion]):

    def _crear_tabla(self) -> None:
        """Crea la tabla automatizaciones si no existe."""
        sql = """
        CREATE TABLE IF NOT EXISTS automatizaciones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_hogar INT NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            dias JSON NOT NULL,
            hora TIME NOT NULL,
            accion VARCHAR(255) NOT NULL,
            fecha_creacion DATETIME,
            fecha_modificacion DATETIME,
            INDEX idx_hogar (id_hogar),
            INDEX idx_nombre (nombre),
            INDEX idx_hora (hora),
            UNIQUE KEY unique_hogar_nombre (id_hogar, nombre)
        )
        """

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)

    def _nombre_tabla(self) -> str:
        """Retorna el nombre de la tabla."""
        return "automatizaciones"

    def _entidad_a_dict(self, entidad: Automatizacion) -> Dict[str, Any]:
        """Convierte una entidad Automatizacion a diccionario."""
        datos = {
            'id_hogar': entidad.id_hogar,
            'nombre': entidad.nombre,
            'dias': json.dumps(entidad.dias),  # Convertir lista a JSON
            'hora': entidad.hora,
            'accion': entidad.accion
        }

        # Si tiene ID y no es None, agregarlo
        if hasattr(entidad, 'id') and entidad.id:
            datos['id'] = entidad.id

        return datos

    def _row_a_entidad(self, row: Dict[str, Any]) -> Automatizacion:
        """Convierte una fila de la BD a una entidad Automatizacion."""
        # Convertir JSON string a lista
        dias = json.loads(row['dias']) if isinstance(
            row['dias'], str) else row['dias']

        # Convertir time a string formato HH:MM
        hora_str = str(row['hora'])
        if len(hora_str) > 5:
            # Si viene como HH:MM:SS, tomar solo HH:MM
            hora_str = hora_str[:5]

        automatizacion = Automatizacion(
            id_hogar=str(row['id_hogar']),
            nombre=row['nombre'],
            dias=dias,
            hora=hora_str,
            accion=row['accion'],
            id=str(row['id'])
        )

        automatizacion.fecha_creacion = row.get('fecha_creacion')
        automatizacion.fecha_modificacion = row.get('fecha_modificacion')

        return automatizacion

    def _validar_entidad(self, entidad: Automatizacion) -> None:
        """Valida la entidad Automatizacion antes de guardarla."""
        if not entidad.id_hogar:
            raise ValueError("El ID del hogar (id_hogar) es obligatorio.")

        if not entidad.nombre or len(entidad.nombre) < 3:
            raise ValueError(
                "El nombre de la automatización es obligatorio y debe tener al menos 3 caracteres.")

        if not isinstance(entidad.dias, list) or not entidad.dias:
            raise ValueError("La lista de días ('dias') es obligatoria.")

        # Validar que los días sean válidos
        dias_validos = {'LUN', 'MAR', 'MIE', 'JUE', 'VIE', 'SAB', 'DOM'}
        for dia in entidad.dias:
            if dia.upper() not in dias_validos:
                raise ValueError(
                    f"El día '{dia}' no es válido. Debe ser uno de: {', '.join(dias_validos)}.")

        # Validación simple de formato de hora (ej: "HH:MM")
        if not entidad.hora or len(entidad.hora) != 5 or entidad.hora[2] != ':':
            raise ValueError("La hora debe estar en formato 'HH:MM'.")

        # Validar que la hora sea válida
        try:
            hora_parts = entidad.hora.split(':')
            horas = int(hora_parts[0])
            minutos = int(hora_parts[1])
            if not (0 <= horas <= 23 and 0 <= minutos <= 59):
                raise ValueError("La hora debe estar entre 00:00 y 23:59.")
        except (ValueError, IndexError):
            raise ValueError("La hora debe estar en formato 'HH:MM' válido.")

        if not entidad.accion or len(entidad.accion) < 5:
            raise ValueError(
                "La acción ('accion') es obligatoria y debe ser descriptiva.")

        # Validar unicidad: No dos automatizaciones con mismo nombre y hogar
        # Solo si no estamos modificando (id existe)
        automatizaciones_existentes = self.listar(
            filtros={'id_hogar': entidad.id_hogar, 'nombre': entidad.nombre})

        for auto in automatizaciones_existentes:
            if str(auto.id) != str(entidad.id):
                raise ValueError(
                    f"Ya existe una automatización con el nombre '{entidad.nombre}' en el hogar '{entidad.id_hogar}'.")

    def listar_por_hogar(self, id_hogar: str) -> List[Automatizacion]:
        """Obtiene todas las automatizaciones configuradas para un hogar específico."""
        return self.listar(filtros={'id_hogar': id_hogar})

    def buscar_por_dia(self, id_hogar: str, dia: str) -> List[Automatizacion]:
        """
        Busca automatizaciones para un hogar que tienen configurado un día específico.
        Utiliza JSON_CONTAINS para búsqueda eficiente en MySQL.
        """
        sql = f"""
        SELECT * FROM {self._nombre_tabla()} 
        WHERE id_hogar = %s 
        AND JSON_CONTAINS(dias, %s, '$')
        """

        # JSON_CONTAINS requiere el valor como JSON string
        dia_json = json.dumps(dia.upper())

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id_hogar, dia_json))
            rows = cursor.fetchall()

            return [self._row_a_entidad(self._row_to_dict(cursor, row)) for row in rows]

    def buscar_por_hora(self, id_hogar: str, hora: str) -> List[Automatizacion]:
        """Busca automatizaciones para un hogar en una hora específica."""
        return self.listar(filtros={'id_hogar': id_hogar, 'hora': hora})

    def listar_por_rango_horario(self, id_hogar: str, hora_inicio: str, hora_fin: str) -> List[Automatizacion]:
        """
        Lista automatizaciones de un hogar en un rango horario.

        Args:
            id_hogar: ID del hogar
            hora_inicio: Hora inicio en formato HH:MM
            hora_fin: Hora fin en formato HH:MM
        """
        sql = f"""
        SELECT * FROM {self._nombre_tabla()} 
        WHERE id_hogar = %s 
        AND hora BETWEEN %s AND %s
        ORDER BY hora
        """

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id_hogar, hora_inicio, hora_fin))
            rows = cursor.fetchall()

            return [self._row_a_entidad(self._row_to_dict(cursor, row)) for row in rows]

    def obtener_proximas_automatizaciones(self, id_hogar: str, hora_actual: str, limite: int = 5) -> List[Automatizacion]:
        """
        Obtiene las próximas N automatizaciones a partir de una hora.

        Args:
            id_hogar: ID del hogar
            hora_actual: Hora actual en formato HH:MM
            limite: Número máximo de resultados
        """
        sql = f"""
        SELECT * FROM {self._nombre_tabla()} 
        WHERE id_hogar = %s 
        AND hora >= %s
        ORDER BY hora
        LIMIT %s
        """

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id_hogar, hora_actual, limite))
            rows = cursor.fetchall()

            return [self._row_a_entidad(self._row_to_dict(cursor, row)) for row in rows]

    def contar_por_hogar(self, id_hogar: str) -> int:
        """Cuenta las automatizaciones de un hogar."""
        return self.contar(filtros={'id_hogar': id_hogar})
