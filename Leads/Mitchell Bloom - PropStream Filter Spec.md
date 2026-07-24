# Mitchell Bloom — PropStream Filter Spec

**ICP:** Vertical 1, Trophy / Residential Owners
**Feeds:** `Copy/Vertical 1. Trophy-Residential Owners (No Selling Signals).md` and `(Selling Signals).md`
**Sequencer:** Instantly · **Merge field needed:** first name + email
**Built:** 2026-07-21, from the July 14 strategy call, the 2nd analysis (ICP-B), and the intake avatar.

---

## Target markets — build one saved search per city

Cities in **bold** are the go-first pick per state (highest embedded-gain density + cleanest individual ownership). Search the small enclaves by name; search big metros by **ZIP**, not city name.

### Tier 1 — build first

**California** — 13.3% top state rate, strongest pitch
- **Beverly Hills** · **Malibu** · **Montecito** · Bel Air · Pacific Palisades · Santa Barbara
- **Atherton** · Hillsborough · Los Altos · Woodside
- Newport Beach · Rancho Santa Fe · La Jolla

**Colorado** — Mitch's home turf, best expected reply rates
- **Vail** · **Aspen** · Snowmass Village · Breckenridge
- **Cherry Hills Village** · Boulder

**New York** — up to 10.9% + NYC local
- **Sagaponack** · **Water Mill** · Bridgehampton · East Hampton
- Scarsdale · Rye · Bronxville
- Manhattan *(co-op complication — test Trust owner type here)*

**Hawaii** — 11%, Mitch flagged it specifically (@21:53 "they pay through the nose")
- **Wailea/Kihei (Maui)** · Kapalua · Kailua-Kona · Kahala (Honolulu)

### Tier 2 — add once Tier 1 is running

- **New Jersey** (10.75%) — **Alpine** · Saddle River · Franklin Lakes · Rumson
- **Massachusetts** (9%) — **Weston** · Wellesley · Nantucket · Edgartown
- **Minnesota** (9.85%) — **Lake Minnetonka** (Wayzata, Orono, Deephaven)
- **Washington DC** (10.75%) — Georgetown · Kalorama
- **Vermont** (8.75%) — Stowe · Manchester
- **Wisconsin** (7.65%) — Lake Geneva

### Do NOT build
Fisher Island FL and anything in **TX / TN / WA / NV / FL**. No state income tax means the pitch loses ~10 points of urgency, and the copy leans on "the state and the IRS."

---

## ⭐ Beverly Hills — exact settings to select (start here)

Do this in order. **After each panel, watch the count at the top.** If it hits 0, the last thing you touched is the culprit — undo it and re-check.

**Location:** `Beverly Hills, CA`

| # | Panel | Setting | Value |
|---|---|---|---|
| 1 | Value & Equity | **Estimated Value** | Min **3,000,000** · Max **25,000,000** |
| 2 | Lead Lists | select one | **High Equity** |
| 3 | Property Details → Residential | check 4 | Single Family · Condo/Townhouse · Condominium (Residential) · Seasonal/Cabin/Vacation |
| 4 | Owner Info & Occupancy | **Owner Type** | **Individual only** (see cost note below — do not add Trust) |
| 5 | Owner Info & Occupancy | **Years of Ownership** | Min **25** |
| 6 | Owner Info & Occupancy | **Pre-Probate** | **Exclude** |
| 7 | Owner Info & Occupancy | **Vacant** | **No** |
| 8 | Owner Info & Occupancy | **Intra-Family Transfer** | **Exclude** |
| 9 | MLS | **On or Off Market** | **Off Market** — then leave every MLS Status blank (List A) |

**Leave blank:** Last Sale Price, Year Built, Estimated Equity %, Owner Occupied, Include Unknown Sales Dates, everything in PropStream Intelligence / Pre-Foreclosure / Lien-Bankruptcy-Divorce.

