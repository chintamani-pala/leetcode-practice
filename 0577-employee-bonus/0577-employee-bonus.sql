# Write your MySQL query statement below
SELECT e.name as "name", b.bonus as "bonus" from Employee e left join Bonus b on e.empId=b.empId where b.bonus is Null or b.bonus < 1000;