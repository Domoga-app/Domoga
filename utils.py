def verificar_contra(contra_usuario, contra_ingresada):
    resultado = contra_usuario == contra_ingresada
    print("Contraseña correcta" if resultado else "Contraseña incorrecta")
    return resultado

def verificar_usuario(usuario,usuario_ingresado):
    resultado = usuario == usuario_ingresado
    print("Usuario correcto") if resultado else print("Usuario incorrecto")
    return resultado