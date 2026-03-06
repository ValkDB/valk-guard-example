# Dist 4: VG106-VG111

This demo bundle intentionally triggers:

- VG106 (unknown filter column)
- VG107 (unknown table reference)
- VG108 (ambiguous unqualified column)
- VG109 (orphan migration table)
- VG110 (duplicate model column mapping)
- VG111 (Go inferred table/column mapping risk)

Coverage in this bundle:

- SQL schema + query files
- Python ORM models/queries
- Python non-ORM raw SQL queries
- Go models for VG110 and VG111
