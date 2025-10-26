README – Ejecución de Scripts en SQL DBMS Online

# Proyecto Dómoga

## ⚙️ Lógica de negocio

## Gestión de usuarios

Los usuarios son las personas que pueden operar el sistema.

Cada usuario tiene:

Un nombre_usuario único (para autenticación).

Un dni único (para identificación).

Un campo booleano es_admin que diferencia usuarios comunes de administradores.

Una contrasena encriptada.

🔹 Regla de negocio: Solo los administradores (es_admin = TRUE) pueden crear o gestionar otros usuarios y dispositivos.

## Gestión de tipos de dispositivos

La tabla tipos_dispositivo define las categorías generales de equipos que el sistema puede manejar (luces, cámaras, sensores, etc.).

Cada tipo tiene un nombre único.

🔹 Regla de negocio: Los dispositivos solo pueden pertenecer a un tipo existente. No se puede crear un dispositivo sin un tipo definido.

## Gestión de dispositivos

La tabla dispositivos representa los equipos físicos inteligentes instalados.

Cada dispositivo tiene:

Un tipo (relación con tipos_dispositivo).

Una ubicacion (dónde está instalado).

Su estado (por defecto 'apagado').

🔹 Regla de negocio:

Un dispositivo siempre pertenece a un tipo (id_tipo obligatorio).

Un dispositivo no puede existir sin un tipo registrado.

El estado solo puede ser 'encendido' o 'apagado' (según la lógica de la aplicación).

## Gestión de automatizaciones

Las automatizaciones representan acciones programadas (por tiempo y día) para controlar dispositivos.

Cada automatización define:

Días de ejecución (dias, por ejemplo LMMJVSD = todos los días).

Una hora (hora).

Una acción (accion), como “encender”, “apagar”, “subir” o “bajar”.

🔹 Regla de negocio:

Una automatización tiene una acción asociada a uno o varios dispositivos.

La relación se define en la tabla automatizacion_dispositivo.

## Relación automatización–dispositivo

Tabla intermedia (automatizacion_dispositivo) que une automatizaciones con dispositivos.

Tiene clave primaria compuesta (automatizacion_id, dispositivo_id).

🔹 Regla de negocio:

Si una automatización o dispositivo se elimina, la relación también desaparece (ON DELETE CASCADE).

Un dispositivo puede participar en más de una automatización.

Una automatización puede controlar más de un dispositivo.
→ Relación muchos a muchos.

## Consultas y subconsultas: reglas operativas

Las consultas SQL al final reflejan comportamientos reales del sistema:

| Tipo de consulta                         | Lógica de negocio                                                |
|------------------------------------------|------------------------------------------------------------------|
| **Dispositivos con su tipo**             | Mostrar información combinada para gestión del inventario.       |
| **Automatizaciones con dispositivos**    | Ver qué acciones están programadas sobre qué equipos.            |
| **Cantidad de dispositivos por tipo**    | Estadística de distribución de dispositivos.                     |
| **Automatizaciones después de las 20:00**| Control de rutinas nocturnas.                                   |
| **Dispositivos del mismo tipo**          | Filtrar por categoría, útil para configuración o mantenimiento.  |
| **Dispositivos sin automatización**      | Detectar equipos sin programación activa.                        |

---

## Contenido del repositorio

1. BDD-Evidencia-5 contiene las consultas DDL y DML pertenecientes a la Evidencia número 5.  
2. BDD-Evidencia-6 contiene las consultas DDL y DML pertenecientes a la Evidencia número 6 con correciones de la Evidencia número 5.
4. Consultas-DDL-ABP.sql - Contiene sentencias para crear la tablas y relaciones para el programa simplificado del Proyecto Final ABP.
5. Consultas-DML-ABP.sql - Contiene sentencias para inserción de registros en las tablas creadas, ademas de ejemplos de consultas multitabla y subconsultas del Proyecto Final ABP.
---

## Cómo ejecutar los scripts en un DBMS online

Se puede usar cualquier DBMS online que soporte MySQL, en nuestro caso elegimos:

- [OneCompiler MySQL](https://onecompiler.com/mysql)

- Link al script 👉 https://onecompiler.com/mysql/442saupne.

### Pasos

1. Abrir el DBMS online https://onecompiler.com/mysql/442saupne.
2. Verificá que este seleccionado MySQL.
3. Ejecuta el script desde el botón "RUN".

## Estructura de tablas

- Usuarios: almacena información de los usuarios y su rol por ejemplo si son administradores.

- Tipos_Dispositivo: almacena los tipos de dispositivos disponibles (Lámpara, Termostato, Cámara, etc.) y su id.

- Dispositivos: dispositivos registrados, con su tipo, ubicación, marca, modelo y estado (encendido/apagado).

- Automatizaciones: reglas de automatización, indicando días, hora y acción a ejecutar.

- Automatizacion_Dispositivo: relación entre automatizaciones y dispositivos asociados, permite múltiples dispositivos por automatización y viceversa.

---

## Autores
Proyecto realizado por:

DNI 38654685 - Angelo Yamila Noelia Belén.
DNI 43067931 - Delebecq Santiago Ezequiel.
DNI 35581397 - Catalas Luis Gerardo.
DNI 36233823 - Murua Hector Marcelo.

como parte de la Tecnicatura Superior en Desarrollo de Software – ISPC.


