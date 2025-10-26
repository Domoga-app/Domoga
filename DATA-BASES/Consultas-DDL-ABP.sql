-- Consultas DDL

-- DEFINICION DE ESTRUCTURA DE LA BASE DE DATOS

-- Creamos la base de datos
CREATE DATABASE IF NOT EXISTS domoga;
USE domoga;

-- Creamos tabla usuarios
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(30) NOT NULL UNIQUE,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    dni VARCHAR(8) NOT NULL UNIQUE,
    es_admin BOOLEAN NOT NULL DEFAULT FALSE,
    contrasena VARCHAR(255) NOT NULL
);

-- Creamos tabla tipos_dispositivo
CREATE TABLE tipos_dispositivo (
    id_tipo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

-- Creamos tabla dispositivos
CREATE TABLE dispositivos (
    id_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
    id_tipo INT NOT NULL,
    ubicacion VARCHAR(30) NOT NULL,
    marca VARCHAR(30),
    modelo VARCHAR(30),
    estado VARCHAR(30) NOT NULL DEFAULT 'apagado',
    FOREIGN KEY (id_tipo) REFERENCES tipos_dispositivo(id_tipo)
);

-- Creamos tabla automatizaciones
CREATE TABLE automatizaciones (
    id_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    dias VARCHAR(7) NOT NULL,
    hora TIME NOT NULL,
    accion VARCHAR(30) NOT NULL
);

-- Creamos tabla automatizacion_dispositivo
CREATE TABLE automatizacion_dispositivo (
    automatizacion_id INT,
    dispositivo_id INT,
    PRIMARY KEY (automatizacion_id, dispositivo_id),
    FOREIGN KEY (automatizacion_id) REFERENCES automatizaciones(id_automatizacion) ON DELETE CASCADE,
    FOREIGN KEY (dispositivo_id) REFERENCES dispositivos(id_dispositivo) ON DELETE CASCADE
);