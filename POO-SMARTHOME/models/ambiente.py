class Ambiente:
    """Clase para manejar ambientes de un hogar."""

    def __init__(self, id_ambiente, id_hogar, nombre):
        self.id_ambiente = id_ambiente
        self.id_hogar = id_hogar
        self.nombre = nombre

    @classmethod
    def crear_ambiente(cls, id_ambiente, id_hogar, nombre):
        """Método de clase para crear un nuevo ambiente."""
        return cls(id_ambiente, id_hogar, nombre)

    def gestionar_ambientes(self, accion, datos=None):
        """Gestiona operaciones sobre el ambiente."""
        if accion == "actualizar" and datos:
            if "nombre" in datos:
                self.nombre = datos["nombre"]
        return True

    def ver_ambientes(self):
        """Devuelve los datos del ambiente."""
        return {
            "id_ambiente": self.id_ambiente,
            "id_hogar": self.id_hogar,
            "nombre": self.nombre
        }

    def eliminar_ambientes(self):
        """Elimina el ambiente actual."""
        return True
