# Write your MySQL query statement below

SELECT d.name AS Department , e.name AS "Employee", e.salary AS Salary FROM Employee e RIGHT JOIN Department d on e.departmentId=d.id WHERE salary = (
    SELECT MAX(e1.salary) AS Salary FROM Employee e1 WHERE e1.departmentId=e.departmentId GROUP BY e1.departmentId 
);
