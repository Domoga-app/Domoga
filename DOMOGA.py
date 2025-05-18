# Sistema Domóga: estructura de menús y acciones
usuarios = {}
usuario_actual = None
hogares = {"hogar": {}, "casa campo": {}}

# Estructura de datos
ambientes = {}
dispositivos = []
automatizaciones = []

def menu_principal():
    while True:
        print("\n\u00a1Bienvenido a Domóga!")
        print("1. Ingresar usuario")
        print("2. ¿Aún no tienes cuenta? Crear nuevo usuario")
        print("3. Recuperar usuario y/o contraseña")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            recuperar_usuario()
        else:
            print("Opción no válida.")

def crear_usuario():
    nombre = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    usuarios[nombre] = contrasena
    print("Usuario creado con éxito.")

def recuperar_usuario():
    print("Funcionalidad de recuperación de usuario a implementar.")

def ingresar_usuario():
    global usuario_actual
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuarios.get(nombre) == contrasena:
        usuario_actual = nombre
        print(f"Hola {nombre}! Bienvenido a casa")
        menu_principal_usuario()
    else:
        print("Usuario o contraseña incorrectos.")

def menu_principal_usuario():
    while True:
        print("\n1. Seleccionar hogar")
        print("2. Administrar automatizaciones del hogar")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_hogar()
        elif opcion == "2":
            mostrar_automatizaciones()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

def menu_hogar():
    print("\n1. hogar")
    print("2. casa campo")
    opcion = input("Seleccione un hogar: ")
    if opcion in ["1", "2"]:
        nombre_hogar = "hogar" if opcion == "1" else "casa campo"
        menu_hogar_opciones(nombre_hogar)
    else:
        print("Opción no válida.")

def menu_hogar_opciones(nombre_hogar):
    while True:
        print(f"\nMenú de {nombre_hogar}:")
        print("1. Ambientes")
        print("2. Dispositivos")
        print("3. Automatizaciones del hogar")
        print("4. Configuración")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_ambientes(nombre_hogar)
        elif opcion == "2":
            gestionar_dispositivos(nombre_hogar)
        elif opcion == "3":
            mostrar_automatizaciones()
        elif opcion == "4":
            menu_configuracion(nombre_hogar)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def gestionar_ambientes(hogar):
    print("\nAmbientes:")
    if hogar not in ambientes or not ambientes[hogar]:
        print("No hay ambientes creados.")
    else:
        for amb in ambientes[hogar]:
            print(f"- {amb}")
            for d in dispositivos:
                if d['hogar'] == hogar and d['ambiente'] == amb:
                    print(f"  * {d['nombre']} ({d['estado']})")
    if input("\n¿Desea crear un nuevo ambiente? (s/n): ") == "s":
        nuevo = input("Nombre del nuevo ambiente: ")
        ambientes.setdefault(hogar, []).append(nuevo)
        print(f"Ambiente '{nuevo}' agregado.")

def gestionar_dispositivos(hogar):
    print("\nDispositivos:")
    encontrados = [d for d in dispositivos if d['hogar'] == hogar]
    if not encontrados:
        print("No hay dispositivos creados.")
    else:
        for d in encontrados:
            print(f"- {d['nombre']} ({d['estado']}) - Ambiente: {d['ambiente']}")
    if input("\n¿Desea crear un nuevo dispositivo? (s/n): ") == "s":
        if not ambientes.get(hogar):
            print("Debe crear un ambiente primero.")
            return
        nombre = input("Nombre del dispositivo: ")
        for i, amb in enumerate(ambientes[hogar], 1):
            print(f"{i}. {amb}")
        amb_idx = int(input("Seleccione el ambiente: ")) - 1
        ambiente = ambientes[hogar][amb_idx]
        dispositivos.append({"nombre": nombre, "estado": "apagado", "hogar": hogar, "ambiente": ambiente})
        print("Dispositivo creado con éxito.")

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
        hora_on = input("Hora de encendido (formato hh:am/pm): ")
        hora_off = input("Hora de apagado (formato hh:am/pm): ")
        automatizaciones.append({"nombre": nombre, "dispositivo": dispositivos[d_idx]['nombre'],
                                 "dias": dias, "hora_on": hora_on, "hora_off": hora_off})
        print("Automatización creada.")

def menu_configuracion(hogar):
    while True:
        print("\nConfiguración:")
        print("1. Eliminar dispositivos")
        print("2. Eliminar ambiente")
        print("3. Eliminar hogar")
        print("4. Eliminar automatización")
        print("5. Cerrar sesión")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            eliminar_dispositivo(hogar)
        elif opcion == "2":
            eliminar_ambiente(hogar)
        elif opcion == "3":
            ambientes.pop(hogar, None)
            dispositivos[:] = [d for d in dispositivos if d['hogar'] != hogar]
            print(f"Hogar '{hogar}' eliminado.")
            break
        elif opcion == "4":
            eliminar_automatizacion()
        elif opcion == "5":
            break
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

def eliminar_dispositivo(hogar):
    dispositivos_hogar = [d for d in dispositivos if d['hogar'] == hogar]
    for i, d in enumerate(dispositivos_hogar, 1):
        print(f"{i}. {d['nombre']}")
    idx = int(input("Seleccione el número del dispositivo a eliminar: ")) - 1
    if 0 <= idx < len(dispositivos_hogar):
        dispositivos.remove(dispositivos_hogar[idx])
        print("Dispositivo eliminado.")

def eliminar_ambiente(hogar):
    if hogar in ambientes:
        for i, amb in enumerate(ambientes[hogar], 1):
            print(f"{i}. {amb}")
        idx = int(input("Seleccione el ambiente a eliminar: ")) - 1
        if 0 <= idx < len(ambientes[hogar]):
            amb = ambientes[hogar].pop(idx)
            dispositivos[:] = [d for d in dispositivos if d['ambiente'] != amb or d['hogar'] != hogar]
            print(f"Ambiente '{amb}' eliminado.")

def eliminar_automatizacion():
    for i, a in enumerate(automatizaciones, 1):
        print(f"{i}. {a['nombre']}")
    idx = int(input("Seleccione la automatización a eliminar: ")) - 1
    if 0 <= idx < len(automatizaciones):
        auto = automatizaciones.pop(idx)
        print(f"Automatización '{auto['nombre']}' eliminada.")

# Iniciar el programa
menu_principal()
