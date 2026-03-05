# Dist 1: VG001-VG003

This demo bundle intentionally triggers:

- VG001 (`SELECT *`)
- VG002 (`UPDATE` without `WHERE`)
- VG003 (`DELETE` without `WHERE`)

Coverage in this bundle:

- SQL files
- Go `database/sql`
- Goqu
- Python ORM
- Python non-ORM (`session.execute(text(...))`)
