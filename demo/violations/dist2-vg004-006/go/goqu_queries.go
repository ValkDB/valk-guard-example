package demo

import goqulib "github.com/doug-martin/goqu/v9"

func GoquViolations() {
	_ = goqulib.L("SELECT id, email FROM users WHERE active = true")
	_ = goqulib.L("SELECT id FROM users WHERE email LIKE '%@example.com' LIMIT 1")
	_ = goqulib.L("SELECT id FROM users FOR UPDATE")
}
