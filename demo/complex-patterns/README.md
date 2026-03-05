# Complex Query Patterns Showcase

This demo shows higher-complexity query constructs across both SQLAlchemy ORM and non-ORM execution paths.

Included patterns:

- CTE (`WITH ...`)
- `UNION ALL`
- `LEFT JOIN`
- ordered and bounded result sets (`ORDER BY ... LIMIT ...`)

Files:

- `sql/complex_queries.sql`
- `python/orm_complex.py`
- `python/raw_complex.py`

Use this folder when validating parser/extractor behavior on realistic query shapes.
