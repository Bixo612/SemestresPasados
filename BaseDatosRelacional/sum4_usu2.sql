Create Or Replace Trigger Tr_ventas_2
AFTER Insert Or Update on detalle_ventas
For Each Row
Declare

Begin    
    Sp_Actualizar_Ventas();
End;
/
    
Create Or Replace Trigger Tr_ventas_3
AFTER delete on detalle_ventas
For Each Row
Declare

Begin 
    update ventas set
        valor_neto = 0,
        iva = 0,
        valor_total = 0
    where 
    Sp_Actualizar_Ventas();
End;
/
    