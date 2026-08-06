# Mitchell Bloom V2, Concentrated-Stock Holders: Scoring and Run Log

Build date: 2026-08-05. Vertical 2, concentrated-stock holders.
Deliverables: `V2 - INSTANTLY UPLOAD (A) long-tenure.csv`, `V2 - INSTANTLY UPLOAD (B) pre-IPO.csv`.

**Result: 10,328 verified sendable contacts against a 10,000 target**, plus 47 held for review.

---

## 1. The funnel, every stage

| Stage | Rows | Note |
|---|---|---|
| Raw Blitz pull | 359,169 | 40 companies, LinkedIn-derived |
| Deduped on `linkedin_url`, geography enforced | | see tier split below |
| Tier 1, 10+ years tenure | 25,828 | |
| Tier 2, 5 to 10 years tenure | 64,760 | |
| **Scored (5+ years, both tiers together)** | **90,588** | Tier 3 (82,535 unknown tenure) excluded, not qualifiable |
| Dropped, impossible tenure | -92 | start date predates the company |
| Dropped, gig or host title | -2,559 | Uber, DoorDash, Airbnb, Lyft only |
| **Clean pool** | **87,937** | |
| Selected for enrichment | 26,000 | state-allocated, ranked within state |
| Enriched via Blitz `enrich-email` | 26,000 | |
| Emails found | 16,022 | **61.6% fill** |
| Dropped, duplicate email | -101 | |
| Dropped, unusable first name | -32 | initials only, e.g. "N", "H.", "G" |
| **Uploaded to MillionVerifier** | **15,889** | |
| Returned good | 10,379 | **65.3% pass rate** |
| Returned risky, catch-all | 4,187 | 26.4%, held for batch 2 |
| Returned risky, unknown | 407 | 2.6%, held for batch 2 |
| Returned bad, invalid | 916 | **5.8% hard invalid** |
| Dropped, true role inbox | -4 | `cs@`, `ap@` x2, `it@` |
| Verified sendable | 10,375 | |
| Held, founder / C-suite / president | -47 | not deleted, see hold-out below |
| **SENDABLE** | **10,328** | |
| **Batch 2, catch-all and unknown** | **4,570** | separate file, separate inboxes |

Every dropped row is written to `_data/V2_DROPPED.csv` with a per-row reason. Nothing was
discarded silently.

### Campaign split

| Campaign | Rows | Definition |
|---|---|---|
| **A, long-tenure holders** | **7,506** | bucket C, older public companies |
| **B, pre-IPO option holders** | **2,822** | buckets A and B, recently IPO'd or still private |
| **C, acquisition trigger** | **0** | **NOT BUILT.** Requires the SEC M&A layer, which was never started |
| Held, executive titles | 47 | `V2 - HELD (executive titles).csv`, reviewable |

Campaign A: 14 companies. Apple 3,245 · Microsoft 1,486 · Broadcom 937 · NVIDIA 760 ·
Tesla 365 · Adobe 361. Tenure min 10.2, median 14.3, max 45.0.

Campaign B: 24 companies. Uber 986 · Airbnb 627 · Pinterest 382 · Snowflake 229 ·
Databricks 189 · MongoDB 108. Tenure min 5.0, median 6.6, max 18.8.

### The executive hold-out, 47 rows

Founder, C-suite and standalone "President" titles are held in
`V2 - HELD (executive titles).csv` rather than sent. **This is a receptivity cut, not a
qualification one.** Jay's point on the call at [25:28] is that an ordinary employee is
far more receptive than someone at the top, and a founder with a family office already
has this advice. The file caught real principals: Brian Chesky (Airbnb), Dara
Khosrowshahi (Uber), Eric Yuan (Zoom), Todd McKinnon (Okta), John Collison (Stripe),
Jay Kreps (Confluent), Reynold Xin (Databricks), Benoit Dageville (Snowflake).

**VP, SVP and EVP level are kept**, 129 rows across both campaigns. A 20-year Apple VP
holding RSUs fits the thesis exactly.

