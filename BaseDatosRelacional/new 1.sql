Investigar que es un bloque anónimo, como se realizan y para que sirven.

bloques anónimos, caracterizados porque no tienen nombre y se suelen crear y ejecutar desde PL/SQL.
------------------------------
Es un bloque de código, el cual puede contener cursores, variables, llamados a procedimientos, función y paquetes, también se pueden utilizar estructuras lógicas de un lenguaje de programación

Sentencia básica:

Declare --Habilita la declaración de variables y cursores
                --Variables
                --Cursores
Begin    --Inicio del proceso
                --Proceso lógico
End;      --Fin del proceso

En un bloque anónimo podemos ejecutar sentencias SQL,  como insertar, actualizar, eliminar y consultar datos, para realizar una tarea específica.

Ejemplo: Se solicita actualizar el precio de todos los carros que sean del año 2015 y 2016, agregando 500000 pesos, y mostrar el resultado en pantalla.

Declare --Habilita la declaración de variables y cursores

   Cursor cur_carros in --Creacion del cursor carros
    Select modelo, ano_carro, marca, precio, estado
     From carros
   Where ano_carro in (2015,2016);

Begin    --Inicio del proceso

    Update carros set precio = precio + 500000 --Actualiza el precio de los carros 
      where ano_carro in (2015,2016);

      for carro in cur_carros loop --Recorre el cursor y muestra los resultados en pantalla
        dbms_output.put_line(‘El carro de la marca  ’||carro. marca || ‘ del año ’|| carro. ano_carro ||’ tiene un precio de ’|| carro. Precio||’ millones.’); 
      end loop; --termina de recorrer el cursor
 
End;      --Fin del proceso
---------------------------
begin
 
  DBMS_OUTPUT.PUT_LINE('Hola mundo');
   
end;
/
 
declare
  i number(8) := 1;
begin
   
  while (i<=10)
  loop
    DBMS_OUTPUT.PUT_LINE(i);
    i := i+1;
  end loop;
 
end;
/
 
declare
  v_codigocliente clientes.codigocliente%type := &codigo;
  v_nombrecliente clientes.nombrecliente%type;
begin
 
  select nombrecliente into v_nombrecliente
  from clientes
  where codigocliente = v_codigocliente;
 
  DBMS_OUTPUT.PUT_LINE('El nombre del cliente es ' || v_nombrecliente);
 
exception
  when no_data_found then
    DBMS_OUTPUT.PUT_LINE('No existe el cliente');
 
end;
/

procedimiento almacenado => no retorna valor
							pero puede recibir o no recibir datos
							

































