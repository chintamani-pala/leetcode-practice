# Write your MySQL query statement below
select DISTINCT sp.name from SalesPerson sp left join Orders o on sp.sales_id = o.sales_id left join Company c on c.com_id=o.com_id where "RED" not in (
    select c1.name from SalesPerson sp1 left join Orders o1 on sp1.sales_id = o1.sales_id left join Company c1 on c1.com_id=o1.com_id where sp1.sales_id = sp.sales_id 
) or o.sales_id is null
