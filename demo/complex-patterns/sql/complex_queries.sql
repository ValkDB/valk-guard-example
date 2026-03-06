-- CTE: SELECT * + unbounded outer query (intentional violations).
WITH active_users AS (
    SELECT *
    FROM users
    WHERE users.active = true
)
SELECT active_users.id, active_users.email
FROM active_users
ORDER BY active_users.id;

-- UNION ALL: unbounded final result (intentional violation).
SELECT users.id, users.email
FROM users
WHERE users.active = true
UNION ALL
SELECT users.id, users.email
FROM users
WHERE users.active = false;

-- LEFT JOIN: unknown filter column on joined table (intentional violation).
SELECT users.id, users.email, orders.status
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.ghost_status = 'pending'
ORDER BY users.id
LIMIT 100;
