set SERVEROUTPUT on;

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