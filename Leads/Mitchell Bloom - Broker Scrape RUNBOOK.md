# Mitchell Bloom — BizBuySell Broker Scrape RUNBOOK

**Created 2026-08-05. Rewritten same day after finding the embedded JSON.**
Operational companion to `Mitchell Bloom - BizBuySell Broker Scrape Spec.md`.
Tool: **`browser-harness`** (real Chrome over CDP). No Apify needed.

---

## 1. The finding that makes this near block-proof

**The best anti-block measure is not making the request.** Every BizBuySell directory page embeds the Angular transfer state as `<script id="BBS-state" type="application/json">` (~161KB), which holds the **full broker records** the page was rendered from — not just what's visible.

```js
JSON.parse(document.getElementById('BBS-state').textContent)
// key: 'api/bff/v2/brokerSearch{"siteId":20,...,"seoName":"/business-brokers/vermont/"}'
//   .value.brokerSearchResult.value  ->  array of 30 full broker objects
```

### Fields confirmed present, per broker, straight off the directory page

| Field | Example | Why it matters |
|---|---|---|
| `firstName` / `lastName` | Jay / Inbar | |
| `companyName` | Inbar Group Inc | |
| **`telephone`** | `+12124735000` | no profile page needed |
| **`companyUrl`** | `https://www.inbargroup.com` | **the domain Apollo/Blitz needs** |
| **`city` / `state` / `zip`** | New York / NY / 10119 | **true HQ**, not serving area |
| **`forSaleListingsCount`** | `54` | the live-deal-flow filter |
| `soldListingsCount` | `124` | track record |
| `messageResponseScore` | `100` | responsiveness signal |
| `url` | `/business-broker/.../340/` | profile link |
| `personLanguagesDescription` | English | |

### What this changes

| | Before | After |
|---|---:|---:|
| Directory page loads | 81 | 81 |
| **Profile page loads** | **~2,000** | **0** |
| **Total requests** | **~2,081** | **81** |

**A 96% reduction in footprint.** The ~2,000 profile loads were the entire block risk; 81 page loads is indistinguishable from a person browsing the directory for a few minutes.

**It also kills the DOM-parsing bug.** The three-tier card problem (Elite / Premium / Basic — see §2) disappears because we stop parsing HTML. The JSON array carries all 30 records regardless of tier.

**And it fixes the geo filter.** Confirmed: **Jay Inbar is listed under Vermont but headquartered in New York, NY 10119.** The directory returns brokers *"serving this area."* With the real `state` field we filter on actual HQ instead of inferring from "Serving Windsor County, VT."

> ⚠️ **Still no email.** Not in the blob, not on the profile page. Phase 4 enrichment stays mandatory — but `companyUrl` gives us the domain to run it against, which is the hard part.

> **Do NOT call `/api/bff/v2/brokerSearch` directly.** It's tempting for bigger page sizes, but hitting an internal API with crafted params is both more bot-shaped and a clearer ToS problem than loading the page a human loads and reading what the page already gave us. 81 normal page loads is already cheap. Don't get greedy.

---

## 2. What the sample proved (and the bug it caught)

4-page sample (VT p1, CA p1-p3), randomized 2-4s + 4-8s delays:

| Check | Result |
|---|---|
| Pages loaded | 4/4 clean |
| Blocked / captcha / "unusual traffic" | **0** |
| Brokers extracted | 91 unique |
| Field quality | clean |

**The HTTP 403 is server-side fetch only.** Real Chrome loads these pages normally.

**The DOM bug (now moot, but documented):** Vermont reported 18 brokers; an Elite-only selector returned **1**. Three card tiers exist — `app-bfs-elite-`, `app-bfs-premium-`, `app-bfs-basic-brokercard-search-result` (VT: 1 + 7 + 10 = 18 ✓). Anyone falling back to DOM parsing must select all three. **Reading `BBS-state` avoids this entirely.**

**Result order is not stable** between loads — the same page can rank brokers differently on repeat visits. Dedupe on `broker_id` and reconcile against the page's own "of N" count per state.

---

## 2b. ⭐ MEASURED funnel rates (252 unique brokers, 9 pages, 7 states)

| Stage | Count | Rate |
|---|---:|---:|
| Sampled unique brokers | 252 | — |
| HQ ZIP inside the 10 target markets | 181 | **71.8%** |
| …**and** `forSaleListingsCount ≥ 1` | 149 | **59.1%** of all sampled |
| of survivors: has `telephone` | 149 | **100.0%** |
| of survivors: has `companyUrl` | 74 | **49.7%** |

