--Realice un �ndice que permita una mejor b�squeda de los datos por medio de la patente_infractora en la tabla multas.

create index patente_infractora on multas(patente_infractora);

--Realice un �ndice que permita una mejor b�squeda de los rut_inspector en la tabla inspectores.

create index rut_inspector on inspectores(rut_inspector);

--------

select * from inspectores;

select * from all_indexes where owner like 'SUM3_BDR';

SELECT
    * FROM multas;
    
select *
from vehiculos order by 1;
    
--Create bitmap index

--CREATE unique INDEX

create index patente_infractora on multas(patente_infractora);

DROP INDEX patente_infractora;

select * from multas where patente_infractora like 'HFCK69'