
from ..models.ambiente import Ambiente


class TestAmbiente:
    def test_crear_ambiente(self):
        ambiente = Ambiente(1, 1, "Sala de estar")
        assert ambiente.id_ambiente == 1
        assert ambiente.id_hogar == 1
        assert ambiente.nombre == "Sala de estar"

    def test_crear_ambiente_metodo_clase(self):
        ambiente = Ambiente.crear_ambiente(2, 1, "Cocina")
        assert isinstance(ambiente, Ambiente)
        assert ambiente.id_ambiente == 2
        assert ambiente.nombre == "Cocina"

    def test_gestionar_ambientes(self):
        ambiente = Ambiente(1, 1, "Sala de estar")
        resultado = ambiente.gestionar_ambientes(
            "actualizar", {"nombre": "Living"})
        assert resultado == True

    def test_ver_ambientes(self):
        ambiente = Ambiente(1, 1, "Sala de estar")
        datos_ambiente = ambiente.ver_ambientes()
        assert datos_ambiente["id_ambiente"] == 1
        assert datos_ambiente["nombre"] == "Sala de estar"

    def test_eliminar_ambientes(self):
        ambiente = Ambiente(1, 1, "Sala de estar")
        resultado = ambiente.eliminar_ambientes()
        assert resultado == True
