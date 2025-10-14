# Clases y Pruebas

Esta carpeta contiene los archivos de clases, junto con pruebas automatizadas usando **pytest**.

## ⚙️ Requisitos

- Python 3.9+ (recomendado)
- [pytest](https://docs.pytest.org/)

Instala pytest con:

```
pip install pytest
```

## ▶️ Ejecutar las pruebas

Posicionando la terminal dentro de esta carpeta, ejecuta:

```
pytest -v
```

Esto ejecutará automáticamente todos los archivos que empiecen con `test_` y mostrará resultados detallados de cada prueba.

## ℹ️ Nota sobre los imports

Es probable que en varios archivos de prueba (`test_*.py`) no se incluya `import pytest` porque actualmente solo estamos utilizando `asserts` básicos de Python.

- `pytest` detecta y ejecuta los tests automáticamente sin necesidad de imports adicionales.
- Si en el futuro se usan características avanzadas de pytest (como `pytest.raises` por ejemplo), entonces sí será necesario agregar ese import, al menos, en esos archivos de prueba:

```python
import pytest
```

⚙️ Dependencias adicionales del proyecto

Para la conexión a la base de datos MySQL y la carga segura de variables de entorno, este proyecto requiere las siguientes dependencias adicionales:

- ``mysql-connector-python`` → permite conectarse a bases de datos MySQL desde Python.
- ``python-dotenv`` → carga las variables del archivo .env (como credenciales de conexión, rutas, etc.).

Instalación recomendada:

```
pip install mysql-connector-python python-dotenv
```