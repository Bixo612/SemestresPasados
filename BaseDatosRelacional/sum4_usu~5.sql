Create Or Replace Trigger Tr_ventas
AFTER Insert Or Update on detalle_ventas
For Each Row
Declare

Begin

    Sp_Actualizar_Ventas();

End;
/

desc detalle_ventas;
select * from total_por_venta;
desc total_por_venta;

select * from ventas where id_venta = 2;
select * from detalle_ventas where id_venta = 2;

insert into detalle_ventas VALUES (5,2,1);