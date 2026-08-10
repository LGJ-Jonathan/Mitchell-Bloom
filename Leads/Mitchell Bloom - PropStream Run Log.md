# Mitchell Bloom — PropStream Run Log

**Config lives in `Mitchell Bloom - PropStream Filters Launch.md`. This file is progress tracking only — never copy filter values into here.**

**Reset 2026-07-31.** Rebuilt for the manual run: 30 markets instead of 228, and **on-market and off-market combined into one search per property type** instead of split. The earlier 228-city / on-market-only version is superseded.

---

## Decisions locked 2026-07-31

- **MLS block stays neutral.** On/Off Market = `All`, Listing Type = `Any`, MLS Status = nothing selected. One search returns both market states. This removes the Listing Type reset bug and the Off-Market-plus-Status zero trap, and folds Pending in automatically.
- **No copy split.** The C1 sequence is no-signal framed and covers both audiences (see that doc, line 8). On-market is ~1% of volume (4 of 366 in SF), so a second track is not worth building. No export-column check needed.
- **Apartment property types expanded to 8 (2026-07-31).** The original 5 plus `Apartments (generic)`, `High-rise Apartments`, `Apartment house (100+ units)`. These are the same asset under different county codes, not a scope change.
- **Storage, parking garages and rooming houses were considered and rejected.** They qualify on the tax logic but they are new asset classes. Mitchell was sold apartment, rental and commercial property, and the list definition sent to him says exactly that. Adding them silently would be scope drift.
- **Cooperative (Residential) excluded on substance.** Co-op ownership is shares in a housing corporation, generally personal property rather than real property, so generally not 1031 or DST eligible. Worth Mitchell confirming.
- **Target raised to ~30,000 contacts (2026-07-31).** Sending capacity explicitly out of scope per Shara. Value band $2M-$25M stays fixed as a client constraint.
- **Years of Ownership stays at 15 pending a client note.** Dropping to 10 is the largest remaining volume lever, but Mitchell's list definition says "held 15 to 20 years or more," so changing it is the same category of deviation as the property types. Not changed unilaterally.
- **State-level search is not supported by PropStream.** Counties are the substitute.
- **Skip Trace stays OFF** on every Add to Marketing List. Skip trace is billed per record. It happens once at the end, on the deduped set, after a total count review.

---

## How this run works

**The unit of work is a LEG, not a city.** A leg = one filter set, run across all 30 cities before the filter panel is touched again. Four filter sets, one pass each.

| Leg | Property Classification | Filter set |
|---|---|---|
| A | Residential | Apartments (5 multi-family 5+ types) |
| B | Residential | Rentals + Mobile-Home Parks (2-4 unit types) |
| C | Commercial | Retail / mixed-use |

**Leg D (Office) was cut 2026-07-31.** San Francisco, the densest market on the list, returned 0 office on-market and about 30 off-market. Not worth a 30-city pass, and it was the only leg requiring the `Other` classification. The Medical Bldg / Dental Bldg types stay parked as a Campaign 3 idea (owners who hold both the practice and the building).

**Per city inside a leg:** clear location → type city → Search → read the count → Add to Marketing List, **Skip Trace unchecked** → record the count here → next city. Nothing else gets touched.

**Rules**
- Counts go in the cells. `0` is a real result. Blank = not run.
- Never guess a number.
- Never hit **Clear Filter** (it sits next to Search).
- Spot-check the applied-filters panel every 10 cities.
- Stop and report if five cities in a row return 0 across a leg.

**Naming:** `V1 - {City} {ST} - {Apartments | Rentals+MHP | Commercial}`

---

## Leg tracker

| Leg | Status | Unit | Progress |
|---|---|---|---|
| A — Apartments | **complete 2026-07-31** — 68 counties run, Chittenden VT and Rutland VT skipped on the $2M floor | 70 counties | list total **4,320** |
| B — Rentals + MHP | **complete 2026-08-03** — all 72 counties run. Saved to `V1-Rentals + Mobile Home Parks`, list total **4,323**, which reconciles exactly to the sum of the 72 recorded counts | 72 counties | list total **4,323** |
| C — Commercial | **BLOCKED 2026-08-04** — PropStream returns 0 for every non-residential classification at every geographic scope, while commercial parcels are demonstrably present in the account. Not a filter problem. Pending PropStream support on account entitlement. See the Leg C section below | 70 counties | 0 / 70 |

---

## THE UNIT OF WORK IS NOW THE COUNTY

**Changed 2026-07-31.** The city-by-city pass is **superseded**. Everything below the county tracker is kept for the record, not as a work list.

**Why the switch.** A county-level location test on the frozen filter set, run against markets already worked city by city:

| Location | County search | City-by-city result |
|---|---|---|
| Kings County NY | 1,248 | 1,248 (Brooklyn) — identical, same geography |
| Los Angeles County CA | 450 | ~6 cities run so far |
| Hudson County NJ | 23 | 5, across nine separate city searches |

Hudson is the case that settles it: nine city searches found 5 records, one county search finds 23. The difference is unincorporated land and municipalities that were never on the city list. The county is a strict superset of the cities inside it, costs one search instead of forty, and PropStream dedupes into the marketing list on the way in.

**Kings, Queens, New York and Bronx counties are deliberately excluded** from the county pass. They are already fully covered by the Brooklyn, Queens, Manhattan and Bronx city runs, and re-adding them burns Saves quota for records already in the list.

**Filter set is frozen for the whole pass.** Locations change, nothing else. Correct state is Lead Lists 1, Property Details 2, Owner Information & Occupancy 5, MLS no badge, Estimated Value 2000000 to 25000000.

---

## County tracker — Leg A (Apartments)

`done` = run and added to `V1-Apartment Rental Commercial Sellers`, Skip Trace unchecked. `0` is a real result.

**70 counties total.**

### New York (4)

Kings, Queens, New York and Bronx excluded — covered by the city runs.

