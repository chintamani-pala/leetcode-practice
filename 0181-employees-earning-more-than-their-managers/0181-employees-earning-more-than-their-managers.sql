# Write your MySQL query statement below
SELECT e2.name as "Employee" FROM Employee e1 INNER JOIN Employee e2 WHERE e1.id = e2.managerId and e2.salary > e1.salary;