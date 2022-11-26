# Write your MySQL query statement below

SELECT DISTINCT sp.name
FROM SalesPerson sp LEFT JOIN Orders o ON sp.sales_id = o.sales_id
WHERE sp.sales_id NOT IN (SELECT sales_id
                            FROM Orders JOIN Company ON Orders.com_id = Company.com_id
                            WHERE name = 'RED');