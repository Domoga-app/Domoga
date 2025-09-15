# test_dispositivo.py
from dispositivo import Dispositivo

luz= Dispositivo(nombre="Lámpara", tipo="LED", marca="MarcaX", modelo="M1")

def test_dispositivo_inicializacion():
    """Verifica que un dispositivo se crea con los valores correctos y estado 'apagado'."""
    assert luz.nombre == "Lámpara"
    assert luz.tipo == "LED"
    assert luz.marca == "MarcaX"
    assert luz.modelo == "M1"
    assert luz.estado == "apagado"

def test_dispositivo_encender():
    """Prueba que el método encender() cambia el estado a 'encendido'."""
    luz.encender()
    assert luz.estado == "encendido"

def test_dispositivo_apagar():
    """Prueba que el método apagar() cambia el estado a 'apagado'."""
    luz.encender()  # Primero encender
    luz.apagar()
    assert luz.estado == "apagado"
    
def test_dispositivo_str():
    """Prueba la representación en string del objeto."""
    assert str(luz) == "Lámpara (LED) - Estado: apagado"
    luz.encender()
    assert str(luz) == "Lámpara (LED) - Estado: encendido"