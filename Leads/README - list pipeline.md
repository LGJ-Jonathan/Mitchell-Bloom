# Lead list pipeline

Two skills cover the whole path from filters to a sendable list. Both live in
`~/.claude/skills/`. Invoke them, don't rebuild the steps by hand.

```
PropStream filters + counties          propstream-list-builder
        ↓  (marketing list, skip trace, export)
raw skip-traced export CSV
        ↓  prepare_verify.py           propstream-export-to-instantly
VERIFY file  →  MillionVerifier  →  FULL REPORT
        ↓  build_final.py
INSTANTLY UPLOAD.csv  +  BATCH 2 (risky, hold).csv
```

## propstream-list-builder
Drives the user's logged-in Chrome to apply a filter spec across counties and
save to a marketing list. Filters are frozen once verified; any change needs
explicit approval in chat, including diagnostic funnels.

## propstream-export-to-instantly
Turns the export into a verified list.

```bash
python3 ~/.claude/skills/propstream-export-to-instantly/scripts/prepare_verify.py \
  "<raw export.csv>" "<out dir>" "<list name>"

# user uploads the VERIFY file to MillionVerifier, downloads the FULL report

python3 ~/.claude/skills/propstream-export-to-instantly/scripts/build_final.py \
  "<FULL_REPORT.csv>" "<MAP.csv>" "<out dir>" "<list name>"
```

Validated against Bloom Campaign 1 leg A: reproduces that run byte-for-byte.

| Stage | Leg A result |
|---|---|
| Raw export | 4,320 rows |
| Owners after dedupe + litigator drop | 3,213 |
| Addresses verified (~$8) | 7,753 |
| Owners with a Good email | 2,354 (74%) |
| **Sendable after name cleanup** | **2,333** |

## Files in this folder

- `V1 Apartments - INSTANTLY UPLOAD.csv` — leg A deliverable, 2,333 contacts
- `V1 Apartments - BATCH 2 (risky, hold).csv` — 596 catch-all/unknown, send only
  after 2-3 weeks of clean reply data, on separate inboxes
- `Mitchell Bloom - PropStream Run Log.md` — county trackers and run decisions
- `Mitchell Bloom - PropStream Filters Launch.md` — the filter spec

The raw export stays in `~/Downloads/` and is the only copy of the phone numbers
and mailing addresses. Do not delete or edit it.
