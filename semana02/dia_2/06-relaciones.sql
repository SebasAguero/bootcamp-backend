CREATE TABLE direcciones (
    id SERIAL PRIMARY KEY,
    calle TEXT NOT NULL,
    numero TEXT,
    referencia TEXT,
    distrito TEXT,
    provincia TEXT,
    profesor_id INT,
    -- Aca vinculamos la direccion con el profesor
    FOREIGN KEY (profesor_id) REFERENCES profesores(id)
);