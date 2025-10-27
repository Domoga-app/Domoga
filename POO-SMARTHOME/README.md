# 🏡 Domoga - Smart Home (POO-SMARTHOME)

Este proyecto corresponde a la **versión final y refactorizada** de *Domoga - Smart Home*, desarrollada aplicando los principios de la **Programación Orientada a Objetos (POO)**, el patrón de diseño **DAO (Data Access Object)** y buenas prácticas de arquitectura en capas.

Permite la gestión de **usuarios** y **dispositivos** en un sistema de hogar inteligente (domótica), con distintos niveles de permisos según el rol del usuario (Administrador o Estándar).

---

## ✨ Características Principales

- Gestión de **usuarios** con roles y autenticación básica.
- Administración de **dispositivos** del hogar (crear, actualizar, eliminar, listar).
- Menú de consola **interactivo** con opciones dinámicas según el rol del usuario.
- Acceso a **base de datos MySQL** mediante capa DAO.
- Aplicación de **validaciones** en los modelos a través de *setters*.
- Arquitectura escalable con separación en **DAO**, **Services**, **Models** y **Views**.
- **Pruebas unitarias** implementadas con `pytest` (enfoque TDD en modelos).
- Configuración mediante archivo `.env` (variables de entorno seguras).

---

## 🧱 Arquitectura del Proyecto

```tree
POO-SMARTHOME/
├── dao/                # Clases de acceso a datos (DAO)
│ └── interfaces/       # Interfaces que definen los contratos DAO
├── models/             # Clases POO del dominio (Usuario, Dispositivo, etc.)
├── services/           # Capa de negocio: lógica entre DAO y vistas
├── views/              # Menús e interacción por consola
├── tests/              # Pruebas unitarias (pytest) centradas en los modelos
├── utils/              # Funciones auxiliares del programa
├── .env.example        # Ejemplo de configuración de variables de entorno
├── requirements.txt    # Dependencias necesarias del proyecto
├── pytest.ini          # Configuración de pytest (marcadores, opciones, warnings)
└── main.py             # Punto de entrada principal de la aplicación
```


---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.12 o superior (probado con Python 3.13)
- **Base de Datos:** MySQL
- **Principales librerías:**
  - `mysql-connector-python` → conexión con MySQL
  - `python-dotenv` → gestión de variables de entorno
  - `pytest` → pruebas unitarias

---

## 🚀 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

1.  **🖥️ Clonar el Repositorio**
    ```bash
    git clone https://github.com/Domoga-app/Domoga.git
    cd Domoga/POO-SMARTHOME
    ```

2.  **⚡ Crear un Entorno Virtual**
    ```bash
    python -m venv venv
    ```
    Actívalo:
    * En Windows: `.\venv\Scripts\activate`
    * En macOS/Linux: `source venv/bin/activate`

3.  **📦 Instalar Dependencias**
    Asegúrate de estar dentro de la carpeta `POO-SMARTHOME` y ejecuta:

    * Puedes instalarlas usando el siguiente comando _(RECOMENDADO)_:
        ```bash
        pip install -r .\requirements.txt
        ```

    * O puedes instalarlas usando el comando:
        ```bash
        pip install pytest mysql-connector-python python-dotenv
        ```

4.  **💾 Configurar la Base de Datos**
    * Asegúrate de tener un servidor MySQL en funcionamiento.
    * Ejecuta el script SQL (`CONSULTAS-DDL.sql`) ubicado en `BD-Evidencia-6` para crear la base de datos `domoga` y sus tablas.

5.  **🔑 Configurar las Variables de Entorno**
    * Dentro de la carpeta `POO-SMARTHOME`, renombra el archivo `.env.example` a `.env`.
    * Abre el archivo que acabas de renombrar (`.env`) y edita los valores para que coincidan con tus credenciales de MySQL:
    ```ini
    DB_HOST=ip_del_servidor
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_NAME=domoga
    DB_PORT=puerto_del_servidor
    ```

6.  **▶️ Ejecutar la Aplicación**
    Desde la carpeta `POO-SMARTHOME`, ejecuta el siguiente comando:
    ```bash
    python main.py
    ```
    Se abrirá el menú principal en consola, con las siguientes opciones:

    * Inicio de sesión
        > El usuario administrador creado por defecto cuenta con nombre de usuario: `admin` y Contraseña: `P@ssw0rd`
    * Registro de usuario
        > Todos los nuevos usuarios registrados seran creados con rol de usuario estándar
    * Cerrar el programa

