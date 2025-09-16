-- CONSULTAS DML

-- Roles (2)
INSERT INTO Roles VALUES (1, 'Administrador');
INSERT INTO Roles VALUES (2, 'Usuario');

-- Usuarios (10)
INSERT INTO Usuarios VALUES (11111111, 1, 'Juan', 'Pérez', '1234');
INSERT INTO Usuarios VALUES (22222222, 2, 'Ana', 'López', 'abcd');
INSERT INTO Usuarios VALUES (33333333, 2, 'Carlos', 'Gómez', 'pass1');
INSERT INTO Usuarios VALUES (44444444, 2, 'Lucía', 'Martínez', 'guest');
INSERT INTO Usuarios VALUES (55555555, 2, 'Pedro', 'Suárez', 'tech123');
INSERT INTO Usuarios VALUES (66666666, 1, 'María', 'Fernández', 'super');
INSERT INTO Usuarios VALUES (77777777, 2, 'Julián', 'Rodríguez', 'julio');
INSERT INTO Usuarios VALUES (88888888, 2, 'Valeria', 'Díaz', 'vale');
INSERT INTO Usuarios VALUES (99999999, 2, 'Sofía', 'Ruiz', 'sofi');
INSERT INTO Usuarios VALUES (10101010, 1, 'Diego', 'Alonso', 'dieguito');

-- Hogares (5)
INSERT INTO Hogares VALUES (1, 'Av. Siempre Viva 742', 'Casa Principal');
INSERT INTO Hogares VALUES (2, 'Calle Falsa 123', 'Departamento Centro');
INSERT INTO Hogares VALUES (3, 'Ruta 9 Km 50', 'Casa Quinta');
INSERT INTO Hogares VALUES (4, 'San Martín 555', 'Oficina');
INSERT INTO Hogares VALUES (5, 'Belgrano 321', 'Casa Playa');

-- UsuariosxHogares (10)
INSERT INTO UsuariosxHogares VALUES (11111111, 1);
INSERT INTO UsuariosxHogares VALUES (22222222, 1);
INSERT INTO UsuariosxHogares VALUES (33333333, 2);
INSERT INTO UsuariosxHogares VALUES (44444444, 3);
INSERT INTO UsuariosxHogares VALUES (55555555, 4);
INSERT INTO UsuariosxHogares VALUES (66666666, 5);
INSERT INTO UsuariosxHogares VALUES (77777777, 2);
INSERT INTO UsuariosxHogares VALUES (88888888, 3);
INSERT INTO UsuariosxHogares VALUES (99999999, 4);
INSERT INTO UsuariosxHogares VALUES (10101010, 5);

-- Ambientes (10)
INSERT INTO Ambientes VALUES (1, 1, 'Living');
INSERT INTO Ambientes VALUES (2, 1, 'Dormitorio');
INSERT INTO Ambientes VALUES (3, 2, 'Cocina');
INSERT INTO Ambientes VALUES (4, 2, 'Baño');
INSERT INTO Ambientes VALUES (5, 3, 'Jardín');
INSERT INTO Ambientes VALUES (6, 3, 'Garage');
INSERT INTO Ambientes VALUES (7, 4, 'Oficina 1');
INSERT INTO Ambientes VALUES (8, 4, 'Oficina 2');
INSERT INTO Ambientes VALUES (9, 5, 'Terraza');
INSERT INTO Ambientes VALUES (10, 5, 'Habitación principal');

-- Tipos de Dispositivos (10)
INSERT INTO Tipos_Dispositivos VALUES (1, 'Luz');
INSERT INTO Tipos_Dispositivos VALUES (2, 'Cámara');
INSERT INTO Tipos_Dispositivos VALUES (3, 'Sensor de movimiento');
INSERT INTO Tipos_Dispositivos VALUES (4, 'Termostato');
INSERT INTO Tipos_Dispositivos VALUES (5, 'Aire acondicionado');
INSERT INTO Tipos_Dispositivos VALUES (6, 'Persiana eléctrica');
INSERT INTO Tipos_Dispositivos VALUES (7, 'TV');
INSERT INTO Tipos_Dispositivos VALUES (8, 'Altavoz inteligente');
INSERT INTO Tipos_Dispositivos VALUES (9, 'Puerta eléctrica');
INSERT INTO Tipos_Dispositivos VALUES (10, 'Proyector');

