from typing import Optional, List, Any


from .baseDao import BaseDAO, T
from .models import Hogar


class HogarDAO(BaseDAO[Hogar]):

    def _validar_entidad(self, entidad: Hogar) -> None:
        """
        Valida la entidad Hogar antes de guardarla.
        """
        if not entidad.nombre or len(entidad.nombre) < 3:
            raise ValueError(
                "El nombre del hogar es obligatorio y debe tener al menos 3 caracteres.")
        if not entidad.direccion or len(entidad.direccion) < 5:
            raise ValueError(
                "La dirección es obligatoria y debe ser detallada.")
        if not entidad.id_hogar_negocio:
            raise ValueError("El ID de negocio del hogar es obligatorio.")

        # Regla de negocio: El nombre del hogar debe ser único globalmente (o por lo menos en la simulación)
        hogares_existentes = self.listar(filtros={'nombre': entidad.nombre})

        for hogar in hogares_existentes:
            if hogar.id != entidad.id:
                raise ValueError(
                    f"Ya existe un hogar registrado con el nombre '{entidad.nombre}'.")

    # Método específico de negocio: Buscar por ID de Negocio

    def obtener_por_id_negocio(self, id_hogar_negocio: str) -> Optional[Hogar]:
        """
        Busca un hogar utilizando su ID de negocio (campo 'id_hogar_negocio').
        """
        resultados = self.listar(
            filtros={'id_hogar_negocio': id_hogar_negocio})
        return resultados[0] if resultados else None

    # Método específico de negocio: Listar por Dirección (búsqueda parcial)
    def buscar_por_direccion(self, parte_direccion: str) -> List[Hogar]:
        """
        Busca hogares cuya dirección contenga la cadena proporcionada.
        """
        entidades = list(self._storage.values())
        return [
            hogar for hogar in entidades
            if parte_direccion.lower() in hogar.direccion.lower()
        ]
