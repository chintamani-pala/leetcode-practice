# Write your MySQL query statement below

-- DELETE FROM Person p where p.id not in (SELECT * FROM (SELECT min(id) as "id" from Person group by email) as temp);

delete p1 from Person p1 INNER JOIN Person p2 ON p1.email = p2.email and p1.id>p2.id;