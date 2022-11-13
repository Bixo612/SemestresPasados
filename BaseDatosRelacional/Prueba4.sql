CREATE TABLE Paises (
	Id_pais 	VARCHAR2 (3) NOT NULL PRIMARY KEY,
	Nombre_pais VARCHAR2(50) NOT NULL
);

CREATE TABLE Servidores (
	Id_sv 		INT NOT NULL PRIMARY KEY,
	Nombre_sv 	VARCHAR2(50) NOT NULL,
	Id_pais 	VARCHAR2 (3) NOT NULL,
	CONSTRAINTS Fk_servidores_pais FOREIGN KEY (Id_pais) REFERENCES paises(Id_pais)
);

CREATE TABLE Usuarios (
	Nickname 			VARCHAR2 (50) NOT NULL UNIQUE,
    Id_user 			INT NOT NULL PRIMARY KEY,
	Primer_nombre 		VARCHAR2 (50) NOT NULL,
	Segundo_nombre 		VARCHAR2 (50),
	Primer_apellido 	VARCHAR2 (50) NOT NULL,
	Segundo_apellido	VARCHAR2 (50),
	Email 				VARCHAR2 (100) NOT NULL UNIQUE,
	Fecha_nacimiento 	DATE NOT NULL,
	Fecha_registro 		DATE NOT NULL,
	Id_pais 			VARCHAR2 (3) NOT NULL,
	CONSTRAINTS Fk_usuarios_pais FOREIGN KEY (Id_pais) REFERENCES paises(Id_pais)
);

CREATE TABLE Moderadores (
	DNI_RUT			VARCHAR2 (20) NOT NULL PRIMARY KEY,
	Direccion		VARCHAR2 (200) NOT NULL,
	Cta_banco		VARCHAR2 (25) NOT NULL,
	Tipo_cta		VARCHAR2 (25) NOT NULL,
	Nombre_banco	VARCHAR2 (100) NOT NULL,
	Id_user 		INT NOT NULL UNIQUE,
	CONSTRAINTS Fk_moderadores_usuarios FOREIGN KEY (Id_user) REFERENCES Usuarios(Id_user)
);

CREATE TABLE Videos (
	Id_video		INT NOT NULL PRIMARY KEY,
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
	CONSTRAINTS Fk_videos_servidores FOREIGN KEY (Id_sv) REFERENCES Servidores(Id_sv)
);

CREATE TABLE Canciones (
	Id_cancion		INT NOT NULL PRIMARY KEY,
	Archivo 		VARCHAR2 (50),
	Titulo	 		VARCHAR2 (50) NOT NULL,
	Id_user			INT NOT NULL,
	Genero 			VARCHAR2 (20) NOT NULL,
	Reproducciones	INT NOT NULL,
	Id_sv 			INT NOT NULL,
	CONSTRAINTS Fk_canciones_usuarios FOREIGN KEY (Id_user) REFERENCES Usuarios(Id_user),
	CONSTRAINTS Fk_canciones_servidores FOREIGN KEY (Id_sv) REFERENCES Servidores(Id_sv)
);

