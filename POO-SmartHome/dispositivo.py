class Dispositivo:
    def __init__(self, nombre: str, tipo: str, marca: str, modelo: str):
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.estado = "apagado"  # Estado inicial por defecto

    def encender(self):
        self.estado = "encendido"
        print(f"💡 Dispositivo '{self.nombre}' encendido.")

    def apagar(self):
        self.estado = "apagado"
        print(f"🔌 Dispositivo '{self.nombre}' apagado.")

    def __str__(self):
        # Un método útil para imprimir el estado del objeto
        return f"{self.nombre} ({self.tipo}) - Estado: {self.estado}"