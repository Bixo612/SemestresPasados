
CREATE TABLE Pais (
	Id_pais INT NOT NULL PRIMARY KEY,
	Nombre_pais VARCHAR2(50) NOT NULL
);

INSERT INTO Pais VALUES (101,'Chile');
INSERT INTO Pais VALUES (102,'Brazil');
INSERT INTO Pais VALUES (103,'Mexico');
INSERT INTO Pais VALUES (104,'España');

select * from pais;

CREATE TABLE Servidores (
	Id_sv INT NOT NULL PRIMARY KEY,
	Nombre_sv VARCHAR2(50) NOT NULL,
	Id_pais INT NOT NULL,
	CONSTRAINTS Fk_servidores_pais FOREIGN KEY (Id_pais) REFERENCES pais(Id_pais)
);

drop table servidores;

select * from servidores;

INSERT INTO Servidores VALUES (10,'Santiago Sur',101);
INSERT INTO Servidores VALUES (11,'Puente Alto',101);
INSERT INTO Servidores VALUES (12,'CDMX',103);
INSERT INTO Servidores VALUES (14,'Madrid',104);
INSERT INTO Servidores VALUES (15,'Barcelona',104);
INSERT INTO Servidores VALUES (13,'Rio do Janeiro',102);

 

