# utils/cierre_controlado.py
import sys

def ejecutar_con_cierre_controlado(func, *args, **kwargs):
    '''
    Ejecuta la función `func` capturando KeyboardInterrupt y EOFError.
    Cuando se detecta Ctrl+C o Ctrl+Z/Ctrl+D, termina el programa sin traceback.
    '''
    
    try:
        func(*args, **kwargs)
    except (KeyboardInterrupt, EOFError):
        print("\nOperación interrumpida por el usuario. Saliendo del programa...")
        sys.exit(0)
