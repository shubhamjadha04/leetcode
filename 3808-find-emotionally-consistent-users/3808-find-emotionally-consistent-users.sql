
WITH reaction_counts AS (
    SELECT
        user_id,
        reaction,
        COUNT(*) AS reaction_count
    FROM Reactions
    GROUP BY user_id, reaction
),
ranked_reactions AS (
    SELECT
        user_id,
        reaction,
        reaction_count,
        SUM(reaction_count) OVER (
            PARTITION BY user_id
        ) AS total_reactions,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY reaction_count DESC, reaction
        ) AS rn
    FROM reaction_counts
),
user_items AS (
    SELECT
        user_id,
        COUNT(DISTINCT content_id) AS total_items
    FROM Reactions
    GROUP BY user_id
)
SELECT
    r.user_id,
    r.reaction AS dominant_reaction,
    ROUND(r.reaction_count / r.total_reactions, 2) AS reaction_ratio
FROM ranked_reactions r
JOIN user_items u
    ON r.user_id = u.user_id
WHERE r.rn = 1
  AND u.total_items >= 5
  AND r.reaction_count / r.total_reactions >= 0.60
ORDER BY reaction_ratio DESC, r.user_id ASC;