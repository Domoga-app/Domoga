from datos import automatizaciones, dispositivos

def mostrar_automatizaciones():
    print("\nAutomatizaciones:")
    if not automatizaciones:
        print("Aún no hay automatizaciones creadas.")
    else:
        for a in automatizaciones:
            print(f"- {a['nombre']}: {a['dispositivo']} ({a['dias']}, {a['hora_on']} - {a['hora_off']})")
    if input("\n¿Desea crear una nueva automatización? (s/n): ") == "s":
        if not dispositivos:
            print("Debe crear un dispositivo primero.")
            return
        nombre = input("Nombre de la automatización: ")
        for i, d in enumerate(dispositivos, 1):
            print(f"{i}. {d['nombre']}")
        d_idx = int(input("Seleccione un dispositivo: ")) - 1
        dias = input("Días de la semana (ej: Lunes,Miércoles): ")
        hora_on = input("Hora de encendido (formato hh:mma/pm): ")
        hora_off = input("Hora de apagado (formato hh:mma/pm): ")
        automatizaciones.append({"nombre": nombre, "dispositivo": dispositivos[d_idx]['nombre'],
                                 "dias": dias, "hora_on": hora_on, "hora_off": hora_off})
        print("Automatización creada.")