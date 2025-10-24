# tests/test_tipo_dispositivo.py
import pytest
from models import TipoDispositivo

def test_tipo_dispositivo_valido():
    tipo = TipoDispositivo()
    
    # Nombre válido
    tipo.nombre = "Lámpara Inteligente"
    assert tipo.nombre == "Lámpara Inteligente"
    
    # Tipo Dispositivo válido
    tipo_con_id = TipoDispositivo(id_tipo=1, nombre="Termostato")
    assert tipo_con_id.id_tipo == 1
    assert tipo_con_id.nombre == "Termostato"
    
    # Verificar __str__
    assert str(tipo_con_id) == "ID: 1, Nombre: Termostato"

def test_tipo_dispositivo_nombre_invalido():
    tipo = TipoDispositivo()
    
    # Nombre vacío
    with pytest.raises(ValueError):
        tipo.nombre = ""
        
    # Nombre demasiado corto
    with pytest.raises(ValueError):
        tipo.nombre = "AB"
        
    # Nombre con solo espacios
    with pytest.raises(ValueError):
        tipo.nombre = "   "
