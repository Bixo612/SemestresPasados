
SELECT * FROM TAB;
DESC employees;

SELECT department_id departamento, manager_id ,SUM(salary) suma
FROM employees
WHERE department_id > 50
GROUP BY department_id,manager_id
HAVING SUM(salary) > 10000
ORDER BY department_id DESC;--asc ascendente y desc desendente

SELECT employee_id, first_name, last_name, department_id, manager_id 
FROM employees 
WHERE department_id = 50 AND manager_id = 100;

SELECT employee_id, first_name, last_name, department_id, manager_id 
FROM employees 
WHERE department_id = 50 OR manager_id = 100;

SELECT employee_id, first_name, last_name, department_id, manager_id, commission_pct 
FROM employees WHERE commission_pct is not null;

SELECT employee_id, first_name, last_name, department_id, manager_id 
FROM employees 
WHERE department_id <> 50 and manager_id <> 100;

----------------

SELECT department_id, MAX (salary), COUNT(*), MIN(salary),AVG(salary)
FROM employees
GROUP BY department_id
ORDER BY department_id ASC;

SELECT department_id departamento, MAX(salary),COUNT(*), AVG(salary)
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5 AND MAX(salary) <13000
ORDER BY department_id
