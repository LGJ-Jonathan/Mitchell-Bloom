# MITCHELL BLOOM — ICP HIERARCHY & LIST-BUILDING

**Bloom Financial / Bloom Tax & Estate Group, LLC**
*Reconciled from the July 14 strategy call, the intake form, and Mitch's July 8 + July 15 emails. Scoped to **3 launch campaigns** (July 24, 2026).*
*🔄 **Updated 2026-08-05 after the Aug 5 call:** Campaign 3 switched from direct business sellers to **business brokers scraped from BizBuySell**. See "AUG 5 CHANGE" below.*

> ### 🔄 AUG 5 CHANGE — Campaign 3: business sellers ➜ business brokers
> **What happened.** We told Mitch the direct business-seller play is blocked: marketplace listings are deliberately anonymized (no company name, no owner, NDA-gated), so there is no path from a listing to an inbox at scale. Mitch's answer: *"You see all the brokers on the right side? Maybe we do a campaign where we reach out to the business brokers."* Jonathan: *"That is a lot more doable."* Mitch has cold-called these brokers and reports **they all pick up the phone**.
> **Effect:** the ~8,800-broker channel (previously Phase 2, rank 5) **is promoted into the Campaign 3 slot**, sourced from **BizBuySell's broker directory** rather than Apollo. The direct business-seller marketplace play is **parked** (its copy stays on file, `Copy/C5 - Business Sellers`).
> **Full scrape spec:** `Leads/Mitchell Bloom - BizBuySell Broker Scrape Spec.md`.

---

## 📛 NAMING KEY (set 2026-08-05 — use these, nothing else)

The old `Vertical N` scheme is retired. It broke because filenames, in-file headers, and
campaign ranks all used different numbers, and two files were both called "Vertical 4."

**Copy docs use `C<rank>`, matching the campaign rank in the launch table below.**
Rank numbers are stable: a campaign keeps its number when its priority or phase changes.
Status (Phase 1 / Phase 2 / PARKED) lives in the doc header, never in the number.

| Campaign | Copy doc | List files |
|---|---|---|
| C1 — Property sellers (apartment / rental / MHP) *(commercial deferred)* | `Copy/C1 - Property Sellers (Apartment, Rental, MHP, Commercial).md` | `Leads/V1 …` |
| C2 — Concentrated-stock holders | `Copy/C2 - Concentrated-Stock Holders.md` | `Leads/V3 Stock Holders …`, `_data/V3 Stock Holders …` |
| C3 — Business brokers (referral channel) | `Copy/C3 - Business Brokers (referral channel).md` | `Leads/V2 Brokers …`, `Leads/V2+V3 Brokers …` ⚠️ |
| C4 — Trophy / residential owners (2 variants) | `Copy/C4 - Trophy-Residential Owners (…).md` | not built |
| C5 — Business sellers ($2M–$20M), **PARKED** | `Copy/C5 - Business Sellers ($2M-$20M) [PARKED].md` | none, play parked Aug 5 |

**🔄 List renumbering, 2026-08-10.** Concentrated stock moved from `V2` to **`V3`**, and **`V2`
now means the business-broker list**. This reverses the mapping recorded here on Aug 5. The
C scale did not move: concentrated-stock copy is still `Copy/C2`. **The V and C numbers are
independent scales and are not meant to line up.**

**Filenames now carry the vertical name**, matching the `V1 Apartments …` and `V2 Brokers …`
pattern, so a bare `V3` prefix no longer appears anywhere for this vertical:

- `Leads/V3 Stock Holders - INSTANTLY UPLOAD.csv`
- `Leads/V3 Stock Holders - Merger Triggers DEFM14A.csv`
- `Leads/V3 Stock Holders - Merger Triggers LIVE.csv`
- `_data/V3 Stock Holders - BATCH 2 (risky, hold).csv`
- `Leads/Mitchell Bloom - V3 Stock Holders Build Spec (Blitz).md`
- `Leads/Mitchell Bloom - V3 Stock Holders Data Engineer Request.md`
- `Leads/Mitchell Bloom - V3 Stock Holders (list + method).md` (the method doc)

**⚠️ Two collisions remain, both in the broker CSVs.** In those filenames `V2`/`V3`/`V4` denote
**scrape legs** (BizBuySell, IBBA, national), not campaigns:

- `V2 Brokers - …` and `V2+V3 Brokers - …` now agree with `V2` meaning brokers, but the `+V3`
  half reads as if it referenced concentrated stock. It does not. It means the IBBA leg.
