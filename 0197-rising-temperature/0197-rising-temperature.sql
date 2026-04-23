# Write your MySQL query statement below
SELECT w1.id from Weather w1 INNER JOIN Weather w2 WHERE datediff(w1.recordDate, w2.recordDate) = 1 and w1.temperature > w2.temperature;