| County | Status |
|---|---|
| Richmond NY | done (1) |
| Westchester NY | done (15) |
| Nassau NY | done (62) |
| Suffolk NY | done (122) |

### California (21)

| County | Status |
|---|---|
| Los Angeles CA | done (450) |
| Orange CA | done (312) |
| San Diego CA | done (118) |
| Alameda CA | done (91) |
| San Francisco CA | done (366) |
| Santa Clara CA | done (397) |
| San Mateo CA | done (56) |
| Contra Costa CA | done (22) |
| Sacramento CA | done (19) |
| Marin CA | done (17) |
| Sonoma CA | done (47) |
| Napa CA | done (3) |
| Solano CA | done (5) |
| Ventura CA | done (4) |
| Santa Barbara CA | done (18) |
| Riverside CA | done (33) |
| San Bernardino CA | done (21) |
| San Joaquin CA | done (3) |
| Stanislaus CA | done (4) |
| Fresno CA | done (4) |
| Kern CA | done (8) |

### New Jersey (10)

| County | Status |
|---|---|
| Hudson NJ | done (23) |
| Essex NJ | done (11) |
| Bergen NJ | done (4) |
| Union NJ | done (2) |
| Passaic NJ | done (2) |
| Middlesex NJ | done (0) |
| Monmouth NJ | done (6) |
| Ocean NJ | done (52) |
| Mercer NJ | done (1) |
| Camden NJ | done (0) |

### Massachusetts (9)

| County | Status |
|---|---|
| Suffolk MA | done (80) |
| Middlesex MA | done (84) |
| Norfolk MA | done (18) |
| Essex MA | done (16) |
| Worcester MA | done (5) |
| Hampden MA | done (0) |
| Bristol MA | done (8) |
| Plymouth MA | done (10) |
| Barnstable MA | done (123) |

### Colorado (8)

| County | Status |
|---|---|
| Denver CO | done (20) |
| Boulder CO | done (78) |
| Jefferson CO | done (9) |
| Arapahoe CO | done (3) |
| Adams CO | done (8) |
| El Paso CO | done (2) |
| Larimer CO | done (3) |
| Weld CO | done (2) |

### Minnesota (5)

| County | Status |
|---|---|
| Hennepin MN | done (32) |
| Ramsey MN | done (11) |
| Dakota MN | done (1) |
| Anoka MN | done (0) |
| St. Louis MN | done (1) |

### Wisconsin (6)

| County | Status |
|---|---|
| Milwaukee WI | done (7) |
| Dane WI | done (0) |
| Waukesha WI | done (0) |
| Brown WI | done (0) |
| Racine WI | done (0) |
| Kenosha WI | done (0) |

### Hawaii (4)

| County | Status |
|---|---|
| Honolulu HI | done (26) |
| Maui HI | done (1) |
| Hawaii HI | done (12) |
| Kauai HI | done (0) |

### Vermont (2)

| County | Status |
|---|---|
| Chittenden VT | skipped - $2M floor, near-certain zero |
| Rutland VT | skipped - $2M floor, near-certain zero |

### District of Columbia (1)

| County | Status |
|---|---|
| District of Columbia | done (190) |

---

## County tracker — Leg B (Rentals + MHP)

`done` = run and added to **`V1-Rentals + Mobile Home Parks`**, Skip Trace unchecked. `0` is a real result.

**72 counties total.**

### Filter set tightened 2026-07-31

Two changes approved mid-leg, after Kings NY returned 8,841 on the original set:

- **Owner Occupied: No** (was Any)
- Years of Ownership stays at **Min 15**. A 20-year variant was tested and rejected.

Correct badge state for the rest of Leg B: **Lead Lists 1, Property Details 2, Owner Information & Occupancy 6, MLS no badge**, Estimated Value 2000000 to 25000000.

**Value & Equity 1 is the Estimated Value gate — expected, not contamination.** PropStream files Estimated Value under Value & Equity, not Property Details, so that badge is the $2M-$25M band being counted, not an extra filter. Correct state is **Lead Lists 1, Property Details 2, Owner Information & Occupancy 6, Value & Equity 1, MLS none.**

**Badge rule amended 2026-08-03 — Value & Equity renders no badge on a loaded saved search.** When the filter set is loaded from `Bloom - Leg B - Rentals+MHP - FROZEN`, the Value & Equity section shows **no badge and no Estimated Value row**, even though the gate is present and working. Confirmed: the inputs read 2000000 and 25000000, and San Francisco returned exactly 282. A hand-built set shows the badge; a loaded one does not.

**At every checkpoint verify the Estimated Value INPUTS read 2000000 and 25000000, not the badge.** Expected badge state is now: **Lead Lists 1, Property Details 2, Owner Information & Occupancy 6, MLS none, and Value & Equity either 1 or none** depending on whether the set was hand-built or loaded from the saved search. A missing Value & Equity badge on a loaded set is not a mismatch.

**Why.** A counts-only funnel on Kings NY, nothing saved:

| Owner Occupied | Kings NY count |
|---|---|
| Any | 8,841 |
| No | 1,463 |
| Yes | 7,378 |

`1,463 + 7,378 = 8,841` exactly, so the occupancy data is complete and no unknown-occupancy bucket is being dropped by either filter. The 83% cut is real Brooklyn owner-occupancy: two- and three-family houses whose owner lives in one unit. Those are not the absentee rental holders this campaign targets. A 15 → 20 year variant was also measured (1,463 → 1,221) and **not** adopted.

### Filter set is now a saved search — 2026-08-03

**`Bloom - Leg B - Rentals+MHP - FROZEN`** in Saved Searches holds the exact frozen set. Load it instead of rebuilding.

Why it exists: an agent-session `/clear` destroys the Chrome MCP tab group, and the reconnect opens a **new** tab with a fresh, unfiltered PropStream. The filter panel does not survive. On 2026-08-03 the whole set had to be rebuilt by hand from the spec below.