-------------------------------------------------------------------------------
INSERT INTO Paises VALUES ('CHI','Chile');
INSERT INTO Paises VALUES ('BRA','Brasil');
INSERT INTO Paises VALUES ('MEX','Mexico');
INSERT INTO Paises VALUES ('ESP','España');
INSERT INTO Paises VALUES ('ARG','Argentina');
INSERT INTO Paises VALUES ('PER','Peru');
INSERT INTO Paises VALUES ('FRA','Francia');
INSERT INTO Paises VALUES ('ESP','España');
INSERT INTO Paises VALUES ('ITA','Italia');
INSERT INTO Paises VALUES ('ALE','Alemania');
INSERT INTO Paises VALUES ('RUS','Rusia');
INSERT INTO Paises VALUES ('FIN','Finlandia');
INSERT INTO Paises VALUES ('SUE','Suecia');
INSERT INTO Paises VALUES ('AUS','Australia');
INSERT INTO Paises VALUES ('JAP','Japon');
INSERT INTO Paises VALUES ('CHN','China');
INSERT INTO Paises VALUES ('CAN','Canada');
INSERT INTO Paises VALUES ('EUA','Estados Unidos');
INSERT INTO Paises VALUES ('COR','Corea del sur');
INSERT INTO Paises VALUES ('GBR','Reino Unido');
-------------------------------------------------------------------------------
INSERT INTO Servidores VALUES (11,'Santiago','CHI');
INSERT INTO Servidores VALUES (13,'Rio de Janeiro','BRA');
INSERT INTO Servidores VALUES (12,'CDMX','MEX');
INSERT INTO Servidores VALUES (14,'Madrid','ESP');
INSERT INTO Servidores VALUES (15,'Barcelona','ESP');
INSERT INTO Servidores VALUES (16,'Buenos aires','ARG');
INSERT INTO Servidores VALUES (17,'Lima','PER');
INSERT INTO Servidores VALUES (18,'Paris','FRA');
INSERT INTO Servidores VALUES (19,'Roma','ITA');
INSERT INTO Servidores VALUES (20,'Berlin','ALE');
INSERT INTO Servidores VALUES (21,'Moscu','RUS');
INSERT INTO Servidores VALUES (22,'Helsinki','FIN');
INSERT INTO Servidores VALUES (23,'Estocolmo','SUE');
INSERT INTO Servidores VALUES (24,'Sydney','AUS');
INSERT INTO Servidores VALUES (25,'Tokio','JAP');
INSERT INTO Servidores VALUES (26,'Beijing','CHN');
INSERT INTO Servidores VALUES (27,'Toronto','CAN');
INSERT INTO Servidores VALUES (28,'New york','EUA');
INSERT INTO Servidores VALUES (29,'Seul','COR');
INSERT INTO Servidores VALUES (30,'Londres','GBR');
INSERT INTO Servidores VALUES (31,'California','EUA');
-------------------------------------------------------------------------------
INSERT INTO Usuarios VALUES ('Bixo612',1,'Vicente',NULL,'Vasquez',NULL,'vicente612@gmail.com','12-jun-96',sysdate-300,'CHI');
INSERT INTO Usuarios VALUES ('Strykez',2,'Santiago',NULL,'Albornoz',NULL,'santiago745@gmail.com','22-jul-97',sysdate-250,'BRA');
INSERT INTO Usuarios VALUES ('GaboDark',3,'Gabriel',NULL,'Gonzalez',NULL,'Gabriel1998@gmail.com','18-sep-98',sysdate-200,'ESP');
INSERT INTO Usuarios VALUES ('Calectini',4,'Valen',NULL,'Stark',NULL,'valen99@gmail.com','09-sep-99',sysdate-150,'ARG');
INSERT INTO Usuarios VALUES ('MsFia16',5,'Sofia',NULL,'Soto',NULL,'sofia16@gmail.com','20-nov-00',sysdate-100,'FIN');
INSERT INTO Usuarios VALUES ('Angelripper',6,'Alfredo',NULL,'Parra',NULL,'amantedelacomida@gmail.com','23-nov-89',sysdate-300,'EUA');
INSERT INTO Usuarios VALUES ('Eldelbar',7,'Juan',NULL,'Gonzalez',NULL,'jdelbar@gmail.com','15-abr-98',sysdate-250,'COR');
INSERT INTO Usuarios VALUES ('Eldelbus',8,'Mauricio',NULL,'Soto',NULL,'mauro1998@gmail.com','10-mar-90',sysdate-200,'CAN');
INSERT INTO Usuarios VALUES ('Aquilesbaeza',9,'Aquiles',NULL,'Baeza',NULL,'aquilescaigo@gmail.com','31-ene-88',sysdate-150,'SUE');
INSERT INTO Usuarios VALUES ('Aggressor',10,'Benjamin',NULL,'Adasme',NULL,'benjatman@gmail.com','10-feb-92',sysdate-100,'FRA');
INSERT INTO Usuarios VALUES ('Papas',11,'constanza',NULL,'Santamaria',NULL,'conpapas@gmail.com','12-may-94',sysdate-300,'ITA');
INSERT INTO Usuarios VALUES ('Belencita',12,'Belen',NULL,'Hidalgo',NULL,'belencilla@gmail.com','22-sep-97',sysdate-250,'MEX');
INSERT INTO Usuarios VALUES ('Eredor',13,'Guillermo',NULL,'Espinoza',NULL,'guille07@gmail.com','10-dec-01',sysdate-200,'PER');
INSERT INTO Usuarios VALUES ('Paltahans',14,'Brian',NULL,'Rogers',NULL,'volantindecuero@gmail.com','09-oct-99',sysdate-150,'AUS');
INSERT INTO Usuarios VALUES ('Carneamarga',15,'Fernando',NULL,'Diaz',NULL,'elmaquina@gmail.com','20-nov-00',sysdate-100,'JAP');
INSERT INTO Usuarios VALUES ('Aragorn',16,'Nelson',NULL,'Montts',NULL,'montarazdelnorte@gmail.com','12-jun-92',sysdate-300,'GBR');
INSERT INTO Usuarios VALUES ('Bananero',17,'Gustavo',NULL,'Henriquez',NULL,'elpelucasabe@gmail.com','22-jul-97',sysdate-250,'ALE');
INSERT INTO Usuarios VALUES ('Pink_teacher',18,'Michael',NULL,'Jackson',NULL,'ayuwoki@gmail.com','30-sep-98',sysdate-200,'ALE');
INSERT INTO Usuarios VALUES ('janna',19,'Alejandra',NULL,'Herrera',NULL,'alehe98@gmail.com','09-sep-15',sysdate-150,'EUA');
INSERT INTO Usuarios VALUES ('Almendark',20,'Almendra',NULL,'Ahumada',NULL,'lacubanita@gmail.com','05-nov-12',sysdate-100,'CHN');
INSERT INTO Usuarios VALUES ('Dylantero',21,'Dylan',NULL,'Fernandez',NULL,'olaquehace@gmail.com','30-sep-90',sysdate-600,'CHI');
INSERT INTO Usuarios VALUES ('Moaigr',22,'Marcos',NULL,'Herrera',NULL,'the-moais@gmail.com','09-sep-90',sysdate-650,'EUA');
INSERT INTO Usuarios VALUES ('Kirby',23,'John',NULL,'Wahignton',NULL,'elpanajohn@gmail.com','05-nov-91',sysdate-625,'EUA');
-------------------------------------------------------------------------------
INSERT INTO moderadores VALUES ('19975621-K','AVENIDA SIEMPRE VIVA #742','147854712','CUENTA CORRIENTE','BANCO SANTANDER', 1);
INSERT INTO moderadores VALUES ('17241665-1','ISLA GUAFO #8942','154684712','CUENTA CORRIENTE','UNICREDIT', 2);
INSERT INTO moderadores VALUES ('18516641-5','BLICKER ST. #8942','785491265','CUENTA CORRIENTE','BANK OF AMERICA', 1)
INSERT INTO moderadores VALUES ('14834678-9','MARIN #014','362589741','CUENTA CORRIENTE','BANCO ESTADO', 1)
INSERT INTO moderadores VALUES ('20467632-3','LAS CANARIAS #454','784659521','CUENTA CORRIENTE','CAIXA BANK', 1)
INSERT INTO moderadores VALUES ('17798646-7','CALLE 13 #133','365298741','CUENTA CORRIENTE','BANCO BRADESCO', 1)
INSERT INTO moderadores VALUES ('15349675-4','ELM ST #1475','528967413','CUENTA CORRIENTE','STATE STREET CORPORATION', 1)
INSERT INTO moderadores VALUES ('17654841-6','CAMPOS ELISEOS #968','528968974','CUENTA CORRIENTE','INTENSA SANPAOLO', 1)
INSERT INTO moderadores VALUES ('13989196-8','OXFORD ST. #6935','745218963','CUENTA CORRIENTE','NATIONWIDE BUILDINGS SOCIETY ', 1)
INSERT INTO moderadores VALUES ('11879424-2','PORTOBELLO #34711','326587419','CUENTA CORRIENTE','BANCO DO BRASIL', 1)
INSERT INTO moderadores VALUES ('14116141-5','FRIEDRICHATRASSE #74185','542128779','CUENTA CORRIENTE','DEUTCHE BANK', 1)
INSERT INTO moderadores VALUES ('9946714-K','TOGOSHI GINZA SHOTENGAI#8942','542211689','CUENTA CORRIENTE','JAPAN POST BANK', 1)
INSERT INTO moderadores VALUES ('17725165-4','SHERBOURNE ST. #9888','741289564','CUENTA CORRIENTE','TORONTO DOMINION BANK', 1)
INSERT INTO moderadores VALUES ('19644274-9','LA MERCERIE #6585','254879631','CUENTA CORRIENTE','RABOBANK', 1)
INSERT INTO moderadores VALUES ('18815625-5','POVARSKAYA #12455','458969632','CUENTA CORRIENTE','DANSKE BANK', 1)
INSERT INTO moderadores VALUES ('15745435-4','AV. COLORADO #69869','741582936','CUENTA CORRIENTE','BANCO SABADELL', 1)
INSERT INTO moderadores VALUES ('18435610-7','SHINCINTOGA #841','478512693','CUENTA CORRIENTE','BANK OF BEIJING', 1)
INSERT INTO moderadores VALUES ('16195891-K','FRANKFURER #96963','548796321','CUENTA CORRIENTE','BARCLAYS', 1)
INSERT INTO moderadores VALUES ('20945870-7','GUANACOS #7442','235689741','CUENTA CORRIENTE','BANCO SABADELL', 1)
INSERT INTO moderadores VALUES ('19675411-3','LORD REIGNER #96369','321456987','CUENTA CORRIENTE','BAYERN LB', 1);
-------------------------------------------------------------------------------
INSERT INTO Canciones VALUES (1,NULL,'Billie Jean',4,'Pop',750,30);
INSERT INTO Canciones VALUES (2,NULL,'Enter Sadman',4,'Metal',600,30);
INSERT INTO Canciones VALUES (3,NULL,'Algun dia volveras',3,'Cumbia',1200,30);
INSERT INTO Canciones VALUES (4,NULL,'Amor de feria',3,'Cumbia',1500,30);
INSERT INTO Canciones VALUES (5,NULL,'Serenata cruel',3,'Cumbia',1400,30);
INSERT INTO Canciones VALUES (6,NULL,'Take Five',4,'Ska',750,30);
INSERT INTO Canciones VALUES (7,NULL,'Skaravan',4,'Ska',600,25);
INSERT INTO Canciones VALUES (8,NULL,'Scream',3,'Punk',1200,25);
INSERT INTO Canciones VALUES (9,NULL,'By the way',7,'Funk',1200,25); 
INSERT INTO Canciones VALUES (10,NULL,'Got the life',8,'Nu metal',1400,25);
INSERT INTO Canciones VALUES (11,NULL,'Could you be loved',3,'Reggae',1400,25);
INSERT INTO Canciones VALUES (12,NULL,'Give your love',4,'Reggae',750,25);
INSERT INTO Canciones VALUES (13,NULL,'Waiting for your love',8,'Reggae',600,25);
INSERT INTO Canciones VALUES (14,NULL,'Paradox',7,'Techno',1200,25);
INSERT INTO Canciones VALUES (15,NULL,'Be my lover',3,'Eurodance',1500,24);
INSERT INTO Canciones VALUES (16,NULL,'Quit Playing games (with my heart)',3,'Pop',1400,24);
INSERT INTO Canciones VALUES (17,NULL,'Sometimes',4,'Pop',750,24);
INSERT INTO Canciones VALUES (18,NULL,'Mi historia entre tus manos',4,'Romantica',600,24);
INSERT INTO Canciones VALUES (19,NULL,'Wannabe',3,'Pop',1200,24);
INSERT INTO Canciones VALUES (20,NULL,'Dejaria todo',3,'Romantica',1500,15);
INSERT INTO Canciones VALUES (21,NULL,'Rock Around the Clock',3,'Rock',1400,15);
INSERT INTO Canciones VALUES (22,NULL,'Dont stop believing',3,'Rock',1400,15);
INSERT INTO Canciones VALUES (23,NULL,'Torero',4,'Pop',2000,15);
INSERT INTO Canciones VALUES (24,NULL,'Running in the 90s',7,'Techno',1050,25);
-------------------------------------------------------------------------------
INSERT INTO Videos VALUES (1,NULL,'Tutorial Ukulele',5,SYSDATE-10,'Publico','TE','Tutoriales',150,10,200,17);
INSERT INTO Videos VALUES (2,NULL,'Tutorial Bajo',5,SYSDATE-10,'Publico','TE','Tutoriales',200,10,200,17);
INSERT INTO Videos VALUES (7,NULL,'Tutorial Harmonica',5,SYSDATE-12,'Publico','TE','Tutoriales',300,15,200,17);
INSERT INTO Videos VALUES (3,NULL,'Gameplay Mortal Kombat 11',2,SYSDATE-9,'No Listado','+18','Videojuegos',2,0,3,19);
INSERT INTO Videos VALUES (4,NULL,'Gameplay Mortal Kombat 11',2,SYSDATE-8,'Privado','+18','Videojuegos',2,0,3,19); 
INSERT INTO Videos VALUES (5,NULL,'Videos de gatos #1',1,SYSDATE-6,'Publico','TE','Animales',250,3,300,18);
INSERT INTO Videos VALUES (6,NULL,'Videos de gatos #2',1,SYSDATE-5,'Publico','TE','Animales',300,2,350,18);
INSERT INTO Videos VALUES (8,NULL,'Videos de gatos #3',1,SYSDATE-80,'Publico','TE','Animales',100,2,70,18);
-------------------------------------------------------------------------------

select * from videos;
desc canciones;

select GENERO,COUNT(*) FROM CANCIONES
GROUP BY GENERO;

SELECT COUNT(*) FROM CANCIONES;

SELECT COUNT(*) FROM videos where fecha_subida > sysdate-31; 

SELECT COUNT(*) FROM MODERADORES;

SELECT COUNT(*) FROM VIDEOS WHERE RESTRICCION = '+18';

select max(reproducciones), titulo from canciones;

desc usuarios;

select count(*) from usuarios where fecha_nacimiento > sysdate-(365*13);

desc videos;

SELECT * FROM videos where Fecha_subida > sysdate-365; 

select * from videos;

commit;

update videos set Fecha_subida = fecha_subida + 30
where Fecha_subida > sysdate-365;

desc usuarios;

update videos set me_gusta = me_gusta + 350;

delete videos where restriccion = '+18';

delete usuarios where fecha_nacimiento > sysdate-(365*13);

ROLLBACK ;










