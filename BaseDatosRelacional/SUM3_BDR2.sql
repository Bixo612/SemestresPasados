--Cree una funci�n llamada fn_jubilacion que permita determinar cu�nto tiempo 
--queda para la edad de jubilaci�n de una persona, para ello la funci�n debe 
--considerar que debe ingresar una fecha de nacimiento y un valor (�m� o �f�) 
--para determinar el sexo masculino o femenino, y de acuerdo o ingresado 
--indicar cuantos d�as quedan para que la persona entre en edad de jubilaci�n, 
--para ello debe considerar que la edad de jubilaci�n es de 60 a�os para las 
--mujeres y 65 a�os para los hombres.
--DIA / MES / A�O
Create Or Replace Function  Fn_Jubilacion (Fecha_Nac Date , Sexo Varchar2) 
Return Number Is
    Anio_Nac NUMBER;
    Anio_Act NUMBER;
    EDAD NUMBER;
    Resultado Number;
Begin   
    Anio_Nac := To_Char(Extract(Year From Fecha_Nac));
    Anio_Act := To_Char(Extract(Year From SYSDATE));
    EDAD := (anio_act-anio_nac);
    
    IF SEXO LIKE 'm' then
        resultado := (65-edad);
    elsif SEXO LIKE 'f' then
        resultado := (60-edad);
    else
        resultado := 0;
    end if;
    Return resultado;
End;
/
--
Declare
    V_Nombre Varchar2(25) := 'Pablo';  
    V_Fecha_Nac Date := (Sysdate-9800);
    V_Sexo Varchar2(1) :='m';
Begin
    Dbms_Output.Put_Line('Los a�os faltantes para la jubilacion de '||V_Nombre||' son ' ||Fn_Jubilacion(V_Fecha_Nac,V_Sexo));
End;
/
