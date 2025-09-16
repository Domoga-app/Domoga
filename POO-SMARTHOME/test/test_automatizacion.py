from ..models.automatizacion import Automatizacion


class TestAutomatizacion:
    def test_crear_automatizacion(self):
        automatizacion = Automatizacion(1, 1, "Luces nocturnas", [
                                        "lunes", "martes"], "22:00", "apagar_luces")
        assert automatizacion.id_automatizacion == 1
        assert automatizacion.id_hogar == 1
        assert automatizacion.nombre == "Luces nocturnas"
        assert automatizacion.dias == ["lunes", "martes"]
        assert automatizacion.hora == "22:00"
        assert automatizacion.accion == "apagar_luces"

    def test_crear_automatizacion_metodo_clase(self):
        automatizacion = Automatizacion.crear_automatizacion(
            2, 1, "Despertador", ["lunes"], "07:00", "encender_luces")
        assert isinstance(automatizacion, Automatizacion)
        assert automatizacion.nombre == "Despertador"

    def test_monitor_automatizaciones(self):
        automatizacion = Automatizacion(1, 1, "Luces nocturnas", [
                                        "lunes"], "22:00", "apagar_luces")
        resultado = automatizacion.monitor_automatizaciones()
        assert resultado == True

    def test_ejecutar_accion(self):
        automatizacion = Automatizacion(1, 1, "Luces nocturnas", [
                                        "lunes"], "22:00", "apagar_luces")
        resultado = automatizacion.ejecutar_accion()
        assert resultado == True

    def test_borrar_automatizaciones(self):
        automatizacion = Automatizacion(1, 1, "Luces nocturnas", [
                                        "lunes"], "22:00", "apagar_luces")
        resultado = automatizacion.borrar_automatizaciones()
        assert resultado == True

    def test_mostrar_automatizaciones(self):
        automatizacion = Automatizacion(1, 1, "Luces nocturnas", [
                                        "lunes"], "22:00", "apagar_luces")
        datos_automatizacion = automatizacion.mostrar_automatizaciones()
        assert datos_automatizacion["nombre"] == "Luces nocturnas"
        assert datos_automatizacion["hora"] == "22:00"
