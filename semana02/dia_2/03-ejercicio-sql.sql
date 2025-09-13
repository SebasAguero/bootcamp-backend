-- Crear una base de datos llamada colegio
CREATE DATABASE colegio;
\c colegio

-- En la base de datos crear una tabla llamada profesores que va a tener la sgte info
-- id serial llave primaria
-- nombre texto no puede ser nulo
-- apellidos texto no puede ser nulo
-- correo texto unico
-- correo_institucional texto unico
-- activo boolean 
-- fecha_contratacion timestamp
CREATE TABLE colegio (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    correo TEXT UNIQUE,
    correo_institucional TEXT UNIQUE,
    activo BOOLEAN,
    fecha_contratacion TIMESTAMP
);

-- Para cambiar el nombre de la tabla de colegio a profesores
ALTER TABLE colegio RENAME TO profesores;