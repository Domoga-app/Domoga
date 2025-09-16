import pytest
class TestTipoDispositivo:
    def test_crear_tipo_dispositivo(self):
        tipo = TipoDispositivo(1, "Luz")
        assert tipo.id_tipo == 1
        assert tipo.nombre == "Luz"
