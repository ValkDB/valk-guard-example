// Package goqu demonstrates the Goqu query builder usage.
package goqu

import (
	"context"
	"database/sql"

	goqulib "github.com/doug-martin/goqu/v9"
)

// OrderStore provides order-related database operations using Goqu.
type OrderStore struct {
	db *goqulib.Database
}

// NewOrderStore creates a new OrderStore.
func NewOrderStore(db *sql.DB) *OrderStore {
	return &OrderStore{db: goqulib.New("postgres", db)}
}

// GetByID retrieves a single order by ID.
func (s *OrderStore) GetByID(ctx context.Context, id int64) error {
	_, _, err := goqulib.From("orders").
		Select("id", "user_id", "status", "total").
		Where(goqulib.C("id").Eq(id)).
		Limit(1).
		ToSQL()
	return err
}

// GetPending retrieves pending orders with a limit.
func (s *OrderStore) GetPending(ctx context.Context) error {
	_, _, err := goqulib.From("orders").
		Select("id", "user_id", "status", "total").
		Where(goqulib.C("status").Eq("pending")).
		Limit(100).
		ToSQL()
	return err
}

// RawHealthCheck demonstrates a safe raw SQL literal via goqu.L(...).
func (s *OrderStore) RawHealthCheck(ctx context.Context) error {
	_ = ctx
	_ = goqulib.L("SELECT id, status FROM orders WHERE id = 1 LIMIT 1")
	return nil
}
