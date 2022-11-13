ROLLBACK;
SELECT * FROM ventas;
select *FROM detalle_ventas;    
select *FROM comisiones;  

alter trigger tr_comisiones ENABLE;

insert into ventas values(30,(sysdate),7,0,0,100000);

update ventas set valor_total =1000 where id_venta = 30;

delete from ventas where id_venta = 30;

COMMIT;


delete from detalle_ventas where id_venta = 1;
delete from ventas where id_venta = 1;

ROLLBACK;