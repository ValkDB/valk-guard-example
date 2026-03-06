package demo

import (
	"context"
	"database/sql"
)

func StdViolations(db *sql.DB) {
	ctx := context.Background()
	_, _ = db.QueryContext(ctx, "SELECT * FROM users LIMIT 1")
	_, _ = db.ExecContext(ctx, "UPDATE users SET active = false")
	_, _ = db.ExecContext(ctx, "DELETE FROM orders")
}
