# Write your MySQL query statement below
select id, movie, description , rating 
from Cinema c 
where  c.description !='boring' AND c.id % 2 =1 order by rating desc 