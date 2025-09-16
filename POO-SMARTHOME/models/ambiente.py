from .dispositivos import Dispositivo


class Ambiente:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.dispositivos = []  # Lista para guardar objetos de la clase Dispositivo

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        self.dispositivos.append(dispositivo)
        print(
            f"Dispositivo '{dispositivo.nombre}' agregado al ambiente '{self.nombre}'.")

    def __str__(self):
        return f"Ambiente: {self.nombre}"
