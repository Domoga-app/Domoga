"""
Configuración compartida para todos los tests.
Este archivo se ejecuta automáticamente por pytest.
"""

import pytest
import sys
import os

# Agregar el directorio raíz del proyecto al path de Python
# Esto permite importar desde models sin problemas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora podemos importar desde models
from models import Usuario, Rol, Hogar, Ambiente, Dispositivo, TipoDispositivo, Automatizacion

@pytest.fixture(scope="session")
def usuario_admin():
    """Fixture de sesión que crea un usuario administrador para todos los tests."""
    return Usuario("12345678", 1, "Admin", "Sistema", "admin123")


@pytest.fixture(scope="session")
def hogar_principal():
    """Fixture de sesión que crea un hogar principal para todos los tests."""
    return Hogar("Av. Principal 123", "Casa de Pruebas", 999)


@pytest.fixture
def ambiente_temporal():
    """Fixture que crea un ambiente temporal para cada test."""
    return Ambiente(999, 999, "Ambiente Temporal")


@pytest.fixture
def dispositivo_temporal():
    """Fixture que crea un dispositivo temporal para cada test."""
    return Dispositivo(1, 999, "TestBrand", "TestModel", "encendido")


@pytest.fixture(scope="class")
def base_datos_mock():
    """Fixture de clase que simula una base de datos para tests."""
    return {
        "usuarios": [],
        "hogares": [],
        "dispositivos": [],
        "automatizaciones": []
    }


@pytest.fixture(autouse=True)
def setup_test_environment():
    """Fixture que se ejecuta automáticamente antes de cada test."""
    yield  # Aquí se ejecuta el test


def pytest_configure(config):
    """Configuración personalizada de pytest."""
    config.addinivalue_line("markers", "slow: marca tests que tardan mucho en ejecutarse")
    config.addinivalue_line("markers", "integration: marca tests de integración")
    config.addinivalue_line("markers", "unit: marca tests unitarios")
    config.addinivalue_line("markers", "smoke: marca tests de smoke testing")


@pytest.fixture(params=[
    ("Juan", "Pérez"),
    ("Ana", "García"),
    ("Carlos", "López")
])
def nombres_usuarios(request):
    """Fixture parametrizada con diferentes nombres de usuario."""
    return request.param