Select Productos.Id_Producto,Productos.Valor From Productos;
Select Detalle_Ventas.Id_Producto,Detalle_Ventas.Id_Venta,Detalle_Ventas.Cantidad From Detalle_Ventas ;
Select Ventas.Id_Venta,Ventas.Valor_Neto From Ventas;
----
CREATE or replace VIEW TOTAL_POR_VENTA AS
SELECT
    detalle_ventas.id_venta VENTA_ID,
    SUM((productos.valor * detalle_ventas.cantidad)) SUMA_VENTA
FROM productos JOIN detalle_ventas on productos.id_producto = detalle_ventas.id_producto 
GROUP BY detalle_ventas.id_venta ORDER BY 1;
COMMIT;
----
create or replace procedure act_ventas as
    cursor c1 is SELECT suma_venta,VENTA_ID FROM total_por_venta;
    REGISTRO C1%ROWTYPE;
begin
    open c1;
    loop 
        FETCH C1 INTO REGISTRO;
        EXIT WHEN C1%NOTFOUND;
        UPDATE VENTAS SET valor_neto = suma_venta WHERE id_venta = VENTA_ID;
    END LOOP;
    CLOSE C1;
END
;
/
-----
select * from ventas;
select * from total_por_venta;
--UPDATE VENTAS SET valor_neto = 150 WHERE id_venta = 1;
ROLLBACK;