USE corporacion_gbs;
-- MYSQL


-- Estructura de tabla para la tabla `expediente`
CREATE TABLE expediente (
    id INT NOT NULL AUTO_INCREMENT,
    tipo_caso VARCHAR(255),
    c_expediente VARCHAR(255),
    escribe_su_caso TEXT,
    archivo_adjunto VARCHAR(255),
    cliente_id INT,
    area VARCHAR(255),
    enfoque VARCHAR(255),
    abogado_id INT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

--Volcado de datos para la tabla `expediente`

INSERT INTO expediente (id, tipo_caso, c_expediente, escribe_su_caso, archivo_adjunto, cliente_id, area, enfoque, abogado_id, created_at) VALUES (6, "familiar", "JUZ-2022-022545", "violencia animal", "", 20, "penal", "derechos", 21, "2023-03-08 03:50:23");
