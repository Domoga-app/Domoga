README – Ejecución de Scripts en SQL DBMS Online

# Proyecto Dómoga – Scripts SQL

Este repositorio contiene los scripts SQL del proyecto , incluyendo la creación de la base de datos, tablas, relaciones y datos de prueba. Está pensado para ejecutarse en un DBMS online o en MySQL.

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


