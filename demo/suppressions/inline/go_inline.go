package suppressions

import (
	"context"
	"database/sql"
)

func GoInlineSuppression(db *sql.DB) {
	ctx := context.Background()

	// valk-guard:disable VG001
	_, _ = db.QueryContext(ctx, "SELECT * FROM users LIMIT 1")

	_, _ = db.QueryContext(ctx, "SELECT * FROM users LIMIT 1")

	// valk-guard:disable
	_, _ = db.ExecContext(ctx, "DELETE FROM orders")
}
