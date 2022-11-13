--- Solucion 1 --- OK

select nro_boleta, fecha,valor_neto,iva,descuento,total,case WHEN descuento is null then 'No tiene descuento' else 'Tiene descuento' end
from boletas;

--- Solucion 2 --- OK

select nombre ||' '||apellido as "NOMBRE_COMPLETO",
SUBSTR(nombre,1,1)||apellido||'@YoTeVendo.cl' as "CORREO_ELECTRONICO"
from empleados;

--- Solucion 3 --- OK

SELECT b.nro_boleta,b.orden_id,b.fecha,e.nombre||' '||e.apellido as NOMBRE_COMPLETO ,
    to_char(b.valor_neto,'$999G999G999') as VALOR_NETO,
    to_char(b.iva,'$999G999G999') as IVA,
    to_char(b.descuento,'$999G999G999')as DESCUENTO,
    to_char(total,'$999G999G999') as TOTAL
FROM boletas b JOIN empleados e on b.empleado_id = e.empleado_id;

--- Solucion 4 --- OK

select 'El empleado '||nombre||' '||apellido||' esta de cumpleaños el '||to_char(TO_DATE (fecha_nac),'day')||
to_char(TO_DATE (fecha_nac),'D')||' de '||to_char(TO_DATE (fecha_nac),'Month')||'y cumple '||
(EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM FECHA_NAC)) ||' años' as "LISTADO_DE_CUMPLEAÑOS"
from empleados;

--- Solucion 5 --- OK

select empleado_id,nombre ||' '||apellido as NOMBRE_COMPLETO,
to_char(sueldo,'$999G999G999') as SALARIO,
to_char(sueldo*1.165,'$999G999G999') as SALARIO_AUMENTADO,
to_char(sueldo*0.165,'$999G999G999') as AUMENTO
from empleados order by 3;

select empleado_id,nombre ||' '||apellido as NOMBRE_COMPLETO,
EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM FECHA_NAC) AS EDAD,
to_char(sueldo,'$999G999G999') as SALARIO,
to_char(sueldo*((((EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM FECHA_NAC))-10)/100+1)),'$999G999G999') as SALARIO_AUMENTADO,
to_char(sueldo*((((EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM FECHA_NAC))-10)/100)),'$999G999G999') as AUMENTO
from empleados order by 3;

--- Solucion 6 ---OK

SELECT nombre_prov,contacto,celular_prov,fijo_prov,CASE when fijo_prov > 2450887 and fijo_prov <2507190 then 'Ok' else 'Aun no se visita'end
FROM proveedores order by fijo_prov ASC;