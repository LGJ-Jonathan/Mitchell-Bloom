# Mitchell Bloom — ICP List-Building Spec

**Purpose:** Build-ready ICP breakdown for list construction, **ordered by priority hierarchy**. Reconciles three sources of truth — the **July 14 strategy call**, the **intake form**, and Mitch's **two emails (July 8 pre-call ICP questions + July 15 post-call reply)** — with an Apollo/PropStream filter set per ICP.

**Scoped to 3 launch campaigns July 24, 2026.** Phase 1 = exactly **three campaigns**, each its own sequence + tracked separately:
1. **Apartment / rental / commercial RE sellers** (individually owned) — PropStream
2. **Concentrated stockholders** — Apollo (+ SEC EDGAR filings, added Aug 5)
3. **Business brokers** (~8,800) — **BizBuySell directory scrape** 🔄 *replaced "business owners, master bucket" on Aug 5*

> ### 🔄 AUG 5 CHANGE — Campaign 3: business owners ➜ business brokers
> The direct business-seller list is unsourceable: marketplace listings are deliberately anonymized (no company name, no owner, NDA-gated), so there is no path from a listing to an owner's inbox at scale. Mitch redirected us on the Aug 5 call: *"You see all the brokers on the right side? Maybe we do a campaign where we reach out to the business brokers."* He has cold-called them and reports **they all pick up the phone**. ICP 5 (business brokers, previously Phase 2) **takes the Campaign 3 slot**, sourced from **BizBuySell's broker directory** instead of Apollo. The direct business-seller/master-bucket play is **parked** (see the parked section below).
> **Full scrape spec:** `Leads/Mitchell Bloom - BizBuySell Broker Scrape Spec.md`

This matches the strategy call's original 3-audience structure and Mitch's core business (~70% real estate per the call) + his July 15 instruction to include apartment/mobile-home-park/commercial sellers. **Everything else moves to Phase 2 or Deferred:** trophy homes (build-ready — filters + copy done), both broker channels, institutional/LLC commercial, and farmland.

**Offer (context for every ICP):** Capital-gains tax **deferral** via a third-party business trust — a Deferred Sales Trust™ / IRC §453 installment-sale structure. Every target is a **seller/holder of a highly appreciated asset facing a large capital-gains hit**, ideally **≤90 days from close** (the strategy must be in place *before* the sale closes).

---

## 0. Priority hierarchy at a glance