**`Mitchell Bloom - PropStream Filters Launch.md` is NOT a valid source for Leg B.** Its SEARCH 2 is the superseded on-market build — it specifies MLS On Market, Listing Type For Sale and four MLS statuses, and has no Owner Occupied line. Building from it produces a wrong set that looks verified. The authoritative spec is the badge state in this section.

**Rebuild calibration.** After any rebuild, run San Francisco County CA counts-only before saving anything. Recorded figure is **282**; within 1% (279-285) passes. The 2026-08-03 rebuild returned exactly 282.

**Checkpoint 2026-08-03, 22 of 72 counties.** Applied-filters panel re-read and matches target exactly: Lead Lists 1, Property Details 2, Owner Information & Occupancy 6, Value & Equity 1, everything else no badge. Marketing list total **3,890** against a recorded-count sum of 3,890 — every save landed, and the SF re-run added 0 net, re-confirming that duplicate saves are free.

**Marketing-list picker gotcha.** In the Add to Marketing List dropdown, `V1-Rentals + Mobile Home Parks` sits next to `V1-Apartment Rental Commercial Sellers` (closed) and `V1 SF CA Apartments`. Typing into the box does not filter — it creates a new list. Scroll and click the exact row, and read the name in the dialog before hitting Save every time.

### Destination list changed 2026-07-31

Leg B now saves to **`V1-Rentals + Mobile Home Parks`**.

`V1-Apartment Rental Commercial Sellers` is **closed**. It holds Leg A (4,320) plus three Leg B counties saved into it by mistake before the change. Nothing further goes into it.

**Kings NY, Queens NY and San Francisco CA were re-run** into the new list on the tightened filters. Their counts in the table below are the new ones. The earlier figures — **Kings 8,841, Queens 547, San Francisco 721** — were taken on the old 15-year, Owner-Occupied-Any filter set and saved to the wrong list. Do not compare the two sets of numbers; they measure different populations.

**The four NYC counties ARE included in Leg B.** Leg A excluded Kings, Queens, New York and Bronx because its city-by-city pass had already covered them. Leg B has no city runs behind it, so they must be run.

### New York (8)

| County | Status |
|---|---|
| Kings NY | done (1464) |
| Queens NY | done (125) |
| New York NY | done (138) |
| Bronx NY | done (9) |
| Richmond NY | done (2) |
| Westchester NY | done (2) |
| Nassau NY | done (6) |
| Suffolk NY | done (88) |

**New York NY — RESOLVED 2026-08-03. The working entry is `New York, NY`.**

Three entries were probed across two sessions. Only the third works:

| Entry probed | Result | Verdict |
|---|---|---|
| `New York County, NY` | typing returns `No data` | does not exist |
| `New York City County, NY` | 0, all lead-list tiles 0 | dead entry |
| `Manhattan, NY` | 0, High Equity 2, Free & Clear 2 | dead entry |
| **`New York, NY`** | **138** | **live — this is the one** |

`New York, NY` returns real Manhattan data: Cash Buyers 91,108, Vacant 6,682, Pre-Foreclosures 743, Bank Owned 288, High Equity 99,999+ (capped). Result addresses are Manhattan ZIPs (10024, 10035) and the map pins sit on Manhattan island, so this is New York County geography, not all five boroughs. 138 saved to `V1-Rentals + Mobile Home Parks`, Skip Trace unchecked.

**Use `New York, NY` for the Leg C commercial pass too.** Do not retry the three dead entries.

### California (21)

| County | Status |
|---|---|
| Los Angeles CA | done (800) |
| Orange CA | done (237) |
| San Diego CA | done (184) |
| Alameda CA | done (106) |
| San Francisco CA | done (282) |
| Santa Clara CA | done (305) |
| San Mateo CA | done (100) |
| Contra Costa CA | done (1) |
| Sacramento CA | done (1) |
| Marin CA | done (23) |
| Sonoma CA | done (10) |
| Napa CA | done (1) |
| Solano CA | done (5) |
| Ventura CA | done (1) |
| Santa Barbara CA | done (8) |
| Riverside CA | done (2) |
| San Bernardino CA | done (4) |
| San Joaquin CA | done (4) |
| Stanislaus CA | done (0) |
| Fresno CA | done (0) |
| Kern CA | done (0) |

### New Jersey (10)

| County | Status |
|---|---|
| Hudson NJ | done (3) |
| Essex NJ | done (0) |
| Bergen NJ | done (0) |
| Union NJ | done (0) |
| Passaic NJ | done (0) |
| Middlesex NJ | done (0) |
| Monmouth NJ | done (2) |
| Ocean NJ | done (81) |
| Mercer NJ | done (0) |
| Camden NJ | done (0) |

### Massachusetts (9)

| County | Status |
|---|---|
| Suffolk MA | done (49) |
| Middlesex MA | done (95) |
| Norfolk MA | done (45) |
| Essex MA | done (3) |
| Worcester MA | done (0) |
| Hampden MA | done (0) |
| Bristol MA | done (0) |
| Plymouth MA | done (0) |
| Barnstable MA | done (19) |

### Colorado (8)

| County | Status |
|---|---|
| Denver CO | done (4) |
| Boulder CO | done (55) |
| Jefferson CO | done (8) |
| Arapahoe CO | done (0) |
| Adams CO | done (0) |
| El Paso CO | done (2) |
| Larimer CO | done (2) |
| Weld CO | done (0) |

### Minnesota (5)

| County | Status |
|---|---|
| Hennepin MN | done (1) |
| Ramsey MN | done (1) |
| Dakota MN | done (0) |
| Anoka MN | done (0) |
| St. Louis MN | done (0) — PropStream entry is `Saint Louis County, MN` |

### Wisconsin (6)

