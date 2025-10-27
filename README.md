# Domoga - Smart Home 🏡

Este proyecto es una aplicación de consola para la gestión de un sistema de hogar inteligente (domótica), desarrollada aplicando los principios de la Programación Orientada a Objetos (POO). El sistema permite la gestión de usuarios con diferentes roles (Administrador y Estándar) y el control de dispositivos dentro del hogar.

## 📈 Evolución del Proyecto

Este repositorio documenta la evolución del proyecto **Domoga**, desarrollado a lo largo de distintas etapas denominadas **“Evidencias de Aprendizaje”**, que reflejan la aplicación progresiva de **Programación Orientada a Objetos (POO)**, **arquitectura en capas**, **buenas prácticas** y **pruebas unitarias**.

- **EVIDENCIA-3** → Punto de partida del proyecto.  
  Contiene el **primer prototipo funcional** que incluye la lógica de usuarios, dispositivos y automatizaciones, sin POO.  
  En esta etapa, los datos se almacenan en estructuras básicas (diccionarios y listas), y la interacción se realiza desde una interfaz de consola sencilla.

- **DIAGRAMA-DE-CLASES / DC-Evidencia-5** → Transición hacia POO.  
  Incluye los **diagramas UML** elaborados durante la Evidencia 5, que representan el diseño orientado a objetos del sistema basado en los modelos de la EVIDENCIA-3.  
  La subcarpeta `DC-Evidencia-5` contiene los diagramas originales de la EV5, mientras que la carpeta `DIAGRAMA-DE-CLASES` incluye los diagramas **actualizados al proyecto final**.  
  El archivo `DC-ABP.drawio.png` refleja el **diagrama de clases definitivo**, incluyendo relaciones de herencia, agregación, composición y asociación.

- **DATA-BASES / BD-Evidencia-5 y BD-Evidencia-6** → Evolución del modelo de base de datos.  
  - La carpeta **BD-Evidencia-5** contiene **únicamente las bases de datos solicitadas en la consigna de la Evidencia 5**, sin modificaciones adicionales.  
  - La carpeta **BD-Evidencia-6** incluye **las bases de datos de la consigna de la Evidencia 6**, donde se agregaron más registros en DML y consultas más avanzadas (joins y subconsultas).  
  - La carpeta **DATA-BASES** principal almacena los **scripts SQL finales del producto completo**:  
    - `Consultas-DDL-ABP.sql`: definición de estructura (tablas, relaciones y claves).  
    - `Consultas-DML-ABP.sql`: inserciones y consultas de prueba del sistema final.

- **POO-SMARTHOME** → Proyecto principal refactorizado (Evidencia 6).  
  Es la **versión final del sistema**, desarrollada bajo principios de **POO** y **arquitectura en capas (DAO, Services, Views)**.  
  Se implementaron **validaciones de modelos**, **manejo seguro de conexiones**, **TDD (Test Driven Development)** y **tratamiento de excepciones controladas**.  
  Incluye una nueva carpeta `utils` con funciones de apoyo utilizadas por distintas capas del sistema.  
  Representa la culminación del proyecto **Domoga** como una aplicación modular, escalable y mantenible.

---

## 📂 Estructura del Repositorio

Raíz del proyecto:

