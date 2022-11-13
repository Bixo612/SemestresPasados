--Cree una función llamada fn_jubilacion que permita determinar cuánto tiempo 
--queda para la edad de jubilación de una persona, para ello la función debe 
--considerar que debe ingresar una fecha de nacimiento y un valor (‘m’ o ‘f’) 
--para determinar el sexo masculino o femenino, y de acuerdo o ingresado 
--indicar cuantos días quedan para que la persona entre en edad de jubilación, 
--para ello debe considerar que la edad de jubilación es de 60 años para las 
--mujeres y 65 años para los hombres.
--DIA / MES / AÑO
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
    Dbms_Output.Put_Line('Los años faltantes para la jubilacion de '||V_Nombre||' son ' ||Fn_Jubilacion(V_Fecha_Nac,V_Sexo));
End;
/
