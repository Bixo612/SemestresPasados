--Vicente Vasquez Galvez 19360397-1

--Debe crear un sinónimo para la tabla municipalidades que se llame municipios, un sinónimo para la tabla juzgados_policia_local que se llame juzgado y un sinónimo a la tabla funcionarios_muinicipales que se llame funcionario.

Create Synonym Municipios For Sum3_Bdr.Municipalidades; 
Create Synonym Juzgado For Sum3_Bdr.Juzgados_Policia_Local; 
Create Synonym Funcionario For Sum3_Bdr.Funcionarios_Muinicipales; 

--Debe crear una vista llamada detalle_infraccion que permita ver el nro_multa, fecha_infraccion, motivo_infraccion, rut_inspector, nombre_juzgado, municipalidad, patente_infractora, marca y modelo del vehículo involucrado.

CREATE VIEW Detalle_Infraccion AS
Select  
    Multas.Nro_Multa,
    Multas.Fecha_Infraccion,
    Multas.Motivo_Infraccion,
    Inspectores.Rut_Inspector,
    Juzgados_Policia_Local.Nombre_Juzgado,
    Municipalidades.Comuna MUNICIPALIDAD,
    Multas.Patente_Infractora,
    Vehiculos.Marca,
    Vehiculos.Modelo    
From Multas 
    Join Inspectores On Multas.Inspector_Observador = Inspectores.Id_Inspector
    Join Juzgados_Policia_Local On Multas.Juzgado_Comparecencia = Juzgados_Policia_Local.Id_Juzgado
    Join Vehiculos On Multas.Patente_Infractora = Vehiculos.Placa_Patente
    Join Municipalidades On Juzgados_Policia_Local.Municipalidad = Municipalidades.Id_Municipalidad
;

Select * From Detalle_Infraccion;

--Realice un índice que permita una mejor búsqueda de los datos por medio de la patente_infractora en la tabla multas.

Create Index Patente_Infractora On Multas(Patente_Infractora);

--Realice un índice que permita una mejor búsqueda de los rut_inspector en la tabla inspectores.

Create Index Rut_Inspector On Inspectores(Rut_Inspector);

--Elimine las vistas llamada vista_temporal, vista_provisoria y vista_momentanea de la base de datos.

Drop View Vista_Temporal;
Drop View Vista_Provisoria;
Drop View Vista_Momentanea;

--Cree un bloque anónimo que permita ver el rut, en nombre completo, el correo electrónico y la fecha de nacimiento del inspector que tenga el id 1.

--
Create View Detalle_Inspector As
Select 
    Inspectores.Rut_Inspector,
    Funcionarios_Municipales.Primer_Nombre||' '||
    Funcionarios_Municipales.Segundo_Nombre||' '||
    Funcionarios_Municipales.Primer_Apellido||' '||
    Funcionarios_Municipales.Segundo_Apellido Nombre_Completo,
    Funcionarios_Municipales.Correo_Electronico,
    Funcionarios_Municipales.Fecha_Nacimiento,
    Inspectores.Id_Inspector
From
    Inspectores Join Funcionarios_Municipales On Inspectores.Rut_Inspector = Funcionarios_Municipales.Rut;
--
Declare 
    V_Rut_Inspector Detalle_Inspector.Rut_Inspector%Type;
    V_Nombre_Completo Detalle_Inspector.Nombre_Completo%Type;
    V_Correo_Electronico Detalle_Inspector.Correo_Electronico%Type;
    V_Fecha_Nacimiento Detalle_Inspector.Fecha_Nacimiento%Type;
Begin
    SELECT Rut_Inspector, Nombre_Completo, Correo_Electronico, Fecha_Nacimiento 
    into V_Rut_Inspector, V_Nombre_Completo, V_Correo_Electronico, V_Fecha_Nacimiento
    from detalle_inspector where id_inspector = 1;
    Dbms_Output.Put_Line('Nombre completo: '||V_Nombre_Completo|| ' / Rut: '||V_Rut_Inspector||' / Coreo: '|| V_Correo_Electronico|| ' / Fecha de nacimiento: '||V_Fecha_Nacimiento);
End;
/

--Cree un bloque anónimo que permita saber cuántas multas posee la patente HFCK69 en la tabla multas, indicando también cual es la marca y el modelo del vehículo.

Create View Registro_Patente As
Select 
    Multas.Patente_Infractora Patente, 
    Vehiculos.Marca Marca, 
    Vehiculos.Modelo Modelo
From Multas Inner Join Vehiculos On Vehiculos.Placa_Patente = Multas.Patente_Infractora;
--
Declare 
    V_Patente Registro_Patente.Patente%Type;
    V_Modelo Registro_Patente.Modelo%Type;
    V_Marca Registro_Patente.Marca%Type;
