"""
Paquete models para el sistema de domótica Smart Home.
Contiene todas las clases del modelo de datos.
"""

# Importar todas las clases para que estén disponibles desde models
from .rol import Rol
from .usuarios import Usuario
from .ambiente import Ambiente
from .hogar import Hogar
from .tipos_dispositivos import TipoDispositivo
from .dispositivos import Dispositivo
from .automatizacion import Automatizacion

# Definir qué se exporta cuando se hace "from models import *"
__all__ = [
    'Usuario', 'Rol', 'Permiso',
    'Hogar', 'Ambiente',
    'Usuario', 'Rol',
    'Hogar', 'Ambiente',
    'Dispositivo', 'TipoDispositivo',
    'Automatizacion'
]

# Información del paquete
__version__ = "1.0.0"
__author__ = "Domoga"
