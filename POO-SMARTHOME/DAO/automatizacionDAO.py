from typing import Optional, Dict, Any, List


from .baseDao import BaseDAO, T
from .models import Automatizacion


class AutomatizacionDAO(BaseDAO[Automatizacion]):
    def _validar_entidad(self, entidad: Automatizacion) -> None:

        if not entidad.id_hogar:
            raise ValueError("El ID del hogar (id_hogar) es obligatorio.")
        if not entidad.nombre or len(entidad.nombre) < 3:
            raise ValueError(
                "El nombre de la automatización es obligatorio y debe tener al menos 3 caracteres.")
        if not isinstance(entidad.dias, list) or not entidad.dias:
            raise ValueError("La lista de días ('dias') es obligatoria.")

        # Validación simple de formato de hora (ej: "HH:MM")
        if not entidad.hora or len(entidad.hora) != 5 or entidad.hora[2] != ':':
            raise ValueError("La hora debe estar en formato 'HH:MM'.")

        if not entidad.accion or len(entidad.accion) < 5:
            raise ValueError(
                "La acción ('accion') es obligatoria y debe ser descriptiva.")

        # Regla de negocio: No debe haber dos automatizaciones activas con el mismo
        # nombre y hogar (simple chequeo de unicidad).
        # Esto es un filtro simple, el DAO base no maneja la concurrencia compleja.
        automatizaciones_existentes = self.listar(
            filtros={'id_hogar': entidad.id_hogar, 'nombre': entidad.nombre})

        for auto in automatizaciones_existentes:
            if auto.id != entidad.id:
                raise ValueError(
                    f"Ya existe una automatización con el nombre '{entidad.nombre}' en el hogar '{entidad.id_hogar}'.")

    def listar_por_hogar(self, id_hogar: str) -> List[Automatizacion]:
        """
        Obtiene todas las automatizaciones configuradas para un hogar específico.
        """
        return self.listar(filtros={'id_hogar': id_hogar})

    # Método específico de negocio: Buscar automatizaciones activas para un día
    def buscar_por_dia(self, id_hogar: str, dia: str) -> List[Automatizacion]:
        """
        Busca automatizaciones para un hogar que tienen configurado un día específico.
        """
        # Se requiere un filtro manual ya que el atributo 'dias' es una lista
        automatizaciones_del_hogar = self.listar_por_hogar(id_hogar)

        # Se filtra la lista manualmente
        resultados = [
            auto for auto in automatizaciones_del_hogar
            if dia.upper() in [d.upper() for d in auto.dias]
        ]
        return resultados