**They are held, not deleted, and the file carries `wouldHaveBeenCampaign` so any row can
be put straight back.** A share of the 47 are ordinary employees with nonsense
self-reported LinkedIn titles rather than real executives: a "Chief Executive Officer" at
Microsoft named Ron Johnson, a "CEO" at Apple, a "Vice CEO" at Microsoft, a bare
"President" at Microsoft. Those are genuine prospects and are worth restoring on review.

Nine further rows were caught by the first pass and returned to the campaigns, because
their titles only *reference* an executive rather than being one: "Executive Assistant to
Chief Executive Officer", "Principal Engineer, Office of the CTO", "Senior Executive
Assistant to the CEO & Co-founder". Those are ordinary employees holding RSUs.

---

## 2. The score

Three factors, all present in the pull. Every row scores 0 to 100, total weight 1.0.

| Factor | Weight | Definition |
|---|---|---|
| State tax | 0.40 | `rate / 13.3`. CA 13.3 · HI 11.0 · NY 10.9 · NJ 10.75 · DC 10.75 · MN 9.85 · MA 9.0 · VT 8.75 · WI 7.65 · CO 4.4 · **WA 0.0** |
| Tenure | 0.40 | `(min(years, 45) - 5) / 40`. Rescaled to the live range: the file starts at 5 years, so 5y maps to 0.0 |
| Cohort | 0.20 | A (IPO 2015-2021) 1.0 · B (still private, tender offers) 1.0 · C (older public) 0.0 |

**The 45-year cap fired on 100 rows.** It exists to neutralise start dates typed as 1901.
Max tenure before the cap was 124.70 years, after it 45.00.

**Tenure was rescaled during the build.** Dividing by 45 on a file whose median tenure is
7.6 years compressed 95% of rows into a 0.11 to 0.44 band, giving tenure roughly 13 points
of range against state's 40 and making the ICP's core signal nearly inert.

### The missing fourth factor

The approved plan specified a gain-multiple factor built from daily closes. **It is not in
this batch.** Stooq sits behind a JavaScript proof-of-work challenge and its robots.txt is
`User-agent: * / Disallow: /`; Yahoo's chart endpoint returns 429 and also disallows all
agents. Neither was worked around.

Consequence, stated plainly: **nothing in this scoring distinguishes a 2015 NVIDIA hire
from a 2015 Cisco hire.** They score identically. Their positions are not remotely alike.
Tenure and cohort are proxies for low basis, not measurements of it.

A Tiingo-based replacement (`_data/prices.mjs`, 33 tickers cached) has since been built and
validated, and a bucket-C-only gain factor is scored in `_data/V2_SCORED_all_GAIN.csv`. It
is **not** applied to this batch and did not influence any contact in these files.

---

## 3. Selection: allocated across states, not a flat top-N

A flat top-26,000 by score would have selected **100% California**, because CA scores a
perfect 1.0 on state tax and holds 46,216 clean rows against the cutoff. That would have
silently converted the approved "downweight WA, do not drop it" decision into a drop, and
zeroed out New York, Minnesota, Wisconsin and Hawaii, which Mitch named on the call.

Instead each state receives an allocation weighted by volume and tax rate, then rows are
ranked **within** each state:

```
allocation_weight = rows_in_state * (0.35 + 0.65 * state_rate / 13.3)
```

The 0.35 floor is what keeps Washington in at a reduced share rather than eliminating it.

| State | Tax % | Clean pool | Allocated | % of selection | Min score |
|---|---|---|---|---|---|
| CA | 13.3 | 46,216 | 17,909 | 68.9% | 45.20 |
| WA | 0.0 | 28,250 | 3,832 | 14.7% | 10.00 |
| NY | 10.9 | 6,122 | 2,094 | 8.1% | 41.08 |
| DC | 10.75 | 1,645 | 558 | 2.1% | 37.63 |
| MA | 9.0 | 1,776 | 544 | 2.1% | 33.37 |
| CO | 4.4 | 1,767 | 387 | 1.5% | 26.73 |
| MN | 9.85 | 999 | 322 | 1.2% | 37.22 |
| WI | 7.65 | 672 | 188 | 0.7% | 30.31 |
| NJ | 10.75 | 325 | 110 | 0.4% | 40.63 |
| HI | 11.0 | 145 | 50 | 0.2% | 41.08 |
| VT | 8.75 | 20 | 6 | 0.0% | 38.32 |

