
Create Or Replace Trigger Tr_Comisiones
AFTER Insert Or Update Or Delete On Ventas
For Each Row
Declare

Begin
    If Inserting Then
        Insert Into Comisiones 
        (Id_Comision,Valor_Comision,Fecha_Comision,Vendedor,Venta) 
        Values (1,Trunc((:New.Valor_Total*0.05)),:New.Fecha_Venta,:New.Vendedor,:New.Id_Venta);
    Elsif Updating Then
        Update Comisiones 
        Set Valor_Comision  = Trunc((:New.Valor_Total*0.05)), 
            Fecha_Comision  = :New.Fecha_Venta, 
            Vendedor        = :New.Vendedor,
            Venta = :New.Id_Venta 
        Where Venta = :New.Id_Venta;         
    Else
        Delete From Comisiones 
        Where Venta = :Old.Id_Venta;
    End If;
End;
/