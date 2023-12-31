# Write your MySQL query statement below
select name from Employee E
inner join
(select  count(*) as NumOFemp,managerId from Employee 
where managerid is not null
group by managerId
having NumOFemp>4 ) as A
on E.id = A.managerId