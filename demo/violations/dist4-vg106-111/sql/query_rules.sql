SELECT q_users.id FROM q_users WHERE ghost_col = 1 LIMIT 1;
SELECT q_users.id FROM q_users INNER JOIN ghost_orders ON q_users.id = ghost_orders.user_id LIMIT 1;
SELECT id FROM q_users INNER JOIN q_orders ON q_users.id = q_orders.user_id LIMIT 1;
