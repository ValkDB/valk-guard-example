package demo

// VG110User intentionally maps the same DB column twice.
type VG110User struct {
	ID       int64  `db:"id"`
	LegacyID int64  `db:"id"`
	Email    string `db:"email"`
}

func (VG110User) TableName() string { return "vg110_users" }

// RiskyInferred intentionally relies on inferred table and column mapping.
type RiskyInferred struct {
	ID    int64
	Email string
}
