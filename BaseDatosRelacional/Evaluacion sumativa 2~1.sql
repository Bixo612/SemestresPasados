select 'El empleado '||nombre||' '||apellido||' esta de cumplea�os el '||to_char(TO_DATE (fecha_nac),'day')||
to_char(TO_DATE (fecha_nac),'D')||' de '||to_char(TO_DATE (fecha_nac),'Month')||'y cumple '||
(EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM FECHA_NAC)) ||' a�os' as "LISTADO_DE_CUMPLEA�OS"
from empleados;