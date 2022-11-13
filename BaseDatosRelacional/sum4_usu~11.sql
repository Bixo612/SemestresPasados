--8

Set Serveroutput On;
Create Or Replace Procedure Sp_Ingreso_Productos (Id_Producto In Int,
Marca In Varchar2,
Descripcion In Varchar2,
Cantidad In Int,
Valor In Int)
As
Begin
Insert Into Productos("Id_Producto","Marca","Descripcion","Cantidad","Valor")
Values (Id_Producto,Marca,Descripcion,Cantidad,Valor);

End Sp_Ingreso_Productos;
/

Begin
Sp_Ingreso_Productos (SQ_PRODUCTOS.nextval,'Ferrero','Nutella',40,2500);
Dbms_Output.Put_Line('===========Producto Ingresado Correctamente=============');
Commit;
End;
/

--9

Set Serveroutput On;
Create Or Replace Procedure Sp_Ingreso_Vendedores (Id_Vendedor In Number,
	Rut In Number,
	Primer_Nombre In Varchar2,
	Segundo_Nombre In Varchar2,
	Primer_Apellido In Varchar2,
	Segundo_Apellido In Varchar2,
	Correo_Electronico In Varchar2,
	Direccion In Varchar2,
	Fecha_Nacimiento In Date) As
Begin
	Insert Into Vendedores("Id_Vendedor","Rut","Primer_Nombre","Segundo_Nombre","Primer_Apellido","Segundo_Apellido","Correo_Electronico","Direccion","Fecha_Nacimiento")
	Values (Id_Vendedor,Rut,Primer_Nombre,Segundo_Nombre,Primer_Apellido,Segundo_Apellido, Correo_Electronico,Direccion,Fecha_Nacimiento );

End Sp_Ingreso_Vendedores;
/

Begin
	Sp_Ingreso_Vendedores (SQ_VENDEDORES.nextval,19123123-1,'Marco','Antonio','Flores', 'Gonsalez', 'Mantonino@Ventas.cl','Isla Guafo 8934', (Sysdate-15000));	
	Dbms_Output.Put_Line('===========Vendedor Ingresado Correctamente=============');
Commit;
End;