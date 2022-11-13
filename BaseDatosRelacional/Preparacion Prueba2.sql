--- SOLUCION 1 ---

CREATE USER usersum1 
IDENTIFIED BY C4ntr@S3gur4
DEFAULT TABLESPACE USERS
TEMPORARY TABLESPACE TEMP;

--- SOLUCION 2 ---

SELECT SUCURSAL.COD_SUCURSAL "CODIGO SUCURSAL", 
      COMUNA.NOMBRE "NOMBRE COMUNA", 
      COUNT(EMPLEADO.COD_EMPLEADO) "CANTIDAD EMPLEADOS",
      TO_CHAR(NVL(SUM(VENTA.VALOR_TOTAL),0),'$999G999G999') "TOTAL VENTAS", 
      TO_CHAR(NVL((SUM(VENTA.VALOR_TOTAL)*0.3),0),'$999G999G999') "UTILIDADES"
FROM SUCURSAL JOIN COMUNA ON SUCURSAL.COMUNA_SUCURSAL = COMUNA.COD_COMUNA
     LEFT OUTER JOIN EMPLEADO ON SUCURSAL.COD_SUCURSAL = EMPLEADO.COD_SUCURSAL
     LEFT OUTER JOIN VENTA ON EMPLEADO.COD_EMPLEADO = VENTA.COD_EMPLEADO
GROUP BY SUCURSAL.COD_SUCURSAL, COMUNA.NOMBRE
ORDER BY SUCURSAL.COD_SUCURSAL ASC;


--- SOLUCION 3 ---

SELECT DISTINCT MEDICAMENTO.COD_MEDICAMENTO "C�DIGO", MEDICAMENTO.NOMBRE_MEDICAMENTO "NOMBRE", 
       MEDICAMENTO.PRECIO_MEDICAMENTO "PRECIO",
       TO_CHAR(ROUND(MEDICAMENTO.PRECIO_MEDICAMENTO*
       (SELECT 1+((PORCENTAJE)/100) 
        FROM DESCUENTOS WHERE MEDICAMENTO.TIPO_MEDICAMENTO = DESCUENTOS.TIPO_MEDICAMENTO)),'$999G999G999') "PRECIO PROYECTADO", 
       TO_CHAR((SELECT SUM(PRECIO_MEDICAMENTO*
                        (SELECT 1+((PORCENTAJE)/100) 
                         FROM DESCUENTOS 
                         WHERE MEDICAMENTO.TIPO_MEDICAMENTO = DESCUENTOS.TIPO_MEDICAMENTO)) 
       FROM DETALLE_VENTA),'$999G999G999')
       "TOTAL VENTAS PROYECTADAS"
FROM MEDICAMENTO JOIN DETALLE_VENTA 
ON MEDICAMENTO.COD_MEDICAMENTO = DETALLE_VENTA.COD_MEDICAMENTO
ORDER BY MEDICAMENTO.NOMBRE_MEDICAMENTO ASC,MEDICAMENTO.PRECIO_MEDICAMENTO DESC;

--- SOLUCION 4 ---

SELECT REGION.NOMBRE "NOMBRE REGION",
	 COUNT(SUCURSAL.COD_SUCURSAL) "CANTIDAD SUCURSALES",
     COUNT(EMPLEADO.COD_EMPLEADO) "CANTIDAD TRABAJADORES"
FROM REGION JOIN COMUNA ON REGION.COD_REGION = COMUNA.COD_REGION
     JOIN SUCURSAL ON SUCURSAL.COMUNA_SUCURSAL = COMUNA.COD_COMUNA
     JOIN EMPLEADO ON EMPLEADO.COD_SUCURSAL = SUCURSAL.COD_SUCURSAL
GROUP BY REGION.NOMBRE
HAVING COUNT(EMPLEADO.COD_SUCURSAL) > (SELECT AVG(COUNT(COD_SUCURSAL))
                                       FROM EMPLEADO
                                       GROUP BY COD_SUCURSAL);									   
--- SOLUCION 5 ---

SELECT NOMBRE "Comunas sin sucursal"
FROM COMUNA
MINUS
SELECT COMUNA.NOMBRE
FROM COMUNA RIGHT OUTER JOIN SUCURSAL ON SUCURSAL.COMUNA_SUCURSAL = COMUNA.COD_COMUNA;

--- SOLUCION 6 ---

SELECT EMPLEADO.NOM_EMPLEADO "NOMBRE", EMPLEADO.A_PATERNO "APELLIDO", 
       EMPLEADO.SALARIO "SALARIO ACTUAL", 
       COUNT(VENTA.FOLIO) "CANTIDAD DE VENTAS",
       SUM(VENTA.VALOR_TOTAL) "VALOR TOTAL VENTAS", 
       AVG(VENTA.VALOR_TOTAL) "PROMEDIO DE VENTAS",
       (AVG(EMPLEADO.SALARIO)*(1+(COUNT(VENTA.FOLIO)/100))) "COMISION",
       (EMPLEADO.SALARIO+(AVG(EMPLEADO.SALARIO)*(1+(COUNT(VENTA.FOLIO)/100))))
       "SUELDO TOTAL"