```tree
DOMOGA/
├───DATA-BASES                  # Evolución del diseño de la base de datos (EV5 y EV6)
│   ├───BD-Evidencia-5          # Bases de datos de la consigna de la Evidencia 5
│   ├───BD-Evidencia-6          # Bases de datos de la consigna de la Evidencia 6
│   ├── Consultas-DDL-ABP.sql   # Script DDL: creación de tablas y relaciones adaptadas al programa final refactorizado
│   └── Consultas-DML-ABP.sql   # Script DML: inserciones y consultas de prueba adaptadas a la nueva base de datos
│
├───DIAGRAMA-DE-CLASES          # Diagramas UML del sistema
│   ├───DC-Evidencia-5          # Diagramas de transición hacia la estructura POO (EV5 y EV6)
│   ├── DC-ABP.drawio.png       # Diagrama de clases actualizado al sistema final
│   └── README.md               # Documentación del diagrama de clases y relaciones UML
│
├───EVIDENCIA-3                 # Proyecto original sin POO (punto de partida)
│   ├───data                    # Datos de ejecución almacenados en estructuras básicas
│   ├───models                  # Modelos iniciales, base para la conversión a POO
│   ├───ui                      # Menús e interfaz de consola
│   ├───utils                   # Funciones auxiliares del programa
│   └── main.py                 # Punto de entrada de la aplicación inicial
│
├───POO-SMARTHOME               # Proyecto principal refactorizado (EV6)
│   ├───dao                     # Capa de acceso a datos
│   │   └───interfaces          # Interfaces DAO para manejo abstracto de datos
│   ├───models                  # Modelos POO del sistema (Usuario, Dispositivo, etc.)
│   ├───services                # Lógica de negocio y conexión entre DAO y views
│   ├───tests                   # Pruebas unitarias (validaciones, TDD, excepciones)
│   ├───utils                   # Funciones auxiliares del sistema refactorizado
│   ├───views                   # Capa de presentación (interfaz de usuario)
│   ├── .env.example            # Ejemplo de configuración de variables de entorno
│   ├── requirements.txt        # Dependencias del proyecto
│   ├── pytest.ini              # Configuración de pytest (marcadores y warnings)
│   └── main.py                 # Punto de entrada de la aplicación final
│
├── .gitignore
├── LICENSE
└── README.md


## ✨ Funcionalidades

El programa ofrece un menú interactivo en consola con distintos niveles de acceso según el rol del usuario:

### 👤 Gestión de Usuarios
* Registro de nuevos usuarios (rol **Estándar** por defecto).
* Inicio y cierre de sesión.
* Cambio de rol (de **Estándar** a **Administrador** y viceversa, solo por administradores).

### 🧩 Menú de Usuario Estándar
* Consultar sus datos personales.
* Consultar todos los dispositivos registrados en el hogar.

### 🛠️ Menú de Administrador
* **Gestión de Dispositivos:**
  * Listar todos los dispositivos.
  * Crear un nuevo dispositivo.
  * Actualizar información de un dispositivo existente.
  * Eliminar un dispositivo.
* **Gestión de Usuarios:**
  * Cambiar el rol de otros usuarios.
  * Ver todos los usuarios registrados.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.12+ (se ha probado con Python 3.13)
* **Base de Datos:** MySQL
* **Librerías Principales:**
  * `mysql-connector-python`: Para la conexión y manejo de la base de datos MySQL.
  * `python-dotenv`: Para la gestión de variables de entorno (como credenciales y configuración).
  * `pytest`: Para la ejecución de pruebas unitarias de los modelos POO.


## 🗄️ Base de Datos

Para la versión final del programa (`POO-SMARTHOME`), se debe utilizar el script de la base de datos ubicado en la carpeta `BD-Evidencia-6`.  
Este script crea una base de datos llamada **`domoga`** con la estructura correcta y los datos iniciales necesarios.

> 💡 *Si lo deseas, puedes editar el script SQL para reemplazar el nombre `domoga` por otro de tu preferencia, siempre que luego actualices el valor correspondiente en el archivo `.env`.*

El script incluye un **usuario administrador por defecto**, necesario para gestionar otros usuarios y dispositivos.  
Los usuarios creados desde la consola son de tipo **Estándar** por defecto.

## 🚀 Instalación y Uso

Sigue estos pasos para ejecutar el **proyecto final y refactorizado** en tu máquina local.

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
        > Todos los nuevos usuarios seran creados con rol de usuario estándar
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


---
## 🧩 Ejecución de la Versión Original (EVIDENCIA-3)

Si deseas ejecutar el proyecto original antes de la refactorización, simplemente navega a la carpeta EVIDENCIA-3 y ejecuta el archivo principal:

```bash
cd EVIDENCIA-3
python main.py
```


> 🟢 *Esta versión no requiere librerías adicionales ni configuración de entorno, ya que no depende de base de datos ni variables externas.*

## 🧑‍💻 Integrantes del equipo

* Luis Gerardo Catalas
* Yamila Noelia Belen Angelo
* Hector Marcelo Murua
* Santiago Ezequiel Delebecq 