from ..models.permisos import Permiso


class TestPermiso:
    def test_crear_permiso(self):
        permiso = Permiso("12345678", 1)
        assert permiso.dni == "12345678"
        assert permiso.id_rol == 1
