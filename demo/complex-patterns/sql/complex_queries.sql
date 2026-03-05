-- CTE with bounded outer select.
WITH active_users AS (
    SELECT users.id, users.email
    FROM users
    WHERE users.active = true
)
SELECT active_users.id, active_users.email
FROM active_users
ORDER BY active_users.id
LIMIT 50;

-- UNION ALL with explicit projection and limit.
SELECT users.id, users.email
FROM users
WHERE users.active = true
UNION ALL
SELECT users.id, users.email
FROM users
WHERE users.active = false
LIMIT 100;

-- LEFT JOIN with qualified columns.
SELECT users.id, users.email, orders.status
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE users.id > 0
ORDER BY users.id
LIMIT 100;
