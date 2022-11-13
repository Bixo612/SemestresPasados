---27-08---------------------------------------------------------
desc countries; --para describir una tabla
desc departments;
desc employees;

--muestra la tabala employees pero esta tiene el valor department_id pero no el nombre del departamento
select * from employees;
--muestra la lista de departamentos con el nombre
select * from departments;

--SUBCONSULTAS

select * from employees
where department_id in (select department_id--primero se resuelve esta sub consulta
                        from departments    --y despues resuelve la consulta anterior
                        where department_name = 'Shipping');
