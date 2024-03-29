--** PRUEBA 4 **--
drop table  videos CASCADE CONSTRAINTS;

CREATE TABLE Pais (
	Id_pais INT NOT NULL PRIMARY KEY,
	Nombre_pais VARCHAR2(50) NOT NULL
);

CREATE TABLE Servidores (
	Id_sv INT NOT NULL PRIMARY KEY,
	Nombre_sv VARCHAR2(50) NOT NULL,
	Id_pais INT NOT NULL,
	CONSTRAINTS Fk_servidores_pais FOREIGN KEY (Id_pais) REFERENCES pais(Id_pais)
);

CREATE TABLE Usuarios (
	Nickname VARCHAR2 (50) NOT NULL UNIQUE,
	Id_user INT NOT NULL PRIMARY KEY,
	Primer_nombre VARCHAR2 (50) NOT NULL,
	Segundo_nombre VARCHAR2 (50),
	Primer_apellido VARCHAR2 (50) NOT NULL,
	Segundo_apellido VARCHAR2 (50),
	Email VARCHAR2 (50) NOT NULL,
	Fecha_nacimiento DATE NOT NULL,
	Fecha_registro DATE NOT NULL,
	Id_pais INT NOT NULL,
	CONSTRAINTS Fk_usuarios_pais FOREIGN KEY (Id_pais) REFERENCES pais(Id_pais)
);

CREATE TABLE Visibilidades (
	Id_visibilidad VARCHAR2 (3) NOT NULL PRIMARY KEY,
	Visibilidad VARCHAR2 (100) NOT NULL UNIQUE
);

CREATE TABLE Restricciones (
	Id_Restriccion VARCHAR2 (3) NOT NULL PRIMARY KEY,
	Restriccion VARCHAR2 (100) NOT NULL UNIQUE
);
 
CREATE TABLE Videos (
	Archivo 		VARCHAR2 (50),
	Nombre 			VARCHAR2 (50) NOT NULL,
	Id_user			INT NOT NULL,
	Fecha_subida	DATE NOT NULL,
	Visibilidad		VARCHAR2 (3) NOT NULL,
	Restriccion		VARCHAR2 (3) NOT NULL,
	Genero 			VARCHAR2 (20) NOT NULL,
	Me_gusta 		INT NOT NULL,
	No_me_gusta 	INT NOT NULL,
	Visitas 		INT NOT NULL,
	CONSTRAINTS Fk_videos_usuarios FOREIGN KEY (Id_user) REFERENCES Usuarios(Id_user),
	CONSTRAINTS Fk_videos_visibilidad FOREIGN KEY (Visibilidad) REFERENCES Visibilidades(Id_visibilidad),
	CONSTRAINTS Fk_videos_restriccion FOREIGN KEY (Restriccion) REFERENCES Restricciones(Id_Restriccion)
);

CREATE TABLE Canciones (
	Archivo 		VARCHAR2 (50),
	Titulo	 		VARCHAR2 (50) NOT NULL,
	Id_user			INT NOT NULL,
	Genero 			VARCHAR2 (20) NOT NULL,
	Reproducciones	INT NOT NULL,
	CONSTRAINTS Fk_canciones_usuarios FOREIGN KEY (Id_user) REFERENCES Usuarios(Id_user)
);

/*	UNIQUE elemento unico
	SYSDATE ingresar la fecha del sistema de ahora ya XD*/

--** DATOS **--

INSERT INTO Pais VALUES (101,'Chile');
INSERT INTO Pais VALUES (102,'Brazil');
INSERT INTO Pais VALUES (103,'Mexico');
INSERT INTO Pais VALUES (104,'Espa�a');

INSERT INTO Servidores VALUES (10,'Santiago Sur',101);
INSERT INTO Servidores VALUES (11,'Puente Alto',101);
INSERT INTO Servidores VALUES (12,'CDMX',103);
INSERT INTO Servidores VALUES (14,'Madrid',104);
INSERT INTO Servidores VALUES (15,'Barcelona',104);
INSERT INTO Servidores VALUES (13,'Rio do Janeiro',102);

INSERT INTO Usuarios VALUES ('Bixo612',1,'Vicente',NULL,'Vasquez',NULL,'vicente612@gmail.com','12-jun-96',sysdate-300,101);
INSERT INTO Usuarios VALUES ('Strykez',2,'Santiago',NULL,'Albornoz',NULL,'santiago745@gmail.com','22-jul-97',sysdate-250,101);
INSERT INTO Usuarios VALUES ('GaboDark',3,'Gabriel',NULL,'Gonzalez',NULL,'Gabriel1998@gmail.com','18-sep-98',sysdate-200,102);
INSERT INTO Usuarios VALUES ('Calectini',4,'Valen',NULL,'Diaz',NULL,'valen99@gmail.com','09-sep-99',sysdate-150,103);
INSERT INTO Usuarios VALUES ('MsFia16',5,'Sofia',NULL,'Soto',NULL,'sofia16@gmail.com','20-nov-00',sysdate-100,104);

INSERT INTO Visibilidades VALUES ('PBL','Publico');
INSERT INTO Visibilidades VALUES ('PRV','Privado');
INSERT INTO Visibilidades VALUES ('NLT','No Listado');

INSERT INTO Restricciones VALUES ('TE','Todo espectador');
INSERT INTO Restricciones VALUES ('+18','Mayores de edad');

INSERT INTO Videos VALUES (NULL,'Tutorial Ukulele',5,SYSDATE-10,'PBL','TE','Tutoriales',150,10,200);
INSERT INTO Videos VALUES (NULL,'Tutorial Bajo',5,SYSDATE-10,'PBL','TE','Tutoriales',200,10,200);
INSERT INTO Videos VALUES (NULL,'Tutorial Guitarra',5,SYSDATE-10,'PBL','TE','Tutoriales',250,10,300);
INSERT INTO Videos VALUES (NULL,'Gameplay Mortal Kombat 11',2,SYSDATE-9,'NLT','+18','Videojuegos',2,0,3);
INSERT INTO Videos VALUES (NULL,'Gameplay Mortal Kombat 11',2,SYSDATE-8,'PRV','+18','Videojuegos',2,0,3); 
INSERT INTO Videos VALUES (NULL,'Videos de gatos #1',1,SYSDATE-6,'PBL','TE','Animales',250,3,300);
INSERT INTO Videos VALUES (NULL,'Videos de gatos #2',1,SYSDATE-5,'PBL','TE','Animales',300,2,350);
INSERT INTO Videos VALUES (NULL,'Videos de gatos #3',1,SYSDATE-4,'PBL','TE','Animales',350,1,400);
INSERT INTO Videos VALUES (NULL,'Videos de gatos #4',1,SYSDATE-3,'PBL','TE','Animales',400,0,450);

INSERT INTO Canciones VALUES (NULL,'Take Five',4,'Ska',750);
INSERT INTO Canciones VALUES (NULL,'Skaravan',4,'Ska',600);
INSERT INTO Canciones VALUES (NULL,'Algun dia volveras',3,'Cumbia',1200);
INSERT INTO Canciones VALUES (NULL,'Amor de feria',3,'Cumbia',1500);
INSERT INTO Canciones VALUES (NULL,'Serenata cruel',3,'Cumbia',1400);

select * from pais;
select * from servidores;
select * from usuarios;
select * from visibilidades;
select * from videos;
select * from canciones;

desc videos;

select * from videos;

select count(id_user),id_user
from videos
group by id_user;



