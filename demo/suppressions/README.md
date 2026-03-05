# Suppression Showcase

This demo shows suppression at two levels:

1. Query-level inline suppression
- Rule-specific: `valk-guard:disable VG001`
- Statement-wide: `valk-guard:disable`

2. Global suppression via config
- `demo/suppressions/config/global_disable_vg001.yaml` disables `VG001` globally.

## Files

- `inline/sql_inline.sql`
- `inline/go_inline.go`
- `inline/python_inline.py`

## Verification

From repo root:

```bash
# Baseline config: query-level suppressions apply, unsuppressed VG001 remains.
valk-guard scan demo/suppressions/inline --config .valk-guard.yaml --format json

# Global config: VG001 disabled globally, so inline folder returns zero findings.
valk-guard scan demo/suppressions/inline --config demo/suppressions/config/global_disable_vg001.yaml --format json
```

Expected behavior:

- Baseline config: only unsuppressed `VG001` findings remain.
- Global config: `VG001` findings are suppressed globally; result is empty.
