# dao/interfaces/__init__.py
from .i_automatizacionDAO import IAutomatizacionDAO
from .i_usuarioDAO import IUsuarioDAO
from .i_dispositivoDAO import IDispositivoDAO
from .i_tipo_dispositivoDAO import ITipoDispositivoDAO


__all__ = [
    'IAutomatizacionDAO',
    'IUsuarioDAO',
    'IDispositivoDAO',
    'ITipoDispositivoDAO'
]