create or replace Trigger Tr_ventas_1
After Insert On detalle_ventas
For Each Row
Declare
    total_nuevo NUMBER;
Begin
    update ventas set
            valor_neto  = 0,
            Iva         = 0,
            Valor_Total = 0
    where id_venta = :new.ID_VENTA;
    SELECT SUMA_VENTA into total_nuevo 
    FROM total_por_venta where venta_id = :new.ID_VENTA;
    update ventas set
            valor_neto  = total_nuevo,
            Iva         = Trunc((total_nuevo*0.19)),
            Valor_Total = Trunc((total_nuevo*1.19))
        where id_venta = :new.ID_VENTA;
end;
/
create or replace Trigger Tr_ventas_2
After DELETE On detalle_ventas
For Each Row
Declare
    total_nuevo NUMBER;
Begin
    update ventas set
            valor_neto  = 0,
            Iva         = 0,
            Valor_Total = 0
        where id_venta = :new.ID_VENTA;
    SELECT SUMA_VENTA into total_nuevo 
    FROM total_por_venta where venta_id = :new.ID_VENTA;
    update ventas set
            valor_neto  = total_nuevo,
            Iva         = Trunc((total_nuevo*0.19)),
            Valor_Total = Trunc((total_nuevo*1.19))
        where id_venta = :new.ID_VENTA;
end;
/
create or replace Trigger Tr_ventas_3
After UPDATE On detalle_ventas
For Each Row
Declare
    total_nuevo NUMBER;
Begin
    update ventas set
            valor_neto  = 0,
            Iva         = 0,
            Valor_Total = 0
        where id_venta = :old.ID_VENTA;
    SELECT SUMA_VENTA into total_nuevo 
    FROM total_por_venta where venta_id = :old.ID_VENTA;  
    update ventas set
            valor_neto  = total_nuevo,
            Iva         = Trunc((total_nuevo*0.19)),
            Valor_Total = Trunc((total_nuevo*1.19))
        where id_venta = :old.ID_VENTA;
end;
/





