# Write your MySQL query statement below
with PreviousWeatherData as 
(
select id , recorddate , 
lag (recorddate,1) over (order by recorddate asc) as previousDate ,
temperature ,
lag (temperature,1) over (order by recorddate asc) as previoustemperature

from Weather
    
)
select id 
from PreviousWeatherData
where temperature >previoustemperature
and recordDate = DATE_ADD(previousDate, INTERVAL 1 DAY)