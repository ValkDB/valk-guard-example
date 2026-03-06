# Dist 2: VG004-VG006

This demo bundle intentionally triggers:

- VG004 (unbounded select)
- VG005 (LIKE with leading wildcard)
- VG006 (`SELECT ... FOR UPDATE` without `WHERE`)

Coverage in this bundle:

- SQL files
- Go `database/sql`
- Goqu
- Python ORM
- Python non-ORM (`session.execute(text(...))`)
