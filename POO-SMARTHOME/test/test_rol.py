
from ..models.rol import Rol


class TestRol:
    def test_crear_rol(self):
        rol = Rol(1, "Administrador")
        assert rol.id_rol == 1
        assert rol.nombre == "Administrador"
