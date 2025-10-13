-- Consulta 1
SELECT H.Nombre_Hogar, A.Nombre_Ambiente, TD.Nombre_Tipo, D.Marca, D.Modelo, D.Estado
FROM Dispositivos D
JOIN Tipos_Dispositivos TD ON D.Id_Tipo = TD.Id_Tipo
JOIN Ambientes A ON D.Id_Ambiente = A.Id_Ambiente
JOIN Hogares H ON A.Id_Hogar = H.Id_Hogar;

-- Consulta 2
SELECT U.Nombre, U.Apellido, R.Nombre AS Rol, H.Nombre_Hogar
FROM Usuarios U
JOIN Roles R ON U.Id_Rol = R.Id_Rol
JOIN UsuariosxHogares UH ON U.DNI = UH.DNI
JOIN Hogares H ON UH.Id_Hogar = H.Id_Hogar
WHERE H.Nombre_Hogar = 'Casa Principal';

-- Consulta 3
SELECT A.Nombre AS Automatizacion, TD.Nombre_Tipo, D.Marca, D.Estado
FROM Automatizaciones A
JOIN Automatizaciones_Dispositivos AD ON A.Id_Automatizacion = AD.Id_Automatizacion
JOIN Dispositivos D ON AD.MAC_Dispositivo = D.MAC
JOIN Tipos_Dispositivos TD ON D.Id_Tipo = TD.Id_Tipo;

-- Consulta 4
SELECT DISTINCT H.Nombre_Hogar, A.Nombre_Ambiente
FROM Ambientes A
JOIN Hogares H ON A.Id_Hogar = H.Id_Hogar
JOIN Dispositivos D ON A.Id_Ambiente = D.Id_Ambiente
WHERE D.Id_Tipo = 2;

-- Subconsulta 1
SELECT Nombre_Hogar
FROM Hogares
WHERE Id_Hogar IN (
    SELECT DISTINCT Id_Hogar FROM Automatizaciones
);

-- Subconsulta 2
SELECT DNI, Nombre, Apellido
FROM Usuarios
WHERE Id_Rol = (
    SELECT Id_Rol FROM Roles WHERE Nombre = 'Administrador'
);