# Complex Query Patterns (Intentional Violations)

This demo intentionally introduces issues in higher-complexity query shapes across both ORM and non-ORM paths.

Patterns covered:

- CTE (`WITH ...`)
- `UNION ALL`
- `LEFT JOIN`

Expected rule families:

- `VG004` (unbounded selects / missing limit)
- `VG106` (unknown filter column on joined table)

Files:

- `sql/complex_queries.sql`
- `python/orm_complex.py`
- `python/raw_complex.py`

Local verification on this branch currently yields:

- 8 findings of `VG004`
- 2 findings of `VG106`

Use this folder as a stress-case fixture for parser/extractor behavior and complex-query rule coverage.
