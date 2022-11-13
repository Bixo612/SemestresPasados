select productos.id_producto,productos.valor from productos;
select detalle_ventas.id_producto,detalle_ventas.id_venta,detalle_ventas.cantidad from detalle_ventas ;
select ventas.id_venta,ventas.valor_neto from ventas;
select productos.valor,detalle_ventas.cantidad,  detalle_ventas.id_venta
from productos JOIN detalle_ventas on productos.id_producto = detalle_ventas.id_producto where detalle_ventas.id_venta;
---
CREATE or replace VIEW TOTAL_POR_VENTA AS    
SELECT
    detalle_ventas.id_venta VENTA_ID,
    SUM((productos.valor * detalle_ventas.cantidad)) SUMA_VENTA
FROM productos JOIN detalle_ventas on productos.id_producto = detalle_ventas.id_producto 
GROUP BY detalle_ventas.id_venta;

SELECT * FROM TOTAL_POR_VENTA;

COMMIT;

create or replace procedure act_ventas is
    cursor c1 is SELECT suma_venta,VENTA_ID FROM total_por_venta;
   -- REGISTRO C1%ROWTYPE;
   v_sum := 0;
   v_id :=0
begin 
    --open c1;
    loop 
        --FETCH C1 INTO REGISTRO;
        --EXIT WHEN C1%NOTFOUND;
        UPDATE VENTAS SET valor_neto = v_sum WHERE id_venta = v_id;
    END LOOP;
    CLOSE C1;
END
;




/
select * from ventas;
UPDATE VENTAS SET valor_neto = 150 WHERE id_venta = 1;
ROLLBACK;
