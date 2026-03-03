#!/usr/bin/env bash
set -euo pipefail

rule="${1:-}"
if [[ -z "$rule" ]]; then
  echo "usage: scripts/create-rule-demo.sh <RULE_ID>"
  echo "example: scripts/create-rule-demo.sh VG105"
  exit 1
fi

case "$rule" in
  VG001|VG002|VG003|VG004|VG005|VG006|VG007|VG008|VG101|VG102|VG103|VG104|VG105|VG106) ;;
  *)
    echo "unsupported rule: $rule"
    echo "supported: VG001-VG008, VG101-VG106"
    exit 1
    ;;
esac

out_dir="demo/violations/${rule}"
rm -rf demo/violations
mkdir -p "$out_dir"

case "$rule" in
  VG001)
    cat > "$out_dir/query.sql" <<'SQL'
SELECT * FROM users LIMIT 1;
SQL
    ;;
  VG002)
    cat > "$out_dir/query.sql" <<'SQL'
UPDATE users SET active = false;
SQL
    ;;
  VG003)
    cat > "$out_dir/query.sql" <<'SQL'
DELETE FROM orders;
SQL
    ;;
  VG004)
    cat > "$out_dir/query.sql" <<'SQL'
SELECT id, email FROM users WHERE active = true;
SQL
    ;;
  VG005)
    cat > "$out_dir/query.sql" <<'SQL'
SELECT id FROM users WHERE email LIKE '%@example.com' LIMIT 1;
SQL
    ;;
  VG006)
    cat > "$out_dir/query.sql" <<'SQL'
SELECT id FROM users LIMIT 1 FOR UPDATE;
SQL
    ;;
  VG007)
    cat > "$out_dir/migration.sql" <<'SQL'
DROP TABLE users;
SQL
    ;;
  VG008)
    cat > "$out_dir/migration.sql" <<'SQL'
CREATE INDEX idx_users_email_bad ON users(email);
SQL
    ;;
  VG101)
    cat > "$out_dir/models.go" <<'GO'
package demo

type User struct {
    Ghost string `db:"ghost_col"`
}
GO
    ;;
  VG102)
    cat > "$out_dir/migration.sql" <<'SQL'
ALTER TABLE users ADD COLUMN tenant_id INTEGER NOT NULL;
SQL
    ;;
  VG103)
    cat > "$out_dir/models.go" <<'GO'
package demo

type User struct {
    Email int64 `db:"email"`
}
GO
    ;;
  VG104)
    cat > "$out_dir/models.py" <<'PY'
class AuditEvent:
    __tablename__ = "audit_events"
PY
    ;;
  VG105)
    cat > "$out_dir/query.sql" <<'SQL'
SELECT users.ghost_col FROM users LIMIT 1;
SQL
    ;;
  VG106)
    cat > "$out_dir/query.sql" <<'SQL'
SELECT users.id FROM users INNER JOIN orders ON users.id = orders.ghost_user_id WHERE users.ghost_col = 1 LIMIT 1;
SQL
    ;;
esac

echo "Created demo patch content in: $out_dir"
echo ""
echo "Suggested next steps:"
echo "  git checkout -b demo/${rule,,}"
echo "  git add demo/violations"
echo "  git commit -m 'demo: trigger ${rule}'"
echo "  valk-guard scan . --config .valk-guard.yaml --format json"
