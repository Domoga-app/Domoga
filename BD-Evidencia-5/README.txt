README – Ejecución de Scripts en SQL DBMS Online

# Proyecto Dómoga – Scripts SQL

Este repositorio contiene los scripts SQL del proyecto , incluyendo la creación de la base de datos, tablas, relaciones y datos de prueba. Está pensado para ejecutarse en un DBMS online o en SQL Server Management Studio (SSMS).

---

## Contenido del repositorio

1. Consultas-DDL.sql – Contiene las sentencias para crear las tablas y relaciones (estructura de la base de datos).  
2. Consultas-DDL.sql – Contiene los datos de ejemplo (30 registros principales) y relaciones de prueba y contiene consultas de prueba para verificar que los datos fueron insertados correctamente.
3. Archivo README.txt con explicación y detalles.

---

## Cómo ejecutar los scripts en un DBMS online

Se puede usar cualquier DBMS online que soporte SQL Server, en nuestro caso elegimos:

- [OneCompiler SQL Server](https://onecompiler.com/sqlserver)

- Link al script 👉 https://onecompiler.com/sqlserver/43wr9eubb

### Pasos

1. Abrir el DBMS online https://onecompiler.com/sqlserver/43wr9eubb.
2. Verificá que este seleccionado SSMS (SQL Server).
3. Ejecuta el script desde el botón "RUN".

## Estructura de tablas

- Roles: almacena los roles (Administrador, Usuario).  
- Usuarios: almacena información de los usuarios y su rol.  
- Hogares: información de los hogares.  
- UsuariosxHogares: relación entre usuarios y hogares.  
- Tipos_Dispositivos: tipos de dispositivos.  
- Dispositivos: dispositivos disponibles.  
- Ambientes: ambientes dentro de cada hogar.  
- Automatizaciones: reglas de automatización por hogar.  
- Automatizaciones_Dispositivos: dispositivos asociados a cada automatización.

---

## Autor
Proyecto realizado por:

DNI 38654685 - Angelo Yamila Noelia Belén.
DNI 43067931 - Delebecq Santiago Ezequiel.
DNI 35581397 - Catalas Luis Gerardo.
DNI 36233823 - Murua Hector Marcelo.

como parte de la Tecnicatura Superior en Desarrollo de Software – ISPC.