| County | Status |
|---|---|
| Milwaukee WI | done (0) |
| Dane WI | done (0) |
| Waukesha WI | done (0) |
| Brown WI | done (0) |
| Racine WI | done (0) |
| Kenosha WI | done (0) |

### Hawaii (4)

| County | Status |
|---|---|
| Honolulu HI | done (16) |
| Maui HI | done (0) |
| Hawaii HI | done (0) |
| Kauai HI | done (0) |

### District of Columbia (1)

| County | Status |
|---|---|
| District of Columbia | done (29) — PropStream entry is `District Of Columbia County, DC` |

---

## County tracker - Leg B EXPANSION (added 2026-08-04)

**This is an addition to Leg B, not a revision of it.** The original 72-county tracker above is closed at **4,323** and is not modified by this pass. Counts for the expansion are recorded here only.

**Why these counties.** The original 72 were cut early on a density heuristic borrowed from Leg A. **Leg B does not follow density, it follows price per door** — a 2-4 unit property has to clear $2M on its own. So the expensive coastal and resort counties that a density cut discarded are the ones most likely to produce here. These 42 counties sit inside the **same ten target states**; no new states are added and the geography rule is unchanged. **Vermont was never run for Leg B at all** and is included here, which closes the tenth target state.

**Wisconsin is deliberately excluded** — all six counties in the original pass returned 0. **Hawaii is already complete** at all four real counties.

**Filter set:** unchanged, loaded from `Bloom - Leg B - Rentals+MHP - FROZEN`. Destination list unchanged: `V1-Rentals + Mobile Home Parks`. Skip Trace unchecked on every save.

**Calibration 2026-08-04:** San Francisco County CA returned **283** against the recorded 282 (pass band 279-285). Within drift, passed. Saves quota checked before the run: **35,758 remaining**, 28% used, resets 08/20/2026.

**Stop rule for this pass:** the five-consecutive-zeros rule is **suspended**. Many of these counties are expected to return 0, particularly upstate New York, Minnesota and Vermont. Zeros are recorded and the run continues.

### Tier 1 - highest expected value (11)

| County | Status |
|---|---|
| Nantucket MA | 39 |
| Dukes MA | 6 |
| Cape May NJ | 38 |
| Pitkin CO | 55 |
| Eagle CO | 6 |
| Summit CO | 0 |
| Routt CO | 0 |
| San Miguel CO | 1 |
| Santa Cruz CA | 17 |
| Monterey CA | 3 |
| San Luis Obispo CA | 4 |

### Tier 2 (17)

| County | Status |
|---|---|
| Atlantic NJ | 4 |
| Morris NJ | 0 |
| Somerset NJ | 0 |
| Burlington NJ | 1 |
| Rockland NY | 8 |
| Orange NY | 0 |
| Dutchess NY | 5 |
| Ulster NY | 4 |
| Putnam NY | 0 |
| Sullivan NY | 1 |
| Columbia NY | 6 |
| Placer CA | 3 |
| El Dorado CA | 1 |
| Nevada CA | 2 |
| Mendocino CA | 0 |
| Berkshire MA | 0 |
| Hampshire MA | 0 |

### Tier 3 (14)

| County | Status |
|---|---|
| Albany NY | 0 |
| Monroe NY | 0 |
| Erie NY | 2 |
| Onondaga NY | 0 |
| Garfield CO | 7 |
| Douglas CO | 0 |
| Pueblo CO | 0 |
| Washington MN | 0 |
| Scott MN | 0 |
| Carver MN | 0 |
| Olmsted MN | 0 |
| Stearns MN | 0 |
| Chittenden VT | 0 |
| Rutland VT | 0 |

### Vermont diagnostic 2026-08-04 (counts only, nothing saved)

Run after the expansion closed, to test whether the Vermont zeros were a data-coverage artifact rather than a real absence. Approved filter change, scoped to this test. **No recorded county count was changed. The zeros stand as run.**

Location: Chittenden County, VT.

| Filter state | Count |
|---|---|
| Frozen set (High Equity + Estimated Value 2000000-25000000) | 0 |
| High Equity removed, value gate still 2000000-25000000 | 0 |
| High Equity removed **and** value gate cleared | 193 |

**Finding: two independent causes, and the value floor alone is sufficient.** Removing High Equity did not move the count off 0, so the $2M floor by itself produces 0 in Chittenden. The 193 properties that appear once the gate is cleared all sit well below $2M (map markers ranged roughly $415K to $990K). Leg B's price-per-door premise simply does not reach Vermont.

**Separately, PropStream appears to carry no equity or mortgage data for Vermont.** On Chittenden every equity-derived lead-list tile reads 0 (High Equity 0, Free & Clear 0, Upside Down 0, Cash Buyers 0) while non-equity tiles populate normally (Senior Owners 10,611, Tired Landlords 9,490, Failed Listings 1,447, Vacant 245, Bank Owned 48). Rutland showed the same High Equity 0 with Cara 1,249 and Vacant 379. This is a coverage gap worth raising with PropStream support alongside the Leg C commercial finding, but it does **not** change the Vermont result, because the value floor zeroes the state on its own.

Saved search reloaded immediately after the test and re-verified: Lead Lists 1, Property Details 2, Owner Information & Occupancy 6, MLS none, Estimated Value inputs 2000000 and 25000000.

### Entry-name cautions for this pass

- `Dukes County, MA` is Martha's Vineyard — that is the literal entry name.
- `Orange County, NY` is not Orange County CA, which is already run in the original pass.
- `San Miguel County, CO` is not San Miguel County NM.
- Use the full `County, ST` form for every location.

---

## Leg C (Commercial) — BLOCKED 2026-08-04

**Leg C is blocked pending PropStream support.** No counties were run. `V1-Commercial` was created and stands at **0**. Nothing was saved, exported, skip traced or ordered at any point during this investigation.

**The finding: PropStream returns 0 for every non-residential property classification, at every geographic scope, while commercial parcels are demonstrably present in the account.** This is an account/entitlement question, not a filter configuration problem. Shara is taking it to PropStream support directly.

