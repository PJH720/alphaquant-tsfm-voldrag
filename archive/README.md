# archive/

`legacy_scripts/` holds one-off scripts from 2026-10-03, written to calibrate page and character counts while compressing the ~97p consolidated draft into the 25–35p submission format.

- They are **superseded** and kept only as a record of how the manuscript was produced.
- They use hardcoded absolute paths to the old flat layout, and several depend on files outside this repository (e.g. a `~/.gemini/.../backup_29p.md` scratch file). They will not run as-is.
- `generate_final_submission_bullseye.py` overwrites the 30P manuscript and Word files when run. Do not re-run it.

The maintained pipeline lives in `scripts/`.
