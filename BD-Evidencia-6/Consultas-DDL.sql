-- CONSULTAS DDL

-- Tabla Roles
CREATE TABLE IF NOT EXISTS Roles (
    Id_Rol INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
);
-- Tabla Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    DNI INT PRIMARY KEY,
    Id_Rol INT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Contrasena VARCHAR(100) NOT NULL,
    FOREIGN KEY (Id_Rol) REFERENCES Roles(Id_Rol)
);
-- Tabla Hogares
CREATE TABLE IF NOT EXISTS Hogares (
    Id_Hogar INT PRIMARY KEY,
    Direccion VARCHAR(100) NOT NULL,
    Nombre_Hogar VARCHAR(50) NOT NULL
);
-- Tabla UsuariosxHogares (relación N a N)
CREATE TABLE IF NOT EXISTS UsuariosxHogares (
    DNI INT,
    Id_Hogar INT,
    PRIMARY KEY (DNI, Id_Hogar),
    FOREIGN KEY (DNI) REFERENCES Usuarios(DNI),
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
);
-- Tabla Ambientes
CREATE TABLE IF NOT EXISTS Ambientes (
    Id_Ambiente INT PRIMARY KEY,
    Id_Hogar INT NOT NULL,
    Nombre_Ambiente VARCHAR(50) NOT NULL,
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
);
-- Tabla Tipos_Dispositivos
CREATE TABLE IF NOT EXISTS Tipos_Dispositivos (
    Id_Tipo INT PRIMARY KEY,
    Nombre_Tipo VARCHAR(50) NOT NULL
);
-- Tabla Dispositivos
CREATE TABLE IF NOT EXISTS Dispositivos (
    MAC CHAR(17) PRIMARY KEY,
    Id_Tipo INT NOT NULL,
    Id_Ambiente INT NOT NULL,
    Marca VARCHAR(50),
    Modelo VARCHAR(50),
    Estado TINYINT(1) DEFAULT 0,
    FOREIGN KEY (Id_Tipo) REFERENCES Tipos_Dispositivos(Id_Tipo),
    FOREIGN KEY (Id_Ambiente) REFERENCES Ambientes(Id_Ambiente)
);
-- Tabla Automatizaciones
CREATE TABLE IF NOT EXISTS Automatizaciones (
    Id_Automatizacion INT PRIMARY KEY,
    Id_Hogar INT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Dias VARCHAR(50),
    Hora TIME,
    Accion VARCHAR(50),
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
);
-- Tabla Automatizaciones_Dispositivos
CREATE TABLE IF NOT EXISTS Automatizaciones_Dispositivos (
    Id_Automatizacion INT,
    MAC_Dispositivo CHAR(17),
    PRIMARY KEY (Id_Automatizacion, MAC_Dispositivo),
    FOREIGN KEY (Id_Automatizacion) REFERENCES Automatizaciones(Id_Automatizacion),
    FOREIGN KEY (MAC_Dispositivo) REFERENCES Dispositivos(MAC)
);