- `V3 IBBA - …` still shares the `V3` prefix with concentrated stock. Adding the vertical name
  to the stock-holder files softens this a lot (`V3 Stock Holders` versus `V3 IBBA` reads
  clearly), but the leg numbers and the vertical numbers still occupy one namespace.

The broker CSVs were **not** renamed: they are live inputs to the Clay and MillionVerifier runs
in flight. Rename the whole broker set to `C3 Brokers - <leg>` once that pipeline finishes, which
removes both collisions at once.

====================================================================
## PART 1 — INTERNAL ICP ANALYSIS & LIST-BUILDING
====================================================================

### LAUNCH STRUCTURE — 3 campaigns, each its own sequence + tracked separately

| Rank | Campaign | Source | Copy | Phase |
|---|---|---|---|---|
| **1** | **Apartment / rental / mobile-home-park sellers** (individually owned) *(commercial deferred)* | PropStream | ❌ to write | 🟢 Phase 1 |
| **2** | **Concentrated stock holders** (85% older public cos, 15% recent IPOs) | **Blitz** | ✅ C2 | 🟢 Phase 1 · list built, 7,499 |
| **3** | **Business brokers** (~8,800 nationwide) 🔄 *replaced business sellers Aug 5* | **BizBuySell directory scrape** (+ IBBA, Apollo/Blitz enrich) | ❌ to write | 🟢 Phase 1 |
| 4 | Trophy / residential home owners | PropStream | ✅ C4 (×2) | 🟡 Phase 2 |
| 5 | Business sellers ($2M–$20M) 🔄 *parked Aug 5, was Campaign 3* | Marketplaces + Apollo | ✅ C5 | 🟠 Parked — sellers anonymized |
| 6 | Luxury real-estate brokers (channel for trophy) | Apollo | — | 🟡 Phase 2 |
| 7 | Institutional / LLC-veiled commercial RE | county / niche | — | 🔴 Deferred |
| 8 | Farmland | TBD | — | 🔴 Unvalidated |
| 9 | Crypto / Bitcoin holders | social-bio scrape | — | 🔴 Best-effort |
| 10 | CPAs (second referral channel) | TBD | — | 🔴 Raised Aug 5, not scoped |

> **Why this order:** Campaign 1 is ~70% of Mitch's existing trust business and his explicit July 15 instruction. Campaign 2 is the LGJ data team's "easiest + most receptive." Campaign 3 is now the **broker channel**, which is sourceable and responsive, where the direct-seller list is neither. Trophy homes are build-ready (filters + copy done) but demoted as a priority call.

--------------------------------------------------------------------
### 🟢 CAMPAIGN 1 — APARTMENT / RENTAL / MOBILE-HOME-PARK SELLERS  ⭐ lead segment
*Added to initial focus by Mitch's July 15 email. Source: PropStream.*

> **🔻 Commercial dropped (2026-08-05)** — not sourceable cold via PropStream (no Estimated Value field, LLC-held, off-MLS). Built list = apartments + rentals/MHP. Commercial deferred to Phase 2 via LoopNet / Crexi.

**Who — the segments in scope (individually owned only):**
1. **Apartment sellers** — small apartment buildings (2–20 units)
2. **Rental property sellers** — duplex / triplex / quad + small rental portfolios (owners of ~5–11 rentals looking to exit) + **mobile-home parks** ("an incredible target")

*(Commercial real-estate sellers — small commercial / strip mall / raw land — attempted and deferred; see note above.)*

**Exclude:** corporate, private-equity, institutional. Those have no reachable person/email.

**How to find (PropStream — paste-ready configs in `Leads/Mitchell Bloom - PropStream Filters Launch.md`, the doc to run):**
- Property Type = Multi-Family 2–4 / 5+, Duplex / Triplex / Quadruplex, Mobile Home or Trailer Park
- **Owner Type = Individual** ← the LLC-stripping filter that makes the reachable slice sourceable
- Estimated Value tiered by market ($2M+ floor) · Years of Ownership 15+ · Pre-Probate **Exclude** (stepped-up basis erases the gain) · High Equity
- High-tax-state market list (below)

