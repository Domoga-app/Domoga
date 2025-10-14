
CREATE DATABASE IF NOT EXISTS domotica;
USE domotica;

CREATE TABLE usuarios (
    dni VARCHAR(20) PRIMARY KEY,
    es_admin BOOLEAN NOT NULL DEFAULT FALSE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    contrasena VARCHAR(255) NOT NULL
);

CREATE TABLE tipos_dispositivo (
    id_tipo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE dispositivos (
    id_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
    id_tipo INT,
    ubicacion VARCHAR(100),
    marca VARCHAR(100),
    modelo VARCHAR(100),
    estado VARCHAR(50) DEFAULT 'apagado',
    FOREIGN KEY (id_tipo) REFERENCES tipos_dispositivo(id_tipo)
);

CREATE TABLE automatizaciones (
    id_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    dias VARCHAR(100),
    hora TIME,
    accion VARCHAR(50)
);

CREATE TABLE automatizacion_dispositivo (
    automatizacion_id INT,
    dispositivo_id INT,
    PRIMARY KEY (automatizacion_id, dispositivo_id),
    FOREIGN KEY (automatizacion_id) REFERENCES automatizaciones(id_automatizacion) ON DELETE CASCADE,
    FOREIGN KEY (dispositivo_id) REFERENCES dispositivos(id_dispositivo) ON DELETE CASCADE
);


INSERT INTO usuarios (dni, es_admin, nombre, apellido, contrasena) VALUES 
('1', TRUE, 'Admin', 'User', '1'),
('2', FALSE, 'Usuario', 'Estandar', '1234');

INSERT INTO tipos_dispositivo (id_tipo, nombre) VALUES
(1, 'Lámpara Inteligente'),
(2, 'Termostato'),
(3, 'Cámara de Seguridad');

INSERT INTO dispositivos (id_tipo, ubicacion, marca, modelo, estado) VALUES
(1, 'Living', 'Philips', 'Hue', 'apagado'),
(2, 'Dormitorio', 'Google', 'Nest', 'encendido');