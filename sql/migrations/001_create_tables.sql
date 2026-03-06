-- Left-join demo branch keeps this migration file in the changed-file scan context.
-- 001_create_tables.sql
-- Clean schema setup. No anti-patterns — valk-guard should report zero findings here.

CREATE TABLE IF NOT EXISTS users (
    id         SERIAL PRIMARY KEY,
    email      VARCHAR(255) UNIQUE NOT NULL,
    name       VARCHAR(255) NOT NULL,
    active     BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS orders (
    id         SERIAL PRIMARY KEY,
    user_id    INTEGER NOT NULL REFERENCES users(id),
    status     VARCHAR(50) DEFAULT 'pending',
    total      NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS products (
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(255) NOT NULL,
    sku      VARCHAR(100) UNIQUE NOT NULL,
    price    NUMERIC(10, 2) NOT NULL,
    stock    INTEGER DEFAULT 0,
    category VARCHAR(100)
);

-- Safe indexes with CONCURRENTLY
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_user_id ON orders(user_id);
