# Domoga - Smart Home 🏡

Este proyecto es una aplicación de consola para la gestión de un sistema de hogar inteligente (domótica), desarrollada aplicando los principios de la Programación Orientada a Objetos (POO). El sistema permite la gestión de usuarios con diferentes roles (Administrador y Estándar) y el control de dispositivos dentro del hogar.

##  Evolución del Proyecto 📈

Este repositorio documenta la evolución del proyecto a través de diferentes etapas o "Evidencias de aprendizaje":

* `EVIDENCIA-3`: Punto de partida del proyecto. Programa funcional original que incluye la lógica de usuarios, dispositivos y automatizaciones, sin POO.
* `DC-Evidencia-5`: Diagramas de Clases creados durante la Evidencia 5, orientados a POO y basados en los modelos de la `EVIDENCIA-3`, luego refactorizados para alinearse con el código de la Evidencia 6.
* ``BD-Evidencia-5`` y `BD-Evidencia-6`: Evolución de la base de datos. La carpeta `BD-Evidencia-5` adapta la base original de la ``EVIDENCIA-3`` a los requisitos de la EV5 y EV6, mientras que `BD-Evidencia-6` contiene el script final coherente con el proyecto refactorizado.
* `POO-SMARTHOME`: Carpeta principal del proyecto final. Contiene los modelos de la `EVIDENCIA-3` convertidos a POO según la EV5, refactorizados y simplificados para cumplir los requisitos de la Evidencia 6 y las correcciones indicadas por los profesores (validaciones de modelos, acceso a datos, cierre de cursores, TDD, y corrección de excepciones en el menú).

## 📂 Estructura del Repositorio

El proyecto está organizado siguiendo el patrón de diseño DAO (Data Access Object) para separar la lógica de negocio de la lógica de acceso a datos.

```
├───BD-Evidencia-5      # Base de datos del proyecto original (EV3) adaptada a EV5 y EV6
├───BD-Evidencia-6      # Base de datos del proyecto refactorizado (EV6)
├───DC-Evidencia-5      # Diagramas actualizados del proyecto refactorizado (EV5 y EV6)
├───EVIDENCIA-3         # Proyecto original previo al refactor (EV5 y EV6)
│   ├───data            # Datos de ejecución almacenados en diccionarios
│   ├───models          # Modelos iniciales, luego convertidos a objetos en EV5
│   ├───ui              # Menús e interfaz de consola
│   └───utils           # Funciones auxiliares del programa
└───POO-SMARTHOME       # Proyecto principal refactorizado (EV6)
    ├───dao             # Clases de acceso a datos
    │   └───interfaces  # Interfaces DAO
    ├───models          # Modelos POO del sistema
    ├───services        # Lógica de negocio y conexión entre DAO y views
    ├───tests           # Pruebas unitarias centradas en los modelos POO y sus validaciones; no cubren servicios ni DAO
    └───views           # Capa de presentación (interfaz de usuario)
```

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

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

1.  **🖥️ Clonar el Repositorio**
    ```bash
    git clone https://github.com/Domoga-app/Domoga.git
    cd Domoga
    ```

2.  **⚡ Crear un Entorno Virtual**
    ```bash
    cd POO-SMARTHOME
    python -m venv venv
    ```
    Actívalo:
    * En Windows: `.\venv\Scripts\activate`
    * En macOS/Linux: `source venv/bin/activate`

3.  **📦 Instalar Dependencias**
    Asegúrate de estar dentro de la carpeta `POO-SMARTHOME` y ejecuta:
    ```bash
     pip install pytest mysql-connector-python python-dotenv
    ```

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
    * Ejecuta el script SQL ubicado en `BD-Evidencia-6` para crear la base de datos `domoga` y sus tablas.

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
