# Mitchell Bloom - V3 Build Spec (Blitz)

**Campaign:** C2, concentrated-stock holders. **List files:** `V3 …` (renumbered from `V2`
on 2026-08-10; `V2` now means the business-broker list).
**Source:** Blitz (`~/.claude/skills/blitz-api`). **Not** Apollo — see below.
**Status:** pull in progress. Method validated; final counts pending run completion.

> Companion doc: `Mitchell Bloom - V3 Data Engineer Request.md` is the same universe
> expressed as an Apollo handoff spec, for when the data engineer runs it instead.

---

## Why Blitz and not Apollo

The ICP docs list this vertical's source as "Apollo + LinkedIn." That was never agreed on the
July 14 call. Jonathan named PropStream for trophy homes and named **nothing** here; LinkedIn was
Mitch guessing at [21:14], not Jay confirming. It's a later inference.

It also isn't viable in practice. The in-house Apollo account is **100 monthly credits,
expiring in 7 days**, with Revenue, Funding and Lookalike filters locked. That's a demo
seat, not a sourcing tool.

Blitz is on **Agency-Enterprise with unlimited credits**, and `/search/people` plus
`/enrichment/email` are both enabled on the key.

---

## The one thing Blitz cannot do, and the workaround

**Blitz has no tenure filter.** Its complete `people` filter set is job_title, job_function,
job_level, min_connections, location, education. Tenure is the *entire* targeting signal for
this ICP, so this looked fatal.

**It isn't, because the data is in the response even though it can't be filtered on.**
Each person carries `experiences[]`, and the current role has `job_start_date`:

```json
"experiences": [{
  "company_name": "NVIDIA",
  "job_start_date": "2025-02-01",
  "job_is_current": true
}]
```

The stock `flattenPerson()` in `blitz-client.mjs` **drops this field**, so a custom flattener
is required. That's what `run_jobs2.mjs` does — it derives `tenure_years` and assigns a tier.

Cost of the workaround: we pull the entire population and discard ~77% locally, rather than
filtering server-side. Acceptable only because credits are unlimited.

---

## Query architecture

Use `search-people` with `company.linkedin_url[]`, **not** `employee-finder`:

| | cap | notes |
|---|---|---|
| `employee-finder` | 10k / company | too small — NVIDIA alone has ~41,500 |
| `search-people` + `company.linkedin_url[]` | 50k / query | takes an **array** of companies, and city pre-filtering shrinks the set before the cap binds |

```json
{
  "company": { "linkedin_url": ["https://www.linkedin.com/company/nvidia"] },
  "people":  { "location": { "city": [ ...target metros... ], "country_code": ["US"] } }
}
```

**Amazon, Microsoft and Apple exceed 50k** and are split into 5 metro-group queries each.
That's why the run is 52 jobs across 40 companies.

---

## ⚠️ Two traps that will corrupt the list

**1. Blitz has no US state filter.** You target cities, and several target city names are
ambiguous within the US:

| City | Also matches |
|---|---|
| Washington | WA state towns, not DC |
| Bloomington | IN, IL |
| Burlington | NC, VT |
| Newark | DE, CA |
| Glendale | AZ |

`country_code: US` removes international but **not** these. A post-filter on `state_code`
against the allowed list is mandatory. Measured leakage on live data: KY, TX, IN, KS rows
appearing in the raw pull. Small (~0.1%) but real.

**Allowed states:** CA, NY, NJ, MA, MN, HI, WI, VT, DC, CO, **WA**.
WA is deliberate — Seattle is in the reviewed spec despite no state income tax, because
employee equity concentrates in tech hubs.

**2. Deduplicate on `linkedin_url`.** The runner is resumable, so an interrupted job re-runs
and re-appends its partial rows. Measured 160 duplicates in an early partial run.

---

## Tiers

| Tier | Tenure | Rationale |
|---|---|---|
| **1 — send first** | 10+ yrs | Joined before the big run-ups. Genuinely low basis. |
| **2 — backfill** | 5–10 yrs | Real but smaller gains. |
| **3 — hold** | unknown | See note below. |

**Do NOT filter on job title or seniority.** Equity is a tenure story. Mitch's own archetype
at [25:46] is "the SpaceX employee who was the cafeteria lady who's now a millionaire," and
Jay's reply was that she'd be *more* receptive. Title is captured as a column for
personalization only.

### On the unknown-tenure bucket (~23%)

These are not lost prospects. Measured on 18k live rows: **76% of unknown-tenure records
have no job title either**, meaning `experiences[]` is empty — thin LinkedIn profiles with no
employment data at all. They can't be qualified, employment can't be confirmed, and they
can't be personalized. The recoverable subset is the ~24% that have a title but no start
date. Handle as a follow-up, not a blocker.

---

## Measured performance

- **Throughput ceiling ~2,700 rows/min.** Identical at concurrency 8 and 20, which indicates
  a server-side cap around 45 rows/sec rather than client-side latency. Raising concurrency
  further will not help.
- Sequential (concurrency 1) runs at ~600/min. Use the concurrent runner.
- Full universe ≈ **386,600 addressable → roughly 2 to 2.5 hours**.
- One client instance only. The 5 RPS gate lives on the client, so running a second process
  in parallel would breach the account limit.

## Funnel (from the NVIDIA and SpaceX samples)

```
addressable in target metros   386,601
  under 5 yrs        ~54%
  unknown tenure     ~23%   (mostly empty profiles)
  5-10 yrs           ~17%   -> Tier 2
  10+ yrs             ~6%   -> Tier 1   ≈ 23,000
```

---

## Scripts

All in the session scratchpad, promote if this becomes recurring.

| File | Purpose |
|---|---|
| `run_jobs2.mjs` | concurrent, streaming, resumable puller with tenure derivation |
| `build_tiers.mjs` | dedupe, state enforcement, tier split, drop reporting |
| `count_per_company.mjs` | per-company addressable counts |
| `build_final_universe.mjs` | applies the company cuts, generates the 52 job configs |

## Next steps

1. Finish pull → `build_tiers.mjs`
2. Enrich **Tier 1 only** first via `blitz.mjs enrich-email` — do not enrich rows you won't send to
3. Verify per `README - list pipeline.md`, bounce target <3%, pause at 5%
4. Load to **Instantly** (not Bison), merge field `{{firstName}}` only

## Blocked on Mitch (blocks the send, not the list)

- Disclaimer verbiage for `[DISCLAIMER PLACEHOLDER]`
- Ad-review sign-off on the WSJ / Business Insider line in E1-C
- Confirm the CAN-SPAM footer postal address
