# services/interfaces/__init__.py
# from .i_automatizacion_service import IAutomatizacionService
from .i_dispositivo_service import IDispositivoService
from .i_tipo_dispositivo_service import ITipoDispositivoService
from .i_usuario_service import IUsuarioService


__all__ = [
    # 'IAutomatizacionService',
    'IDispositivoService',
    'ITipoDispositivoService',
    'IUsuarioService'
]