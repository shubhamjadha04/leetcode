WITH recovery AS (
    SELECT
        p.patient_id,
        MIN(p.test_date) AS first_positive
    FROM covid_tests p
    WHERE p.result = 'Positive'
    GROUP BY p.patient_id
),

negative AS (
    SELECT
        r.patient_id,
        r.first_positive,
        MIN(c.test_date) AS first_negative
    FROM recovery r
    JOIN covid_tests c
        ON r.patient_id = c.patient_id
    WHERE c.result = 'Negative'
      AND c.test_date > r.first_positive
    GROUP BY r.patient_id, r.first_positive
)

SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(n.first_negative, n.first_positive) AS recovery_time
FROM negative n
JOIN patients p
    ON n.patient_id = p.patient_id
ORDER BY recovery_time ASC, p.patient_name ASC;