### The Leg C filter set that was built and approved

Commercial classification; four chips covering the six spec'd types (`Neighborhood Shopping Center, Strip Center/Mall, Enterprise Zone` is a single combined chip in PropStream's UI, not three); Owner Type Individual; Owner Occupied deliberately unset (on commercial, owner-occupied means the owner's business operates there — a strong prospect, not a disqualifier); Vacant No; Pre-Probate Exclude; Intra-Family Transfer Exclude; Years of Ownership 15+; High Equity; **no value gate** (Estimated Value is blank on commercial records, so any floor returns 0 across the board); MLS neutral.

### Test results — all zero

**Value-gate funnel, San Francisco County, counts only.** Ruled out the owner/equity block as the cause — it was already 0 before any of those filters applied:

| Step | Filters | Count |
|---|---|---|
| a | Commercial classification only | 0 |
| b | a + the four type chips | 0 |
| c | b + Owner Type Individual | 0 |
| d | c + High Equity | 0 |
| e | d + Years of Ownership 15+ | 0 |
| f | e + Vacant No, Pre-Probate Exclude, Intra-Family Exclude | 0 |

**Classification and control tests:**

| Test | Location | Count |
|---|---|---|
| Classification = **All**, no other filters | San Francisco County | **18,949** |
| Commercial + **Select All** (57 types), no other filters | San Francisco County | 0 |
| Commercial + **Select All** (57 types), no other filters | Los Angeles County | 0 |
| Leg B frozen Residential set (control) | San Francisco County | **282** |

**Geographic scope tests, Commercial + all 57 types, no other filters:**

| Location unit | Count |
|---|---|
| San Francisco, CA (city) | 0 |
| ZIP 94103 | 0 |
| ZIP 94110 | 0 |
| Hand-drawn map polygon, Market/Mission corridor | 0 |
| Classification = **Other** + all 7 type groups, San Francisco County | 0 |

Every search verifiably scoped correctly — the Lead List badges rescoped at each level rather than going stale (ZIP 94103 High Equity 3,728; ZIP 94110 High Equity 10,826; drawn boundary High Equity 9, Cash Buyers 8, Vacant 1). These are real zeros, not searches that failed to run.

### Commercial records DO exist in this account

Direct address lookup on **845 Market St, San Francisco** returns **six records, all with commercial property types**:

| APN | Property Type |
|---|---|
| 3705-050 | Regional Shopping Center or Mall with Anchor store |
| 3705-051 | Department Store (apparel, household goods, furniture) |
| 3705-052 | Commercial Office (General) |
| 3705-055 | Theater |
| 3705-056 | Regional Shopping Center or Mall with Anchor store |
| A1130626 | Equipment / Supplies |

**Map-pin observation (2026-08-04).** While positioning the map for the drawn-polygon test, a pin inside the Market Street corridor returned **845 Market St, 52,636 SqFt / 188,238 lot**, with a commercial icon — **a commercial parcel rendering as a live pin on the map while the results pane simultaneously read 0 PROPERTIES.** The parcel is in the account, inside the searched geography, visible in the viewport, and invisible to the classification filter at the same moment.

### What this narrows it to

- **Both non-residential classifications are affected.** `Other` (which holds the Office Property Types group) is equally dead — 0 with all 7 type groups selected. So this is not specific to the Commercial classification.
- **Residential is unaffected.** Leg B's frozen set still returns exactly 282 on San Francisco County, the same calibration figure as when it was built.
- **The property types were never the constraint.** The funnel was already 0 at step (a), before any type chip, owner filter or lead list applied.
- **Location unit is not the variable.** County, city, ZIP and hand-drawn polygon all behave identically.
- **Sampled commercial records show `Owner Type: Corporate` and blank `Estimated Value`.** The blank Estimated Value corroborates the earlier 2026-07-29 note that commercial records carry no EST. VALUE and no EST. EQUITY, and that map pins read N/A. Note that Corporate ownership would in any case be stripped by the spec'd `Owner Type: Individual` — but that filter never got the chance to bind.

### On the 205 figure from 2026-07-29

`PropStream Filters Launch.md` records San Francisco returning **205** individually-owned, 15-year-held, high-equity commercial properties with the value filter removed. That cannot be reconciled with what the account does today. Either that figure was wrong — the run log already flags every number from that session as unreliable — or non-residential access has changed since. Not resolvable from inside the search panel. **Treat 205 as a lead, not a baseline.**

### Options if support confirms non-residential is not included

1. **Source Leg C elsewhere.** `PropStream Filters Launch.md` already anticipated this: *"Commercial is the one segment where LoopNet / Crexi may simply be a better source than PropStream."* Written before the filter was known to be broken; now the more practical route.
2. **Drop Leg C.** Legs A and B delivered 8,643 records combined against a realistic landing zone of 10,000-15,000 across all three legs. Commercial was always expected to be the thinnest leg, and it is the one with no working value gate even if the filter worked.

---

## SUPERSEDED — City tracker — Leg A (Apartments)

> **This section is history, not a work list.** The county pass above replaces it. Do not resume city-by-city work from here. Records already added by these city runs stay in the marketing list and dedupe against the county pass on the way in.
>
> Kept because it records which markets were touched, what they returned, and the two five-consecutive-zero stops that led to the county switch.

`done` = was run and added to `V1-Apartment Rental Commercial Sellers`. Counts are not tracked per city; the list total is the metric.

> **Restart the agent session every ~40 cities.** In the agent's terminal tab run `/clear`, then paste the launch prompt again. All state lives in this file, so nothing is lost and it resumes at the first unmarked city.
>
> Why: every browser tool result stays in context for the whole session, so cost per city climbs steadily even though the work per city is identical. Measured on this run, **92% of usage was at >150k context and 86% came from the `claude-in-chrome` MCP server**. Restarting resets both to near zero. Prefer `/clear` over `/compact` here, since the conversation holds nothing this file does not.
>
> Check progress from a separate terminal tab, never by typing into the agent's tab:
> ```bash
> cd ~/Desktop/LGJ\ Clients/Mitchell-Bloom && f='Leads/Mitchell Bloom - PropStream Run Log.md' && echo "$(grep -cE '^\| [^|]+ \| done \|$' "$f") of $(grep -cE '^\| [^|]+ \|( done)? +\|$' "$f") cities"
> ```

**303 cities total. 41 done, 262 remaining.**

> ⚠️ The first 30 cities were run on the **original 5 property types**, before `Apartments (generic)`, `High-rise Apartments` and `Apartment house (100+ units)` were added. Whatever those three hold in Brooklyn, Los Angeles, San Francisco and the rest is still uncollected. Sweep those 30 again if the total lands short.

---

## SUPERSEDED — TIER 1 — Mitchell's sweet spot

Dense, older, individually-owned multi-family in the highest-tax states, at values that land inside $2M-$25M rather than above it.

**Why these:** Brooklyn returned **1,248** on this exact filter set. San Jose returned **75**. Same day, same filters. Brooklyn is wall-to-wall pre-war walkups bought decades ago and still held personally; San Jose is newer stock at higher per-unit values with more entity ownership. Every market in Tier 1 was picked for the Brooklyn pattern: age of stock, density of 5-20 unit buildings, individual ownership, high state capital-gains rate, and a value band that clears $2M without blowing past $25M.

### New York metro (5 of 31 done)

| City | Status |
|---|---|
| Manhattan / New York | done |
| Brooklyn | done |
| Queens | done |
| Bronx | done |
| Staten Island | done |
| Yonkers | done |
| Mount Vernon | done (0) |
| New Rochelle | done (0) |
| White Plains | done |
| Port Chester | done (0) |
| Peekskill | done (0) |
| Spring Valley | done (0) |
| Nyack | done (0) |
| Newburgh | done |
| Beacon | done (0) |
| Kingston | done (0) |
| Hempstead | done (0) |
| Freeport | done (0) |
| Long Beach NY | done (0) |
| Valley Stream | skipped - suburban, no qualifying stock |
| Lynbrook | skipped - suburban, no qualifying stock |
| Rockville Centre | skipped - suburban, no qualifying stock |
| Baldwin | skipped - suburban, no qualifying stock |
| Oceanside NY | skipped - suburban, no qualifying stock |
| Elmont | skipped - suburban, no qualifying stock |
| Glen Cove | skipped - suburban, no qualifying stock |
| Great Neck | skipped - suburban, no qualifying stock |
| Mineola | skipped - suburban, no qualifying stock |
| Hicksville | skipped - suburban, no qualifying stock |
| Huntington NY | skipped - suburban, no qualifying stock |
| Patchogue | skipped - suburban, no qualifying stock |

### North Jersey (3 of 43 done)

| City | Status |
|---|---|
| Jersey City | done |
| Hoboken | done |
| Union City | done |
| West New York | done |
| North Bergen | done (0) |
| Weehawken | done |
| Guttenberg | done (0) |
| Secaucus | done (0) |
| Bayonne | done (0) |
| Harrison NJ | done (0) |
| Kearny | done (0) |
| Newark | done |
| East Orange | done (0) |
| Irvington |  |
| Bloomfield |  |
| Montclair |  |
| Belleville |  |
| Nutley |  |
| Clifton |  |
| Passaic |  |
| Paterson |  |
| Garfield |  |
| Lodi |  |
| Rutherford |  |
| Lyndhurst |  |
| Elizabeth |  |
| Union NJ |  |
| Linden |  |
| Rahway |  |
| Roselle |  |
| Plainfield |  |
| Fort Lee |  |
| Cliffside Park |  |
| Palisades Park |  |
| Fairview NJ |  |
| Ridgefield NJ |  |
| Edgewater |  |
| Englewood NJ |  |
| Teaneck |  |
| Bergenfield |  |
| Hackensack |  |
| Perth Amboy |  |
| New Brunswick |  |

### Bay Area (15 of 37 done)

| City | Status |
|---|---|
| San Francisco | done |
| Oakland | done |
| Berkeley | done |
| Alameda | done |
| Emeryville | done |
| Richmond | done |
| San Leandro |  |
| Hayward |  |
| Union City CA |  |
| Fremont | done |
| Milpitas | done |
| Daly City | done |
| South San Francisco | done |
| San Bruno | done |
| Millbrae | done |
| Burlingame | done |
| San Mateo | done |
| Belmont | done |
| San Carlos | done |
| Redwood City | done |
| Menlo Park | done |
| Palo Alto | done |
| Mountain View | done |
| Sunnyvale | done |
| Santa Clara | done |
| San Jose | done |
| Campbell | done |
| Vallejo | done |
| Concord | done |
| Walnut Creek | done |
| Antioch | done (0) |
| Pittsburg | done (0) |
| San Rafael | done |
| Novato | done |
| Petaluma | done |
| Santa Rosa | done |
| Napa | done |

### LA basin + Orange + San Diego (6 of 48 done)

| City | Status |
|---|---|
| Los Angeles | done |
| Long Beach | done |
| Santa Monica | done |
| West Hollywood | done |
| Culver City |  |
| Glendale |  |
| Burbank |  |
| Pasadena | done |
| Alhambra |  |
| Monterey Park |  |
| San Gabriel |  |
| El Monte |  |
| Huntington Park |  |
| South Gate |  |
| Bell |  |
| Bell Gardens |  |
| Lynwood |  |
| Compton |  |
| Inglewood |  |
| Hawthorne |  |
| Gardena |  |
| Torrance |  |
| Carson |  |
| Bellflower |  |
| Downey |  |
| Norwalk |  |
| Whittier |  |
| Anaheim |  |
| Santa Ana |  |
| Garden Grove |  |
| Westminster CA |  |
| Fullerton |  |
| Buena Park |  |
| La Habra |  |
| Orange |  |
| Costa Mesa |  |
| Huntington Beach |  |
| Newport Beach | done |
| Tustin |  |
| San Diego | done |
| National City |  |
| Chula Vista |  |
| La Mesa |  |
| El Cajon |  |
| Escondido |  |
| Oceanside |  |
| Vista |  |
| San Marcos |  |

### Boston inner ring + MA gateway cities (4 of 32 done)

| City | Status |
|---|---|
| Boston | done |
| Cambridge | done |
| Somerville | done |
| Chelsea |  |
| Everett |  |
| Malden |  |
| Medford |  |
| Revere |  |
| Winthrop |  |
| Quincy |  |
| Brookline |  |
| Newton |  |
| Watertown |  |
| Waltham |  |
| Arlington |  |
| Lynn |  |
| Salem |  |
| Peabody |  |
| Saugus |  |
| Randolph |  |
| Milton |  |
| Lowell |  |
| Lawrence |  |
| Haverhill |  |
| Methuen |  |
| Worcester | done |
| Springfield |  |
| Chicopee |  |
| Holyoke |  |
| New Bedford |  |
| Fall River |  |
| Brockton |  |

### Hawaii + DC (2 of 15 done)

| City | Status |
|---|---|
| Honolulu | done |
| Pearl City |  |
| Waipahu |  |
| Kaneohe |  |
| Kailua |  |
| Mililani |  |
| Ewa Beach |  |
| Kapolei |  |
| Wailuku |  |
| Kahului |  |
| Kihei |  |
| Lahaina |  |
| Hilo |  |
| Kailua-Kona |  |
| Washington DC | done |

**TIER 1 — Mitchell's sweet spot (run these first): 206 cities, 35 done, 171 remaining.**

---

## SUPERSEDED — TIER 2 — secondary

Lower state tax, newer or thinner multi-family stock, or values that struggle to clear the $2M floor.

> Colorado, Minnesota, Wisconsin and Vermont are expected to return **thin or empty**. Individually-owned multi-family in Milwaukee, Duluth or Burlington rarely clears $2M, and their state capital-gains rates are a fraction of CA, NY, NJ or HI. Near-zero here is the value floor working, not a broken filter. Run them last, and only if Tier 1 lands short of target.

### California, inland and outer (2 of 19 done)

| City | Status |
|---|---|
| Sacramento | done |
| Stockton |  |
| Modesto |  |
| Fresno |  |
| Bakersfield |  |
| Riverside |  |
| San Bernardino |  |
| Ontario |  |
| Pomona |  |
| Corona |  |
| Ventura |  |
| Oxnard |  |
| Thousand Oaks |  |
| Simi Valley |  |
| Santa Barbara | done |
| Palm Springs |  |
| Palm Desert |  |
| Pleasanton |  |
| Livermore |  |

### New York, upstate (0 of 10 done)

| City | Status |
|---|---|
| Buffalo |  |
| Rochester NY |  |
| Syracuse |  |
| Albany |  |
| Schenectady |  |
| Troy |  |
| Utica |  |
| Binghamton |  |
| Niagara Falls |  |
| Poughkeepsie |  |

### New Jersey, south and shore (0 of 9 done)

| City | Status |
|---|---|
| Woodbridge |  |
| Edison |  |
| Trenton |  |
| Camden |  |
| Atlantic City |  |
| Vineland |  |
| Toms River |  |
| Lakewood |  |
| Cherry Hill |  |

### Massachusetts, outer (0 of 6 done)

| City | Status |
|---|---|
| Framingham |  |
| Taunton |  |
| Weymouth |  |
| Beverly |  |
| Pittsfield |  |
| Barnstable |  |

### Colorado (2 of 18 done)

| City | Status |
|---|---|
| Denver | done |
| Boulder | done |
| Aurora |  |
| Lakewood |  |
| Littleton |  |
| Englewood CO |  |
| Wheat Ridge |  |
| Arvada |  |
| Westminster CO |  |
| Thornton |  |
| Broomfield |  |
| Longmont |  |
| Loveland |  |
| Fort Collins |  |
| Greeley |  |
| Colorado Springs |  |
| Pueblo |  |
| Grand Junction |  |

### Minnesota (1 of 16 done)

| City | Status |
|---|---|
| Minneapolis | done |
| St. Paul |  |
| Bloomington |  |
| Richfield |  |
| St. Louis Park |  |
| Edina |  |
| Minnetonka |  |
| Brooklyn Park |  |
| Coon Rapids |  |
| Burnsville |  |
| Eagan |  |
| Duluth |  |
| Rochester MN |  |
| St. Cloud |  |
| Mankato |  |
| Moorhead |  |

### Wisconsin (1 of 14 done)

| City | Status |
|---|---|
| Milwaukee | done |
| West Allis |  |
| Wauwatosa |  |
| Madison |  |
| Green Bay |  |
| Kenosha |  |
| Racine |  |
| Appleton |  |
| Oshkosh |  |
| Eau Claire |  |
| La Crosse |  |
| Janesville |  |
| Sheboygan |  |
| Waukesha |  |

### Vermont (0 of 5 done)

| City | Status |
|---|---|
| Burlington |  |
| South Burlington |  |
| Rutland |  |
| Essex |  |
| Colchester |  |

**TIER 2 — secondary (run after Tier 1): 97 cities, 6 done, 91 remaining.**

---

## Note on the stale reference numbers

The 2026-07-29 agent run recorded a San Francisco funnel of `787 → 267` at the value gate. The 2026-07-31 manual rebuild recorded `506 → 366` with every filter screenshot-verified against the spec (property types, owner block, value gate, neutral MLS block). The two cannot both be right, and the earlier session's exact filter state is not recoverable. **366 is treated as authoritative.** The earlier per-leg SF numbers (267 / 723 / 205 / 30) are therefore unreliable as build checks and should not be used to validate legs B, C or D.

---

## Next passes, in order

1. **Leg A county pass** with the 8-type set. Covers every city already run, adds the three new types, extends to every market inside each county. Existing records dedupe on the way in.
2. **Leg B county pass** — Multi-Family 2-4, Duplex, Triplex, Quadruplex, Mobile Home or Trailer Park. Includes the mobile-home parks Mitchell asked for.
3. **Leg C county pass** — Commercial. Check here for mobile-home parks if leg B returns near-zero.

Counties (~43):

```
CA   Los Angeles, Orange, San Diego, Santa Clara, Alameda, San Francisco,
     San Mateo, Contra Costa, Sacramento, Riverside, Ventura, Santa Barbara
NY   Kings, Queens, New York, Bronx, Richmond, Nassau, Suffolk, Westchester
NJ   Hudson, Essex, Bergen, Union, Passaic, Middlesex, Monmouth
MA   Suffolk, Middlesex, Norfolk, Essex, Worcester
CO   Denver, Boulder, Jefferson, Arapahoe, Adams
MN   Hennepin, Ramsey
WI   Milwaukee
HI   Honolulu, Maui
DC   District of Columbia
```

> The $2M floor will make WI, MN and VT come back thin or empty. That is the floor doing its job, not a broken filter. Volume comes from CA, NY, NJ, MA, CO, HI and DC.

---

## Finding — duplicate saves are free (2026-07-31)

**Re-saving a property already in the marketing list does not consume Saves quota.** Verified at leg A close: Saves used **4,330** against a list total of **4,320**, ten apart, despite the county pass re-covering every city already run in the superseded city pass. Minnesota and Wisconsin's 52 saves netted only 15 unique records and the rest were deduped on the way in.

Consequences:
- Overlapping geography is free. No need to skip a county because its cities were already run.
- The earlier warning that re-runs burn quota was wrong. Ignore it.
- Skip trace is still billed **per match** and is a separate pool. This finding does not apply there.

---

## Decision — filters frozen (2026-07-31)

Shara, 2026-07-31: **do not involve Mitchell further and do not change the agreed filter set.** The $2M-$25M band, Years of Ownership 15, Owner Type Individual and High Equity all stay exactly as they are.

**There is no fixed contact target.** The goal is as many qualified contacts as the agreed filters honestly yield. Do not loosen anything to hit a number, and do not treat a thin market as a problem to solve.

Realistic landing zone on these filters is roughly 10,000-15,000 across all three legs. That is the answer, not a shortfall.

The New Jersey diagnostic still runs, but only to document *why* the market is thin, not to justify a change.

---

## Finding — density beats tax rate (2026-07-31)

The Tier 1 thesis was "high state capital-gains tax plus NYC-adjacent." That was wrong. **The driver is density of pre-war multi-family stock, not the tax rate.**

Verified on the New York metro secondary block: 9 of 14 cities returned **zero**, and the four that produced anything gave **4 records combined**. Westchester, Rockland, Hudson Valley and Nassau are single-family towns. Great Neck and Scarsdale hold enormous wealth and almost no individually-owned 5+ unit buildings over $2M. The five boroughs and Yonkers carry the entire New York volume.

**Rule for the rest of the run:** dense pre-war urban cores produce; affluent suburbs return zero regardless of state tax.

Blocks still carrying this trap:
- **Massachusetts:** Winthrop, Saugus, Randolph, Milton will likely zero. Chelsea, Everett, Malden, Lynn, Lawrence, Brockton should produce.
- **LA basin:** Buena Park, La Habra, Tustin will likely zero. Huntington Park, Bell, Bell Gardens, Lynwood, Compton, Alhambra, Monterey Park should produce.
- **Bay Area:** the Peninsula cities already ran thin (~18 records each) for the same reason.

Cities marked `skipped` in the tracker were ruled out on this basis, not run and found empty. Do not re-run them.

---

## ⚠️ BEFORE EXPORTING OR SKIP TRACING — read this first

Shara asked to be reminded of this at the export phase (2026-07-31). Skip trace is the only real spend in this build.

1. **Dedupe by owner name before ordering, not after.** PropStream bills **per match**. One owner holding five buildings is five billable records for one human who receives one email. Largest avoidable cost by far.
2. **Dedupe on APN across legs.** Leg A's *Multi-Family Dwellings (Generic 2+)* and leg B's *Multi-Family 2-4* both contain duplexes. One shared marketing list resolves most of it, but verify.
3. **Read the Order Details panel before Place Order.** Selected Contacts, Eligible Contacts, Price Per Match ($0.10), Subtotal, Free Skip Trace Credits, Total. Free credits often bring an order to $0.00, so `count x $0.10` badly overstates cost.
4. **Re-Skip Trace OFF.** On thousands of records it re-bills for data already owned.
5. **Never click Place Order without explicit confirmation**, even at $0.00.
6. **Check the Saves quota** (gear icon, left rail). ~50,000/month, one per property added to a list. A 30k target burns most of it before any skip trace, and running out is silent.
7. **Verify emails before uploading to Instantly.** PropStream contact data is estimated and multi-match; bounce rate is the launch risk.

---

## Open items
- **Dedupe required before skip trace.** Leg A's *Multi-Family Dwellings (Generic 2+)* and Leg B's *Multi-Family 2-4* both contain duplexes, so the same property can appear in both. Dedupe on APN before paying for contacts.
- **Commercial value gate.** Estimated Value is empty on commercial and office records. With the MLS block now neutral, MLS Listing Amount only covers the on-market slice, so legs C and D have no working value gate. Deal size gets qualified by hand after export. Decide before starting leg C.
- **E1-A opener** presumes the reader has not listed. Reword proposed, not yet applied, awaiting Shara's call.
- **Target list size** — working assumption 5,000-10,000 contacts.
