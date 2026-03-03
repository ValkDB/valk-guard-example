// Package goqu demonstrates the Goqu query builder usage.
package goqu

import "time"

// Order represents a customer order.
type Order struct {
	ID        int64     `db:"id"         goqu:"skipinsert"`
	UserID    int64     `db:"user_id"`
	Status    string    `db:"status"`
	Total     float64   `db:"total"`
	CreatedAt time.Time `db:"created_at" goqu:"skipupdate"`
}

// Product represents an item in the catalog.
type Product struct {
	ID       int64   `db:"id"       goqu:"skipinsert"`
	Name     string  `db:"name"`
	SKU      string  `db:"sku"      goqu:"skipupdate"`
	Price    float64 `db:"price"`
	Stock    int     `db:"stock"`
	Category string  `db:"category"`
}
