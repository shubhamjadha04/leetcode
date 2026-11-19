
WITH ranked_reviews AS (
    SELECT
        e.employee_id,
        e.name,
        p.review_id,
        p.review_date,
        p.rating,

        ROW_NUMBER() OVER (
            PARTITION BY e.employee_id
            ORDER BY p.review_date DESC, p.review_id DESC
        ) AS rn

    FROM employees e
    INNER JOIN performance_reviews p
        ON e.employee_id = p.employee_id
),

last_three AS (
    SELECT *
    FROM ranked_reviews
    WHERE rn <= 3
),

employee_ratings AS (
    SELECT
        employee_id,
        name,

        MAX(CASE WHEN rn = 3 THEN rating END) AS first_rating,
        MAX(CASE WHEN rn = 2 THEN rating END) AS second_rating,
        MAX(CASE WHEN rn = 1 THEN rating END) AS latest_rating

    FROM last_three
    GROUP BY employee_id, name
    HAVING COUNT(*) = 3
)

SELECT
    employee_id,
    name,
    latest_rating - first_rating AS improvement_score

FROM employee_ratings

WHERE first_rating < second_rating
  AND second_rating < latest_rating

ORDER BY
    improvement_score DESC,
    name ASC;
