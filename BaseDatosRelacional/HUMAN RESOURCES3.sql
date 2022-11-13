SELECT department_id departamento, MAX(salary),COUNT(*), AVG(salary)
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5 AND MAX(salary) <13000
ORDER BY department_id