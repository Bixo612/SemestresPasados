select 'El empleado '||nombre||' '||apellido||' esta de cumpleaños el '||to_char(TO_DATE (fecha_nac),'day')||
to_char(TO_DATE (fecha_nac),'D')||' de '||to_char(TO_DATE (fecha_nac),'Month')||'y cumple '||
(EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM FECHA_NAC)) ||' años' as "LISTADO_DE_CUMPLEAÑOS"
from empleados;