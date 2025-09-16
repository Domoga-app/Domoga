-- CONSULTAS DDL

-- Tabla Roles
CREATE TABLE Roles (
    Id_Rol INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Tabla Permisos
CREATE TABLE Permisos (
    DNI INT PRIMARY KEY,
    Id_Rol INT NOT NULL,
    FOREIGN KEY (Id_Rol) REFERENCES Roles(Id_Rol)
) ENGINE=InnoDB;

-- Tabla Usuarios
CREATE TABLE Usuarios (
    DNI INT PRIMARY KEY,
    Id_Rol INT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Contrasena VARCHAR(100) NOT NULL,
    FOREIGN KEY (Id_Rol) REFERENCES Roles(Id_Rol)
) ENGINE=InnoDB;

-- Tabla Tipos_Dispositivos
CREATE TABLE Tipos_Dispositivos (
    Id_Tipo INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Tabla Dispositivos
CREATE TABLE Dispositivos (
    MAC CHAR(17) PRIMARY KEY, -- Ejemplo: 00:1B:44:11:3A:B7
    Id_Tipo INT NOT NULL,
    Marca VARCHAR(50),
    Modelo VARCHAR(50),
    Estado TINYINT(1) DEFAULT 0, -- 0=Apagado, 1=Encendido
    FOREIGN KEY (Id_Tipo) REFERENCES Tipos_Dispositivos(Id_Tipo)
) ENGINE=InnoDB;

-- Tabla Hogares
CREATE TABLE Hogares (
    Id_Hogar INT PRIMARY KEY,
    Direccion VARCHAR(100) NOT NULL,
    Nombre VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Tabla UsuariosxHogares (relación N a N)
CREATE TABLE UsuariosxHogares (
    DNI INT,
    Id_Hogar INT,
    PRIMARY KEY (DNI, Id_Hogar),
    FOREIGN KEY (DNI) REFERENCES Usuarios(DNI),
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
) ENGINE=InnoDB;

-- Tabla Ambientes
CREATE TABLE Ambientes (
    Id_Ambiente INT PRIMARY KEY,
    Id_Hogar INT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
) ENGINE=InnoDB;

-- Tabla Automatizaciones
CREATE TABLE Automatizaciones (
    Id_Automatizacion INT PRIMARY KEY,
    Id_Hogar INT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Dias VARCHAR(50), -- Ej: "Lunes,Martes"
    Hora TIME,
    Accion VARCHAR(50),
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
) ENGINE=InnoDB;

-- Tabla Automatizaciones_Dispositivos (N a N)
CREATE TABLE Automatizaciones_Dispositivos (
    Id_Automatizacion INT,
    MAC_Dispositivo CHAR(17),
    PRIMARY KEY (Id_Automatizacion, MAC_Dispositivo),
    FOREIGN KEY (Id_Automatizacion) REFERENCES Automatizaciones(Id_Automatizacion),
    FOREIGN KEY (MAC_Dispositivo) REFERENCES Dispositivos(MAC)
) ENGINE=InnoDB;