**⚠️ The two traps that keep zeroing this out:**
- **Off Market + any MLS Status selected = 0 across every city.** A property cannot be off market AND actively listed. When the toggle is Off Market, all statuses must be clear.
- **Listing Type resets to "Any" or "For Rent"** whenever you flip the On/Off toggle. If you build List B (On Market), set Listing Type to **For Sale** or you will pull rental listings ($15k–$25k "list price" = monthly rent, not a sale).

**For List B (Selling Signals) in Beverly Hills:** same as above but step 9 = **On Market**, **Listing Type: For Sale**, **MLS Status: Active · Active Under Contract · Coming Soon · Contingent** (not Pending). Expect this list to be a fraction the size of List A — that is normal.

**If Beverly Hills returns under ~20:** drop Estimated Value min to $2.5M, then Years of Ownership 25 → 20. Do not touch the exclusions.

**Owner Type = Individual only — cost decision (2026-07-21):** we are billed per contact. Trust-held records (revocable living trusts, common in these markets) frequently return the owner as *"[Family] Trust"* with no personal email, which breaks `{{firstName}}` personalization and wastes credits. Trust owners face the same capital-gains problem and the offer fits them fine — this is purely a data-quality + cost call, not an offer-fit one. Skip Corporate and Mixed too (no reachable person). Individual gives full volume anyway (1,508 in Beverly Hills alone).

---

## The qualifying math (why these filters exist)

```
Estimated Value  −  Last Sale Price  =  embedded capital gain
```

Mitch's floor is a **$2M+ transaction** with **$1M+ capital gains exposure**. For a primary residence the Section 121 exclusion ($250k single / $500k married) wipes out the first chunk, so a high-value home is not enough on its own. You need a **large spread** between today's value and what they paid.

Every filter below exists to widen or protect that spread. Anything that does not affect it is noise.

---

## 1. Estimated Value — set this FIRST (the bottleneck)

This is the filter that collapses the list to zero if it is miscalibrated. Set it before anything else, then build outward.

**Rule: keep at least a $1.5M spread between the value floor and the basis cap.**

| Market tier | Estimated Value min | Max |
|---|---|---|
| Beverly Hills, Bel Air, Malibu, Montecito, Atherton, Aspen | **$3,000,000** | $25,000,000 |
| Santa Barbara, Newport Beach, Rancho Santa Fe, Los Altos, Vail, Hamptons, Greenwich | **$2,500,000** | $25,000,000 |
| Cherry Hills, Boulder, Scarsdale, Wellesley, Maui, broader Tier 2 metros | **$2,000,000** | $25,000,000 |

**Why the $25M ceiling:** above it, essentially everything is LLC or trust held, which the Owner Type filter strips anyway. Adding headroom just adds an empty tier.

**If a market returns under ~20 leads:** lower the floor one tier before touching any other filter.

---

## 2. Owner Type — the second most important filter

**Panel:** Owner Information & Occupancy

- ✅ **Individual** — only this one
- ❌ **Trust** — skip. Billed per contact, and trust records often return as *"[Family] Trust"* with no personal email (breaks `{{firstName}}`, wastes credits). The offer fits trust owners fine — this is a data-quality + cost call. See the Beverly Hills cost note.
- ❌ Corporate — no reachable person (the bucket that killed the commercial ICP)
- ❌ Mixed

This single filter is what makes the residential ICP viable where the commercial ICP was not.

---

## 3. Years of Ownership

**Panel:** Owner Information & Occupancy

- **Min: 25** (use 20 if a market comes back thin)
- Max: blank

Long ownership is the real proxy for embedded gain. Mitch, transcript @21:53: *"they bought them in the 70s or the 80s, and their property is worth $15 million, $20 million, and they bought their property for $70,000."*

**Do not also set Last Sale Date.** Redundant.

---

## 4. Last Sale Price — use sparingly

**Panel:** Owner Information & Occupancy

Leave **blank by default.** Years of Ownership already does this job, and a basis cap set too low is what zeroed out the first Beverly Hills build.

Only apply it if a market returns an unmanageably large list. Then cap at **value floor minus $1.5M**.

---

## 5. Lead List

**Panel:** Lead Lists — one selection only

- ✅ **High Equity**

Superset of Free & Clear, so you keep the extra volume at no cost in quality.

