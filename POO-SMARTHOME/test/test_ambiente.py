# test_ambiente.py
from ..models.ambiente import Ambiente
from ..models.dispositivos import Dispositivo

luz = Dispositivo(nombre="Lámpara", tipo="LED", marca="MarcaX", modelo="M1")
ambiente = Ambiente("Living")


def test_ambiente_inicializacion():
    """Verifica que un ambiente se crea sin dispositivos."""
    assert ambiente.nombre == "Living"
    assert ambiente.dispositivos == []
    assert len(ambiente.dispositivos) == 0


def test_ambiente_agregar_dispositivo():
    """Verifica que se puede agregar un dispositivo a la lista del ambiente."""
    ambiente.agregar_dispositivo(luz)
    assert len(ambiente.dispositivos) == 1
    assert luz in ambiente.dispositivos
