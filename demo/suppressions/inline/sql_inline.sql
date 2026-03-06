-- valk-guard:disable VG001
SELECT * FROM users LIMIT 1;

SELECT * FROM users LIMIT 1;

-- valk-guard:disable
UPDATE users SET active = false;