**⭐ Timing (per Mitch, comment on the copy doc, July 29): prioritize just listed or pending.**
- **Primary list:** properties just listed or under contract — MLS On Market, Listing Type For Sale, Status **Active · Active Under Contract · Coming Soon · Contingent**. The highest-intent sellers, and what Mitch asked us to lead with.
- **Pending:** included per Mitch, run as its **own separate list** so its performance is visible. Caveat to watch: pending typically closes in ~30 days and the structure must be set up before close, so a share will already be too late.
- **Secondary list:** owners who fit the profile but have not listed yet (Off Market), kept for volume because the listed or pending pool is small in any one market. SF apartments: 509 off-market vs **6** on-market.

**Copy (to write):** own sequence — lead with **depreciation recapture** + **failed-1031** (Kelly & David is an exact match) and the *"toilets, trash, tenants, maintenance"* pain. Do **not** reuse the trophy-home "your home" copy on a landlord.

--------------------------------------------------------------------
### 🟢 CAMPAIGN 2 — CONCENTRATED STOCK HOLDERS  ⭐ highest confidence ("the easiest")
*Source: **Blitz** (LinkedIn-derived), not Apollo. Copy: `Copy/C2 - Concentrated-Stock Holders.md` (written).*
*List: `Leads/V3 Stock Holders - INSTANTLY UPLOAD.csv`, **7,499 verified**. Method: `Leads/Mitchell Bloom - V3 Stock Holders (list + method).md`.*

> **⚠️ Built and verified 2026-08-10. The list that exists differs materially from the ICP
> as originally written.** The section below states what the list *is*. The original
> intent is preserved underneath it, because the gap is a decision to revisit, not an
> error to hide.

**Who it actually is:** **current** employees, 5+ years at their employer, at companies
whose stock appreciated substantially, so shares were granted at much lower prices and
carry large unrealized gains. Tenure minimum 5.0 years, median 13.2.

| Company | Rows | Share |
|---|---|---|
| Apple | 3,244 | 43.3% |
| Microsoft | 1,495 | 19.9% |
| NVIDIA | 759 | 10.1% |
| Airbnb | 629 | 8.4% |
| Tesla | 364 | 4.9% |
| Adobe | 361 | 4.8% |

Apple and Microsoft alone are **63%**. Geography: CA 74.2%, WA 17.6%, NY 3.9%, everything
else under 2%. By city: Bay Area ~61%, Seattle metro ~16%, Los Angeles 3.4%, New York 3.4%.

**Five claims in the original ICP that the built list does not support:**

1. **"Employees and former employees."** No former employees. Every row is a current
   employee, filtered on `job_is_current`.
2. **"SpaceX, NVIDIA, Uber."** SpaceX is **5 rows**, Uber is **34**. Only NVIDIA holds up
   at 759. Uber was 973 until the 2026-08-10 re-verification, when their mail server
   blocked the SMTP probes and 953 rows moved to
   `_data/V3 Stock Holders - WAVE 2 (verifier-blocked domains).csv`. SpaceX was never
   large here (235 at its widest) because the company is young and private.
3. **"Companies that IPO'd in the last 5-10 years."** That cohort is roughly **15%** of
   the list. **85% is older public companies.** The widening was deliberate, because
   Mitch's own archetype at [18:50] is a 30-year UPS employee and UPS IPO'd in 1999, but
   it was never ratified.
4. **"High-tax metros ... Seattle."** Washington has **no state income tax**. Those 1,318
   rows face 23.8% federal only, so the "losing a third of their gains" line is a
   California number and does not apply to them.
5. **"Los Angeles and New York."** 3.4% each. Real but marginal, not a concentration.

**Two claims that do hold:** 5+ years tenure (minimum is exactly 5.0), and broad
seniority (no title filter, minus 23 verified founders and officers removed deliberately
on receptivity grounds per Jay at [25:28]).

**Client-safe description:**

> Current employees with five or more years at companies whose stock has appreciated
> substantially, so their shares were granted at much lower prices and carry large
> unrealized gains. Weighted toward long-tenured staff at established tech companies
> (Apple, Microsoft, NVIDIA, Tesla, Adobe), with a smaller group from recent IPOs such as
> Airbnb. Concentrated in the Bay Area, with Seattle second. No seniority filter, since
> the biggest surprise gains often sit with long-tenured non-executive staff.

**Open decisions, not defects:**
- Sending wave 2 restores Uber to 973 and Broadcom to 936. Those addresses are valid; the
  domains refused verification probes. Held on separate inboxes pending first-send data.
- Restoring SpaceX and Uber to the weight the ICP implies needs a different company
  universe, not a filter change.

