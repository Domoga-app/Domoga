"""
Paquete models para el sistema de domótica Smart Home.
Contiene todas las clases del modelo de datos.
"""

# Importar todas las clases para que estén disponibles desde models
from .rol import Rol
from .usuarios import Usuario
from .tipos_dispositivos import TipoDispositivo
from .dispositivos import Dispositivo
from .automatizacion import Automatizacion

# Definir qué se exporta cuando se hace "from models import *"
__all__ = [
    'Rol',
    'Usuario',
    'TipoDispositivo',
    'Dispositivo',
    'Automatizacion'
    # Solo incluir 'Permiso' si se importa arriba: 'Permiso'
]