-- Dispositivos (10)
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B1', 1, 'Philips', 'Hue123', 0);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B2', 2, 'Logitech', 'CamPro', 1);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B3', 3, 'Xiaomi', 'MiSensor', 0);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B4', 4, 'Nest', 'ThermoX', 1);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B5', 5, 'Samsung', 'AirMax', 0);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B6', 6, 'Somfy', 'PersiaX', 1);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B7', 7, 'Sony', 'Bravia55', 0);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B8', 8, 'Amazon', 'EchoDot', 1);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:B9', 9, 'Chamberlain', 'DoorPro', 0);
INSERT INTO Dispositivos VALUES ('00:1B:44:11:3A:BA', 10, 'Epson', 'ProyX', 1);

-- Automatizaciones (5)
INSERT INTO Automatizaciones VALUES (1, 1, 'Encender luces noche', 'Lunes,Martes,Miercoles', '21:00:00', 'Encender');
INSERT INTO Automatizaciones VALUES (2, 2, 'Apagar TV madrugada', 'Todos', '01:00:00', 'Apagar');
INSERT INTO Automatizaciones VALUES (3, 3, 'Encender aire tarde', 'Viernes', '19:00:00', 'Encender');
INSERT INTO Automatizaciones VALUES (4, 4, 'Subir persianas mañana', 'Lunes a Viernes', '08:00:00', 'Subir');
INSERT INTO Automatizaciones VALUES (5, 5, 'Proyector cine', 'Sábado', '22:00:00', 'Encender');

-- Automatizaciones_Dispositivos (10)
INSERT INTO Automatizaciones_Dispositivos VALUES (1, '00:1B:44:11:3A:B1');
INSERT INTO Automatizaciones_Dispositivos VALUES (1, '00:1B:44:11:3A:B2');
INSERT INTO Automatizaciones_Dispositivos VALUES (2, '00:1B:44:11:3A:B7');
INSERT INTO Automatizaciones_Dispositivos VALUES (3, '00:1B:44:11:3A:B5');
INSERT INTO Automatizaciones_Dispositivos VALUES (4, '00:1B:44:11:3A:B6');
INSERT INTO Automatizaciones_Dispositivos VALUES (5, '00:1B:44:11:3A:BA');
INSERT INTO Automatizaciones_Dispositivos VALUES (2, '00:1B:44:11:3A:B8');
INSERT INTO Automatizaciones_Dispositivos VALUES (3, '00:1B:44:11:3A:B9');
INSERT INTO Automatizaciones_Dispositivos VALUES (4, '00:1B:44:11:3A:B3');
INSERT INTO Automatizaciones_Dispositivos VALUES (5, '00:1B:44:11:3A:B4');

-- CONSULTAS DE PRUEBA

-- Usuarios con su Rol
SELECT U.Nombre, U.Apellido, R.Nombre AS Rol
FROM Usuarios U
JOIN Roles R ON U.Id_Rol = R.Id_Rol;

-- Dispositivos vinculados a automatizaciones
SELECT A.Nombre AS Automatizacion, D.Marca, D.Modelo, T.Nombre AS Tipo
FROM Automatizaciones A
JOIN Automatizaciones_Dispositivos AD ON A.Id_Automatizacion = AD.Id_Automatizacion
JOIN Dispositivos D ON AD.MAC_Dispositivo = D.MAC
JOIN Tipos_Dispositivos T ON D.Id_Tipo = T.Id_Tipo;