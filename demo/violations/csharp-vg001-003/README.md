# C# EF Core: VG001-VG003

This demo bundle intentionally triggers:

- VG001 (`SELECT *`)
- VG002 (`UPDATE` without `WHERE`)
- VG003 (`DELETE` without `WHERE`)

Coverage in this bundle:

- C# EF Core raw SQL through `Database.ExecuteSqlRaw(...)`
