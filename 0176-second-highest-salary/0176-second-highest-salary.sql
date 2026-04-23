# Write your MySQL query statement below
-- SELECT DISTINCT salary AS SecondHighestSalary
-- from Employee 
-- order by salary DESC 
-- LIMIT 1 OFFSET 1

select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee)