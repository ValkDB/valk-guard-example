// Package goqu demonstrates LEFT JOIN query patterns with Goqu.
package goqu

import (
	"context"
	"database/sql"

	goqulib "github.com/doug-martin/goqu/v9"
)

// JoinAuditStore demonstrates safe and broken LEFT JOIN queries.
type JoinAuditStore struct {
	db *goqulib.Database
}

// NewJoinAuditStore creates a new JoinAuditStore.
func NewJoinAuditStore(db *sql.DB) *JoinAuditStore {
	return &JoinAuditStore{db: goqulib.New("postgres", db)}
}

// ListUserOrderStatus demonstrates a safe LEFT JOIN query.
func (s *JoinAuditStore) ListUserOrderStatus(ctx context.Context) error {
	_ = ctx
	_, _, err := goqulib.From("users").
		LeftJoin(
			goqulib.T("orders"),
			goqulib.On(goqulib.I("orders.user_id").Eq(goqulib.I("users.id"))),
		).
		Select("users.id", "users.email", "orders.status").
		Where(goqulib.I("users.active").Eq(true)).
		Limit(25).
		ToSQL()
	return err
}

// ListBrokenUserOrderStatus demonstrates a broken LEFT JOIN query.
func (s *JoinAuditStore) ListBrokenUserOrderStatus(ctx context.Context) error {
	_ = ctx
	_, _, err := goqulib.From("users").
		LeftJoin(
			goqulib.T("orders"),
			goqulib.On(goqulib.I("orders.user_id").Eq(goqulib.I("users.id"))),
		).
		Select("users.id", "users.email", "orders.ghost_status").
		Where(goqulib.I("orders.missing_flag").Eq("pending")).
		ToSQL()
	return err
}
