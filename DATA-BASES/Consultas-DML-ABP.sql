-- Consultas DML

-- INSERCIÓN DE DATOS

-- Usuarios
INSERT INTO usuarios (dni, es_admin, nombre, apellido, contrasena) VALUES 
('1', TRUE, 'Admin', 'User', '1'),
('2', FALSE, 'Usuario', 'Estandar', '1234'),
('3', FALSE, 'Lucía', 'Gómez', 'abcd1234'),
('4', FALSE, 'Carlos', 'Pérez', 'pass456'),
('5', TRUE, 'Mariana', 'Lopez', 'admin123'),
('6', FALSE, 'Sofía', 'Martínez', 'sof456'),
('7', FALSE, 'Andrés', 'Fernández', 'andres1'),
('8', FALSE, 'Laura', 'Sosa', 'ls123'),
('9', TRUE, 'Ricardo', 'Romero', 'rradmin'),
('10', FALSE, 'Julieta', 'Benítez', 'jb789');

-- Tipos de dispositivos
INSERT INTO tipos_dispositivo (id_tipo, nombre) VALUES
(1, 'Lámpara Inteligente'),
(2, 'Termostato'),
(3, 'Cámara de Seguridad'),
(4, 'Sensor de Movimiento'),
(5, 'Aire Acondicionado'),
(6, 'Persiana Automática'),
(7, 'Televisor Inteligente'),
(8, 'Alarma Sonora'),
(9, 'Router WiFi'),
(10, 'Riego Automático');

-- Dispositivos
INSERT INTO dispositivos (id_tipo, ubicacion, marca, modelo, estado) VALUES
(1, 'Living', 'Philips', 'Hue', 'apagado'),
(2, 'Dormitorio', 'Google', 'Nest', 'encendido'),
(3, 'Cocina', 'Philips', 'Hue Mini', 'encendido'),
(4, 'Comedor', 'Google', 'Nest Therm', 'apagado'),
(5, 'Living', 'Xiaomi', 'Cam Pro', 'encendido'),
(6, 'Baño', 'Samsung', 'SensorX', 'apagado'),
(7, 'Garage', 'LG', 'SmartAC', 'apagado'),
(8, 'Patio', 'TP-Link', 'RouterX', 'encendido'),
(9, 'Dormitorio', 'Philips', 'Luz Ambi', 'apagado'),
(10, 'Jardín', 'Irrigreen', 'Spray2', 'encendido');

-- Automatizaciones
INSERT INTO automatizaciones (nombre, dias, hora, accion) VALUES
('Encender luces noche', 'LMMJVSD', '20:00:00', 'encender'),
('Apagar luces mañana', 'LMMJVSD', '07:00:00', 'apagar'),
('Activar alarma', 'LMMJVSD', '23:00:00', 'encender'),
('Desactivar alarma', 'LMMJVSD', '06:30:00', 'apagar'),
('Subir persianas', 'LMMJVSD', '08:00:00', 'subir'),
('Bajar persianas', 'LMMJVSD', '19:00:00', 'bajar'),
('Encender aire', 'LMMJVSD', '18:30:00', 'encender'),
('Regar jardín', 'LM--V--', '06:00:00', 'encender'),
('Encender TV', 'S-D----', '21:00:00', 'encender'),
('Apagar TV', 'S-D----', '23:30:00', 'apagar');

-- Automatización - Dispositivo
INSERT INTO automatizacion_dispositivo (automatizacion_id, dispositivo_id) VALUES
(1, 1),
(2, 1),
(3, 5),
(4, 5),
(5, 9),
(6, 9),
(7, 7),
(8, 10),
(9, 8),
(10, 8);

-- CONSULTAS SIMPLES

SELECT * FROM usuarios;
SELECT * FROM tipos_dispositivo;
SELECT * FROM dispositivos;
SELECT * FROM automatizaciones;
SELECT * FROM automatizacion_dispositivo;

-- CONSULTAS MULTITABLA

--  Dispositivos con su tipo
SELECT d.id_dispositivo, d.ubicacion, td.nombre AS tipo_dispositivo, d.estado
FROM dispositivos d
JOIN tipos_dispositivo td ON d.id_tipo = td.id_tipo;

--  Automatizaciones con los dispositivos asociados
SELECT a.nombre AS automatizacion, a.hora, d.ubicacion, td.nombre AS tipo_dispositivo, a.accion
FROM automatizaciones a
JOIN automatizacion_dispositivo ad ON a.id_automatizacion = ad.automatizacion_id
JOIN dispositivos d ON ad.dispositivo_id = d.id_dispositivo
JOIN tipos_dispositivo td ON d.id_tipo = td.id_tipo;

--  Cantidad de dispositivos por tipo
SELECT td.nombre AS tipo, COUNT(d.id_dispositivo) AS cantidad
FROM tipos_dispositivo td
LEFT JOIN dispositivos d ON td.id_tipo = d.id_tipo
GROUP BY td.nombre;

-- Automatizaciones programadas después de las 20:00
SELECT a.nombre AS automatizacion, a.hora, d.ubicacion, d.estado
FROM automatizaciones a
JOIN automatizacion_dispositivo ad ON a.id_automatizacion = ad.automatizacion_id
JOIN dispositivos d ON ad.dispositivo_id = d.id_dispositivo
WHERE a.hora > '20:00:00';

-- SUBCONSULTAS

--  Dispositivos que pertenecen al mismo tipo que el 'Termostato'
SELECT * FROM dispositivos
WHERE id_tipo = (
    SELECT id_tipo FROM tipos_dispositivo WHERE nombre = 'Termostato'
);

--  Dispositivos que no están en ninguna automatización
SELECT id_dispositivo, marca, ubicacion
FROM dispositivos
WHERE id_dispositivo NOT IN (
    SELECT dispositivo_id
    FROM automatizacion_dispositivo
);

