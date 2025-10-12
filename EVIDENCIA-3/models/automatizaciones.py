
import time
from datetime import datetime
from data.datos import automatizaciones, ambientes



def ejecutar_accion(nombre_dispositivo, accion):
    hora_accion = datetime.now().strftime("%H:%M")
    if accion == "encender":
        print(f"🟢 [AUTO] {nombre_dispositivo} se encendió a las {hora_accion}")
    else:
        print(f"🔴 [AUTO] {nombre_dispositivo} se apagó a las {hora_accion}")
        

def parse_hora(hora_str):
    try:
        hora, minuto = map(int, hora_str.strip().split(":"))
        return (hora, minuto)
    except ValueError:
        return None

def dia_actual():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[datetime.today().weekday()]

def monitor_automatizaciones():
    while True:
        ahora = datetime.now()
        hoy = dia_actual()
        for auto in automatizaciones:
            dias_activos = [d.strip() for d in auto["dias"].split(",")]
            if hoy in dias_activos and not auto.get("ejecutado", False):
                hora = parse_hora(auto["hora"])
                if hora and (ahora.hour, ahora.minute) == hora:
                    ejecutar_accion(auto["dispositivo"], auto["accion"])
                    auto["ejecutado"] = True
            if hoy not in dias_activos:
                auto["ejecutado"] = False  # Reset al día siguiente
        time.sleep(30)

def mostrar_automatizaciones():
    print("\n📋 Automatizaciones:")
    if not automatizaciones:
        print("Aún no hay automatizaciones creadas.")
    else:
        for i, a in enumerate(automatizaciones, 1):
            status = "✔️ Ejecutada" if a.get("ejecutado") else "⏳ Pendiente"
            print(f"{i}. {a['nombre']} -> {a['accion']} {a['dispositivo']} ({a['dias']} a las {a['hora']}) - {status}")

def crear_automatizacion():
    if input("\n¿Desea crear una nueva automatización? (s/n): ").lower() == "s":
        dispositivos_disponibles = []
        for amb in ambientes:
            for d in amb["dispositivos"]:
                dispositivos_disponibles.append({"ambiente": amb["ambiente"], "nombre": d["nombre"]})

        if not dispositivos_disponibles:
            print("Debe crear un dispositivo primero.")
            return


        nombre = input("Nombre de la automatización: ")
        
        print("Dispositivos disponibles:")
        for i, d in enumerate(dispositivos_disponibles, 1):
            print(f"{i}. {d['nombre']} (Ambiente: {d['ambiente']})")

        try:
            d_idx = int(input("Seleccione un dispositivo: ")) - 1
            dispositivo = dispositivos_disponibles[d_idx]['nombre']
        except (ValueError, IndexError):
            print("Selección inválida.")
            return

        
        
        letras_a_dias = {
            "l": "Lunes", "m": "Martes", "x": "Miércoles",
            "j": "Jueves", "v": "Viernes", "s": "Sábado", "d": "Domingo"
        }
        entrada_dias = input("L = Lunes, M = Martes, X = Miércoles, J = Jueves, V = Viernes, S = Sábado, D = Domingo\nDías de la semana (ej: lmx | l, m , x | l m x): ").lower()

        dia_seleccionado = entrada_dias.replace(",", " ").split()

        dias = []
        for letra in dia_seleccionado:
            for l in letra:
                if l in letras_a_dias:
                    dia = letras_a_dias[l]
                    if dia not in dias:
                        dias.append(dia)
                else:
                    print(f"⚠️ Letra inválida: '{l}' fue ignorada por no corresponder con un día válido.")

        if not dias:
            print("❌ No se seleccionaron días válidos.")
            return
        
        orden_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        def obtener_indice(dia):
            return orden_dias.index(dia)
        dias = sorted(dias, key=obtener_indice)
        if len(dias) > 1:
            dias = ", ".join(dias[:-1]) + " y " + dias[-1]
        else:
            dias = dias[0]


        hora = input("Hora de ejecución (formato HH:MM en 24hs): ")
        
        acciones_validas = ["encender", "apagar"]
        print("Seleccione una acción:")
        for i, a in enumerate(acciones_validas, 1):
            print(f"{i}. {a.capitalize()}")

        try:
            opcion = int(input("Ingrese el número de la acción: ")) - 1
            accion = acciones_validas[opcion]
        except (ValueError, IndexError):
            print("Acción inválida.")
            return
        
        automatizaciones.append({
            "nombre": nombre,
            "dispositivo": dispositivo,
            "dias": dias,
            "hora": hora,
            "accion": accion,
            "ejecutado": False
        })
        print("✅ Automatización creada.")

def eliminar_automatizacion():
    if not automatizaciones:
        print("No hay automatizaciones para eliminar.")
        return

    print("\n📋 Automatizaciones disponibles:")
    for i, a in enumerate(automatizaciones, 1):
        print(f"{i}. {a['nombre']} -> {a['accion']} {a['dispositivo']} ({a['dias']} a las {a['hora']})")

    try:
        opcion = int(input("Ingrese el número de la automatización a eliminar: ")) - 1
        if 0 <= opcion < len(automatizaciones):
            confirmacion = input(f"¿Está seguro que desea eliminar '{automatizaciones[opcion]['nombre']}'? (s/n): ").lower()
            if confirmacion == "s":
                eliminada = automatizaciones.pop(opcion)
                print(f"✅ Automatización '{eliminada['nombre']}' eliminada.")
            else:
                print("❌ Eliminación cancelada.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada inválida.")

        