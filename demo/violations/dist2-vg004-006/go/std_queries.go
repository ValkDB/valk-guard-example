package demo

import (
	"context"
	"database/sql"
)

func StdViolations(db *sql.DB) {
	ctx := context.Background()
	_, _ = db.QueryContext(ctx, "SELECT id, email FROM users WHERE active = true")
	_, _ = db.QueryContext(ctx, "SELECT id FROM users WHERE email LIKE '%@example.com' LIMIT 1")
	_, _ = db.QueryContext(ctx, "SELECT id FROM users FOR UPDATE")
}
