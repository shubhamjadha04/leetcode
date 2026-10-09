# Write your MySQL query statement below
select user_id,
ROUND(AVG(CASE
        WHEN activity_type = "free_trial" THEN activity_duration ELSE NULL END
),2) as trial_avg_duration,

ROUND(AVG(CASE
        WHEN activity_type = "paid" THEN activity_duration ELSE NULL END
),2) as paid_avg_duration

from UserActivity
group by user_id
having count(case 
        WHEN activity_type = "paid" THEN 1 ELSE NULL END
        ) >=1
        AND
        count(case 
        WHEN activity_type = "free_trial" THEN 1 ELSE NULL END
        ) >=1

ORDER BY user_id;