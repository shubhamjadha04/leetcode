# Write your MySQL query statement below
select distinct num as ConsecutiveNums 
from(
    select num,
    LAG(num) over (order by id) as prev_num,
    LEAD(num) over (order by id ) as next_num
    from logs
) t
where num = prev_num and num = next_num;