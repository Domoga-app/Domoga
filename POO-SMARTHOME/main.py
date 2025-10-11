#!/usr/bin/env python3
"""
Ejemplo de uso del sistema de domótica Smart Home.
Este archivo demuestra cómo usar las clases desde el paquete models.
"""

# Importar desde el paquete models
from models import (
    Usuario, Rol, Hogar, Ambiente, 
    Dispositivo, TipoDispositivo, Automatizacion
)


def main():
    print("=== Sistema de Domótica Smart Home ===\n")
    
    try:
        # Crear roles
        print("1. Creando roles...")
        rol_admin = Rol(1, "Administrador")
        rol_usuario = Rol(2, "Usuario")
        print(f"   - {rol_admin}")
        print(f"   - {rol_usuario}")
        
        # Crear usuarios
        print("\n2. Creando usuarios...")
        usuario1 = Usuario.crear_usuario("12345678", 1, "Juan", "Pérez", "admin123")
        usuario2 = Usuario("87654321", 2, "Ana", "García", "user456")
        print(f"   - {usuario1}")
        print(f"   - {usuario2}")
        
        # Autenticar usuario
        print("\n3. Autenticando usuarios...")
        if usuario1.ingresar_usuario("12345678", "admin123"):
            print("   ✅ Autenticación exitosa para Juan Pérez")
        else:
            print("   ❌ Fallo en autenticación")
        
        # Crear hogar
        print("\n4. Creando hogar...")
        hogar = Hogar.agregar_hogar("Av. Libertador 1234", "Casa Principal", 1)
        print(f"   - {hogar}")
        
        # Crear ambientes
        print("\n5. Creando ambientes...")
        sala = Ambiente.crear_ambiente(1, 1, "Sala de estar")
        cocina = Ambiente.crear_ambiente(2, 1, "Cocina")
        print(f"   - {sala}")
        print(f"   - {cocina}")
        
        # Crear tipos de dispositivos
        print("\n6. Creando tipos de dispositivos...")
        tipo_luz = TipoDispositivo(1, "Lámpara inteligente")
        tipo_sensor = TipoDispositivo(2, "Sensor de temperatura")
        print(f"   - {tipo_luz}")
        print(f"   - {tipo_sensor}")
        
        # Crear dispositivos
        print("\n7. Creando dispositivos...")
        lampara_sala = Dispositivo.crear_dispositivos(1, 1, "Philips", "Hue White", "encendido")
        sensor_cocina = Dispositivo(2, 2, "Xiaomi", "Mi Temperature", "activo")
        print(f"   - {lampara_sala}")
        print(f"   - {sensor_cocina}")
        
        # Ejecutar acciones en dispositivos
        print("\n8. Ejecutando acciones en dispositivos...")
        print(f"   - Estado inicial de la lámpara: {lampara_sala.estado}")
        lampara_sala.ejecutar_accion("apagar")
        print(f"   - Estado después de apagar: {lampara_sala.estado}")
        
        # Crear automatizaciones
        print("\n9. Creando automatizaciones...")
        auto_nocturna = Automatizacion.crear_automatizacion(
            1, 1, "Luces nocturnas", ["lunes", "martes", "miércoles", "jueves", "viernes"], 
            "22:00", "apagar_todas_luces"
        )
        auto_despertador = Automatizacion(
            2, 1, "Despertador matutino", ["lunes", "martes", "miércoles", "jueves", "viernes"],
            "07:00", "encender_luces_dormitorio"
        )
        print(f"   - {auto_nocturna}")
        print(f"   - {auto_despertador}")
        
        # Mostrar información de automatizaciones
        print("\n10. Información de automatizaciones...")
        info_auto = auto_nocturna.mostrar_automatizaciones()
        print(f"    - Nombre: {info_auto['nombre']}")
        print(f"    - Días: {', '.join(info_auto['dias'])}")
        print(f"    - Hora: {info_auto['hora']}")
        print(f"    - Acción: {info_auto['accion']}")
        
        print("\n✅ === Sistema inicializado correctamente ===")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())