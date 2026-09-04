# Mitchell Bloom — V4 Stock Holders QA Report

**Run:** 2026-09-04 UTC  
**Artifact:** `Mitchell Bloom - V4 Concentrated Stock Holders - INSTANTLY UPLOAD.csv`  
**Rows:** 7,685  
**Columns:** 28  
**Bytes:** 2,600,584  
**SHA-256:** `17297c4f74b1d7b4597a8881c817d1eaa8919bc80d19490ffc32b587111a2827`

## Automated checks

| Check | Result |
|---|---|
| Non-empty output | PASS |
| Unique normalized emails | PASS — 7,685 / 7,685 |
| Unique normalized LinkedIn URLs | PASS — 7,685 / 7,685 |
| Allowed states only | PASS |
| WA/TX/TN/NV/FL absent | PASS |
| Current-company tenure ≥5 years | PASS |
| Modeled liquidatable gain ≥$1M | PASS |
| Usable `firstName` | PASS |
| Email syntax | PASS |
| Independent verification recorded | PASS |
| EmailGuard-invalid rows absent | PASS |
| Core upload/audit fields complete | PASS |
| Founder/C-suite/officer exclusion | PASS |
| Public price basis complete | PASS |
| ≤20 contacts/employer/send wave | PASS |

**Result:** 15/15 passed.

## Population audit

### Cohort

| Cohort | Rows | Share |
|---|---:|---:|
| Repriced public | 7,039 | 91.59% |
| Recent public | 395 | 5.14% |
| Private tender/secondary | 251 | 3.27% |

The final mix is more heavily repriced-public than the universe because the modeled `$1M+` exposure and independent-verification gates sharply reduce recent-public/private yield. The strict file was retained rather than padding to 10,000.

### Tenure

| Tier | Rows |
|---|---:|
| 5–10 years | 4,290 |
| 10+ years | 3,395 |

### Geography

| State/jurisdiction | Rows |
|---|---:|
| CA | 6,188 |
| MA | 435 |
| CO | 398 |
| NY | 394 |
| DC | 141 |
| MN | 78 |
| NJ | 22 |
| WI | 17 |
| VT | 9 |
| HI | 3 |

California is 80.52% of the final file. This reflects the employer/employee population and the state-tax ranking; it is not a random national sample.

### Concentration

- NVIDIA: 2,379 rows (30.96%).
- Broadcom: 1,618 rows (21.05%).
- Applied Materials: 684 rows.
- Dell Technologies: 675 rows.
- No employer domain exceeds 20 contacts inside a `send_wave`.
- 119 waves are required to exhaust the largest employer at the 20/domain/wave control.

## Email audit

- 10,016 unique work emails were available after final scoring.
- 7,685 delivered emails passed EmailGuard as `valid`.
- 2,045 were removed as EmailGuard `invalid`.
- 218 were removed because independent verification remained unknown/unavailable.
- 73 valid-format emails were removed because the domain did not match the current employer or an approved alias.
- 42 duplicates, three unusable first names, and one role inbox were removed.

## Suppression audit

- Exact V3 CSV: unavailable; it was ignored/uncommitted.
- Direct C2 lead export: unavailable because HTM's export route required a browser session.
- Live C2 sends: **0**.
- Deployment mode: **replacement, not append**.

This artifact must not be represented as net-new against V3. If used additively, recover/export V3 and repeat normalized-email/LinkedIn suppression before upload.

## Known limitations

1. Employer tenure and title-based grant bands are proxies, not proof of current holdings.
2. Public start-date prices are not award-specific tax basis.
3. The first public close is a conservative pre-IPO floor, not a 409A valuation.
4. Private valuation multiples and tender availability must be refreshed before event-specific messaging.
5. No row should be described in copy as owning a known amount or having a known gain.
