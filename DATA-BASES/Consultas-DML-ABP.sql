-- Consultas DML

-- INSERCIÓN DE DATOS

-- Usuarios
INSERT INTO usuarios (nombre_usuario, nombre, apellido, dni, es_admin, contrasena) VALUES
('admin',    'Admin',    'User',      '00000000',  TRUE,  'P@sw0rd!'),
('user',     'Usuario',  'Estandar',  '3456789',   FALSE, 'P@sw0rd!'),
('lucia',    'Lucía',    'Gómez',     '27894512',  FALSE, 'P@sw0rd!'),
('carlos',   'Carlos',   'Pérez',     '4012345',   FALSE, 'P@sw0rd!'),
('mariana',  'Mariana',  'Lopez',     '50123456',  TRUE,  'P@sw0rd!'),
('sofia',    'Sofía',    'Martínez',  '61234567',  FALSE, 'P@sw0rd!'),
('andres',   'Andrés',   'Fernández', '7234567',   FALSE, 'P@sw0rd!'),
('laura',    'Laura',    'Sosa',      '82345678',  FALSE, 'P@sw0rd!'),
('ricardo',  'Ricardo',  'Romero',    '9345678',   TRUE,  'P@sw0rd!'),
('julieta',  'Julieta',  'Benítez',   '1234567',   FALSE, 'P@sw0rd!');


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

--  Dispositivos que pertenecen al mismo tipo que en este caso 'Termostato'
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