---

**Original ICP intent, as written before the build (retained for reference):**

**Who:** long-tenured / early employees holding concentrated, highly appreciated stock at companies that IPO'd in the last 5–10 years with broad employee equity. Examples raised: **SpaceX, NVIDIA, Uber, Yahoo**; the 30-year employee with founder-priced shares. Concentrated in high-tax states.

**How to find (Apollo filters):**
- **Current Company:** curated list of IPO'd-2015–2021 companies with broad employee equity (SpaceX, NVIDIA, Uber, Airbnb, Snowflake, Coinbase, DoorDash, Palantir, Rivian, Datadog, CrowdStrike…) — paste as company-name list
- **Years in Current Company: 5+** (proxy for early / vested equity)
- **Person Location:** SF Bay Area, San Jose, LA, Seattle, NYC + high-tax states
- **Seniority: broad** — do NOT restrict to execs; rank-and-file hold the biggest surprise gains (equity is a tenure story, not a seniority story)
- **Email status:** Verified

*Apollo was never used. The in-house seat is 100 monthly credits with Revenue and Lookalike
filters locked, which is a demo seat rather than a sourcing tool. Blitz replaced it.*

--------------------------------------------------------------------
### 🟢 CAMPAIGN 3 — BUSINESS BROKERS (~8,800 nationwide)  🔄 *new as of Aug 5*
*Source: **BizBuySell broker directory scrape** + IBBA, enriched via Apollo/Blitz. Copy: **not written**. Full spec: `Leads/Mitchell Bloom - BizBuySell Broker Scrape Spec.md`.*

**Why it replaced business sellers.** The direct-seller marketplace play died on the Aug 5 call: listings are deliberately anonymized ("10-person plumbing business in Wisconsin"), no company name, no owner, usually NDA-gated. Mitch redirected us to the brokers listed alongside those listings. He has cold-called them himself: *"They all pick up their phone."* Responsive channel, sourceable list.

**Who:** business brokers, M&A advisors and business intermediaries with **live deal flow** — a broker with active BizBuySell listings is sitting on owners who are actively selling right now.

**✅ VERIFIED COUNTS (2026-08-05, live site probe):** CA **926** · NY **446** · NJ **262** · CO **248** · MA **197** · MN 83 · WI 79 · DC 48 · HI 28 · VT 18 = **2,335 raw** across the 10 target markets. Mitch's "~8,800 in the country" was never checked and isn't our number. ⚠️ 2,335 is **before dedupe**: the directory returns brokers *"serving this area,"* not headquartered there, so brokers repeat across states and some sit outside the map entirely (confirmed a Phoenix broker on the California page). Unique in-market brokers will be meaningfully lower, and the sendable count lower again after email enrichment.

**How to find (BizBuySell directory, geo-seeded):**
| Level | URL pattern |
|---|---|
| State (main seed) | `bizbuysell.com/business-brokers/california/` |
| County | `bizbuysell.com/business-brokers/california/santa-clara-county/` |
| City | `bizbuysell.com/business-brokers/california/los-angeles/` |
| Broker profile | `bizbuysell.com/business-broker/{firm-slug}/{firm-slug}/{brokerId}/` |

**Filters:**
- **Geography:** the fixed high-tax map — CA · NY · NJ · MA · MN · HI · WI · VT · DC + CO. No expansion.
- **`active_listing_count ≥ 1`** — live deal flow, and it is what makes the email personalizable
- **Tier 1:** ≥1 active listing at **asking price ≥ $2M** (matches the deal-size floor / ~$1M cap-gains exposure). **Tier 2:** active listings all under $2M, kept at lower priority with a generic angle.
- **Exclude** franchise-resale-only brokers (no seller cap-gains event at target size) and dead profiles (0 active, 0 sold)
- **Cap 3 brokers per firm** — big brokerages list a dozen agents at one office; blasting all of them burns the domain
- Certifications (CBI / M&AMI) are a quality sort, not a gate

**Fields to scrape:** broker name, firm, title, phone, firm website, profile URL, city/state/ZIP, service areas, industries served, certifications, license #, active + sold listing counts, bio, LinkedIn. **Plus a child table of their active listings** — headline, industry, city/state, asking price, cash flow, revenue, EBITDA, status, date listed. The listing rows are the personalization payload: Jonathan's line on the call was *"Dara, I saw your listing on BizBuySell for 1.4, about the two retail locations."* No listing join, no first line.

