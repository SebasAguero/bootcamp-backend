SELECT * 
FROM profesores LEFT JOIN direcciones  -- LEFT JOIN devolvera todo lo de la izq y si tiene alguna relacion con la derecha
        ON profesores.id = direcciones.profesor_id;


-- Sirve para cambiar la visualizacion en formato de tabla a un formato de tarjetas
\x


-- Todos los profesores y si tienen direcciones tambien y sino, tambien
SELECT * 
FROM profesores AS prof LEFT JOIN direcciones AS dir
        ON prof.id = dir.profesor_id
ORDER BY prof.id ASC;


INSERT INTO direcciones (id, calle, numero, referencia, distrito, provincia, profesor_id) VALUES 
                        (DEFAULT, 'Los tulipanes', '120A', 'A dos cuadras de la cancha sintetica', 'Jesus Maria', 'Lima', null),
                        (DEFAULT, 'Los Jazmines', '1040A', null, 'Manuel Pastor', 'Moquegua', null),
                        (DEFAULT, 'Los Rosales', '2050A', 'Al frente del tambo', 'Cayma', 'Arequipa', null);


-- Todas las direcciones aun asi no tengan profesores asociados
SELECT * 
FROM profesores AS prof RIGHT JOIN direcciones AS dir
        ON prof.id = dir.profesor_id
ORDER BY dir.profesor_id DESC;


-- Esto devolvera todos los registros de los profesores aun asi no tengan direcciones asociadas y todas las direcciones aun asi no tengan profesores asociados
SELECT *
FROM profesores AS prof FULL OUTER JOIN direcciones AS dir
        ON prof.id = dir.profesor_id;




-- 1. Mostrar los nombres de los profesores que vivan en Jesus Maria o Lima
SELECT DISTINCT prof.nombre FROM profesores AS prof INNER JOIN direcciones dir ON prof.id = dir.profesor_id
WHERE dir.distrito IN ('Jesus Maria', 'Lima');


SELECT prof.nombre FROM profesores AS prof WHERE prof.id IN (SELECT profesor_id FROM direcciones WHERE distrito IN ('Jesus Maria', 'Lima'));

-- En ambas queries ya bien sea usando el join con distinct o la subquery para devolver los id, la query mas optima en este caso es casi la misma entre las dos


-- 2. Mostrar los correos de los profesores que vivan en el distrito de Trujillo y la provincia de  Cajabamba
SELECT prof.correo FROM profesores AS prof INNER JOIN direcciones dir ON prof.id = dir.profesor_id WHERE dir.distrito = 'Trujillo' AND dir.provincia = 'Cajabamba';


-- 3. Contar todos los profesores que tengan direcciones
  SELECT COUNT(DISTINCT prof.id) 
  FROM profesores AS prof INNER JOIN direcciones dir ON prof.id = dir.profesor_id;

-- Sin hacer uso del inner join podemos utilizar el count en la columna profesor_id usando la clausula DISTINCT para que solo cuente una sola vez cada profesor_id 
SELECT COUNT(DISTINCT profesor_id ) FROM direcciones;

-- 4. Contar todos los profesores que tengan 2 o mas direcciones
SELECT COUNT(*) 
FROM (
    SELECT prof.id 
    FROM profesores AS prof INNER JOIN direcciones AS dir ON prof.id = dir.profesor_id
    -- En la clausula WHERE no se pueden utilizar funciones de agregacion, cuando queremos usar condicionales con funciones de agregacion tenemos que usar la clausula HAVING
    GROUP BY prof.id
    -- El HAVING va despues del group by y si se puede utilizar el having y el where en la misma consulta
    HAVING COUNT(dir.id) >= 2
);


-- 5. Contar todos los profesores que no tengan direcciones asociadas
SELECT COUNT(*) 
FROM profesores AS prof LEFT JOIN direcciones AS dir 
        ON prof.id = dir.profesor_id WHERE dir.id IS NULL;