No state was capped at its available rows. No state received zero.

---

## 4. Data-quality filters

### Filter 1: impossible tenure, 92 rows dropped

Rows claiming longer tenure than the company has existed. Uber 19 · Amazon 14 ·
DoorDash 11 · Tesla 8 · Costco 7 · Anduril 7 · Airbnb 5 · SpaceX 4 · NVIDIA 3, plus 11
companies at 1 to 2 each.

**Dropped, not clamped.** Clamping "Uber, 45 years" down to Uber's actual age would relabel
the person a founding-year Uber employee, which is also false. The underlying start date is
garbage, so everything derived from it is garbage.

These were only 0.4% of the selection but **12 of the top 12 rows** and 58 of the top 500,
because the score rewards tenure. The 45-year cap catches 1901 typos; it does not catch
"Uber, 45 years".

### Filter 2: gig and host titles, 2,559 rows dropped

Applied at **Uber, DoorDash, Airbnb and Lyft only**. These people list the platform as
their employer on LinkedIn but hold no equity, so the concentrated-position premise does
not apply to them.

DoorDash 1,180 of 1,738 (67.9%) · Uber 1,009 of 2,574 (39.2%) · Airbnb 370 of 1,427 (25.9%).

Patterns: driver, delivery, delivery partner, dasher, deliverer, doordasher, door dash
(anchored), courier, rideshare, host, independent contractor, owner operator, shopper,
captain, creator, uber partner, private contractor, vacation rental owner, property
manager, business owner, photographer, chauffeur, contractor, partner (anchored),
plus non-Latin driver titles and blank or punctuation-only titles.

Two patterns are deliberately anchored:

- **`partner`** matches only titles that are *only* the word Partner. An unanchored
  `\bpartners?\b` dropped 46 salaried staff (HR Business Partner, Compensation Partner,
  Enterprise Partner Manager), who are exactly the RSU-holding employees this list is for.
- **`door dash`** matches only titles that are *only* those two words, because it is also
  the company name and an unanchored pattern would delete "Software Engineer, DoorDash".

**UPS drivers were deliberately kept.** Filter 2 does not touch UPS. Long-tenure UPS
employees are W-2 staff holding real UPS stock and are the closest match to Mitch's stated
archetype on the call.

### Excluded companies: verified absent

Lyft, Rivian, Roblox, Unity, Affirm, Robinhood, Coinbase, Block and Notion were excluded
from the universe because each traded below its IPO price for extended stretches, so their
employees hold losses rather than gains. **All nine return zero rows** in both the raw pull
and the scored file. The exclusion held at the job-manifest stage.

---

## 5. Enrichment and verification

- **Fill rate 61.6%** (16,022 of 26,000). A stratified 500-row pre-test measured 60.0%,
  so the projection held.
- **Fill varies sharply by cohort**: bucket A 68.8%, bucket C 60.7%, bucket B 43.7%.
- **Verification pass rate 65.3%** (10,379 good of 15,889 uploaded).
- Throughput was roughly 200 rows per minute against a 5 requests-per-second ceiling.

Full verification breakdown, from the FULL report:

| Quality | Result | Rows | Share | Disposition |
|---|---|---|---|---|
| good | ok | 10,379 | 65.3% | campaigns A and B |
| risky | catch_all | 4,187 | 26.4% | batch 2 |
| risky | unknown | 407 | 2.6% | batch 2 |
| bad | invalid | 916 | 5.8% | discarded |

**Only 5.8% were hard invalid.** The large middle band is catch-all: domains that accept
all mail at the SMTP layer, so the address is unproven rather than known-dead. Corporate
domains at this scale are frequently configured that way, which is why the band is much
larger here than V1's 596 catch-alls on a personal-domain list.

