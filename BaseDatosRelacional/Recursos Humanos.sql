select * from employees;

select d.department_id, d.location_id, d.department_name, e.employee_id, e.salary, e.first_name||' '||e.last_name 
from departments d,employees e
where d.department_id = e.department_id;	

select d.department_id, d.location_id, d.department_name, e.employee_id, e.salary, e.first_name||' '||e.last_name, l.city 
from departments d,employees e, locations l
where d.department_id = e.department_id and d.location_id = l.location_id;

select d.department_id, d.location_id, d.department_name, e.employee_id, e.salary, 
		e.first_name||' '||e.last_name, l.city 
from departments d,employees e, locations l
where d.department_id = e.department_id and d.location_id = l.location_id
group by d.department_id, d.location_id, d.department_name, e.employee_id, e.salary, 
		e.first_name||' '||e.last_name, l.city
having salary < (select avg (salary) from employees);	