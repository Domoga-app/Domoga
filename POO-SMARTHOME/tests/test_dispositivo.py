# tests/test_dispositivo.py
import pytest
from models import Dispositivo, TipoDispositivo

def test_dispositivo_valido():
    tipo = TipoDispositivo(id_tipo=1, nombre="Lámpara Inteligente")
    
    dispositivo = Dispositivo()
    
    # Tipo válido
    dispositivo.tipo = tipo
    assert dispositivo.tipo == tipo
    
    # Ubicación válida
    dispositivo.ubicacion = "Living"
    assert dispositivo.ubicacion == "Living"
    
    # Marca y modelo válidos (Estos atributos son opcionales)
    # Vacio
    dispositivo.marca = ""
    dispositivo.modelo = ""
    assert dispositivo.marca == ""
    assert dispositivo.modelo == ""
    # Con datos
    dispositivo.marca = "Philips"
    dispositivo.modelo = "Hue"
    assert dispositivo.marca == "Philips"
    assert dispositivo.modelo == "Hue"
    
    # Estado
    dispositivo.estado = "Encendido"
    assert dispositivo.estado == "Encendido"
    
    # Crea un dispositivo con todos los valores en constructor
    # Cómo para simular los que se traen de la base de datos y se crearian desde el DAO
    dispositivo2 = Dispositivo(
        id_dispositivo=10,
        tipo_dispositivo=tipo,
        ubicacion="Dormitorio",
        marca="Google",
        modelo="Nest",
        estado="Apagado"
    )
    assert dispositivo2.id_dispositivo == 10
    assert dispositivo2.tipo == tipo
    assert dispositivo2.ubicacion == "Dormitorio"
    assert dispositivo2.marca == "Google"
    assert dispositivo2.modelo == "Nest"
    assert dispositivo2.estado == "Apagado"
    
    # Verificar __str__
    expected_str = "ID: 10, Tipo: Lámpara Inteligente, Ubicación: Dormitorio, Marca: Google, Modelo: Nest, Estado: Apagado"
    assert str(dispositivo2) == expected_str

# Comprueba que el tipo de dispositivo sea un objeto TipoDispositivo()
def test_dispositivo_tipo_invalido():
    dispositivo = Dispositivo()
    with pytest.raises(ValueError):
        dispositivo.tipo = "No es un tipo valido"

def test_dispositivo_ubicacion_invalida():
    dispositivo = Dispositivo(tipo_dispositivo=TipoDispositivo(nombre="Termostato"))
    with pytest.raises(ValueError):
        dispositivo.ubicacion = "" # Sin ubicación
    with pytest.raises(ValueError):
        dispositivo.ubicacion = "ab"  # Menos de 3 caracteres
    with pytest.raises(ValueError):
        dispositivo.ubicacion = "   "  # Solo espacios
    with pytest.raises(ValueError):
        dispositivo.ubicacion = "ubicaciónconmásde30carácteressss" 

def test_dispositivo_estado_invalido():
    dispositivo = Dispositivo(tipo_dispositivo=TipoDispositivo(nombre="Cámara"))
    with pytest.raises(ValueError):
        dispositivo.estado = "" # Sin estado
    with pytest.raises(ValueError):
        dispositivo.estado = "ab"  # Menos de 3 caracteres
    with pytest.raises(ValueError):
        dispositivo.estado = "   "  # Solo espacios
    with pytest.raises(ValueError):
        dispositivo.estado = "estadoconmásde30carácteressssss" 