**⚠️ Email is not on BizBuySell — verified.** Checked a live profile: zero `mailto:` links, zero email strings on the page. Mitch's *"they all have their email address, you can look them all up"* is true of the broker's firm site, not of BizBuySell. What we **do** get is name, firm, **phone** (`tel:` sits in the DOM even behind the "Show Phone Number" button) and the **firm's website** — and the website is the key that makes enrichment work. Pipeline: profile → firm domain → Apollo/Blitz by name + domain → MillionVerifier. The **IBBA directory** (~2,800 certified brokers) runs as Leg B because it does expose a public email field.

**Mechanics (verified):** pagination is `/business-brokers/{state}/{page}/`, **30 brokers per page**, ~80 pages for all 10 states. The page is Angular **server-side rendered**, so broker data ships in the HTML — there is no JSON API to hit, parse the DOM.

**⚠️ Tooling:** the **403 is server-side fetch only** — real Chrome loads the directory with no captcha and no challenge, so this is a `browser-harness` job, not a paid-actor job. Probe on local Chrome; run the **bulk pull on Browser Use Cloud** (`start_remote_daemon`) for proxies + stealth, which is what keeps it off Shara's browser and IP. Stay signed out, throttle. Apify is fallback only. Still worth running the IBBA actor as Leg B at ~$2.90 since it is a different source that carries emails. Review CoStar ToS before anything recurring.

**Copy direction (to write):** channel/referral message, not a seller message. Mitch's requested angle verbatim: ***"Plan first, sell second."*** Offer the broker four things: their client keeps more so the deal actually closes, the **Value Builder** program to raise business value pre-sale, the broker's own income-tax exposure as a top producer, and Mitch as an outside partner in their network. Pre-empt the two objections Mitch named: *"that's up to the tax person"* and *"I don't want to kill my deal"* (frame as deal-saver — sellers blindsided by a 30-45% hit walk away from closings).

--------------------------------------------------------------------
### 🟠 PARKED — BUSINESS SELLERS ($2M–$20M)  *was Campaign 3 until Aug 5*
*Copy already written and kept on file: `Copy/C5 - Business Sellers ($2M-$20M) [PARKED].md`.*

**Why parked:** marketplace listings hide the seller. There is no reliable path from an anonymized listing to an owner's inbox at scale, which is exactly what triggered the Aug 5 pivot to brokers. Not deleted — if the broker channel produces sellers, or if a match-and-enrich route proves out, this comes back.

**The pipeline as designed** (unchanged, for the record): scrape public listing pages across BizBuySell / BusinessesForSale.com / BizQuest / LoopNet / BusinessMart / BizForSale.co → filter to **$2M+ in target states** → AI-match each anonymized listing to a real company (Clay; industry + city + revenue + headcount + "established 1987" usually pins it) → enrich the owner via Apollo/Blitz → sequence direct. Match rates were never going to be 100%.

**Broad master bucket via Apollo** (the volume fallback, never run): Seniority Owner/Founder/Partner/CEO · Headcount 1–50 (200 for mfg/aerospace) · Revenue $2M–$20M · industry/keyword lists per vertical · high-tax states · Founded before ~2005.

--------------------------------------------------------------------
### 🟡 PHASE 2 — launch when promoted

**4. TROPHY / RESIDENTIAL HOME OWNERS** — PropStream. Individual owners of high-value, long-held homes (bought decades ago, huge appreciation; NOT new builds). **Most build-ready segment:** filters done (1,508 in Beverly Hills) + both sequences written (`Copy/C4 - Trophy-Residential Owners…`). Same PropStream method + On/Off-Market timing split as Campaign 1. Demoted as a priority call; launches fast when promoted.

