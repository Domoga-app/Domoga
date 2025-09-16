<<<<<<< HEAD
# Proyecto Domóga - Sistema Domótico

Este proyecto modular implementa un sistema domótico básico en Python.

## Estructura
- `datos.py`: Datos globales compartidos (usuarios, hogares, dispositivos, automatizaciones)
- `automatizaciones.py`: Gestión y menú para automatizaciones (programar encendido/apagado)
- `menu_usuario.py`: Ejemplo de menú principal de usuario que integra automatizaciones

## Uso
Ejecutar el menú principal del usuario para acceder a opciones de automatización.

## Gitignore
Ignora archivos compilados y carpetas comunes de entornos y editores.
=======
# Domoga

**Domóga.app**  (Dom “domótica”, Óga “hogar o casa en guaraní”) surge como una alternativa a otras apps de domótica y control de dispositivos donde nos topamos con problemas de integraciones. Nuestra app permite que mediante un solo hub integrado al hogar podamos conectarnos y controlar diversos dispositivos ya sea mediante conexión wifi, señal rts, Bluetooth, etc.
**Domóga** nos permite vincular diversos dispositivos y generar controladores personalizados para cada uno de manera sencilla. Con nuestro usuario único podremos tener la total administración de nuestros hogares con la tranquilidad de que cada usuario y hogar cuenta con su clave de seguridad de doble confirmación.
Mediante notificaciones en la app y mensajería, Domóga nos informa de todos los cambios y estados de nuestros dispositivos ya sea que estemos en nuestro hogar o fuera.


## ⚙️ Funcionalidades
- Creación de usuario: permite generar el nombre y clave con el cual ingresaremos en la app. Este es único e irrepetible y se vincula con una cuenta de email de preferencia que nos permitirá tener avisos de la app, recuperar la contraseña, etc.
- Creación de Hogar: es el primer paso para vincular dispositivos. La creación de un hogar nos permite vincular un Hub a la red wifi de la casa y permitir que detecte los diversos dispositivos que en ella se encuentran. Aquí también podremos crear y personalizar los espacios o ambientes que tenga nuestro hogar los cuales nos permitirán organizar la disposición de nuestros dispositivos
- particular de nuestro hogar, elegir que tipo de dispositivo es(tv, luz, cortina, equipo de musica,etc), identificarlo con un nombre y acceder al controlador del mismo
- Automatización de dispositivos: nos permite generar configuraciones automáticas para cada dispositivo y espacio, ya sea prender una luz a x hora, activar los aspersores del patio durante más tiempo en verano que en invierno, bajar las cortinas si la temperatura subo por encima de 30 grados, etc.

👤 Autor
Domoga App – @Domoga-app
>>>>>>> d0f00d1c4c6b8fe5cd03b8e8f72d4a9a5c017cba
