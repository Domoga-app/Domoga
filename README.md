# Proyecto Domótica - Smart Home (POO) 🏡

Este proyecto es una aplicación de consola para la gestión de un sistema de hogar inteligente (domótica), desarrollada aplicando los principios de la Programación Orientada a Objetos (POO). El sistema permite la gestión de usuarios con diferentes roles (Administrador y Estándar) y el control de dispositivos dentro del hogar.

##  Evolución del Proyecto 📈

Este repositorio documenta la evolución del proyecto a través de diferentes etapas o "Evidencias":

* `EVIDENCIA-3`: Contiene el punto de partida del proyecto. Un programa funcional original que incluye la lógica de usuarios, dispositivos y automatizaciones.
* `DC-Evidencia-5`: Incluye los Diagramas de Clases correspondientes al diseño de la Evidencia 5.
* `BD-Evidencia-5` y `BD-Evidencia-6`: Muestran la evolución de la base de datos. La carpeta `BD-Evidencia-6` contiene tanto el script de la base de datos original como el **nuevo script simplificado**, que es el que se debe usar para la versión final del programa.
* `POO-SMARTHOME`: Es la carpeta principal del proyecto final. Contiene el código de la Evidencia 5, que fue **refactorizado y simplificado** para cumplir con los requisitos de la Evidencia 6.

## 📂 Estructura del Proyecto Principal (`POO-SMARTHOME`)

El proyecto está organizado siguiendo el patrón de diseño DAO (Data Access Object) para separar la lógica de negocio de la lógica de acceso a datos.

```
POO-SMARTHOME/
│
├── conn/
│   └── db_conn.py            # Gestiona la conexión con la base de datos.
│
├── dao/
│   ├── interface/            # Define las interfaces (contratos) para los DAOs.
│   │   ├── i_automatizacionDAO.py
│   │   ├── i_dispositivoDAO.py
│   │   └── ...
│   ├── automatizacionDAO.py  # Implementación de la lógica CRUD para automatizaciones.
│   ├── dispositivoDAO.py     # Implementación de la lógica CRUD para dispositivos.
│   └── ...
│
├── models/
│   ├── automatizacion.py     # Clase que modela una automatización.
│   ├── dispositivo.py        # Clase que modela un dispositivo.
│   └── ...
│
├── .env                      # (Archivo local) Credenciales de la base de datos.
├── .env.example              # Plantilla para el archivo .env.
├── main.py                   # Punto de entrada de la aplicación, gestiona los menús.
└── requirements.txt          # Lista de dependencias de Python.
```

## ✨ Funcionalidades

El programa ofrece un menú interactivo en la consola con las siguientes capacidades:

* **Gestión de Usuarios:**
    * Registro de nuevos usuarios (rol Estándar por defecto).
    * Inicio de sesión.
* **Menú de Usuario Estándar:**
    * Consultar sus datos personales.
    * Consultar todos los dispositivos de la casa.
* **Menú de Administrador:**
    * Gestionar dispositivos (Crear, Listar, Actualizar, Eliminar).
    * Cambiar el rol de un usuario existente (de Estándar a Administrador y viceversa).

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Base de Datos:** MySQL
* **Librerías Principales:**
    * `mysql-connector-python`: Para la conexión con la base de datos MySQL.
    * `python-dotenv`: Para la gestión de variables de entorno (credenciales).

## 🗄️ Base de Datos

Para la versión final del programa (`POO-SMARTHOME`), se debe utilizar el **script de la base de datos simplificada** que se encuentra en la carpeta `BD-Evidencia-6`. Este script crea una base de datos llamada `domotica` con la estructura correcta y los datos iniciales necesarios.

## 🚀 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

1.  **Clonar el Repositorio**
    ```bash
    git clone https://github.com/Domoga-app/Domoga.git
    cd Domoga
    ```

2.  **Crear un Entorno Virtual**
    ```bash
    python -m venv venv
    ```
    Actívalo:
    * En Windows: `.\venv\Scripts\activate`
    * En macOS/Linux: `source venv/bin/activate`

3.  **Instalar Dependencias**
    Asegúrate de estar dentro de la carpeta `POO-SMARTHOME` y ejecuta:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar la Base de Datos**
    * Asegúrate de tener un servidor MySQL en funcionamiento.
    * Ejecuta el script SQL ubicado en `BD-Evidencia-6` para crear la base de datos `domotica` y sus tablas.

5.  **Configurar las Variables de Entorno**
    * Dentro de la carpeta `POO-SMARTHOME`, renombra el archivo `.env.example` a `.env`.
    * Abre el archivo `.env` y edita los valores para que coincidan con tus credenciales de MySQL:
    ```ini
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=tu_contraseña
    DB_NAME=domotica
    DB_PORT=3306
    ```

6.  **Ejecutar la Aplicación**
    Desde la carpeta `POO-SMARTHOME`, ejecuta el siguiente comando:
    ```bash
    python main.py
    ```