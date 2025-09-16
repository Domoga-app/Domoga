
from ..models.dispositivos import Dispositivo


class TestDispositivo:
    def test_crear_dispositivo(self):
        dispositivo = Dispositivo(1, 1, "Philips", "Hue", "encendido")
        assert dispositivo.id_tipo == 1
        assert dispositivo.id_ubicacion == 1
        assert dispositivo.marca == "Philips"
        assert dispositivo.modelo == "Hue"
        assert dispositivo.estado == "encendido"

    def test_crear_dispositivos_metodo_clase(self):
        dispositivo = Dispositivo.crear_dispositivos(
            2, 1, "Samsung", "SmartTV", "apagado")
        assert isinstance(dispositivo, Dispositivo)
        assert dispositivo.marca == "Samsung"

    def test_gestionar_dispositivos(self):
        dispositivo = Dispositivo(1, 1, "Philips", "Hue", "encendido")
        resultado = dispositivo.gestionar_dispositivos(
            "cambiar_estado", {"estado": "apagado"})
        assert resultado == True

    def test_ver_dispositivos(self):
        dispositivo = Dispositivo(1, 1, "Philips", "Hue", "encendido")
        datos_dispositivo = dispositivo.ver_dispositivos()
        assert datos_dispositivo["marca"] == "Philips"
        assert datos_dispositivo["estado"] == "encendido"

    def test_ejecutar_accion(self):
        dispositivo = Dispositivo(1, 1, "Philips", "Hue", "encendido")
        resultado = dispositivo.ejecutar_accion("apagar")
        assert resultado == True

    def test_borrar_dispositivos(self):
        dispositivo = Dispositivo(1, 1, "Philips", "Hue", "encendido")
        resultado = dispositivo.borrar_dispositivos()
        assert resultado == True