- Median `forSaleListingsCount` among survivors: **4**
- **31.7%** of brokers appear on a state page that is not their HQ state — the serving-area problem, now quantified
- 19% of records had no usable ZIP and were excluded as unknown, so 71.8% is **conservative**

> **⚠️ There is no top-level `state` field.** Derive HQ state from **`zip`**. Confirmed cases: a broker on the *Vermont* page HQ'd at zip 10119 (New York, NY); a broker on the *Minnesota* page at zip 53066 (Wisconsin). `areasServed[].region` is where they're *licensed*, not where they sit.

> **Phone coverage is 100%; email coverage will be the bottleneck.** Only half the qualified brokers even expose a company domain to enrich against. Worth remembering Mitch's own line: *"They all pick up their phone."*

---

## 3. Not-getting-blocked rules

1. **Never sign in.** A logged-in session ties any strike to a real account.
2. **Single tab, sequential.** `new_tab()` once, then `goto_url()`. Never 81 tabs, never parallel workers.
3. **Randomized delays, 4-8s.** Fixed intervals are the clearest bot signal there is.
4. **Checkpoint to CSV every 10 pages.** An abort should cost nothing.
5. **Resume by skipping known `broker_id`s.** Never re-fetch what we have.
6. **Read `BBS-state`, don't parse the DOM.** Fewer requests, more fields, no tier bug.

**Abort triggers — stop the run the moment any fire**
- body text matches `/access denied|unusual traffic|captcha|are you a human/i`
- **2 consecutive pages with 0 records**
- `#BBS-state` missing, or body text length < 1500 (stub / challenge page)
- URL redirected away from what was requested

On abort: stop, keep the partial CSV, wait hours, resume. **Do not retry in a tight loop** — that's what turns a soft throttle into a hard ban.

**If it ever does get blocked**, the fallback ladder is: wait and resume → move to **Browser Use Cloud** (`browser-harness auth login` → `start_remote_daemon`) for proxies + stealth off Shara's IP → **IBBA directory** (a genuinely different source that also carries emails, ~$2.90) → Apify actor. We are never one block away from losing the campaign.

---

## 4. Phases

### Phase 1 — Directory sweep  *(local Chrome, 81 loads, ~15 min)*
10 states, all pages, extracting from `#BBS-state`.
**Output:** `Leads/V2 Brokers - RAW directory.csv`
**Control:** per-state unique count vs the site's own "of N". Log gaps; a shortfall means the order-shuffle dropped records and that state needs a second pass.

### Phase 2 — Dedupe + filter  *(no network)*
1. Dedupe on `broker_id`.
2. Keep only brokers whose **`state`** is in CA/NY/NJ/CO/MA/MN/WI/DC/HI/VT — real HQ, not serving area.
3. `forSaleListingsCount ≥ 1` (live deal flow).
4. Drop 0-for-sale **and** 0-sold (dead profiles).
5. Cap **3 brokers per firm**, ranked by `forSaleListingsCount` then `messageResponseScore`.
6. Report: raw 2,335 → unique → in-state → with-deal-flow. **First honest number for Mitch.**

### ~~Phase 3 — Profile enrichment~~ — **ELIMINATED.** Phone, website, HQ and listing counts all come from Phase 1.

### Phase 4 — Email
1. **IBBA directory** (~2,800 certified brokers, `hasEmail` filter, ~$2.90) — separate source that carries emails. Merge, dedupe on name + firm.
2. Gaps: `companyUrl` domain → **Apollo / Blitz** by name + domain.
3. **MillionVerifier**, keep valid only.
> Dedupe before paying per record. Same rule as skip-trace.

### Phase 5 — Tier + export
- **Tier 1:** ≥1 active listing ≥ **$2M** asking *(needs listing-level detail — the counts alone don't carry price, so this tier requires either the profile's For Sale tab or the listings search. Decide after Phase 2 shows how many brokers survive.)*
- **Tier 2:** has listings, price unknown or under $2M
- Export `V2 Brokers - INSTANTLY UPLOAD.csv`

---

## 5. Blocker

**Campaign 3 has no copy.** The sequence does not exist. This produces a list nobody can mail. The angle is specced (*"plan first, sell second"*, Value Builder, the broker's own tax exposure, and the two objections to pre-empt) but nothing is written.

---

## 6. Open

1. **Deal-size floor** — intake says $1M cap-gains min; the call said $2M. Sets the Tier 1 threshold. Pick one.
2. **Tier 1 needs listing prices**, which the counts don't carry. If Tier 1 matters, that's a scoped second pass over surviving brokers only — decide after Phase 2.
3. **CoStar ToS** review before anything recurring.
4. **Email fill rate unknown** until Phase 4. Don't quote Mitch a final count before then.
