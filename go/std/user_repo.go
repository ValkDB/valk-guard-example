// Package std demonstrates Go's standard database/sql usage.
package std

import (
	"context"
	"database/sql"
)

// UserRepo provides user-related database operations.
type UserRepo struct {
	db *sql.DB
}

// NewUserRepo creates a new UserRepo.
func NewUserRepo(db *sql.DB) *UserRepo {
	return &UserRepo{db: db}
}

// GetByID retrieves a user by ID.
func (r *UserRepo) GetByID(ctx context.Context, id int64) *sql.Row {
	return r.db.QueryRowContext(ctx, "SELECT id, email, name, active FROM users WHERE id = $1 LIMIT 1", id)
}

// GetRecent retrieves recent active users with a limit.
func (r *UserRepo) GetRecent(ctx context.Context) (*sql.Rows, error) {
	return r.db.QueryContext(ctx, "SELECT id, email, name FROM users WHERE active = true ORDER BY created_at DESC LIMIT 50")
}

// Deactivate marks a user as inactive.
func (r *UserRepo) Deactivate(ctx context.Context, id int64) (sql.Result, error) {
	return r.db.ExecContext(ctx, "UPDATE users SET active = false, updated_at = NOW() WHERE id = $1", id)
}
