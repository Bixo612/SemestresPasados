Insert into EMPLEADOS (EMPLEADO_ID,NOMBRE,APELLIDO,FECHA_NAC,SUELDO,REPORTA_A,EXTENSION) values ('8','VICENTE','VASQUEZ',to_date('25/12/96','DD/MM/RR'),650000,'3','261');
Insert into EMPLEADOS (EMPLEADO_ID,NOMBRE,APELLIDO,FECHA_NAC,SUELDO,REPORTA_A,EXTENSION) values ('9','lAURA','HEANO',to_date('15/01/96','DD/MM/RR'),650000,'3','261');

SELECT * FROM EMPLEADOS ORDER BY fecha_nac;