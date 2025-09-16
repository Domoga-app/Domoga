from ..models.usuarios import Usuario


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
