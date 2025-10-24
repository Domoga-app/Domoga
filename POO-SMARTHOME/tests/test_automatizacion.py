# tests/test_automatizacion.py
import pytest
from datetime import time
from models import Automatizacion, Dispositivo, TipoDispositivo

def test_automatizacion_valida():
    tipo = TipoDispositivo(id_tipo=1, nombre="Lámpara Inteligente")
    dispositivo = Dispositivo(id_dispositivo=1, tipo_dispositivo=tipo, ubicacion="Living", marca="Philips", modelo="Hue", estado="Encendido")

    auto = Automatizacion()
    
    # Nombre
    auto.nombre = "Encender luces"
    assert auto.nombre == "Encender luces"
    
    # Días como string
    auto.dias = "LMX"
    assert auto._dias_str() == "LMX"
    assert auto.dias == "Lunes, Martes, Miércoles"
    
    # Días como lista
    auto.dias = ["J","V"]
    assert auto._dias_str() == "JV"
    assert auto.dias == "Jueves, Viernes"
    
    # Hora
    auto.hora = "14:30"
    assert isinstance(auto.hora, time)
    assert auto._hora_str() == "14:30"
    
    auto.hora = time(9, 15)
    assert auto.hora == time(9, 15)
    assert auto._hora_str() == "09:15"
    
    # Acción
    auto.accion = "Encender"
    assert auto.accion == "Encender"
    
    # Dispositivos afectados
    auto.agregar_dispositivo(dispositivo)
    assert len(auto.dispositivos_afectados) == 1
    assert auto.dispositivos_afectados[0] == dispositivo

    # Verificar __str__
    expected_str = f"ID: {auto.id_automatizacion}, Nombre: {auto.nombre}, Día(s): {auto.dias}, Hora: {auto.hora}, Acción: {auto.accion}, Afecta a 1 dispositivo(s)"
    assert str(auto) == expected_str

def test_automatizacion_nombre_invalido():
    auto = Automatizacion()
    with pytest.raises(ValueError):
        auto.nombre = ""
    with pytest.raises(ValueError):
        auto.nombre = "ab"

def test_automatizacion_dias_invalidos():
    auto = Automatizacion()
    with pytest.raises(ValueError):
        auto.dias = 123  # No es str ni lista

def test_automatizacion_hora_invalida():
    auto = Automatizacion()
    with pytest.raises(ValueError):
        auto.hora = "25:00"
    with pytest.raises(ValueError):
        auto.hora = 12345  # No es str ni time

def test_automatizacion_accion_invalida():
    auto = Automatizacion()
    with pytest.raises(ValueError):
        auto.accion = ""
    with pytest.raises(ValueError):
        auto.accion = "ab"
