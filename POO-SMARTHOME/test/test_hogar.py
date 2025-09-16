import pytest
from models import Hogar


class TestHogar:
    def test_crear_hogar(self):
        hogar = Hogar("Calle Falsa 123", "Casa Principal", 1)
        assert hogar.direccion == "Calle Falsa 123"
        assert hogar.nombre == "Casa Principal"
        assert hogar.id_hogar == 1

    def test_agregar_hogar(self):
        hogar = Hogar.agregar_hogar("Av. Libertador 456", "Casa de Verano", 2)
        assert isinstance(hogar, Hogar)
        assert hogar.id_hogar == 2
        assert hogar.nombre == "Casa de Verano"

    def test_eliminar_hogar(self):
        hogar = Hogar("Calle Falsa 123", "Casa Principal", 1)
        resultado = hogar.eliminar_hogar()
        assert resultado == True

    def test_ver_hogares(self):
        hogar = Hogar("Calle Falsa 123", "Casa Principal", 1)
        datos_hogar = hogar.ver_hogares()
        assert datos_hogar["id_hogar"] == 1
        assert datos_hogar["nombre"] == "Casa Principal"
        assert datos_hogar["direccion"] == "Calle Falsa 123"
