# services/automatizacion_service.py

# Nota: Aunque este servicio no fue implementado porque no era parte de la consigna,
# presentamos la interfaz completa como guía de lo que podría incluir en el futuro.
# Contempla todos los métodos de CRUD, vinculación de dispositivos, consultas avanzadas
# y lógica de negocio relacionada con las automatizaciones.

# from models import Automatizacion, Dispositivo

# class IAutomatizacionService:
    
#     def crear_automatizacion(self, automatizacion: Automatizacion) -> int | None:
#         pass

#     def obtener_por_id(self, id_automatizacion: int) -> Automatizacion | None:
#         pass

#     def obtener_todas(self) -> list[Automatizacion]:
#         pass

#     def actualizar_automatizacion(self, id_automatizacion: int, automatizacion: Automatizacion) -> bool:
#         pass

#     def eliminar_automatizacion(self, id_automatizacion: int) -> bool:
#         pass

#     # Vinculación de dispositivos
#     def vincular_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
#         pass

#     def desvincular_dispositivo(self, id_automatizacion: int, id_dispositivo: int) -> bool:
#         pass

#     # Consultas avanzadas
#     def obtener_dispositivos_asociados(self, id_automatizacion: int) -> list[Dispositivo]:
#         pass

#     def obtener_automatizaciones_por_dispositivo(self, id_dispositivo: int) -> list[Automatizacion]:
#         pass

#     def filtrar_por_dia(self, dia: str) -> list[Automatizacion]:
#         pass

#     def filtrar_por_hora(self, hora: str) -> list[Automatizacion]:
#         pass

#     # Ejecución de automatización
#     def ejecutar_automatizacion(self, id_automatizacion: int) -> bool:
#         pass

#     # Métodos adicionales posibles
#     def validar_automatizacion(self, automatizacion: Automatizacion) -> bool:
#         pass
