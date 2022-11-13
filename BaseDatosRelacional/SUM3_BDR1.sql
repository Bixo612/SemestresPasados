--Cree un bloque anónimo que permita ver el rut, en nombre completo, el correo electrónico y la fecha de nacimiento del inspector que tenga el id 1.



desc inspectores;
select * from inspectores  where rut_inspector like '13555478-4';

desc funcionarios_municipales;
select * from funcionarios_municipales where rut like '13555478-4';

select 
    inspectores.rut_inspector,
    funcionarios_municipales.primer_nombre,
    funcionarios_municipales.segundo_nombre,
    funcionarios_municipales.primer_apellido,
    funcionarios_municipales.segundo_apellido,
    funcionarios_municipales.correo_electronico,
    funcionarios_municipales.fecha_nacimiento
from
    inspectores JOIN funcionarios_municipales on inspectores.rut_inspector = funcionarios_municipales.rut
where inspectores.id_inspector = 1
;

--Cree un bloque anónimo que permita saber cuántas multas posee la patente HFCK69 en la tabla multas, indicando también cual es la marca y el modelo del vehículo.

desc multas;
select * from multas;

SELECT 
vehiculos.marca,
vehiculos.modelo,
vehiculos.placa_patente,
count(multas.patente_infractora) 
FROM multas join vehiculos on multas.patente_infractora = vehiculos.placa_patente
WHERE vehiculos.placa_patente like 'HFCK69';


--


set SERVEROUTPUT on
BEGIN
    DBMS_OUTPUT.PUT_LINE('Hola mundo');
END;
/


begin
    select inspectores.rut_inspector,
        funcionarios_municipales.primer_nombre,
        funcionarios_municipales.segundo_nombre,
        funcionarios_municipales.primer_apellido,
        funcionarios_municipales.segundo_apellido,
        funcionarios_municipales.correo_electronico,
        funcionarios_municipales.fecha_nacimiento
    from
        inspectores JOIN funcionarios_municipales on inspectores.rut_inspector = funcionarios_municipales.rut
    --where inspectores.id_inspector = 1
    ;
end;
/
--

select * from juzgados_policia_local;
select * from municipalidades;
DESC MUNICIPALIDADES;
----Cree un procedimiento almacenado llamado sp_informe_juzgados que muestre la 
--información de los juzgados de policía local asociados a una municipalidad en 
--específico, para ello se solicita que ingrese el nombre de la comuna que se 
--requiere saber por parámetros y que despliegue esa información por medio del terminal.


CREATE OR REPLACE PROCEDURE sp_informe_juzgados AS
    V_COMUNA VARCHAR(70) :='';
Begin
    SELECT COMUNA
    FROM municipalidades
    where comuna like v_comuna ;
EXCEPTION
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('error :c');
END;
/

BEGIN
    sp_informe_juzgados();
end;


































