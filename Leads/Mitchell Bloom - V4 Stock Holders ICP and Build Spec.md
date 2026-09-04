# Mitchell Bloom — V4 Concentrated Stock Holders ICP & Build Spec

**Built:** 2026-09-03  
**Campaign:** C2 — Concentrated Stock Holders  
**Purpose:** Replace V3 with a higher-timing, higher-appreciation list. V4 is not a net-new append to V3.

## Offer-to-list fit

Bloom Tax & Estate Group helps a seller put a tax-deferral structure in place **before** a sale closes. For this segment, the relevant sale is a public-market disposition, employee tender/secondary sale, IPO/lockup release, or forced conversion in an acquisition. The list therefore prioritizes probable low-basis employer equity plus usable liquidity.

The list is a research model. It does **not** establish actual holdings, tax basis, vesting, award type, intent to sell, accredited-investor status, or tax eligibility for any person.

## V4 person-level hard gates

Every delivered row must have:

1. A non-empty employment history and a **current** experience matching the target company's LinkedIn account.
2. A usable current title and a known current-employer start date.
3. At least **5.0 years** at the current employer.
4. No impossible pre-founding start date, except documented successor/restructuring employers where legacy tenure is legitimate.
5. Current residence in `CA, NY, NJ, MA, MN, HI, WI, VT, DC, or CO`.
6. No residence in `WA, TX, TN, NV, or FL`. Washington is deliberately excluded despite its separate capital-gains tax because the live pitch is broad state-and-federal income-tax exposure.
7. No founder/co-founder, current C-suite/corporate officer, current company president, chairman, or board-only role.
8. No Uber/DoorDash/Airbnb driver, courier, host, property-manager, or other platform-participant record.
9. A cohort-appropriate low-basis/appreciation test.
10. At least **$1,000,000 of modeled liquidatable gain exposure** under the proxy below.
11. A syntactically valid, independently verified work email whose domain matches the current employer or a documented employer alias.
12. A usable first name for the live `{{firstName}}` merge field.

No general seniority minimum is applied. Long-tenured engineers, scientists, product staff, operations staff, and other individual contributors remain eligible.

## Company cohorts

### A — Recent public

Public-market debut in roughly the last 5–10 years. A person passes only when they started at least six months before the first public-price observation or their start-date-to-current split-adjusted multiple is at least 2.0x. IPO recency by itself is not enough.

### B — Private tender / employee secondary

Still-private companies specified for recurring or recent employee liquidity: SpaceX, Stripe, Databricks, Anduril, Rippling, Ramp, OpenAI, and Anthropic. The live C2 copy may be used only as evergreen pre-sale planning copy. Before using event-specific language, refresh the tender eligibility, deadline, common-share price, and permitted sale fraction.

### C — Repriced public

Older public companies pass the company screen only when actual split-adjusted appreciation is at least 150% over three years or 190% over five years. A person must also have at least a 2.0x split-adjusted start-date-to-current price multiple.

## Price and basis logic

Public prices use Yahoo Finance's chart endpoint with split-adjusted daily closes, captured 2026-09-03:

`https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?range=max&interval=1d&events=history&includeAdjustedClose=true`

- **Post-public hire:** basis-price proxy is the first split-adjusted close on or after the current-employer start date.
- **Pre-public hire:** basis-price proxy is the first public split-adjusted close. This is an intentionally conservative floor; an actual pre-IPO option strike may be lower.
- V4 never assigns the company's best historical multiple to a person whose tenure predates the available series. That corrects the principal V3 gain-floor bug.
- Private-company rows use a documented/research valuation-multiple proxy rather than a public ticker. They carry lower basis/equity-evidence confidence.

## $1M exposure proxy

V4 does not claim known holdings. It uses title only to estimate cumulative employer-equity grant value; title does not otherwise determine eligibility.

| Role band | Initial grant-value proxy | Annual refresh proxy |
|---|---:|---:|
| VP / SVP / EVP | $500,000 | $150,000 |
| Director / Head / GM | $300,000 | $100,000 |
| Experienced professional (manager, lead, principal, staff, senior, engineer, scientist) | $200,000 | $60,000 |
| Professional default | $100,000 | $30,000 |
| Frontline/support/admin/technician/operator/coordinator | $25,000 | $5,000 |

