# README - Diagrama UML de Domoga

## 🌟 Descripción General

Este proyecto modela un **sistema de Smarthome**, incluyendo usuarios, dispositivos, tipos de dispositivos y automatizaciones.  
La arquitectura sigue un enfoque en capas, separando **modelos**, **DAOs** (Data Access Objects), **servicios** y **vistas**, para mantener el código modular y escalable.

---

## 🏠 Modelos

### **Usuario**
Representa a un usuario del sistema.

**Atributos:**
- `id_usuario`: Identificador único.
- `nombre_usuario`: Nombre de usuario para login.
- `nombre` y `apellido`: Datos personales.
- `dni`: Documento de identidad.
- `es_admin`: Indica si el usuario tiene privilegios de administrador.
- `contrasena`: Contraseña del usuario.

**Métodos:**
- `verificar_contrasena(contrasena: str): bool` — Comprueba si la contraseña ingresada es correcta.

---

### **TipoDispositivo**
Representa el tipo de un dispositivo (ej. Sensor, Bombilla, Termostato).

**Atributos:**
- `id_tipo`: Identificador único del tipo.
- `nombre`: Nombre del tipo.

---

### **Dispositivo**
Representa un dispositivo físico dentro del hogar.

**Atributos:**
- `id_dispositivo`: Identificador único.
- `tipo`: Referencia a `TipoDispositivo`.
- `ubicacion`: Ubicación dentro del hogar.
- `marca`, `modelo`: Información técnica.
- `estado`: Estado actual.

**Relaciones:**
- Cada dispositivo tiene un tipo  
  `Dispositivo "1" *-- "1" TipoDispositivo : tiene`

---

### **Automatizacion**
Define reglas automáticas que afectan a dispositivos.

**Atributos:**
- `id_automatizacion`: Identificador único.
- `nombre`: Nombre de la automatización.
- `dias`: Lista de días en que se ejecuta.
- `hora`: Hora de ejecución.
- `accion`: Acción a realizar.
- `dispositivos_afectados`: Lista de dispositivos que se ven afectados.

**Métodos:**
- `agregar_dispositivo(dispositivo: Dispositivo)` — Vincula un dispositivo a la automatización.

**Relaciones:**
- Una automatización puede afectar múltiples dispositivos  
  `Automatizacion "1" -- "0..*" Dispositivo : afecta`

---

## 🗃️ Interfaces DAO

Los DAOs definen métodos de acceso a datos para cada modelo:

- `IUsuarioDAO`, `IDispositivoDAO`, `ITipoDispositivoDAO`, `IAutomatizacionDAO`.

**Métodos incluyen:**
- Crear, obtener, actualizar, eliminar.
- Operaciones específicas, como vincular dispositivos a automatizaciones.

---

## 📦 Clases DAO

- `UsuarioDAO`, `DispositivoDAO`, `TipoDispositivoDAO`, `AutomatizacionDAO`  

**Implementan sus respectivas interfaces DAO** (`<<implementa Interface>>`) y **manejan directamente un modelo**:  
Ejemplo: `UsuarioDAO --> Usuario : maneja`

---

## ⚙️ Interfaces Service

Las capas de servicio exponen la **lógica de negocio** del sistema:

- `IUsuarioService`, `IDispositivoService`, `ITipoDispositivoService`.

**Métodos incluyen:**  
- Operaciones de negocio como registrar usuarios, iniciar sesión, crear dispositivos y obtener listas completas.

---

## 🛠️ Clases Service

- `UsuarioService`, `DispositivoService`, `TipoDispositivoService`  

**Implementan sus interfaces de servicio** y **usan su DAO correspondiente**:  
Ejemplo: `DispositivoService --> DispositivoDAO : usa`

---

## 🔗 Relaciones entre Capas

### Modelos y DAOs
- Cada DAO tiene una relación de manejo con su modelo.  
  Ejemplo: `DispositivoDAO --> Dispositivo : maneja`

### DAOs y Interfaces
- Los DAOs implementan interfaces que definen los métodos obligatorios.  
  Ejemplo: `UsuarioDAO ..|> IUsuarioDAO`

### Servicios y DAOs
- Los servicios utilizan los DAOs para acceder a la base de datos.  
  Ejemplo: `DispositivoService --> DispositivoDAO : usa`

### Servicios e Interfaces
- Los servicios implementan interfaces que definen la lógica de negocio a exponer.  
  Ejemplo: `UsuarioService ..|> IUsuarioService`

---

## 📝 Notas

- El sistema está diseñado para ser **modular**, permitiendo reemplazar la capa de acceso a datos sin afectar la lógica de negocio.
- Los métodos específicos de negocio (como `verificar_contrasena` o `agregar_dispositivo`) se encuentran en los modelos y servicios según corresponda.
- Este diagrama proporciona una **visión conceptual**, sin entrar en detalles de implementación como getters/setters de cada atributo.