**Do not also set an Estimated Equity percentage in the Value & Equity panel.** That double-filters equity with two different definitions and was a contributor to the zero-result build.

---

## 6. Property Types

**Panel:** Property Details → **Residential** tab

Check exactly four:
- ✅ Single Family
- ✅ Condo/Townhouse
- ✅ Condominium (Residential)
- ✅ Seasonal, Cabin, Vacation Residence *(sharpest type: second homes get **no** Section 121 exclusion, so the full gain is exposed. Critical for Vail, Aspen, Montecito.)*

**Multi-Family: select none.** The Vertical 1 copy is written around the word *home*. A duplex or trailer-park owner receiving it reads as spray-and-pray. See the parked segment at the bottom of this doc.

**Year Built: leave blank.** Redundant against Years of Ownership.

Skip beds, baths, square footage, lot size. They say nothing about capital gain.

---

## 7. MLS — this is what splits the two campaigns

**Panel:** MLS

### List A — No Selling Signals (primary, higher volume)
- **On or Off Market:** `Off Market`
- MLS Status: clear all

Feeds `Vertical 1. Trophy-Residential Owners (No Selling Signals).md`. These owners are off market **because** of the tax hit, which is exactly the angle the copy leads with.

### List B — Selling Signals (smaller, hotter)
- **On or Off Market:** `On Market`
- **Listing Type:** `For Sale` *(never "Any" — that pulls in For Rent)*
- **MLS Status:** Active, Active Under Contract, Coming Soon, Contingent
- ❌ **Not Pending** — residential pending closes in ~30 days, the sequence runs 12+ days, and the structure must be in place **before** close. Likely already too late.
- ❌ Not Canceled, Expired, Failed, Withdrawn, Sold

Feeds `(Selling Signals).md`. Expect this list to be roughly 5-10% the size of List A. That is normal and correct.

Leave MLS Status Date, Days on Market, MLS Listing Amount, Listed Below Market Price, and MLS Keywords blank. Keywords in particular ("motivated seller," "as-is") pull toward distress.

---

## 8. Exclusions that protect list quality

**Panel:** Owner Information & Occupancy
- **Pre-Probate (Deceased Owners): `Exclude`** — **the most important exclusion on this page.** Inherited property receives a **stepped-up basis** at death. The gain is erased. There is nothing to defer and no product to sell. These leads look perfect on paper (old purchase, low price, high value) and are worthless.
- **Intra-Family Transfer: `Exclude`** — records at nominal or $0 prices, which corrupts any basis logic.
- **Vacant: `No`** — USPS no-mail-delivery flag. Signals abandoned or derelict, and correlates with bad contact data.
- **Include Unknown Sales Dates: `Any`** — leave open. Setting Exclude drops a large share of otherwise good records in trust-heavy markets.
- **Owner Occupied: `Any`** — leave open until you have volume. *(Later refinement: `No` isolates second homes and investment property, which get no Section 121 exclusion. Sharper segment, smaller list.)*

**Panel:** Lien, Bankruptcy & Divorce
- Leave everything on `Any`. Beverly Hills showed Bankruptcy 0 and Divorce 0, and exclusion filters silently drop records with missing fields.

---

## Panels to skip entirely

| Panel | Why |
|---|---|
| **PropStream Intelligence** | Property condition and foreclosure scoring. Built for investors hunting distressed discounts. Mitch's prospect is the opposite: a well-maintained appreciated asset with no financial pressure. |
| **Pre-Foreclosure & Bank Owned** | Distress, often negative equity. No gain, wrong emotional frame. |
| **Tax Exemption Status** | Not needed now. *(Homestead flags a primary residence, useful later if isolating second homes.)* |
| **Assessed Land Value / Estimated Wholesale Price / Growth %** | Tax artifacts and investor metrics. None measure gain since purchase. |

---

## Lead Lists: what never to use

