CREATE TABLE funcionarios_municipales (
    rut                VARCHAR2(12) NOT NULL,
    primer_nombre      VARCHAR2(20) NOT NULL,
    segundo_nombre     VARCHAR2(20),
    primer_apellido    VARCHAR2(20) NOT NULL,
    segundo_apellido   VARCHAR2(20),
    sexo               VARCHAR2(1) NOT NULL,
    correo_electronico VARCHAR2(100) NOT NULL,
    fecha_nacimiento   DATE NOT NULL,
    telefono           VARCHAR2(15) NOT NULL,
    municipalidad      INTEGER NOT NULL
);

ALTER TABLE funcionarios_municipales ADD CONSTRAINT funcionario_municipal_pk PRIMARY KEY ( rut );

CREATE TABLE inspectores (
    id_inspector  INTEGER NOT NULL,
    fecha_ingreso DATE NOT NULL,
    rut_inspector VARCHAR2(12) NOT NULL
);

ALTER TABLE inspectores ADD CONSTRAINT inspector_pk PRIMARY KEY ( id_inspector );

CREATE TABLE juzgados_policia_local (
    id_juzgado     INTEGER NOT NULL,
    nombre_juzgado VARCHAR2(50) NOT NULL,
    municipalidad  INTEGER NOT NULL
);

ALTER TABLE juzgados_policia_local ADD CONSTRAINT juzgado_policia_local_pk PRIMARY KEY ( id_juzgado );

CREATE TABLE log_multas (
    id_log  INTEGER NOT NULL,
    accion  VARCHAR2(15) NOT NULL,
    fecha   DATE,
    usuario VARCHAR2(30) NOT NULL
);

ALTER TABLE log_multas ADD CONSTRAINT log_multas_pk PRIMARY KEY ( id_log );

CREATE TABLE multas (
    nro_multa             INTEGER NOT NULL,
    direccion_infraccion  VARCHAR2(100) NOT NULL,
    fecha_infraccion      DATE NOT NULL,
    motivo_infraccion     VARCHAR2(100) NOT NULL,
    valor_infraccion      INTEGER NOT NULL,
    patente_infractora    VARCHAR2(6) NOT NULL,
    inspector_observador  INTEGER NOT NULL,
    juzgado_comparecencia INTEGER NOT NULL
);

ALTER TABLE multas ADD CONSTRAINT multa_pk PRIMARY KEY ( nro_multa );

CREATE TABLE municipalidades (
    id_municipalidad INTEGER NOT NULL,
    comuna           VARCHAR2(70) NOT NULL
);

ALTER TABLE municipalidades ADD CONSTRAINT municipalidad_pk PRIMARY KEY ( id_municipalidad );

CREATE TABLE vehiculos (
    placa_patente VARCHAR2(6) NOT NULL,
    marca         VARCHAR2(20) NOT NULL,
    modelo        VARCHAR2(20) NOT NULL
);

ALTER TABLE vehiculos ADD CONSTRAINT vehiculo_pk PRIMARY KEY ( placa_patente );

ALTER TABLE funcionarios_municipales
    ADD CONSTRAINT fk_funcionario_municipalidad FOREIGN KEY ( municipalidad )
        REFERENCES municipalidades ( id_municipalidad );

ALTER TABLE inspectores
    ADD CONSTRAINT fk_inspector_funcionario FOREIGN KEY ( rut_inspector )
        REFERENCES funcionarios_municipales ( rut );

ALTER TABLE multas
    ADD CONSTRAINT fk_multa_inspector FOREIGN KEY ( inspector_observador )
        REFERENCES inspectores ( id_inspector );

ALTER TABLE multas
    ADD CONSTRAINT fk_multa_juzgado FOREIGN KEY ( juzgado_comparecencia )
        REFERENCES juzgados_policia_local ( id_juzgado );

ALTER TABLE multas
    ADD CONSTRAINT fk_multa_vehiculo FOREIGN KEY ( patente_infractora )
        REFERENCES vehiculos ( placa_patente );

ALTER TABLE juzgados_policia_local
    ADD CONSTRAINT fk_municipalidad_juzgado FOREIGN KEY ( municipalidad )
        REFERENCES municipalidades ( id_municipalidad );


CREATE VIEW vista_temporal AS SELECT * FROM MUNICIPALIDADES;

CREATE VIEW vista_provisoria AS SELECT * FROM MULTAS;

CREATE VIEW vista_momentanea AS SELECT * FROM INSPECTORES;
