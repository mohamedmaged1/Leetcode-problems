select score , DENSE_RANK() over (order by score desc) `rank`  
from Scores 
order by score desc  