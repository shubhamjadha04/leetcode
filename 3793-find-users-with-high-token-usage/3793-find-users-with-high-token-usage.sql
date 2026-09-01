WITH user_stats AS (
    SELECT
        user_id,
        COUNT(*) AS prompt_count,
        AVG(tokens) AS avg_tokens
    FROM prompts
    GROUP BY user_id
),

qualified_users AS (
    SELECT DISTINCT
        p.user_id
    FROM prompts p
    JOIN user_stats u
        ON p.user_id = u.user_id
    WHERE p.tokens > u.avg_tokens
)

SELECT
    u.user_id,
    u.prompt_count,
    ROUND(u.avg_tokens, 2) AS avg_tokens
FROM user_stats u
JOIN qualified_users q
    ON u.user_id = q.user_id
WHERE u.prompt_count >= 3
ORDER BY avg_tokens DESC, u.user_id ASC;