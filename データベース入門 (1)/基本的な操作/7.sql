WITH ranked_results AS (
    SELECT email, game_id, score FROM results
    EXCEPT
    SELECT email, game_id, score FROM optout
)
SELECT
    email
FROM
    ranked_results
GROUP BY
    email
ORDER BY
    SUM(score) DESC
LIMIT 10;
