import pytest
from ..models.ambiente import Ambiente
from ..models.automatizacion import Automatizacion
from ..models.dispositivos import Dispositivo
from ..models.hogar import Hogar
from ..models.permisos import Permiso
from ..models.rol import Rol
from ..models.usuarios import Usuario


class TestRol:
    def test_crear_rol(self):
        rol = Rol(1, "Administrador")
        assert rol.id_rol == 1
        assert rol.nombre == "Administrador"


class TestUsuario:
    def test_crear_usuario(self):
        usuario = Usuario("12345678", 1, "Juan", "Pérez", "password123")
        assert usuario.dni == "12345678"
        assert usuario.id_rol == 1
        assert usuario.nombre == "Juan"
        assert usuario.apellido == "Pérez"
        assert usuario.contraseña == "password123"

    def test_crear_usuario_metodo_clase(self):
        usuario = Usuario.crear_usuario(
            "12345678", 1, "Ana", "García", "pass456")
        assert isinstance(usuario, Usuario)
        assert usuario.dni == "12345678"
        assert usuario.nombre == "Ana"

    def test_recuperar_usuario(self):
        usuario = Usuario("12345678", 1, "Juan", "Pérez", "password123")
        datos_usuario = usuario.recuperar_usuario()
        assert datos_usuario["dni"] == "12345678"
        assert datos_usuario["nombre"] == "Juan"
        assert datos_usuario["apellido"] == "Pérez"

    def test_ingresar_usuario_credenciales_correctas(self):
        usuario = Usuario("12345678", 1, "Juan", "Pérez", "password123")
        assert usuario.ingresar_usuario("12345678", "password123") == True

    def test_ingresar_usuario_credenciales_incorrectas(self):
        usuario = Usuario("12345678", 1, "Juan", "Pérez", "password123")
        assert usuario.ingresar_usuario("12345678", "wrongpass") == False


class TestPermiso:
    def test_crear_permiso(self):
        permiso = Permiso("12345678", 1)
        assert permiso.dni == "12345678"
        assert permiso.id_rol == 1


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


class TestTipoDispositivo:
    def test_crear_tipo_dispositivo(self):
        tipo = TipoDispositivo(1, "Luz")
        assert tipo.id_tipo == 1
        assert tipo.nombre == "Luz"


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
