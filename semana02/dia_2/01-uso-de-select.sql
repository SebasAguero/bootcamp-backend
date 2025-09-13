-- Los selects es la forma en la cual podemos obtener la informacion

-- LIKE : se usa para obtener similitudes por una parte del texto
SELECT * FROM personas WHERE nombre LIKE '%ardo%';



INSERT INTO personas (nombre, apellido, correo, fecha_nacimiento) VALUES
                     ('Ardonesio', null, 'ardoni@gmail.com', '1992-09-01');


-- ILIKE: sera como un like pero insensible a mayus y minus en el texto a buscar
SELECT * FROM personas WHERE nombre ILIKE '%ardo%'; -- ARDO | ardo | aRdO | ArDo | Ardo 

-- Mostrar todas las peronas que tengan correos gmail o outlook
SELECT * FROM personas WHERE correo LIKE '%gmail.com' OR correo LIKE '%outlook.com';
 

-- Si queremos hacer la busqueda de varios elementos de una misma columna pero por una busqueda exacta
SELECT * FROM personas WHERE nombre IN ('Eduardo', 'Luis');

SELECT * FROM personas WHERE id IN (2, 4, 5);

-- Si al usar el like o ilike se desea ver en que posicion exacta esta el valor a buscar se usa _
SELECT * FROM personas WHERE apellido ILIKE '__m%';

