-- Cuando queremos actualizar informacion de alguna tabla , SIEMPRE COLOCAR UNA CONDICION
-- Siempre se recomienda que en el WHERE colocar columnas unicas para evitar actualizacion masiva
UPDATE personas SET nombre = 'Ramiro', apellido = 'de Rivero' WHERE correo ='ederiveroman@gmail.com';

-- Adicional al CREAR , ACTUALIZAR o ELIMINAR si queremos ver el resultado de la operacion podemos, al final de todo, agregar RETURNING y las columnas que queremos ver (* si queremos ver todas)
UPDATE personas SET nombre = 'Ramiro', apellido = 'de Rivero' WHERE correo ='ederiveroman@gmail.com' RETURNING *;

-- Cuando queremos eliminar la informacion de manera PERMANTE 
DELETE FROM personas WHERE id = 6 RETURNING *;