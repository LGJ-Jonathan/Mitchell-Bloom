# Mitchell Bloom — V4 Stock Holders (List + Method)

**Completed:** 2026-09-04 UTC  
**Campaign:** C2 — Concentrated Stock Holders  
**Deliverable:** `Leads/Mitchell Bloom - V4 Concentrated Stock Holders - INSTANTLY UPLOAD.csv`

## Result

V4 contains **7,685 upload-ready, independently verified work-email leads**. It is intentionally smaller than the 10,000-row working target because V4 enforces both a modeled `$1M+` liquidatable-gain floor and a strict independent email-verification gate.

This is the strict file. Expanding it to 10,000 would require weakening one of those gates, adding additional qualified companies, or holding `unknown` emails. None of those compromises was made.

### Final composition

| Dimension | Rows |
|---|---:|
| Repriced older-public companies | 7,039 |
| Private tender/secondary companies | 251 |
| Recent-public companies | 395 |
| 5–10 years current-company tenure | 4,290 |
| 10+ years current-company tenure | 3,395 |
| California | 6,188 |
| All other included high-tax jurisdictions | 1,497 |

Largest company populations are NVIDIA (2,379), Broadcom (1,618), Dell Technologies (675), Applied Materials (684), Supermicro (343), Arista Networks (335), and KLA (326). This concentration follows the measured appreciation and modeled-gain rules rather than a generic seniority ranking.

## Why V4 differs from V3

V3's tenure/data-hygiene work remains the baseline, but V4 corrects or strengthens these areas:

1. **Actual price factor.** Public-company selection uses measured three- and five-year split-adjusted performance rather than reputation.
2. **Employee-level price alignment.** A post-public employee is measured from the first close on or after their start date. A pre-public employee uses first public close only as a conservative floor.
3. **No max-history backfill.** V4 never gives an employee the company's best historical multiple when the employee was not there.
4. **Modeled `$1M+` exposure gate.** Tenure, title-based grant bands, price multiple, and a 50% retained-share assumption are combined into a transparent proxy.
5. **Current-employment integrity.** A non-empty experience matching the exact target-company LinkedIn account is mandatory.
6. **Founding-date validation.** Impossible employment starts are removed, with explicit successor-company exceptions for legitimate legacy tenure.
7. **No generic seniority filter.** Engineers, scientists, operations staff, and other long-tenured contributors can qualify.
8. **Founder/officer suppression.** Founders, C-suite/corporate officers, presidents, chairpersons, and board-only profiles are excluded; assistants and field/regional technical roles are not treated as officers.
9. **Washington removed.** V4 uses `CA, NY, NJ, MA, MN, HI, WI, VT, DC, CO` and excludes `WA, TX, TN, NV, FL`.
10. **Work-email integrity.** Every delivered email passed EmailGuard as `valid`, matches the current employer or a documented employer alias, and is unique.
11. **Domain-safe waves.** `send_wave` limits every employer domain to at most 20 leads in each wave.

The exact gates, formulas, cohort rules, and assumptions are in `Mitchell Bloom - V4 Stock Holders ICP and Build Spec.md`. Company-level market evidence is in `Mitchell Bloom - V4 Stock Holders Company Evidence.md`.

## Build funnel

| Stage | Rows | Notes |
|---|---:|---|
| Raw Blitz person records | 127,749 | Pulled across exact company + target-metro/state searches |
| Current-company records with 5+ years tenure | 27,060 | Geography, current-experience, start-date, and tenure gates |
| Passed executive/gig/founding-date, cohort-price, and modeled `$1M+` gates | 15,986 | Scored V4 population |
| Unique enriched work emails | 10,016 | 62.65% of the final scored population |
| Delivered | **7,685** | EmailGuard valid + syntax/name/domain/dedup QA |

### Final-stage removals

| Reason | Rows |
|---|---:|
| No work email found | 5,919 |
| EmailGuard invalid | 2,045 |
| EmailGuard unknown/not independently verified | 218 |
| Current-employer email-domain mismatch | 73 |
| Duplicate email | 42 |
| Unusable first name | 3 |
| Role inbox | 1 |

The stage removals are evaluated in pipeline order, so counts should not be added as independent population estimates.

## Automated QA

**15/15 checks passed:**

- non-empty output;
- unique normalized email;
- unique normalized LinkedIn URL;
- only allowed states;
- WA/TX/TN/NV/FL absent;
- tenure at least five years;
- modeled liquidatable gain at least `$1,000,000`;
- usable `firstName` for the live sequence;
- valid email syntax;
- independent verification provider recorded;
- no EmailGuard-invalid rows;
- required upload/audit fields complete;
- founders/C-suite/officers absent, while assistant-reference titles remain allowed;
- public rows have complete price-basis fields;
- no employer domain exceeds 20 contacts in a `send_wave`.

There are **7,685 unique emails and 7,685 unique LinkedIn URLs**. The output has 28 columns and 2,600,584 bytes.

**SHA-256:** `17297c4f74b1d7b4597a8881c817d1eaa8919bc80d19490ffc32b587111a2827`

## Suppression and campaign handling

The V3 upload file and risky hold file were ignored/uncommitted and could not be recovered from the server. The source Mac remained unreachable over Tailscale, and the session-gated HTM lead export returned `Unauthorized`.

However, live campaign metadata shows C2 has 7,499 loaded leads, is still draft/status 0, and has sent **zero** emails. V4 is therefore built as a **replacement** for C2, not a net-new append:

1. Do not append this file to the existing 7,499 leads.
2. Replace/clear the existing C2 lead population, then upload V4 by `send_wave`.
3. Do not describe the file as net-new to V3.
4. If deploying to a new additive campaign instead, recover/export V3 first and suppress normalized email plus LinkedIn URL.

## Deployment notes

- The live copy uses `{{firstName}}`; the upload column is named `firstName` exactly.
- Upload by ascending `send_wave`. Each wave has no more than 20 leads per employer domain.
- E1-C (“buyers approaching you”) should be limited to the private-tender/secondary cohort.
- E1-H (QSBS) should be limited to private/pre-IPO rows and still requires Mitch's sign-off.
- Refresh price, employment, and verification data if deployment occurs more than 30 days after the build.
- Never state a modeled gain, inferred stock position, employee tender eligibility, or personal cost basis as a known fact in copy.

## Data/privacy handling

The contact CSV is intentionally excluded from Git by the repository's tabular-data ignore rules. Methodology and QA documentation are committed; the upload CSV remains a local client artifact and is attached in the delivery message.