Begin
    Select Count (Patente), Modelo, Marca Into V_Patente, V_Modelo, V_Marca
    From Registro_Patente Where Patente Like 'HFCK69' Group By Modelo,Marca;
    Dbms_Output.Put_Line('Numero de multas: '||V_Patente|| ' / Modelo: '||V_Modelo||' / Marca: '|| V_Marca);
End;
/

--Cree un procedimiento almacenado llamado sp_informe juzgados que muestre la información de los juzgados de policía local asociados a una municipalidad en específico, para ello se solicita que ingrese el nombre de la comuna que se requiere saber por parámetros y que despliegue esa información por medio del terminal.

Create View Informe_Juzgados As
Select 
    Juzgados_Policia_Local.Id_Juzgado,
    Juzgados_Policia_Local.Nombre_Juzgado,
    Municipalidades.Comuna
From Juzgados_Policia_Local Join Municipalidades On Juzgados_Policia_Local.Municipalidad = Municipalidades.Id_Municipalidad;
--
Create Or Replace Procedure Sp_Informe_Juzgados(V_Comuna In Municipalidades.Comuna%Type) As 
    Cursor V_Cursor1 Is Select Id_Juzgado,Nombre_Juzgado 
                From Informe_Juzgados Where Comuna Like V_Comuna Order By  Id_Juzgado;
    Registro V_Cursor1%Rowtype;
Begin
    Dbms_Output.Put_Line('Los juzgados de la comuna ' || V_Comuna || ' son:');
    Open V_Cursor1;
    Loop
        Fetch V_Cursor1 Into Registro;
        Exit When V_Cursor1%Notfound;
        Dbms_Output.Put_Line('Id del juzgado: '||Registro.Id_Juzgado|| ' / Nombre '|| Registro.Nombre_Juzgado);
    End Loop;
    Close V_Cursor1;
Exception
    When No_Data_Found Then
        Dbms_Output.Put_Line('Oh rayos no hay datos');
    When Others Then
        Dbms_Output.Put_Line('Oh rayos algo paso y no se que es :c');
End;
/
--
Begin 
    Sp_Informe_Juzgados('PROVIDENCIA');
End;
/

--Cree una función llamada fn_jubilacion que permita determinar cuánto tiempo queda para la edad de jubilación de una persona, para ello la función debe considerar que debe ingresar una fecha de nacimiento y un valor (‘m’ o ‘f’) para determinar el sexo masculino o femenino, y de acuerdo o ingresado indicar cuantos días quedan para que la persona entre en edad de jubilación, para ello debe considerar que la edad de jubilación es de 60 años para las mujeres y 65 años para los hombres.

Create Or Replace Function  Fn_Jubilacion (Fecha_Nac Date , Sexo Varchar2) 
Return Number Is
    Anio_Nac Number;
    Anio_Act Number;
    Edad Number;
    Resultado Number;
Begin   
    Anio_Nac := To_Char(Extract(Year From Fecha_Nac));
    Anio_Act := To_Char(Extract(Year From Sysdate));
    Edad := (Anio_Act-Anio_Nac);
    
    If Sexo Like 'm' Then
        Resultado := (65-Edad);
    Elsif Sexo Like 'f' Then
        Resultado := (60-Edad);
    End If;
    Return Resultado;
End;
/
--
Declare
    V_Nombre Varchar2(25) := 'Pablo';  
    V_Fecha_Nac Date := (Sysdate-9800);
    V_Sexo Varchar2(1) :='m';
Begin
    Dbms_Output.Put_Line('Los años faltantes para la jubilacion de '||V_Nombre||' son ' ||Fn_Jubilacion(V_Fecha_Nac,V_Sexo));
End;
/

--Cree un trigger que permita el monitoreo de la tabla multas, para ello debe indicar que tipo de acción se realizó (inserción, actualización o eliminación de datos), cual es la fecha en la que fue realizada la acción y el nombre del usuario que realizó la acción, esta información debe ser guardada en la tabla log_multas que se encuentra en la base de datos, para ingresar la llave primaria debe utilizar la secuencia sq_log.

Create Or Replace Trigger Tr_Multas
Before Insert Or Update Or Delete On Multas
For Each Row 
Declare 
    Accion Varchar2(15);
Begin 
    If Inserting Then
        Accion := 'Insercion';
        Insert Into Log_Multas(Id_Log,Accion,Fecha,Usuario)
            Values(Sq_Log.Nextval,Accion,Sysdate,User);
    --
    Elsif Updating Then
        Accion := 'Actualizacion';
        Insert Into Log_Multas(Id_Log,Accion,Fecha,Usuario)
            Values(Sq_Log.Nextval,Accion,Sysdate,User);
    --
    Else
        Accion := 'Eliminacion';
        Insert Into Log_Multas(Id_Log,Accion,Fecha,Usuario)
            Values(Sq_Log.Nextval,Accion,Sysdate,User);
    --
    End If;
End;
/