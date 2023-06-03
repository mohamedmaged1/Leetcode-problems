with w1 as (select rank() over (partition by DepartmentId order by Salary desc) rankk, 
    DepartmentId, 
    Name, 
    Salary
from Employee) 

select d.name as Department , w.name as employee , w.salary  from w1 w,Department D where rankk=1 and w.departmentid = D.id
