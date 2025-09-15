-- Consultas DDL para la creación de tablas y relaciones

-- Tabla Roles
CREATE TABLE Roles (
    Id_Rol INT PRIMARY KEY,
    Nombre NVARCHAR(50) NOT NULL
);

-- Tabla Permisos
CREATE TABLE Permisos (
    DNI INT PRIMARY KEY,
    Id_Rol INT NOT NULL,
    FOREIGN KEY (Id_Rol) REFERENCES Roles(Id_Rol)
);

-- Tabla Usuarios
CREATE TABLE Usuarios (
    DNI INT PRIMARY KEY,
    Id_Rol INT NOT NULL,
    Nombre NVARCHAR(50) NOT NULL,
    Apellido NVARCHAR(50) NOT NULL,
    Contrasena NVARCHAR(100) NOT NULL,
    FOREIGN KEY (Id_Rol) REFERENCES Roles(Id_Rol)
);

-- Tabla Tipos_Dispositivos
CREATE TABLE Tipos_Dispositivos (
    Id_Tipo INT PRIMARY KEY,
    Nombre NVARCHAR(50) NOT NULL
);

-- Tabla Dispositivos
CREATE TABLE Dispositivos (
    MAC CHAR(17) PRIMARY KEY, -- Ejemplo: 00:1B:44:11:3A:B7
    Id_Tipo INT NOT NULL,
    Marca NVARCHAR(50),
    Modelo NVARCHAR(50),
    Estado BIT DEFAULT 0, -- 0=Apagado, 1=Encendido
    FOREIGN KEY (Id_Tipo) REFERENCES Tipos_Dispositivos(Id_Tipo)
);

-- Tabla Hogares
CREATE TABLE Hogares (
    Id_Hogar INT PRIMARY KEY,
    Direccion NVARCHAR(100) NOT NULL,
    Nombre NVARCHAR(50) NOT NULL
);

-- Tabla UsuariosxHogares (relación N a N)
CREATE TABLE UsuariosxHogares (
    DNI INT,
    Id_Hogar INT,
    PRIMARY KEY (DNI, Id_Hogar),
    FOREIGN KEY (DNI) REFERENCES Usuarios(DNI),
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
);

-- Tabla Ambientes
CREATE TABLE Ambientes (
    Id_Ambiente INT PRIMARY KEY,
    Id_Hogar INT NOT NULL,
    Nombre NVARCHAR(50) NOT NULL,
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
);

-- Tabla Automatizaciones
CREATE TABLE Automatizaciones (
    Id_Automatizacion INT PRIMARY KEY,
    Id_Hogar INT NOT NULL,
    Nombre NVARCHAR(50) NOT NULL,
    Dias NVARCHAR(50), -- Ej: "Lunes,Martes"
    Hora TIME,
    Accion NVARCHAR(50),
    FOREIGN KEY (Id_Hogar) REFERENCES Hogares(Id_Hogar)
);

-- Tabla Automatizaciones_Dispositivos (N a N)
CREATE TABLE Automatizaciones_Dispositivos (
    Id_Automatizacion INT,
    MAC_Dispositivo CHAR(17),
    PRIMARY KEY (Id_Automatizacion, MAC_Dispositivo),
    FOREIGN KEY (Id_Automatizacion) REFERENCES Automatizaciones(Id_Automatizacion),
    FOREIGN KEY (MAC_Dispositivo) REFERENCES Dispositivos(MAC)
);
