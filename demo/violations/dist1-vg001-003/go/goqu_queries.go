package demo

import goqulib "github.com/doug-martin/goqu/v9"

func GoquViolations() {
	_ = goqulib.L("SELECT * FROM users LIMIT 1")
	_ = goqulib.L("UPDATE users SET active = false")
	_ = goqulib.L("DELETE FROM orders")
}