`V2 - BATCH 2 (risky, hold).csv` holds 4,570 of these (4,163 catch-all, 407 unknown, after
the role and executive cuts). **Send on separate inboxes from the main campaigns**, so a
higher bounce rate cannot damage the domains carrying the primary send. Batch 2 splits
A 2,123 and B 2,447 and carries a `campaign` column so it can be routed straight into the
matching sequence.

The fill-rate test sample was taken as **every 44th row of the selection**, not the top 500.
Profile completeness correlates with tenure, so testing the top of a tenure-ranked list
would have biased the estimate high, and that estimate is what the selection size rested on.

**The selection was raised from 22,000 to 26,000** after the fill test came in. At 60% fill,
22,000 yields 13,200 emails, which clears 10,000 only if verification lands at 76% or
better. It landed at 65.3%. The increase to 26,000 is the reason this build hit its target.

### Every address is a corporate domain

**16,022 of 16,022 found emails sit on a company domain. Zero personal addresses.**

This matters for two reasons:

1. **There is exactly one email per person, so there is no second slot.** The PropStream
   flow verifies up to three addresses each, which is why roughly 50% of addresses verify
   but ~75% of owners end up with a good one. Here the per-address pass rate **is** the
   per-person pass rate.
2. **Deliverability into corporate inboxes at large enterprises is untested for this
   client.** The V1 apartments list was personal-domain heavy and is not a read on this.
   Watch the first send rather than assuming V1's numbers transfer.

About **1.9%** of found emails (300 of 15,889) sit on a domain that is not the stated
employer's, concentrated in SpaceX (29%) and Home Depot (22%), both small-n.

---

## 6. Known limitations

- **Campaign C does not exist.** The SEC M&A trigger layer was never built. Campaign C is
  the only one of the three with a dated, compulsory liquidity event, and it was the plan's
  argued first send. Campaigns A and B carry no timing signal at all: they identify people
  who probably hold a gain, with no indication of when they might sell.
- **No row here is confirmed to hold stock.** Nothing in the data proves equity ownership.
  Long tenure at a company that granted broad equity is a proxy.
- **Job titles are self-reported LinkedIn text** and some are junk ("Stockholder",
  "Soulseeker", a "Chief Executive Officer" at Microsoft who is not).
- **Catch-all addresses are unproven, not verified.** The 4,163 catch-all rows in batch 2
  sit on domains that accept all mail at the SMTP layer, so verification cannot confirm or
  deny them. Some share will bounce. That is the reason for separate inboxes.
- **Buckets A and B are exhausted.** All 6,713 A rows and 1,731 B rows in the clean pool
  were selected. Campaign B cannot grow without expanding the company universe beyond the
  current 40, which the plan deferred to batch two.
- **Confluent's price series ends 2026-03-17 and HashiCorp's ends 2025-02-27** because both
  were acquired. Those are deal prices, not stale data. This affects only the gain file.

---

## 7. Blocked on Mitch, blocks the send and not the list

- Disclaimer verbiage for the `[DISCLAIMER PLACEHOLDER]` in every email
- Ad-review sign-off on the WSJ / Business Insider line in E1-C
- Confirm the CAN-SPAM footer postal address

---

## 8. Files

**Deliverables, this directory:**
- `V2 - INSTANTLY UPLOAD (A) long-tenure.csv` (7,506)
- `V2 - INSTANTLY UPLOAD (B) pre-IPO.csv` (2,822)
- `V2 - HELD (executive titles).csv` (47, review before discarding)
- `V2 - BATCH 2 (risky, hold).csv` (4,570, separate inboxes, later send)

**Working files, `_data/` (gitignored):**
`score_icp.mjs` · `blitz_to_verify.py` · `build_campaigns.py` · `company_founded.json` ·
`prices.mjs` · `V2_SCORED_all.csv` · `V2_DROPPED.csv` · `V2_SELECTED_26000.csv` ·
`V2_ENRICHED_26000.csv` · the VERIFY and MAP pair · `score_icp_gain.mjs` and
`V2_SCORED_all_GAIN.csv` (next batch, not used here).