Refresh years are capped at eight. The model assumes 50% of cumulative granted value remains available to sell:

```text
modeled_equity_cost = initial_grant + annual_refresh * min(max(tenure_years - 4, 0), 8)
modeled_liquidatable_gain = modeled_equity_cost * max(price_multiple - 1, 0) * 0.50
```

Rows below `$1,000,000` are excluded. This is a conservative prioritization proxy, not tax or investment advice.

## V4 score

Only hard-gate passers are scored.

```text
gain_norm = 0.50 + 0.50 * clamp(ln(modeled_gain / 1,000,000) / ln(5), 0, 1)
liquidity_norm = 0.80 private employee-tender/secondary cohort
                 0.45 live public market
state_norm = state_top_rate / 13.3
tenure_norm = clamp((tenure_years - 5) / 15, 0, 1)

V4 score =
    40 * gain_norm
  + 20 * liquidity_norm
  + 15 * state_norm
  + 10 * basis_confidence
  + 10 * tenure_norm
  +  5 * equity_evidence_score
```

Basis confidence is 0.80 for a measured post-public start-date close and 0.65 for a pre-public first-close or private valuation proxy. Equity-evidence score is 0.80 for public filers and 0.60 for private tender/secondary companies.

## Data and verification pipeline

1. Read and preserve the V3 method as the baseline.
2. Resolve each target company to its official LinkedIn company URL with Blitz.
3. Pull US profiles by target high-tax-state metro locations with Blitz `/search/people`.
4. Match a current experience to the exact company LinkedIn URL.
5. Apply state, tenure, title, founding-date, cohort, price, and modeled-gain gates.
6. Deduplicate by normalized LinkedIn URL.
7. Enrich work emails with Blitz `/enrichment/email`.
8. Independently batch-verify emails with EmailGuard.
9. Drop role/disposable/invalid/unknown emails, current-employer domain mismatches, unusable first names, duplicate emails, and rows no longer present in the final scored population.
10. Rank by V4 score, then tenure. Add a `send_wave` field so deployment can limit each employer domain to 20 new contacts per week.

## Suppression and replacement rule

The documented V3 source file (10,352 rows) and its 4,570-row risky hold file were never committed and are unavailable on the server. The Mac path could not be reached over Tailscale, and the session-gated HTM lead-export route returned `Unauthorized`.

Live HTM metadata shows C2 has 7,499 leads, remains draft/status 0, and has sent zero emails. Therefore:

- V4 is safe as a **replacement build** for C2.
- Do not append V4 to the existing C2 lead population.
- Do not call V4 “net-new to V3.”
- If the team wants an additive campaign, first recover/export V3 and suppress by normalized email plus LinkedIn URL.

## Copy routing

The live sequence uses `{{firstName}}` only.

- E1-A/B/D/E/F and E2/E3 are broadly usable.
- E1-C (“buyers approaching you”) should be restricted to private-tender/secondary rows; it is not justified for ordinary public-market holders.
- E1-H (QSBS) should be restricted to private or genuinely pre-IPO rows and still requires Mitch's sign-off documented in the copy file.
- Do not inject modeled gain, stock multiple, inferred holdings, or tender assumptions into copy as facts.

## SEC merger trigger feed

On 2026-09-03, the repository's EDGAR pipeline reviewed five quarters and returned 91 apparently pending DEFM14A filers: 53 classified targets, 22 acquirers, and 16 unknown. Those records are a separate timing overlay, not automatic C2 qualifiers. An acquisition target still needs the low-basis, tenure, geography, and modeled-gain gates before entering this list.

## Refresh cadence

- Refresh public prices within five trading days of deployment.
- Reconfirm current employment and email immediately before upload if the build is more than 30 days old.
- Reconfirm private tender terms before event-specific messaging.
- Re-run V3/global suppression if V4 is deployed additively rather than as a replacement.