FROM EMPLEADO JOIN VENTA ON EMPLEADO.COD_EMPLEADO = VENTA.COD_EMPLEADO 
GROUP BY  EMPLEADO.SALARIO, EMPLEADO.NOM_EMPLEADO, EMPLEADO.A_PATERNO
HAVING COUNT(VENTA.FOLIO)> 1
ORDER BY EMPLEADO.NOM_EMPLEADO ASC, EMPLEADO.A_PATERNO DESC;

--- SOLUCION 7 ---

SELECT EMPLEADO.NOM_EMPLEADO "NOMBRE", EMPLEADO.A_PATERNO "APELLIDO",
       EMPLEADO.DIRECCION "DIRECCION", EMPLEADO.FECHNAC_EMPLEADO "FECHA NACIMIENTO", 
       EXTRACT(YEAR FROM SYSDATE)-EXTRACT(YEAR FROM EMPLEADO.FECH_INCORPORACION) "A�OS TRABAJANDO",
       EXTRACT(YEAR FROM SYSDATE)-EXTRACT(YEAR FROM EMPLEADO.FECH_INCORPORACION)
	   ||SUBSTR(EMPLEADO.A_PATERNO,-2)||EXTRACT(YEAR FROM EMPLEADO.FECHNAC_EMPLEADO)||
	   '@ventas.econofarmacos.cl' "CORREO ELECTR�NICO"
FROM EMPLEADO JOIN VENTA ON EMPLEADO.COD_EMPLEADO = VENTA.COD_EMPLEADO
WHERE MONTHS_BETWEEN(SYSDATE,EMPLEADO.FECH_INCORPORACION) > 24
GROUP BY EMPLEADO.NOM_EMPLEADO, EMPLEADO.A_PATERNO, EMPLEADO.DIRECCION, 
         EMPLEADO.FECHNAC_EMPLEADO, EXTRACT(YEAR FROM SYSDATE)-EXTRACT(YEAR FROM EMPLEADO.FECH_INCORPORACION),
       EXTRACT(YEAR FROM SYSDATE)-EXTRACT(YEAR FROM EMPLEADO.FECH_INCORPORACION)
	   ||SUBSTR(EMPLEADO.A_PATERNO,-2)||EXTRACT(YEAR FROM EMPLEADO.FECHNAC_EMPLEADO)||
	   '@ventas.econofarmacos.cl'
HAVING COUNT(VENTA.FOLIO) < 3
ORDER BY EMPLEADO.A_PATERNO DESC, EMPLEADO.NOM_EMPLEADO ASC;

--- SOLUCION 8 ---

SELECT * FROM VENTA
INTERSECT
SELECT * FROM VENTAS;

--- SOLUCION 9 ---

INSERT INTO INFORME_VENTAS(FOLIO,FECHA_VENTA,VALOR_TOTAL,FORMA_PAGO,COD_EMPLEADO,
						   COD_MEDICAMENTO, CANTIDAD,DETALLE_VENTA)
						(SELECT VENTAS.FOLIO,VENTAS.FECHA_VENTA,VENTAS.VALOR_TOTAL,VENTAS.FORMA_PAGO,
							   VENTAS.COD_EMPLEADO,DETALLE_VENTA.COD_MEDICAMENTO, 
							   DETALLE_VENTA.CANTIDAD, DETALLE_VENTA.DETALLE_VENTA
						FROM VENTAS LEFT OUTER JOIN DETALLE_VENTA 
							 ON Ventas.FOLIO = DETALLE_VENTA.FOLIO
						MINUS
						SELECT VENTAS.FOLIO,VENTAS.FECHA_VENTA,VENTAS.VALOR_TOTAL,VENTAS.FORMA_PAGO,
							   VENTAS.COD_EMPLEADO,DETALLE_VENTA.COD_MEDICAMENTO, 
							   DETALLE_VENTA.CANTIDAD, DETALLE_VENTA.DETALLE_VENTA
						FROM VENTAS JOIN DETALLE_VENTA 
							 ON Ventas.FOLIO = DETALLE_VENTA.FOLIO);
						
--- SOLUCION 10 ---

UPDATE MEDICAMENTO
SET PRECIO_MEDICAMENTO = (PRECIO_MEDICAMENTO*1.025)
WHERE COD_MEDICAMENTO IN (SELECT MEDICAMENTO.COD_MEDICAMENTO
                       FROM MEDICAMENTO, MEDICAMENT_RESP
                       WHERE MEDICAMENTO.COD_MEDICAMENTO = MEDICAMENT_RESP.COD_MEDICAMENTO 
                       AND MEDICAMENTO.PRECIO_MEDICAMENTO != MEDICAMENT_RESP.PRECIO_MEDICAMENTO);