| Rank | ICP | Source | Phase |
|---|---|---|---|
| **Campaign 1** | **Apartment / rental / commercial RE sellers** (individually owned) | PropStream | 🟢 **Phase 1 — build now** |
| **Campaign 2** | **Concentrated stockholders** (IPO'd cos) | Apollo | 🟢 Phase 1 |
| **Campaign 3** | **Business brokers** (~8,800) 🔄 *new Aug 5* | **BizBuySell scrape** + IBBA → Apollo/Blitz enrich | 🟢 Phase 1 |
| 4 | Trophy / residential home owners | PropStream | 🟡 **Phase 2 — ready, launch when promoted** |
| 5 | Business owners / sellers 🔄 *parked Aug 5* | Marketplaces + Apollo | 🟠 Parked — sellers anonymized |
| 6 | Luxury real-estate brokers (channel for trophy) | Apollo | 🟡 Phase 2 |
| 7 | Institutional / LLC-veiled commercial RE | county / niche | 🔴 Deferred — unsourceable cold |
| 8 | Farmland | TBD | 🔴 Unvalidated — scope first |
| 9 | Crypto holders | social-bio scrape | 🔴 Best-effort / low priority |
| 10 | CPAs (second referral channel) | TBD | 🔴 Raised by Mitch Aug 5 — not scoped |

---

## 1. Shared qualifiers (apply to all ICPs)

| Qualifier | Value | Filterable? |
|---|---|---|
| **⭐ Timing — Mitch's #1 target** | **Under contract / pending / on-market / ≤90 days from close.** July 8 email: *"This is the most important question… that is my highest value target."* | ✅ **PropStream** (MLS status) — primary sort · ⚠️ marketplaces (visible, seller broker-gated) · ❌ Apollo |
| Deal / asset size | RE floor **$2M**; business sweet spot **$2–10M**, agreed target **$2–20M**; min **$1M capital-gains exposure** (intake USP) | Partial — **company revenue** (Apollo) or **value − last-sale-price** (PropStream) |
| Decision-maker | **Single / clean** owner, not a committee | ✅ Apollo (seniority + small headcount) · ✅ PropStream (Owner Type = Individual) |
| Target states (high-tax) | **CA, NY, NJ, MA, MN, HI, WI, VT, DC** (intake + July 8 email) + **CO** (call: Vail/Aspen/Cherry Hills) | ✅ Location |
| Avatar lean | **Primarily women, Gen X–Boomer, 45–70**, net worth **$3M–$30M** | ❌ Copy lean only — NOT a hard filter |
| Job titles | Owner, Founder, Co-founder, CEO, Managing Director, Managing Member, Principal, Sole Proprietor, Administrator, Chairperson | ✅ Apollo Titles / Seniority |

> **Timing note:** the timing signal is only *scrapeable at the seller level* for real property via PropStream (On-Market / Pending is a real field). Marketplaces show pending status but **hide the seller behind a broker** — which is exactly why Campaign 3 now targets the broker instead. Apollo has no timing filter → those ICPs run as master-bucket / pipeline.
>
> **🔄 Aug 5 — timing via the broker:** for businesses we now buy the timing signal one step removed. A broker's **active listing count** and their listings' **asking price / status** are the proxy: a broker with live $2M+ listings is holding actively-selling owners today. It is the closest thing to a real timing filter available on the business side.
>
> **Avatar note:** none of the avatar attributes (gender, age, net worth) exist in Apollo or PropStream. Copy angle only — never a list filter, or lists shrink to nothing.

---

# 🟢 PHASE 1 — the 3 launch campaigns (build now)

## Campaign 1 — Apartment / rental / commercial real-estate sellers (individually owned)  ⭐ lead segment
**Source: PropStream.** Paste-ready filter configs + full city list in **`Leads/Mitchell Bloom - PropStream Filters Launch.md`** (the doc to run). Click-by-click method, cost rules, and troubleshooting rationale in `Leads/Mitchell Bloom - PropStream Filter Spec.md` (trophy / Campaign 4 doc, reference only).

**Who — the three Mitch named for the first campaign, all in scope:**
1. **Apartment sellers** — small apartment buildings (2–20 units)
2. **Rental property sellers** — duplex / triplex / quad + small rental portfolios + mobile-home parks (*"an incredible target"*)
3. **Commercial real-estate sellers** — small commercial / strip mall

All **individually owned only** (Mitch: *"ma-pa"*; explicitly **exclude PE / institutional / corporate** — those have no reachable person/email). **Expect the commercial list to be the smallest of the three** (more of it is LLC-held).

**Why #1:** ~70% of Mitch's existing trust business is apartments + commercial RE, and his July 15 email put these in the initial focus. The **Owner Type = Individual** filter is the LLC-stripping workaround that makes the reachable slice sourceable (the same method that works for trophy homes).

**PropStream method:** Property Type = Multi-Family 2–4 / 5+, Duplex/Triplex/Quadruplex, Mobile Home or Trailer Park (+ small commercial where available) · Owner Type **Individual** · Years of Ownership 15+ · Pre-Probate **Exclude** · High Equity · high-tax-state market list.
**⭐ ON-MARKET PRIMARY (2026-07-29, per Mitch — supersedes the July 24 off-market call below):** Mitch, comment on the copy doc: *"Very good. Would be optimal to find properties just listed and/or pending."* So: **On Market** (Listing Type For Sale; Status Active, Active Under Contract, Coming Soon, Contingent) is the primary list, **Pending** runs as its own separate list, and **Off Market** is the secondary volume backfill. Full recipe in `Leads/Mitchell Bloom - PropStream Filters Launch.md`.

> *Superseded reasoning, kept for context (July 24):* on-market-only produced rounding-error counts (SF apartments: 509 qualified owners → **6** actively listed), and off-market is arguably the better-timed list for a DST since the trust must be set up **before** a sale closes. Mitch's own call language — *"people actually delay selling because they don't want to pay that capital gains"* — describes off-market holders. That volume problem is real and has not gone away, which is why off-market stays as the backfill rather than being dropped. But the priority call is the client's, and he made it.
**✅ Copy — written:** `Copy/Vertical 4. Apartment-Rental-Commercial Sellers.md`. One **no-signal** sequence (3/2/2, stops at E3) covers **both** the off-market and on-market lists. Leads with **depreciation recapture** + **failed-1031** (Kelly & David) + the *"toilets, trash, tenants, maintenance"* pain; uses investor-native terms (1031, recapture) this audience knows.

## Campaign 2 — Concentrated appreciated stockholders  ⭐ highest scrape confidence
**Source: Apollo (+ LinkedIn).**
**Who:** long-tenured / early employees on concentrated, highly appreciated stock at companies that IPO'd in the last 5–10 years with broad employee equity. Cited: **SpaceX, NVIDIA, Uber, Yahoo**; archetype = 30-yr employee with founder-priced shares.
**Why high:** easy to find, most receptive, concentrated in high-tax metros (CA ≈ ⅓ of gains to tax). LGJ data team's pick as easiest + most receptive.

**Apollo filters:**
- **Current Company:** curated IPO'd-2015–2021 list w/ broad employee equity (SpaceX, NVIDIA, Uber, Airbnb, Snowflake, Coinbase, DoorDash, Palantir, Rivian, Datadog, CrowdStrike, etc.) — paste as company-name list
- **Years in Current Company:** **5+** (proxy for early/vested equity)
- **Person Location:** SF Bay Area, San Jose, LA, Seattle, NYC + high-tax states
- **Seniority:** leave **broad** (rank-and-file hold the biggest surprise gains)
- **Email status:** Verified
> Do not filter on title/department — equity is a tenure story, not a seniority story.

**🔄 Aug 5 — SEC EDGAR as a second source (confirmed on the call).** Registration statements (**S-1**) and related filings name early employees and their share counts, and EDGAR is API-accessible back to the 1990s. Mitch confirmed the database (*"it's listed with the SEC EDGAR database"*) and steered us past the household names: the value is in the **companies that never picked up broad public traction**, plus the current AI/data-center and crypto-adjacent wave where *"all these stealth little companies"* are minting holders now. Work already in flight under `Leads/sec-triggers/` and the V2 merger-trigger files. Mitch's own caution: don't bother going back as far as the 1990s.

## Campaign 3 — Business brokers (~8,800 nationwide)  🔄 *new as of Aug 5*
**Source: BizBuySell broker directory scrape (Leg A) + IBBA member directory (Leg B) → Apollo/Blitz email enrich → MillionVerifier.**
Full build spec, run order and cost: **`Leads/Mitchell Bloom - BizBuySell Broker Scrape Spec.md`**.

**Who:** business brokers, M&A advisors and business intermediaries **with live deal flow**. A broker carrying active BizBuySell listings is sitting on multiple owners who are actively selling right now — which is the timing signal we could never get on the sellers themselves.
**Why it replaced the master bucket:** marketplace listings hide the seller by design, and the Apollo master bucket has no timing filter at all. The broker channel is the one path to actively-selling owners that is both sourceable and, per Mitch's own cold-calling, responsive.

**Scrape seeds (geo-first):**
| Level | URL pattern |
|---|---|
| State (main seed) | `bizbuysell.com/business-brokers/california/` |
| County | `bizbuysell.com/business-brokers/california/santa-clara-county/` |
| City | `bizbuysell.com/business-brokers/california/los-angeles/` |
| Broker profile | `bizbuysell.com/business-broker/{firm-slug}/{firm-slug}/{brokerId}/` |

**Filters:**
- **Location:** the fixed high-tax map only — **CA, NY, NJ, MA, MN, HI, WI, VT, DC + CO**. No expansion.
- **`active_listing_count ≥ 1`** (live deal flow + personalization payload)
- **Tier 1:** ≥1 active listing with **asking price ≥ $2M** · **Tier 2:** active listings all under $2M (lower priority, generic angle)
- **Exclude:** franchise-resale-only brokers · profiles with 0 active *and* 0 sold listings
- **Cap 3 brokers per firm** (applied after email verification)
- **Industry lean (soft sort, not a gate):** the fast-selling verticals already agreed — healthcare practices, medical clinics/aesthetics, veterinary, construction, laboratories, manufacturing, logistics, aerospace/defense, HVAC/plumbing/electrical, industrial waste
- Certifications (CBI / M&AMI / Master CBI) = quality sort, not a gate

**Fields:** broker name · firm · title · phone · firm website · profile URL · city/state/ZIP · service areas · industries served · certifications · license # · active + sold listing counts · bio · LinkedIn — **plus a child table of their active listings** (headline, industry, city/state, asking price, cash flow, revenue, EBITDA, status, date listed). The listing rows are the personalization payload; Jonathan's line on the call was *"Dara, I saw your listing on BizBuySell for 1.4, about the two retail locations."*

**✅ VERIFIED COUNTS (2026-08-05, live probe):** CA **926** · NY **446** · NJ **262** · CO **248** · MA **197** · MN 83 · WI 79 · DC 48 · HI 28 · VT 18 = **2,335 raw**. Mitch's "~8,800 nationwide" is his figure, never checked, and not what we're working from. ⚠️ **2,335 is pre-dedupe** — the directory lists brokers *"serving this area,"* not headquartered there, so brokers repeat across states and some are out-of-map entirely (a Phoenix broker showed up on the California page). Dedupe on `brokerId`, then drop out-of-map profile locations, then enrich. Real sendable count will be materially lower.

**⚠️ Email is not exposed on BizBuySell — verified on a live profile.** Zero `mailto:` links, zero email strings. Mitch's belief (*"they all have their email address"*) holds for the broker's own firm site, not for BizBuySell. What the page **does** give us: name, firm, **phone** (`tel:` present in the DOM even behind the "Show Phone Number" button), and the **firm website** — that domain is what makes enrichment possible. Chain: profile → firm domain → Apollo/Blitz by name + domain → MillionVerifier. IBBA (Leg B, ~2,800 certified brokers) exposes a public email field with a `hasEmail` filter, which is why it runs alongside.

**Mechanics (verified):** `/business-brokers/{state}/{page}/`, **30 per page**, ~80 pages for all 10 states. Angular **SSR** — broker data is in the HTML, no JSON API, parse the DOM.

**⚠️ Tooling:** the **HTTP 403 is server-side fetch only.** Real Chrome loads the directory clean — no captcha, no challenge — so this is a **`browser-harness`** job, not a paid-actor job. Probe locally; run the bulk pull on **Browser Use Cloud** (`browser-harness auth login` → `start_remote_daemon`) for proxies and stealth, which is what keeps volume off Shara's browser and IP. Stay signed out, throttle, stop the daemon when done. Apify is fallback only, though the IBBA actor is still worth ~$2.90 as a separate email-bearing source. Review CoStar ToS before scheduling recurring runs.

**Copy — not written.** Channel/referral message, distinct from every seller sequence. Mitch's requested angle, verbatim: ***"Plan first, sell second."*** Four levers: (1) the broker's client keeps more so the deal closes instead of stalling on tax, (2) **Value Builder** to raise business value pre-sale, (3) the top-producing broker's *own* income-tax exposure, (4) Mitch as the capital-gains partner in their network. Pre-empt the two objections Mitch named: *"that's up to the tax person"* and *"I don't want to kill my deal"* — frame as deal-saver, since sellers blindsided by a 30-45% hit walk away from closings.

---

# 🟡 PHASE 2 — launch when promoted

## ICP 4 — Trophy / residential home owners  (filters + copy already built)
**Source: PropStream.**
Individual owners of high-value, long-held homes (bought decades ago, huge appreciation; NOT new builds).
**Status:** most build-ready segment we have — PropStream filters done (1,508 in Beverly Hills) and **both sequences already written** (`Copy/Vertical 1…`). Demoted to Phase 2 as a *priority* call (real property above is Mitch's bigger business), but it can launch on short notice.
**Core method:** Estimated Value tiered by market ($2–3M floor) · Owner Type **Individual** · Years of Ownership 15–25+ · Pre-Probate **Exclude** · High Equity.
**⭐ Timing split:** List A — On Market / For Sale (prioritize) · List B — Off Market.

## ICP 6 — Luxury / high-echelon real-estate brokers  (channel for trophy)
**Source: Apollo.**
**Who:** brokers at the **top ~1,000 US brokerages (~$2.25T volume)** selling trophy/luxury/second homes in ultra-high-value micro-markets. Follows ICP 4 (trophy) — they source trophy-home sellers, so they share that segment's phase.

**Apollo filters:** Titles "Real Estate Broker", "Luxury Real Estate Advisor", "Realtor", "Associate Broker" · Keywords luxury/trophy/estate/high-net-worth/waterfront · Company Sotheby's / Christie's / Compass / Douglas Elliman / Coldwell Banker Global Luxury · Person Location = the luxury micro-markets (see PropStream market list) · Email Verified

---

# 🟠 PARKED (Aug 5)

## ICP 5 — Business owners / sellers  *was Campaign 3 until Aug 5*
**Why parked:** marketplace listings are anonymized by design, so there is no reliable route from a listing to the owner's inbox at scale — the finding that triggered the Aug 5 pivot to brokers. Copy already exists and stays on file: `Copy/Vertical 3. Business Sellers ($2M-$20M).md`. Revisit if the broker channel surfaces sellers directly, or if a match-and-enrich route proves out.

**The Apollo master bucket as designed (never run):** Seniority Owner/Founder/Partner/CEO · Titles Owner, Founder, President, CEO, Managing Member, Principal, Sole Proprietor · Headcount **1–50** (200 for mfg/aerospace) · Revenue **$2M–$20M** · industry/keyword lists per vertical (dental/orthodontics, veterinary, med-spa/aesthetics, HVAC/plumbing/electrical, construction, manufacturing, logistics, aerospace/defense, industrial waste) · Company Location high-tax states · Founded before ~2005.
**The marketplace signal play as designed:** scrape listing pages (BizBuySell, BusinessesForSale.com, BizQuest, LoopNet, BusinessMart, BizForSale.co) → filter $2M+ in target states → AI-match the anonymized listing to a real company (Clay) → enrich owner via Apollo/Blitz.

> **Note the reversal:** on July 14 Mitch said brokers usually won't engage and to go direct to owners. On Aug 5 he reversed it himself once the direct-seller list proved unsourceable, reporting that brokers all answer their phones. Their two objections are now copy problems, not reasons to skip the segment.

---

# 🔴 DEFERRED / UNVALIDATED (documented, not for launch)

## ICP 10 — CPAs  ❌ raised Aug 5, not scoped
Mitch, same call: *"maybe we approach CPAs at some point."* Same logic as the brokers — CPAs steer clear of tax-mitigation structures (CRTs, opportunity zones, DSTs, 1031s) out of audit fear or unfamiliarity, so their clients leave money on the table. A second referral channel. **No source, filters or copy defined.**

## ICP 7 — Institutional / LLC-veiled commercial RE  ❌ deferred
Large commercial, strip malls, office, raw land held behind **LLCs / corps / trusts**. On the call this was ~70% of Mitch's existing trust business, but it **cannot be sourced cold at scale** (no individual, no email). Revisit via county records / a "needle in a haystack" test after Phase 1 is live. *(ICP 1 already captures the individually-owned overlap.)*

## ICP 8 — Farmland  ❌ unvalidated — scope before committing
Mitch floated it (*"maybe farmland"*) July 15 — note the hedge. **Not validated:** no agreed deal-size floor, and the biggest US farmland sits **outside** the high-tax states that power the pitch, so the offer is weaker there. Same LLC/trust veiling as ICP 7. **Resolve first:** (a) does farmland volume exist *in the target states*; (b) which source returns owner contact data. Do not build until answered.

## ICP 9 — Crypto holders  ⚠️ best-effort
Big Bitcoin/crypto gains wanting to sell. Findable because crypto people put it in social bios (X/LinkedIn bio scrape, not Apollo). Low precision — deprioritize vs. the core ICPs.

---

## 2. Copy / enrichment levers (personalization, not filters)

- **Pain hooks:** *"done with the toilets, trash, tenants, and maintenance"*; outgrew their CPA; got *"conflicting advice on CRTs/CLTs"*; failed/feared 1031; dreads losing **30–45%** to cap-gains.
- **Desire:** exit day-to-day, retire, leave a **dynastic/multi-generational legacy**, 100% virtual + plain-English process.
- **Proof:** Kelly & David — **$7.6M** Midwest multifamily, failed 1031, deferred **$1.1M**. Featured in **WSJ, MarketWatch, Business Insider, US News**. (Rob Lowe — do **not** use publicly.)
- **Compliance:** disclaimer on every email; avoid "tax"/"free" in sending domains; no promissory claims; "defer" never "avoid."

---

## 3. Open items to resolve

1. **⚠️ Guarantee & B2C tension (raise with Jay — not a list decision).** Mitch's July 8 email flags real anxiety: his agreement reportedly requires leads to be Apollo-available, companies **<50 employees**, and **not filtered by city/zip**. His actual targeting is geo-specific (high-tax states), **individual-owner (arguably B2C)**, and value-filtered — and his highest-value target (in-contract sellers) isn't an Apollo motion at all. Close expectations with him directly so the guarantee terms and the real campaign match. He was explicit he doesn't want "unfulfilled expectations."
2. ~~ICP 1 copy~~ — **written** (`Copy/Vertical 4. Apartment-Rental-Commercial Sellers.md`). **The Phase-1 build blocker is now the Campaign 3 broker sequence, which does not exist yet.**
3. **Deal-size floor:** intake USP says **$1M** cap-gains min / 90 days; call set **$2M** RE floor. Pick one threshold for the revenue/value proxy.
4. **Broker referral message:** Campaign 3 (business brokers) and ICP 6 (luxury RE brokers) both run a referral/channel message, distinct from every seller sequence. Campaign 3's needs writing.
5. **CoStar ToS** on recurring BizBuySell broker-directory scraping — review before scheduling a repeat run.
6. **Broker email fill rate is unknown** until Leg A + Leg B run. BizBuySell exposes no email, so the whole list depends on the Apollo/Blitz enrich step. Do not quote Mitch a broker count before we see a verified-email rate.
7. **ICP 7 / 8 (deferred):** don't let the slowest, LLC-veiled segments gate launch. Institutional commercial = post-launch test; farmland = scope data first.

---

*Scoped to 3 launch campaigns from the July 14 strategy call, the intake form, and Mitch's July 8 + July 15 emails, **revised 2026-08-05 after the Aug 5 call**. Phase 1 = apartment/rental/commercial sellers + concentrated stockholders + **business brokers (BizBuySell)**. Direct business sellers parked (anonymized listings); trophy homes and luxury RE brokers in Phase 2; institutional commercial, farmland and CPAs deferred pending sourcing validation.*
