# tests/test_usuario.py
import pytest
from models import Usuario

def test_usuario_validaciones():
    '''
    Crea un Usuario vacio, al que luego se le asignan los valores para forzar el paso por setters
    Los setters tienen las validaciones
    '''
    usuario = Usuario()
    
    # DNI válido
    usuario.dni = "12345678"
    assert usuario.dni == "12345678"
    
    # Nombre de usuario válido
    usuario.nombre_usuario = "gera"
    assert usuario.nombre_usuario == "gera"
    
    # Nombre válido
    usuario.nombre = "Gerardo"
    assert usuario.nombre == "Gerardo"
    
    # Apellido válido
    usuario.apellido = "Catalas"
    assert usuario.apellido == "Catalas"
    
    # Contraseña válida
    # Tiene una mayúscula, una minúscula, un número y un símbolo
    contrasena_valida = "Abcdef1!"
    usuario.contrasena = contrasena_valida
    
    # Contraseña real es la que se envia a la base de datos
    assert usuario._contrasena_real() == contrasena_valida
    
    # El getter público siempre devuelve 8 asteriscos
    assert usuario.contrasena == "********"
    
    # Cambiar rol
    usuario.es_admin = True
    assert usuario.es_admin is True
    usuario.es_admin = False
    assert usuario.es_admin is False
    
    # Crea un usuario con todos los valores en constructor
    # Cómo para simular los que se traen de la base de datos y se crearian desde el DAO
    usuario2 = Usuario(
        id_usuario=11,
        nombre_usuario="gera",
        nombre="Gerardo",
        apellido="Catalas",
        dni="12345678",
        es_admin=False,
        contrasena="P@sw0rd!"
    )
    assert usuario2.nombre_usuario == "gera"
    assert usuario2.nombre == "Gerardo"
    assert usuario2.apellido == "Catalas"
    assert usuario2.dni == "12345678"
    assert usuario2.es_admin == False
    assert usuario2._contrasena_real() == "P@sw0rd!"
    
    # Prueba el str
    str_esperado = "Usuario: gera, Nombre: Gerardo, Apellido: Catalas, DNI: 12345678, Rol: Estandar"
    assert str(usuario2) == str_esperado
    

def test_usuario_nombre_usuario_invalido():
    usuario = Usuario()
    with pytest.raises(ValueError):
        usuario.nombre_usuario = "A"  # Muy corto
    with pytest.raises(ValueError):
        usuario.nombre_usuario = ""   # Vacío
    with pytest.raises(ValueError):
        usuario.nombre_usuario = "nombredeusuarioconmasde30caracteres"   # Muy largo

def test_usuario_dni_invalido():
    usuario = Usuario()
    with pytest.raises(ValueError):
        usuario.dni = "123"  # Menos de 7 dígitos
    with pytest.raises(ValueError):
        usuario.dni = "123456789"  # Más de 8 dígitos
    with pytest.raises(ValueError):
        usuario.dni = "abcdefg"  # Letras no permitidas

def test_usuario_nombre_invalido():
    usuario = Usuario()
    with pytest.raises(ValueError):
        usuario.nombre = "A"  # Muy corto
    with pytest.raises(ValueError):
        usuario.nombre = ""   # Vacío
    with pytest.raises(ValueError):
        usuario.nombre = "nombreconmasde30caracteressssss"   # Muy largo

def test_usuario_apellido_invalido():
    usuario = Usuario()
    with pytest.raises(ValueError):
        usuario.apellido = "B"  # Muy corto
    with pytest.raises(ValueError):
        usuario.apellido = ""   # Vacío
    with pytest.raises(ValueError):
        usuario.apellido = "apellidoconmasde30caracteressssss"   # Muy largo

def test_usuario_contrasena_invalida():
    usuario = Usuario()
    # Menos de 8 caracteres
    with pytest.raises(ValueError):
        usuario.contrasena = "Ab1!"
    # Sin mayúscula
    with pytest.raises(ValueError):
        usuario.contrasena = "abcdef1!"
    # Sin minúscula
    with pytest.raises(ValueError):
        usuario.contrasena = "ABCDEFG1!"
    # Sin número
    with pytest.raises(ValueError):
        usuario.contrasena = "Abcdefg!"
    # Sin caracter especial
    with pytest.raises(ValueError):
        usuario.contrasena = "Abcdefg1"
