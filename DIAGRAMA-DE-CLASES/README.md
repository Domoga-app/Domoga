## 📐 Diseño Orientado a Objetos (Diagrama de Clases UML)

El siguiente diagrama UML muestra la estructura lógica de la aplicación **Domoga**, definiendo las clases principales, sus atributos, operaciones y las relaciones entre la lógica de negocio (`models`) y la persistencia de datos (`DAO`).

![Diagrama de Clases de Domoga](DIAGRAMA DE CLASES/DC-Evidencia-6/Diagrama de clasea nuevo.drawio.png)
---

### **Componentes y Relaciones Clave**

El sistema se estructura en las siguientes clases y tipos de relaciones:

#### **Clases de Dominio (Modelos)**
* **`Usuario`**: Representa a la persona que interactúa con el sistema (Administrador o Estándar). Contiene atributos como `dni`, `nombre` y `rol`.
* **`Dispositivo`**: Es la clase base para cualquier objeto del hogar (Luz, Sensor, etc.). Sus atributos son genéricos (`id`, `nombre`, `estado`).
* **Subclases de Dispositivo**: (e.g., `Luz`, `Termostato`): **Heredan (Generalización)** de la clase `Dispositivo` y añaden atributos o métodos específicos.

#### **Relaciones de Persistencia (DAO)**
* **Realización / Implementación:** Las clases de Acceso a Datos (e.g., `UsuarioDAO`, `DispositivoDAO`) **implementan** la lógica de conexión y manipulación de datos para sus respectivas clases de modelo.
* **Relación:** `Usuario` es gestionado por `UsuarioDAO` (relación de dependencia o realización). Esto separa la lógica de negocio de la base de datos.

#### **Asociaciones Lógicas**
* **Asociación entre `Usuario` y `Dispositivo`**: Un `Usuario` (especialmente el Administrador) **controla** la gestión y el estado de múltiples `Dispositivos`.
* **Multiplicidad:** Se establece la cardinalidad para definir cuántos objetos de una clase se relacionan con cuántos objetos de otra (ej. 1 Usuario puede controlar 0 a muchos Dispositivos: `1 -- 0..*`).

| Relación | Clases Involucradas | Tipo UML | Descripción |
| :--- | :--- | :--- | :--- |
| **Persistencia** | `Usuario` y `UsuarioDAO` | Realización/Dependencia | El DAO contiene la lógica SQL para la clase Modelo. |
| **Control** | `Usuario` y `Dispositivo` | Asociación | El usuario administra y opera los dispositivos. |
| **Especialización** | `Dispositivo` y Subclases | Herencia / Generalización | Las subclases extienden la funcionalidad base del dispositivo. |
