--04-09--Union--------------------
select * from jobs;
select * from job_history;
desc employees;
select * from employees;

--para ver resultados sin duplicados
select employee_id id_empleado, department_id id_departamento
from job_history
union
select employee_id id_empleado, department_id id_departamento
from employees;

--para ver todos los resultados
select employee_id id_empleado, department_id id_departamento
from job_history
union all
select employee_id id_empleado, department_id id_departamento
from employees
order by 1;

--union multtabla
select employee_id id_empleado, j.department_id id_departamento, department_name nombre
from job_history j inner join departments d
	on j.department_id inner join d.department_id
union
select employee_id id_empleado, d.department_id id_departamento, department_name nombre
from employees e inner join departments de
	on e.department_id = d.department_id;
    
    select employee_id id_empleado, j.department_id id_departamento, department_name nombre
from job_history j inner join departments d
	on j.department_id inner join d.department_id
intersect
select employee_id id_empleado, d.department_id id_departamento, department_name nombre
from employees e inner join departments de
	on e.department_id = d.department_id;