| Tile | Why |
|---|---|
| **Pre-Probate** | Stepped-up basis erases the gain. The trap on that screen. |
| Pre-Foreclosures, Tax Delinquency, Liens, Bankruptcy, Upside Down, Zombie, Auctions, Bank Owned | Distress, not appreciation. |
| Divorce | Real gain exists, but cold-emailing a divorce list is a bad look for a Colorado RIA. |
| Vacant / Vacant Land | No gain story, wrong ICP. |
| Cash Buyers, Flippers | Buyers and short-hold investors. Opposite of a long-held trophy home. |
| Senior Owners | Right instinct, too narrow standalone. Better as a layered age filter. |

---

## Market list — build one saved search per market

This is a **multi-market campaign**. A single city yields dozens, not thousands. Expect 20-60 qualified owners per market, so 20 markets ≈ 500-1,000 leads.

**Tier 1 — high state income tax + Mitch's named targets**

*California*
Beverly Hills · Bel Air · Malibu · Pacific Palisades · Montecito · Santa Barbara · Atherton · Los Altos · Hillsborough · Rancho Santa Fe · Newport Beach · San Francisco

*Colorado (home turf, best expected reply rates)*
Vail · Aspen · Snowmass Village · Breckenridge · Cherry Hills Village · Boulder

*New York*
Manhattan · Sagaponack · Water Mill · Bridgehampton · East Hampton · Scarsdale · Rye

*Hawaii* — Mitch @21:53: *"sellers in Hawaii... they pay through the nose."*
Maui (Wailea, Kapalua) · Kailua-Kona · Honolulu (Kahala)

**Tier 2**
Greenwich CT · Wellesley, Weston, Nantucket MA · Alpine, Saddle River NJ · Lake Minnetonka MN · Washington DC · Stowe VT

**Do not build**
Fisher Island FL and any TX / TN / WA / NV market. No state income tax means the pitch loses ~10 percentage points of urgency. Federal-only exposure is a materially weaker angle.

---

## Troubleshooting: loosen in this order

When a market returns too few, undo in this sequence and check the count after each step:

1. Clear **Last Sale Price** cap (if set)
2. Clear any **Estimated Equity** percentage (redundant with the High Equity lead list)
3. Clear **Year Built** (redundant with Years of Ownership)
4. **Include Unknown Sales Dates** → `Any`
5. **Years of Ownership** 25 → 20
6. **Estimated Value** floor down one tier
7. Add **Trust** to Owner Type and check whether emails come through
8. Switch from On Market to **Off Market** (List A is always far larger)

Do **not** loosen: Owner Type Individual, Pre-Probate Exclude, or the residential-only property types. Those protect list quality, and loosening them puts unqualified people into a compliance-sensitive sequence.

---

## Naming and handoff

Save each search as: `Bloom — V1 — {Market} — {Off Market | On Market}`

Export separately per campaign. Do not merge List A and List B, they run different sequences in Instantly.

**Before upload:** run the emails through verification. PropStream contact data is estimated and multi-match (often several emails per property). Bounce rate is the launch risk here, and warmed domains are already an open blocker on Mitch's side.

---

## Parked: the small multifamily segment

Not part of this campaign, but a real opportunity worth revisiting.

Small multi-family (Duplex, Triplex, Quadruplex, Multi-Family 2-4, Apartment house 5+, Mobile Home or Trailer Park) is frequently **individually owned**, so the Owner Type filter reaches it where it could not reach commercial. Mitch @13:27: *"Mobile home parks would really be an incredible target... owned by individuals."*

The pitch is arguably **stronger** than trophy homes:
- **Depreciation recapture** — a tax the owner cannot escape any other way
- **Failed 1031** — the exact situation in the Kelly & David case study
- The intake's own language: *"sick and tired of toilets, trash, tenants and maintenance"*

It needs its own sequence, swapping "home" for "property" and leading with recapture. The cleared Kelly & David proof ($7.6M sale, $1.1M deferred, Midwest multifamily) is a precise match.

---

*Grounded in the July 14 strategy call, `Copy/Mitchell Bloom - 2nd Analysis by Jay.md` (ICP-B), and the intake avatar. Compliance rails per `Copy/Mitchell Bloom - CAN-SPAM Compliance Standard.md`.*
