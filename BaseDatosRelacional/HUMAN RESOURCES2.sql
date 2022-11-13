DESC employees;

SELECT *
FROM employees
WHERE department_id = 1 or department_id = 100 or department_id = 20 or department_id = 40;

---- IN
SELECT *
FROM employees
WHERE department_id IN (1,100,20,40);

SELECT *
FROM employees
WHERE department_id = 1 or department_id = 40 or department_id = 20 
	or department_id = 100 AND first_name LIKE '%i%';
    
SELECT *
FROM employees
WHERE department_id IN (1,100,20,40) AND first_name LIKE '%i%';

-- Funciona con todo los tipos de elementos pero deben ser busquedas exactas
SELECT *
FROM employees
WHERE first_name IN ('i','%a%');

SELECT *
FROM employees
WHERE first_name IN ('Susan','Kevin','John');

select * from employees;