# Mitchell Bloom: Build State and Next Steps

Session close: 2026-08-06. Written as a handoff so work can resume without re-deriving anything.

---

## Where things stand

| Vertical | State |
|---|---|
| **V2, concentrated-stock holders** | **DONE.** 10,328 verified sendable, delivered, ready to load into Instantly |
| V2 batch 2 | 4,570 catch-all and unknown addresses, held for a later send on separate inboxes |
| **Campaign C, M&A trigger** | **Discovery only.** Gated before the Blitz pull. See below |
| V3, business sellers (BizBuySell) | 2,591 raw listings pulled, not enriched. Parked |
| V1, apartments and rentals | Previously delivered |

---

## V2 deliverables, all in `Leads/`

| File | Rows |
|---|---|
| `V2 - INSTANTLY UPLOAD (merged).csv` | **10,328** with a `cohort` column, A or B |
| `V2 - INSTANTLY UPLOAD (A) long-tenure.csv` | 7,506 |
| `V2 - INSTANTLY UPLOAD (B) pre-IPO.csv` | 2,822 |
| `V2 - BATCH 2 (risky, hold).csv` | 4,570 |
| `V2 - HELD (executive titles).csv` | 47 |

The merged file is the one to load. The V2 sequence uses `{{firstName}}` and nothing else,
so two campaigns with identical copy only buys reporting; the `cohort` column gives that
inside a single campaign. Split files kept for convenience.

Full methodology, funnel and limitations: `Mitchell Bloom - V2 Scoring & Run Log.md`.

### Open decisions on V2

1. **The 47 held executive rows.** Printed for review, not yet ruled on. Some are real
   principals (Bill Gates, Hock Tan, Palmer Luckey, Kimbal Musk, Dara Khosrowshahi,
   Brian Chesky). Some are self-reported nonsense worth restoring ("Georgia / Microsoft /
   President", "Vice CEO", "Ocean Trump / CFO"). Rows for Snowflake "Field CTO Office",
   "Ea to CEO" and DoorDash "Sr Executive Business Partner" look like staff the
   `office of the` / `assistant to` filter missed. Restoring is a copy-paste; every row
   carries `wouldHaveBeenCampaign`.
2. **Batch 2 needs separate inboxes.** These are catch-all addresses, unproven rather than
   verified. Do not send them from the domains carrying the main campaign.
3. **Corporate-inbox deliverability is untested for this client.** Every one of the 10,328
   is a work address at a large enterprise with mature filtering. V1 was personal-domain
   heavy and is not a read on this. Watch the first 200 sends.

---

## Campaign C, M&A trigger: discovery complete, pull NOT run

Source files: `Leads/V2 Merger Triggers - *.csv` and `Leads/sec-triggers/`.

```
247  DEFM14A filings, trailing 12 months
 89  pending at the Aug 4 build
 50  classified as TARGET (26 acquirer, 13 unknown, all dropped)
 49  resolved to a LinkedIn company page
 25  have 500+ employees, and hold 99.2% of the headcount
 11  of those 25 are headquartered in our 11-state footprint
```

**Two fields the plan requires are missing and were never extracted:**

- **Announced per-share price: absent entirely.** No price column exists in any file.
- **Expected close date: free text only,** present on 33 of 50, and vague. A representative
  value reads "we expect to complete the merger promptly following the receipt of all
  required approvals." That is not a deadline.

Both are recoverable by parsing the DEFM14A documents, which are already linked per row.
That is a build step, not a lookup.

**Rough projection if the pull runs**, using this build's own measured rates. Order of
magnitude only, and the weakest assumption is that in-geography employee share resembles
HQ share:

```
136,728  global headcount, in-geography targets with 500+ employees
   ~25%  survive 5+ year tenure   (V2 measured 90,588 of 359,169)
~34,000  reachable
   ~60%  email fill               (V2 measured 61.6%)
   ~65%  verification pass        (V2 measured 65.3%)
~13,000  sendable
```

**Recommendation carried forward: extract price and close date before spending the pull.**
Those two fields are the only thing that makes Campaign C different from A and B. Without
them it is another list of people who probably hold equity, which already exists at 10,328.

**Also: the deal list is perishable.** Roughly 20 new filings a month and they close in
months. The pending check is as of Aug 4, so refresh before any send.

---

## Working files, `_data/`, gitignored and local only

| Script | Does |
|---|---|
| `score_icp.mjs` | three-factor score, filters, state-allocated selection |
| `blitz_to_verify.py` | Blitz output to MillionVerifier upload format |
| `build_campaigns.py` | verified report to campaign files, merged file, batch 2, held file |
| `prices.mjs` | Tiingo daily closes, 33 tickers cached |
| `score_icp_gain.mjs` | four-factor proposal, bucket C only, NOT used in this batch |
| `company_founded.json` | founding years for the impossible-tenure filter |

Data: `V2_SCORED_all.csv`, `V2_DROPPED.csv` (2,651 with reasons), `V2_SELECTED_26000.csv`,
`V2_ENRICHED_26000.csv`, the VERIFY and MAP pair, `V2_SCORED_all_GAIN.csv`, `prices/`.

Credentials live in `_data/.tiingo.env` (mode 600) and the blitz-api skill's own `.env`.
Neither is committed.

### The gain-multiple factor, built but not applied

Stooq is unusable: JS proof-of-work challenge and `Disallow: /` in robots.txt. Yahoo's
chart endpoint 429s and also disallows all agents. Replaced with Tiingo, 33 tickers cached,
**33 of 50 free-tier symbols used this month, cache is precious**.

Gate passed decisively: NVDA from 2015-01-01 returns 439.2x against Cisco's 6.2x, and the
NVDA 2015 adjusted close of $0.4825 confirms the 4:1 and 10:1 splits are applied.

Design agreed but **not wired into any delivered list**: score it on **bucket C only**, in
the 0.20 weight slot that the cohort bump occupies for buckets A and B, so total weight
stays 1.0. It is deliberately not applied to A and B because for pre-IPO hires the multiple
is not merely incomplete, it is inverted: a 2016 Airbnb hire measured from the 2020 IPO
close computes to roughly flat while their real gain is enormous.

**One unresolved bug.** The floor rule for rows predating a price series gives each row its
company's best-ever multiple, which saturates the 100x cap. Result: all of the top 50 are
`floored` rows, and the best genuinely measured row sits at rank 135. Suggested fix, not yet
applied or approved: use the company's **median** computed multiple instead of the max.

---

## Repo hygiene

Public remote: `https://github.com/LGJ-Jonathan/Mitchell-Bloom.git`. Visibility is decided
and staying public.

**Verified: no contact data has ever been committed on any ref.** History is markdown only.
`.gitignore` covers `_data/`, `*.csv`, `*.xlsx`, `*.xls`, `*.json`, `*.tsv`, `*.parquet`, so
lead files cannot be committed regardless of export format.

---

## Blocked on Mitch, blocks the send and not the list

- Disclaimer verbiage for the `[DISCLAIMER PLACEHOLDER]` in every email
- Ad-review sign-off on the WSJ / Business Insider line in E1-C
- Confirm the CAN-SPAM footer postal address
