CREATE TABLE Paises (
	Id_pais 	VARCHAR2 (3) NOT NULL PRIMARY KEY,
	Nombre_pais VARCHAR2(50) NOT NULL UNIQUE
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
	Id_nacional		VARCHAR2 (20) NOT NULL PRIMARY KEY,
	Direccion		VARCHAR2 (200) NOT NULL,
	Cta_banco		VARCHAR2 (25) NOT NULL,
	Tipo_cta		VARCHAR2 (25) NOT NULL,
	Nombre_banco	VARCHAR2 (100) NOT NULL,
	Id_user 		INT NOT NULL UNIQUE,
	Tipo_moderador	VARCHAR2 (25) NOT NULL,
	CONSTRAINTS Fk_moderadores_usuarios FOREIGN KEY (Id_user) REFERENCES Usuarios(Id_user)
);

CREATE TABLE Videos (
	Id_video		INT NOT NULL PRIMARY KEY,
	Archivo 		VARCHAR2 (50),
	Nombre 			VARCHAR2 (50) NOT NULL,
	Id_user			INT NOT NULL,
	Fecha_subida	DATE NOT NULL,
	Visibilidad		VARCHAR2 (15) NOT NULL,
	Restriccion		VARCHAR2 (15) NOT NULL,
	Genero 			VARCHAR2 (50) NOT NULL,
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

--DATOS

INSERT INTO Paises VALUES ('CHI','Chile');
INSERT INTO Paises VALUES ('BRA','Brasil');
INSERT INTO Paises VALUES ('MEX','Mexico');
INSERT INTO Paises VALUES ('ESP','Espana');
INSERT INTO Paises VALUES ('ARG','Argentina');
INSERT INTO Paises VALUES ('PER','Peru');
INSERT INTO Paises VALUES ('FRA','Francia');
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
INSERT INTO Paises VALUES ('URU','Uruguay');
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
-------------------------------------------------------------------------------
INSERT INTO Usuarios VALUES ('Bixo612',1,'Vicente',NULL,'Vasquez',NULL,'vicente612@gmail.com','12-jun-96',sysdate-750,'CHI');
INSERT INTO Usuarios VALUES ('Strykez',2,'Santiago',NULL,'Albornoz',NULL,'santiago745@gmail.com','22-jul-97',sysdate-700,'BRA');
INSERT INTO Usuarios VALUES ('GaboDark',3,'Gabriel',NULL,'Gonzalez',NULL,'Gabriel1998@gmail.com','18-sep-98',sysdate-650,'ESP');
INSERT INTO Usuarios VALUES ('Calectini',4,'Valen',NULL,'Stark',NULL,'valen99@gmail.com','09-sep-99',sysdate-600,'ARG');
INSERT INTO Usuarios VALUES ('MsFia16',5,'Sofia',NULL,'Soto',NULL,'sofia16@gmail.com','20-nov-00',sysdate-550,'FIN');
INSERT INTO Usuarios VALUES ('Angelripper',6,'Alfredo',NULL,'Parra',NULL,'amantedelacomida@gmail.com','23-nov-89',sysdate-500,'EUA');
INSERT INTO Usuarios VALUES ('Eldelbar',7,'Juan',NULL,'Gonzalez',NULL,'jdelbar@gmail.com','15-abr-98',sysdate-450,'COR');
INSERT INTO Usuarios VALUES ('Eldelbus',8,'Mauricio',NULL,'Soto',NULL,'mauro1998@gmail.com','10-mar-90',sysdate-400,'CAN');
INSERT INTO Usuarios VALUES ('Aquilesbaeza',9,'Aquiles',NULL,'Baeza',NULL,'aquilescaigo@gmail.com','31-ene-88',sysdate-350,'SUE');
INSERT INTO Usuarios VALUES ('Aggressor',10,'Benjamin',NULL,'Adasme',NULL,'benjatman@gmail.com','10-feb-92',sysdate-300,'FRA');
INSERT INTO Usuarios VALUES ('Papas',11,'constanza',NULL,'Santamaria',NULL,'conpapas@gmail.com','12-may-94',sysdate-250,'ITA');
INSERT INTO Usuarios VALUES ('Belencita',12,'Belen',NULL,'Hidalgo',NULL,'belencilla@gmail.com','22-sep-97',sysdate-200,'MEX');
INSERT INTO Usuarios VALUES ('Eredor',13,'Guillermo',NULL,'Espinoza',NULL,'guille07@gmail.com','10-dec-01',sysdate-150,'PER');
INSERT INTO Usuarios VALUES ('Paltahans',14,'Brian',NULL,'Rogers',NULL,'volantindecuero@gmail.com','09-oct-99',sysdate-100,'AUS');
INSERT INTO Usuarios VALUES ('Carneamarga',15,'Fernando',NULL,'Diaz',NULL,'elmaquina@gmail.com','20-nov-00',sysdate-50,'JAP');
INSERT INTO Usuarios VALUES ('Aragorn',16,'Nelson',NULL,'Montts',NULL,'montarazdelnorte@gmail.com','12-jun-92',sysdate,'GBR');
INSERT INTO Usuarios VALUES ('Bananero',17,'Gustavo',NULL,'Henriquez',NULL,'elpelucasabe@gmail.com','22-jul-97',sysdate-800,'ALE');
INSERT INTO Usuarios VALUES ('Pink_teacher',18,'Michael',NULL,'Jackson',NULL,'ayuwoki@gmail.com','30-sep-98',sysdate-850,'ALE');
INSERT INTO Usuarios VALUES ('Janna',19,'Alejandra',NULL,'Herrera',NULL,'alehe98@gmail.com','11-sep-02',sysdate-900,'EUA');
INSERT INTO Usuarios VALUES ('Almendark',20,'Almendra',NULL,'Ahumada',NULL,'lacubanita@gmail.com','05-nov-00',sysdate-950,'CHN');
INSERT INTO Usuarios VALUES ('Dylantero',21,'Dylan',NULL,'Fernandez',NULL,'olaquehace@gmail.com','30-sep-19',sysdate-25,'CHI');
INSERT INTO Usuarios VALUES ('Moaigr',22,'Marcos',NULL,'Herrera',NULL,'the-moais@gmail.com','09-sep-18',sysdate-20,'EUA');
INSERT INTO Usuarios VALUES ('Kirby',23,'John',NULL,'Wahignton',NULL,'elpanajohn@gmail.com','05-nov-17',sysdate-15,'EUA');
INSERT INTO Usuarios VALUES ('Yondu',24,'Sebastian',NULL,'Diaz',NULL,'sebaxx@gmail.com','20-feb-20',sysdate-10,'URU');
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
INSERT INTO Canciones VALUES (14,NULL,'Paradox',7,'techno',1200,25);
INSERT INTO Canciones VALUES (15,NULL,'Be my lover',3,'Eurodance',1500,24);
INSERT INTO Canciones VALUES (16,NULL,'Quit Playing games (with my heart)',3,'Pop',1400,24);
INSERT INTO Canciones VALUES (17,NULL,'Sometimes',4,'Pop',750,24);
INSERT INTO Canciones VALUES (18,NULL,'Mi historia entre tus manos',4,'Romantica',600,24);
INSERT INTO Canciones VALUES (19,NULL,'Wannabe',3,'Pop',1200,24);
INSERT INTO Canciones VALUES (20,NULL,'Dejaria todo',3,'Romantica',1500,15);
INSERT INTO Canciones VALUES (21,NULL,'Rock Around the Clock',3,'Rock',1400,15);
INSERT INTO Canciones VALUES (22,NULL,'Dont stop believing',3,'Rock',1400,15);
INSERT INTO Canciones VALUES (23,NULL,'Toreo',4,'Pop',2000,15);
-------------------------------------------------------------------------------
INSERT INTO Videos VALUES (1,NULL,'Tutorial Ukulele',5,SYSDATE-60,'Publico','TE','Tutoriales',150,10,200,11);
INSERT INTO Videos VALUES (2,NULL,'Tutorial Bajo',5,SYSDATE-61,'Publico','TE','Tutoriales',200,10,200,13);
INSERT INTO Videos VALUES (3,NULL,'Gameplay Mortal Kombat 11',2,SYSDATE-9,'Privado','+18','Videojuegos',2,0,3,20);
INSERT INTO Videos VALUES (4,NULL,'Gameplay Mortal Kombat 11',2,SYSDATE-8,'Privado','+18','Videojuegos',2,0,3,25); 
INSERT INTO Videos VALUES (5,NULL,'Videos de gatos #1',1,SYSDATE-58,'Publico','TE','Animales',250,3,300,12);
INSERT INTO Videos VALUES (6,NULL,'Chascarros de piñera',1,SYSDATE-9,'Publico','TE','Graciosos',300,2,350,15);
INSERT INTO Videos VALUES (7,NULL,'Atentado torres gemelas',3,SYSDATE-10,'No listado','+18','Noticias',150,10,200,26);
INSERT INTO Videos VALUES (8,NULL,'Frases graciosas de homero',3,SYSDATE-10,'Privado','TE','Graciosos',200,10,210,30);
INSERT INTO Videos VALUES (9,NULL,'Opening slamdunk',2,SYSDATE-9,'Publico','TE','Anime',120,10,140,14);
INSERT INTO Videos VALUES (10,NULL,'Receta pavo al horno',7,SYSDATE-8,'Publico','TE','Tutoriales',115,30,160,21); 
INSERT INTO Videos VALUES (11,NULL,'Curso de oracle desde cero',4,SYSDATE-46,'Publico','TE','Tutoriales',285,3,300,29);
INSERT INTO Videos VALUES (12,NULL,'Curso de python desde cero',4,SYSDATE-45,'Publico','TE','Tutoriales',320,5,350,16);
INSERT INTO Videos VALUES (13,NULL,'La caida de Edgar',1,SYSDATE-6,'Publico','TE','Graciosos',400,2,410,28);
INSERT INTO Videos VALUES (14,NULL,'Muerte de Lady Di',3,SYSDATE-5,'No listado','+18','Noticias',300,2,340,22);
INSERT INTO Videos VALUES (15,NULL,'Tutorial Harmonica',5,SYSDATE-59,'Publico','TE','Tutoriales',300,15,200,17);
INSERT INTO Videos VALUES (16,NULL,'Toxicity drum cover',5,SYSDATE-10,'Publico','TE','Tutoriales',220,10,240,23);
INSERT INTO Videos VALUES (17,NULL,'Una hora de sonata claro de luna',2,SYSDATE-9,'Publico','TE','Musica',2,0,3,17);
INSERT INTO Videos VALUES (18,NULL,'Curso de yoga',2,SYSDATE-8,'Publico','TE','Tutoriales',80,3,90,18); 
INSERT INTO Videos VALUES (19,NULL,'Como formatear tu computador',4,SYSDATE-45,'Publico','TE','Tutoriales',250,3,300,24);
INSERT INTO Videos VALUES (20,NULL,'La mayor tragedia del futbol',1,SYSDATE-5,'Privado','+18','Noticias',300,2,350,25);
-------------------------------------------------------------------------------
INSERT INTO Moderadores VALUES ('19945621-K','Isla Guafo #8942','154684712','Cta Corriente','Banco Estado',1,'Super Moderador');
INSERT INTO Moderadores VALUES ('20007042-9','Ministro Carvajal #7770','154684712','Cta Corriente','Banco De Chile',2,'Super Moderador');
INSERT INTO Moderadores VALUES ('19975621-K','Aveninda Siempre Viva #742','147854712','Cta Vista','Banco Santander',3,'Super Moderador');
INSERT INTO Moderadores VALUES ('17241665-1','Isla Guafo #8942','154684712','Cta Corriente','Unicredit',4,'Super Moderador');
INSERT INTO Moderadores VALUES ('18516641-5','Blicker St. #8942','785491265','Cta Corriente','Bank Of America',5,'Moderador Normal');
INSERT INTO Moderadores VALUES ('14834678-9','Marin #014','362589741','Cta Corriente','Banco Estado',6,'Moderador Normal');
INSERT INTO Moderadores VALUES ('20467632-3','Las Canarias #454','784659521','Cta Corriente','Caixa Bank',7,'Moderador Normal');
INSERT INTO Moderadores VALUES ('17798646-7','Calle 13 #133','365298741','Cta Corriente','Banco Bradesco',8,'Moderador Normal');
INSERT INTO Moderadores VALUES ('15349675-4','Elm St #1475','528967413','Cta Corriente','State Street Corporation',9,'Moderador Normal');
INSERT INTO Moderadores VALUES ('17654841-6','Campos Eliseos #968','528968974','Cta Corriente','Intensa Sanpaolo',10,'Moderador Superior');
INSERT INTO Moderadores VALUES ('13989196-8','Oxford St. #6935','745218963','Cta Corriente','Nationwide Buildings Society ',11,'Moderador Superior');
INSERT INTO Moderadores VALUES ('11879424-2','Portobello #34711','326587419','Cta Vista','Banco Do Brasil',12,'Moderador Superior');
INSERT INTO Moderadores VALUES ('14116141-5','Friedrichatrasse #74185','542128779','Cta Corriente','Deutche Bank',13,'Moderador Superior');
INSERT INTO Moderadores VALUES ('9946714-K','Togoshi Ginza Shotengai#8942','542211689','Cta Corriente','Japan Post Bank',14,'Moderador Superior');
INSERT INTO Moderadores VALUES ('17725165-4','Sherbourne St. #9888','741289564','Cta Corriente','Toronto Dominion Bank',15,'Moderador Superior');
INSERT INTO Moderadores VALUES ('19644274-9','La Mercerie #6585','254879631','Cta Corriente','Rabobank',16,'Moderador Superior');
INSERT INTO Moderadores VALUES ('18815625-5','Povarskaya #12455','458969632','Cta Corriente','Danske Bank',17,'Moderador Superior');
INSERT INTO Moderadores VALUES ('15745435-4','Av. Colorado #69869','741582936','Cta Corriente','Banco Sabadell',18,'Moderador Superior');
INSERT INTO Moderadores VALUES ('18435610-7','Shincintoga #841','478512693','Cta Corriente','Bank Of Beijing',19,'Moderador Superior');
INSERT INTO Moderadores VALUES ('16195891-K','Frankfurer #96963','548796321','Cta Corriente','Barclays',20,'Moderador Normal');

-- CONSULTAS

COMMIT;
--¿Cuál es la cantidad de videos subidos por cada usuario?
SELECT ID_USER,COUNT(*) FROM VIDEOS
GROUP BY ID_USER;
--¿Cuál es la cantidad de videos subidos por cada género de interés?
SELECT GENERO,COUNT(*) FROM VIDEOS GROUP BY GENERO;
--¿Cuantas canciones se han subido?
SELECT COUNT(*) FROM CANCIONES;
--¿Cuantos usuarios hay en la plataforma que tengan más de un año de antigüedad?
SELECT COUNT(*) FROM Usuarios where Fecha_registro > sysdate-365; 
--¿Cuantos usuarios tienen menos de un año de antigüedad?
SELECT COUNT(*) FROM Usuarios where Fecha_registro < sysdate-365; 
--¿Cuantos moderadores hay en la plataforma?
SELECT COUNT(*) FROM MODERADORES;
--¿Cuantos videos con calificación para mayores de 18 hay en la plataforma?
SELECT COUNT(*) FROM VIDEOS WHERE RESTRICCION = '+18';
--¿Cuantas canciones hay en cada género?
SELECT genero,COUNT(*) FROM canciones GROUP BY genero;
--¿Cuáles son los videos publicados en el último mes?
SELECT COUNT(*) FROM videos where fecha_subida > sysdate-31; 
--¿Cuál es la canción más escuchada de la aplicación?**********
SELECT MAX(reproducciones)
FROM canciones;
SELECT id_cancion,titulo, genero, MAX(reproducciones)
FROM canciones
GROUP BY id_cancion, titulo, genero
HAVING MAX(reproducciones) >1500
ORDER BY id_cancion ASC;
--¿Cuantos usuarios registrados son menores de 13 años?
SELECT COUNT(*) FROM USUARIOS WHERE FECHA_NACIMIENTO > SYSDATE-(365*13);
--Modifique la fecha de todos los videos aumentando sus días de subido en 30 a todos los videos subidos con menos de 365 dias de antigüedad.
UPDATE videos SET fecha_subida = fecha_subida + 30
WHERE fecha_subida > sysdate-365;
--Modifique la cantidad de me gusta de los videos aumentando el valor en 350.
UPDATE videos SET me_gusta = me_gusta + 350;
--Elimine todos los videos que tengan una calificación para mayores de 18.
DELETE videos WHERE restriccion = '+18';
--Elimine a todos los usuarios que tengan menos de 13 años.
DELETE usuarios WHERE fecha_nacimiento > sysdate-(365*13);

ROLLBACK;