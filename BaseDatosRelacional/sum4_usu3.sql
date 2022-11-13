



commit;

EXEC Sp_Actualizar_Ventas();

SELECT * FROM detalle_ventas where id_venta = 2;
select * from total_por_venta where venta_id = 2;
SELECT * FROM ventas where id_venta = 2;
update ventas set valor_neto = 0,Iva = 0, Valor_Total = 0
        where id_venta = 2;
delete from detalle_ventas WHERE id_venta = 2;
insert into detalle_ventas VALUES (3,2,4);
insert into detalle_ventas VALUES (5,2,1);