## 🧪 Pruebas Unitarias

El proyecto incluye pruebas unitarias centradas exclusivamente en los **modelos POO** y las **validaciones implementadas en sus setters**, ubicadas en la carpeta `tests` dentro de `POO-SMARTHOME`.  

Para ejecutar todas las pruebas, asegurate de estar dentro de la carpeta `POO-SMARTHOME` y ejecutar:

```bash
pytest
```

Opcionalmente, podés ejecutar un archivo de pruebas específico:

```bash
pytest tests/test_usuario.py
```

> 💡 *Estas pruebas no cubren la lógica de negocio (services) ni el acceso a datos (DAO).*
> *Gracias a la configuración de pytest.ini, se aplican automáticamente opciones de verbosidad, filtros de warnings y marcadores personalizados.*


## 🧩 Estructura de Capas

| Capa	| Directorio | Descripción
|----------|-------------|------|
| Models | /models | Contiene las clases principales (Usuario, Dispositivo, etc.) con validaciones.
| DAO	| /dao | Gestiona la conexión con MySQL y operaciones CRUD.
| Services | /services | Intermediario entre la lógica de negocio y los DAO.
| Views	| /views | Controla la interacción por consola (menús, opciones, entradas del usuario).
| Tests	| /tests | Contiene las pruebas unitarias con pytest.


## 🔐 Usuarios y Roles

* **Administrador**: puede gestionar usuarios y dispositivos.
* **Estándar**: puede consultar información personal y ver los dispositivos disponibles.

El sistema incluye un usuario administrador por defecto definido en la base de datos inicial. Cuya cuenta de usuario es `admin` y contraseña es `P@ssw0rd`

## 🧠 Buenas Prácticas Implementadas

* Separación de responsabilidades por capa.
* Manejo de excepciones y cierre seguro de cursores.
* Validaciones mediante setters en los modelos.
* Uso de with y context managers para operaciones con base de datos.
* Inyección de dependencias en services.
* Configuración externa mediante `.env`.

## 🧱 Convención de nombres

> ⚠️ Nota: En nuestro equipo **no usamos atributos públicos ni protegidos** por el momento, 
> ya que no tenemos clases hijas aparte de las DAO (por ejemplo, `AutomatizacionDAO`, `UsuarioDAO`), 
> que heredan de **clases abstractas usadas como interfaces**. 
> Los atributos **encapsulados con doble guion bajo (`__`) se usan únicamente en los modelos**, y actualmente se definen en el constructor; se accede a ellos mediante decoradores `@property` y `@nombre_atributo.setter`.
> Las funciones internas de un módulo que **no deben ser usadas fuera de ese módulo** se nombran con `_snake_case`.



| Tipo de elemento           | Escritura utilizada      | Descripción |
|----------------------------|------------------------|-------------|
| Clases                     | PascalCase             | Cada palabra inicia con mayúscula. Se usa para representar entidades, modelos y clases DAO/Service. |
| Métodos y funciones        | snake_case             | Todas las letras en minúsculas, separadas por guion bajo. Usadas para acciones o comportamientos dentro de clases. |
| Funciones internas de módulo | _snake_case          | No deben ser usadas desde otros módulos; marcan que son privadas al módulo. |
| Atributos privados         | __doble_guion_bajo      | Encapsulación fuerte. Previene acceso directo desde fuera de la clase; se accede mediante propiedades. |
| Atributos protegidos       | _guion_bajo            | Actualmente no se usan. Indican acceso recomendado solo desde subclases. |
| Atributos públicos         | snake_case             | Actualmente no se usan. Accesibles desde cualquier lugar; se recomienda usarlos solo si es necesario. |
| Propiedades (getters/setters) | @property y @nombre_variable.setter | Usadas para controlar acceso y validación sin romper la interfaz pública. |
| Variables locales          | snake_case            | Nombres descriptivos y en minúsculas; usadas dentro de funciones o métodos. |
| Constantes                 | UPPER_CASE_SNAKE       | Todo en mayúsculas y separado por guion bajo. Usadas para valores inmutables. |
| Interfaces | IPrefijoNombre         | Uso del prefijo `I` seguido del nombre en PascalCase. Indica una interfaz abstracta. |
