SELECT * FROM TAB;

select * from sucursal;
select * from comuna;
select * from empleado;


SELECT cod_sucursal s, c.nombre
FROM sucursal s left join comuna c 
    on s.comuna_sucursal = c.cod_comuna
;

SELECT s.cod_sucursal , c.nombre,e.cod_sucursal,COUNT(*)
FROM sucursal s left join comuna c 
    on s.comuna_sucursal = c.cod_comuna 
                left JOIN empleado e on s.cod_sucursal = e.cod_sucursal
group BY e.cod_sucursal
;

select COUNT(*),cod_sucursal from empleado
GROUP BY cod_sucursal;




