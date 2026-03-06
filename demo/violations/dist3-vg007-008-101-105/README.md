# Dist 3: VG007, VG008, VG101-VG105

This demo bundle intentionally triggers:

- VG007 (destructive DDL)
- VG008 (non-concurrent index)
- VG101 (model column missing in migration)
- VG102 (required migration column missing in model)
- VG103 (model/migration type mismatch)
- VG104 (explicit model table not found)
- VG105 (unknown projection column)

Coverage in this bundle:

- SQL migrations and SQL queries
- Python ORM models (schema drift)
- Python non-ORM query execution
