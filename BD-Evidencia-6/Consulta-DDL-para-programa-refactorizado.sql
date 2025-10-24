
CREATE DATABASE IF NOT EXISTS domoga;
USE domoga;

CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    dni VARCHAR(8) NOT NULL UNIQUE,
    es_admin BOOLEAN NOT NULL DEFAULT FALSE,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    contrasena VARCHAR(255) NOT NULL
);

CREATE TABLE tipos_dispositivo (
    id_tipo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE dispositivos (
    id_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
    id_tipo INT NOT NULL,
    ubicacion VARCHAR(30) NOT NULL,
    marca VARCHAR(30),
    modelo VARCHAR(30),
    estado VARCHAR(30) NOT NULL DEFAULT 'apagado',
    FOREIGN KEY (id_tipo) REFERENCES tipos_dispositivo(id_tipo)
);

CREATE TABLE automatizaciones (
    id_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    dias VARCHAR(7) NOT NULL,
    hora TIME NOT NULL,
    accion VARCHAR(30) NOT NULL
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