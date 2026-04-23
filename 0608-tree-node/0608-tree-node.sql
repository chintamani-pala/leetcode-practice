# Write your MySQL query statement below
SELECT t.id, 
    CASE
        WHEN t.p_id IS NULL THEN 'Root'
        WHEN t.id IN(SELECT DISTINCT p_id from Tree WHERE p_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
from Tree t;