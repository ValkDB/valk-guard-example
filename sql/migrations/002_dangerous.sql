-- 002_dangerous.sql
-- Baseline is intentionally clean on main; use demo patches/script to create dangerous variants per rule.

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_status ON orders(status);
