from typing import Optional, Dict, Any, List

from .baseDao import BaseDAO
from .models import Dispositivo


class DispositivoDAO(BaseDAO[Dispositivo]):

    def _validar_entidad(self, entidad: Dispositivo) -> None:
        """
        Valida la entidad Dispositivo antes de guardarla.
        """
        # Reglas de validación básicas
        if not entidad.id_tipo:
            raise ValueError(
                "El tipo de dispositivo (id_tipo) es obligatorio.")
        if not entidad.id_ubicacion:
            raise ValueError(
                "La ubicación del dispositivo (id_ubicacion) es obligatoria.")
        if not entidad.marca or len(entidad.marca) < 1:
            raise ValueError("La marca del dispositivo es obligatoria.")
        if not entidad.modelo or len(entidad.modelo) < 1:
            raise ValueError("El modelo del dispositivo es obligatorio.")

        # Lista de estados permitidos (ejemplo)
        estados_permitidos = {"encendido", "apagado", "standby", "desconocido"}
        if entidad.estado.lower() not in estados_permitidos:
            raise ValueError(
                f"El estado '{entidad.estado}' no es válido. Debe ser uno de: {', '.join(estados_permitidos)}.")

    # Método específico de negocio: Listar por Ubicación

    def listar_por_ubicacion(self, id_ubicacion: str) -> List[Dispositivo]:
        """
        Obtiene todos los dispositivos en una ubicación específica.
        """
        return self.listar(filtros={'id_ubicacion': id_ubicacion})

    # Método específico de negocio: Obtener por Tipo y Estado
    def obtener_por_tipo_y_estado(self, id_tipo: str, estado: str) -> List[Dispositivo]:
        """
        Obtiene dispositivos de un tipo específico que están en un estado particular.
        """
        return self.listar(filtros={'id_tipo': id_tipo, 'estado': estado})
