# Write your MySQL query statement below
select distinct l.num as ConsecutiveNums
from logs l , logs l1 , logs l2 
where l.id = l1.id -1 and l.num = l1.num
and l1.id = l2.id -1 and l2.num = l1.num