**5. ~~BUSINESS BROKERS~~ — 🔄 promoted to Campaign 3 on Aug 5.** See the Campaign 3 section above. (Note the reversal: on the July 14 call Mitch said brokers usually won't engage and to go direct to owners; on Aug 5 he reversed that himself once the direct-seller list proved unsourceable, and reported brokers all answer their phones.)

**6. LUXURY REAL-ESTATE BROKERS** (top ~1,000 brokerages, ~$2.25T volume) — Apollo. Channel for trophy sellers; follows Campaign 4's phase. Sotheby's / Christie's / Compass / Douglas Elliman / Coldwell Banker Global Luxury, in the luxury micro-markets.

--------------------------------------------------------------------
### 🔴 DEFERRED / UNVALIDATED

**7. INSTITUTIONAL / LLC-VEILED COMMERCIAL RE** — large commercial, office, strip malls, raw land behind LLCs/corps/trusts. ~70% of Mitch's existing trust business but **can't be sourced cold at scale** (no individual, no email). Revisit post-launch via county records / the "needle in a haystack" test (email known owners, ask who's selling). *(Campaign 1 already captures the individually-owned overlap.)*

**8. FARMLAND** — Mitch's own wording was "*maybe* farmland"; never discussed on the call. **Not validated:** no agreed deal-size floor; biggest US farmland sits **outside** the high-tax states that power the pitch. Resolve first: (a) does volume exist in target states; (b) which source returns owner contact data.

**9. CRYPTO / BITCOIN HOLDERS** — big gains wanting to sell. Findable because holders put it in social bios (filter + signal; X/LinkedIn bio scrape, not Apollo). Jay confirmed doable. Low precision — best-effort.

--------------------------------------------------------------------
### WHAT WE'RE AVOIDING (from the call)
- ~~**Brokers / realtors as the target**~~ — 🔄 **reversed Aug 5 for business brokers only.** The July 14 position was go-direct-to-owners because brokers fear busting the deal. That still holds for *real-estate* brokers/realtors (they push 1031s), but business brokers are now Campaign 3 because the direct business-seller list can't be built. Their two objections are now copy problems to solve, not reasons to skip the segment.
- Corporate / private-equity / institutional-owned property
- New-build trophy homes (no appreciation yet)
- Deals under **$2M**
- Multi-stakeholder businesses (too many decision-makers)
- People merely delaying a sale out of fear (not actually transacting) — secondary, not primary

--------------------------------------------------------------------
### DATA SOURCE PER CAMPAIGN
- **Campaign 1 — Apartment/rental/commercial sellers:** PropStream (Owner Type = Individual) + county records for edge cases
- **Campaign 2 — Stock holders:** Apollo + LinkedIn (list of recently-IPO'd companies)
- **Campaign 3 — Business brokers:** BizBuySell broker directory scrape (Apify, residential proxies) + IBBA directory → dedupe → Apollo/Blitz email enrich → MillionVerifier
- Phase 2 trophy / luxury RE brokers: PropStream + Apollo · Crypto: social-bio scrape · Farmland: TBD · Parked business sellers: marketplaces → Clay match → Apollo/Blitz

--------------------------------------------------------------------
### TARGET GEOGRAPHY (high state-income-tax)
**Internal filter list:** CA · NY · NJ · MA · MN · HI · WI · VT · DC + **CO** (Vail / Aspen / Cherry Hills — Mitch's home turf).
**Avoid** no-income-tax states (TX/TN/WA/NV/FL) — the pitch leans on "the state and the IRS."
*(Full PropStream city/ZIP target list in the Filter Spec doc.)*

--------------------------------------------------------------------
### PLATFORM, MESSAGING & PROOF (from the call)
- **Send on INSTANTLY** (not Bison), given the B2C-leaning audience.
- **Domains:** Bloom Financial root; avoid the words "**tax**" and "**free**" in sending domains (read as promissory).
- **Trust framing:** lead with *"Would it be okay if I sent over the mechanism so you can review it with your CPA?"* — financially literate people with existing CPAs. Every email carries a disclaimer; no promissory claims; **"defer," never "avoid."**
- **Proof (cleared):** Kelly & David — **$7.6M** Midwest multifamily sale, failed 1031, deferred **$1.1M** in capital-gains. Featured in **WSJ, MarketWatch, Business Insider, US News**.
- **Do NOT use:** Rob Lowe's name (used the trust, not referenceable publicly) · audit statistics / "audits with no findings" (never hint a lead might be audited) · pricing · "secret method" · indemnification.

--------------------------------------------------------------------
### OPEN QUESTIONS TO RESOLVE
1. **⚠️ Guarantee & B2C tension (raise with Jay).** Mitch's July 8 email: his agreement reportedly requires leads Apollo-available, companies <50 employees, **not filtered by city/zip**. His real targeting is geo-specific, individual-owner (arguably B2C), value-filtered, and his top target (in-contract sellers) isn't an Apollo motion. Close expectations directly — he was explicit he doesn't want "unfulfilled expectations."
2. **Campaign 1 copy** is written (`Copy/C1 - Property Sellers`), reviewed by Mitch, and revised per his notes (1031 distinction added; listed/pending prioritized). **The open build blocker is now the Campaign 3 broker sequence — it does not exist yet.**
2b. **Broker email fill rate is unknown** until the BizBuySell + IBBA legs run. BizBuySell exposes no email, so the list depends entirely on the Apollo/Blitz enrich step. Don't quote Mitch a broker count before we see a verified rate.
2c. **CoStar ToS** on recurring BizBuySell scraping — review before scheduling a repeat run.
3. Can we find commercial / MHP owners in bulk via PropStream Individual filter, or fall back to the "needle in a haystack" test? (Campaign 1 tests this.)
4. How to frame proof without hinting a lead might be audited → resolved: audits are banned from copy.
5. Deal-size floor: intake USP **$1M** cap-gains min vs. call **$2M** RE floor — pick one for the revenue/value proxy.
6. Farmland: scope data + high-tax-state overlap before treating it as a segment at all.

====================================================================
## PART 2 — CLIENT-FACING SUMMARY (concise — okay to share)
====================================================================

**MITCHELL BLOOM — WHO WE'RE TARGETING**
*A plain-English overview of the audience we agreed on, in the order we'll launch.*

### THE CORE IDEA
We reach people who are about to sell a highly appreciated asset and want to avoid the large capital-gains hit at closing — while there's still time to put your strategy in place before the sale closes.

### THE FIRST THREE CAMPAIGNS
> **Campaign 1:** Sellers of apartment buildings, mobile-home parks and rental properties
> **Campaign 2:** Holders of highly appreciated company stock
> **Campaign 3:** Business brokers who are actively selling businesses right now
> *Next up (already prepared):* owners of trophy / luxury homes, plus holders of large crypto / Bitcoin gains.

### CAMPAIGN 1 — SELLERS OF APARTMENTS, MOBILE-HOME PARKS & RENTAL PROPERTIES
- **Who they are:** Independent, family-owned owners heading for a sale. We exclude corporate, private-equity and institutionally owned property. We're also looking at farmland as a possible addition.
- **Why they fit:** This is the closest match to where your business already comes from.
- **Worth knowing:** These owners usually hold property through an LLC or trust, so we pull them from property records rather than a contact database. We reach the independently-owned ones directly; those lists take a little longer to build and refine. Farmland we're treating as a question to confirm, not a commitment.

### CAMPAIGN 2 — HOLDERS OF HIGHLY APPRECIATED COMPANY STOCK
- **Who they are:** Long-time employees at companies that went public in the last 5–10 years (for example SpaceX or NVIDIA) holding stock with large built-in gains.
- **Why they fit:** Our easiest group to find and the most receptive to your help.

### CAMPAIGN 3 — BUSINESS BROKERS
- **Who they are:** Business brokers and M&A advisors who currently have businesses listed for sale, pulled from the BizBuySell broker directory in your target states.
- **Why they fit:** This is the change we agreed on the August 5 call. The business listings themselves are anonymous by design, so there is no reliable way to reach the owner behind them. The brokers are public, they have live deal flow, and you have found they answer. Each broker is sitting on multiple owners who are selling right now.
- **The angle:** plan first, sell second. We help their client keep more so the deal closes instead of stalling on the tax bill, we bring in Value Builder to raise the value before the sale, and we position you as the capital gains partner in their network.
- **Note:** Owners of businesses listed for sale are still on file as a group we can revisit if a workable way to reach them opens up.

### NEXT UP (ALREADY PREPARED)
- **Trophy / luxury homes** — long-held high-value homes in top markets (Beverly Hills, Montecito, Vail and similar). Filters and copy are already built, so this launches quickly once the first three are running.
- **Large crypto / Bitcoin gains** — people sitting on significant gains who want to sell without losing a large share to tax.

### WHERE WE FOCUS
High state-income-tax states, where your offer matters most: **New York · California · Colorado · Minnesota · Wisconsin · Hawaii** (and other high-tax states).

### HOW WE FIND THEM
We pull each group from the best fit data source: property records for the real estate groups, a professional database for the employees holding stock, and the BizBuySell broker directory for the brokers, then refine from there. The property based groups take a little longer to build than the database based ones.

### HOW WE'LL SPEAK TO THEM
We lead with trust: offering to share exactly how the strategy works so prospects can review it with their own CPA. Every email carries the proper disclaimer, with no promissory claims.
