Create Or Replace View Total_Por_Venta As
Select
    Detalle_Ventas.Id_Venta Venta_Id,
    Sum((Productos.Valor * Detalle_Ventas.Cantidad)) Suma_Venta
From Productos Join Detalle_Ventas On Productos.Id_Producto = Detalle_Ventas.Id_Producto 
Group By Detalle_Ventas.Id_Venta;
Commit;
Select * From Total_Por_Venta;
    
Create Or Replace Procedure Sp_Actualizar_Ventas Is
    V_Suma_Venta Number;
    V_Id_Venta Number;
    Cursor Vcursor1 Is 
    Select Venta_Id,Suma_Venta From Total_Por_Venta;
    --REGISTRO vcursor1%ROWTYPE;
Begin
    Open Vcursor1;
    Loop
        Fetch Vcursor1 Into V_Id_Venta,V_Suma_Venta;
        Exit When Vcursor1%Notfound;
        Update Ventas Set Valor_Neto = V_Suma_Venta Where Id_Venta = V_Id_Venta;
        Update Ventas Set Iva = Trunc((V_Suma_Venta*0.19)) Where Id_Venta = V_Id_Venta;
        Update Ventas Set Valor_Total = Trunc((V_Suma_Venta*1.19)) Where Id_Venta = V_Id_Venta;
    End Loop;
    Close Vcursor1;
Exception
    When No_Data_Found Then
        Dbms_Output.Put_Line('No hay datos');
    When Others Then
        Dbms_Output.Put_Line('error inesperado');
End;
/

select * from Productos Join Detalle_Ventas On Productos.Id_Producto = Detalle_Ventas.Id_Producto order by detalle_ventas.id_venta;
