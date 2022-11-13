Set Serveroutput On;


Create Or Replace Procedure Sp_Ingreso_Vendedores (
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
	Values (SQ_VENDEDORES.nextval,Rut,Primer_Nombre,Segundo_Nombre,Primer_Apellido,Segundo_Apellido, Correo_Electronico,Direccion,Fecha_Nacimiento );

End Sp_Ingreso_Vendedores;
/
Begin
	Sp_Ingreso_Vendedores (19123123-1,'Marco','Antonio','Flores', 'Gonsalez', 'Mantonino@Ventas.cl','Isla Guafo 8934', (Sysdate-15000));	
	Dbms_Output.Put_Line('===========Vendedor Ingresado Correctamente=============');
Commit;
End;



SET SERVEROUTPUT ON;
CREATE OR REPLACE PROCEDURE SP_INGRESO_VENDEDORES (ID_VENDEDOR IN NUMBER,
RUT IN NUMBER,
PRIMER_NOMBRE IN VARCHAR2,
SEGUNDO_NOMBRE IN VARCHAR2,
PRIMER_APELLIDO IN VARCHAR2,
SEGUNDO_APELLIDO IN VARCHAR2,
CORREO_ELECTRONICO IN VARCHAR2,
DIRECCION IN VARCHAR2,
FECHA_NACIMIENTO IN DATE)
AS
BEGIN
insert into VENDEDORES("ID_VENDEDOR","RUT","PRIMER_NOMBRE","SEGUNDO_NOMBRE","PRIMER_APELLIDO","SEGUNDO_APELLIDO","CORREO_ELECTRONICO","DIRECCION","FECHA_NACIMIENTO")
values (ID_VENDEDOR,RUT,PRIMER_NOMBRE,SEGUNDO_NOMBRE,PRIMER_APELLIDO,SEGUNDO_APELLIDO, CORREO_ELECTRONICO,DIRECCION,FECHA_NACIMIENTO );
END SP_INGRESO_VENDEDORES;
/

BEGIN
SP_INGRESO_VENDEDORES (SQ_VENDEDORES.nextval,27411558-1,'DAVID','ANTONIO','INATI', 'WHESLEYSH', 'D.INATI@VENDEDORA.CL','LA ROSALEDA 104', (sysdate-16241));
DBMS_OUTPUT.PUT_LINE('========================================================');
DBMS_OUTPUT.PUT_LINE('===========VENDEDOR INGRESADO CORRECTAMENTE=============');
DBMS_OUTPUT.PUT_LINE('========================================================');
COMMIT;
END;

