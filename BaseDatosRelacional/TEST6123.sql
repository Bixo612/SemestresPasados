--** PRUEBA 4 **--

CREATE TABLE Paises (
	Id_pais 	VARCHAR2 (3) NOT NULL PRIMARY KEY,
	Nombre_pais VARCHAR2(50) NOT NULL
);

INSERT INTO Paises VALUES ('CHI','Chile');
INSERT INTO Paises VALUES ('BRA','Brazil');
INSERT INTO Paises VALUES ('MEX','Mexico');
INSERT INTO Paises VALUES ('ESP','España');

CREATE TABLE Servidores (
	Id_sv 		INT NOT NULL PRIMARY KEY,
	Nombre_sv 	VARCHAR2(50) NOT NULL,
	Id_pais 	VARCHAR2 (3) NOT NULL,
	CONSTRAINTS Fk_servidores_pais FOREIGN KEY (Id_pais) REFERENCES pais(Id_pais)
);

INSERT INTO Servidores VALUES (10,'Santiago Sur','CHI');
INSERT INTO Servidores VALUES (11,'Puente Alto','CHI');
INSERT INTO Servidores VALUES (12,'CDMX','MEX');
INSERT INTO Servidores VALUES (14,'Madrid','ESP');
INSERT INTO Servidores VALUES (15,'Barcelona','ESP');
INSERT INTO Servidores VALUES (13,'Rio do Janeiro','BRA');

CREATE TABLE Usuarios (
	Id_user 			INT NOT NULL PRIMARY KEY,
	Nickname 			VARCHAR2 (50) NOT NULL UNIQUE,
	Primer_nombre 		VARCHAR2 (50) NOT NULL,
	Segundo_nombre 		VARCHAR2 (50),
	Primer_apellido 	VARCHAR2 (50) NOT NULL,
	Segundo_apellido	VARCHAR2 (50),
	Email 				VARCHAR2 (100) NOT NULL UNIQUE,
	Fecha_nacimiento 	DATE NOT NULL,
	Fecha_registro 		DATE NOT NULL,
	Id_pais 			VARCHAR2 (3) NOT NULL,
	CONSTRAINTS Fk_usuarios_pais FOREIGN KEY (Id_pais) REFERENCES pais(Id_pais)
);

INSERT INTO Usuarios VALUES (1,'BIXO612','VICENTE',NULL,'VASQUEZ',NULL,'vicente612@gmail.com','12-jun-96',sysdate-300,'CHI');
INSERT INTO Usuarios VALUES (2,'Strykez','Santiago',NULL,'Albornoz',NULL,'santiago745@gmail.com','22-jul-97',sysdate-250,'CHI');
INSERT INTO Usuarios VALUES (3,'GaboDark','Gabriel',NULL,'Gonzalez',NULL,'Gabriel1998@gmail.com','18-sep-98',sysdate-200,'BRA');
INSERT INTO Usuarios VALUES (4,'Calectini','Valen',NULL,'Diaz',NULL,'valen99@gmail.com','09-sep-99',sysdate-150,'MEX');
INSERT INTO Usuarios VALUES (5,'MsFia16','Sofia',NULL,'Soto',NULL,'sofia16@gmail.com','20-nov-00',sysdate-100,'ESP');

CREATE TABLE Moderadores (
	DNI_RUT			VARCHAR2 (20) NOT NULL PRIMARY KEY;
	Direccion		VARCHAR2 (150) NOT NULL,
	Nombre_banco	VARCHAR2 (100) NOT NULL,
	Tipo_cta		VARCHAR2 (25) NOT NULL,
	Cta_banco		VARCHAR2 (25) NOT NULL,
	Id_user 		INT NOT NULL
	CONSTRAINTS Fk_moderadores_usuarios FOREIGN KEY (Id_user) REFERENCES Usuarios(Id_user),
);

INSERT INTO Moderadores VALUES ('19945621-K','Isla guafo #8942','154684712','Cta Corriente','Banco Estado',1);
INSERT INTO Moderadores VALUES ('20007042-9','Ministro Carvajal #7770','154684712','Cta Corriente','Banco de Chile',2);

CREATE TABLE Videos (
	Id_video		INT NOT NULL PRIMARY KEY;
	Archivo 		VARCHAR2 (50),
	Nombre 			VARCHAR2 (50) NOT NULL,
	Id_user			INT NOT NULL,
	Fecha_subida	DATE NOT NULL,
	Visibilidad		VARCHAR2 (10) NOT NULL,
	Restriccion		VARCHAR2 (10) NOT NULL,
	Genero 			VARCHAR2 (20) NOT NULL,
	Me_gusta 		INT NOT NULL,
	No_me_gusta 	INT NOT NULL,
	Visitas 		INT NOT NULL,
	Id_sv 			INT NOT NULL,
	CONSTRAINTS Fk_videos_usuarios FOREIGN KEY (Id_user) REFERENCES Usuarios(Id_user),
	CONSTRAINTS Fk_videos_servidores FOREIGN KEY (Id_sv) REFERENCES Servidores(Id_sv),
);

INSERT INTO Videos VALUES (1,NULL,'Tutorial Ukulele',5,SYSDATE-10,'PBL','TE','Tutoriales',150,10,200);
INSERT INTO Videos VALUES (2,NULL,'Tutorial Bajo',5,SYSDATE-10,'PBL','TE','Tutoriales',200,10,200);
INSERT INTO Videos VALUES (3,NULL,'Gameplay Mortal Kombat 11',2,SYSDATE-9,'NLT','+18','Videojuegos',2,0,3);
INSERT INTO Videos VALUES (4,NULL,'Gameplay Mortal Kombat 11',2,SYSDATE-8,'PRV','+18','Videojuegos',2,0,3); 
INSERT INTO Videos VALUES (5,NULL,'Videos de gatos #1',1,SYSDATE-6,'PBL','TE','Animales',250,3,300);
INSERT INTO Videos VALUES (6,NULL,'Videos de gatos #2',1,SYSDATE-5,'PBL','TE','Animales',300,2,350);

CREATE TABLE Canciones (
	Id_video		INT NOT NULL PRIMARY KEY;
	Archivo 		VARCHAR2 (50),
	Titulo	 		VARCHAR2 (50) NOT NULL,
	Id_user			INT NOT NULL,
	Genero 			VARCHAR2 (20) NOT NULL,
	Reproducciones	INT NOT NULL,
	Id_sv 			INT NOT NULL,
	CONSTRAINTS Fk_canciones_usuarios FOREIGN KEY (Id_user) REFERENCES Usuarios(Id_user),
	CONSTRAINTS Fk_canciones_servidores FOREIGN KEY (Id_sv) REFERENCES Servidores(Id_sv),
);

INSERT INTO Canciones VALUES (1,NULL,'Take Five',4,'Ska',750);
INSERT INTO Canciones VALUES (2,NULL,'Skaravan',4,'Ska',600);
INSERT INTO Canciones VALUES (3,NULL,'Algun dia volveras',3,'Cumbia',1200)
INSERT INTO Canciones VALUES (4,NULL,'Amor de feria',3,'Cumbia',1500)
INSERT INTO Canciones VALUES (5,NULL,'Serenata cruel',3,'Cumbia',1400)
