# Mitchell Bloom — PropStream Filters Launch

> **THIS IS THE DOC TO RUN.** Paste-ready PropStream filter configs for Campaign 1, the launch campaign. If you are building a PropStream list for Bloom, use this file.
> Not to be confused with `Mitchell Bloom - PropStream Filter Spec.md`, which is the **trophy / luxury HOMES (Campaign 4, Phase 2)** spec and is rationale-only.
>
> **Plain-English scope:** income-producing property. Somebody's **investment**, not somebody's **home**. Apartment buildings, duplexes/triplexes/quads, mobile-home parks, small retail/office/mixed-use.
>
> **⚠️ "Residential" means two different things — do not filter on the word:**
> Searches 1 and 2 below sit under PropStream's **`Residential` tab**, because that is where PropStream files **Multi-Family**. That does **not** make this the trophy/residential-homes campaign. Single Family, Condo, and Seasonal/Vacation are **never** selected here — those belong to Campaign 4. Go by property type, not by tab name.

**Campaign 1:** Apartment / rental / mobile-home-park sellers — **individually owned, ON-MARKET first (just listed / under contract / pending).**
> **🔻 Commercial (Search 3) is DEFERRED as of 2026-08-05** — it is not sourceable cold via PropStream (no Estimated Value field on commercial records, most is LLC-held, most trades off-MLS). Search 3 is kept below for its diagnostics, but **do not run it as part of the current Campaign 1 list.** Commercial moves to Phase 2, sourced from LoopNet / Crexi.

> **⭐ TIMING: ON-MARKET IS THE PRIMARY LIST (decision, 2026-07-29). Supersedes the July 24 off-market-only decision.**
> Mitchell, comment on the copy doc (July 29): *"Very good. Would be optimal to find properties just listed and/or pending."*
> - **Pass 1, primary: ON MARKET** — just listed, under contract, pending. Highest intent, and what the client asked us to lead with.
> - **Pass 2, secondary volume backfill: OFF MARKET** — owners who fit but have not listed. Run only where Pass 1 comes back thin.
>
> *(This doc says "Pass 1 / Pass 2," not "List A / List B." The trophy Filter Spec uses List A = off market and List B = on market, which is the reverse ordering. Different docs, different labels, on purpose — do not carry the letters across.)*
>
> **Known tradeoff, do not treat it as a broken filter:** on-market counts are small. SF apartments = 509 qualified owners off-market vs **6** actively listed. Expect Pass 1 to be 1-5% the size of Pass 2. Run Pass 1 across **every** city before backfilling, since the volume has to come from market count, not from loosening filters.
>
> **Pending is included on purpose.** Mitchell named it explicitly. Note the tension: residential/commercial pending typically closes in ~30 days and the structure must be in place **before** close, so some pending records will already be too late. It is kept as its **own separate saved search** so the count is visible and can be dropped on evidence rather than assumption.

**Use:** paste-ready filter configs + full city list for an automated PropStream scrape.
**Grounded in:** the July 14 strategy call, intake, Mitch's July 15 email (see `Leads/Mitchell Bloom - ICP List-Building Spec.md`), and Mitch's July 29 comments on the copy doc. Full recipe rationale in `Leads/Mitchell Bloom - PropStream Filter Spec.md` (that doc is the **trophy / C4** spec — use it for method and rationale only, not for this campaign's property types).

**Billing warning:** PropStream charges **per contact at export**. Confirm counts before exporting. Keep the 3 property-type searches separate so the same property is never paid for twice.

---

## Run matrix

**Pass 1 (do this first):** all 3 searches × every city, **On Market** → 3 × ~215 = **~645 saved searches.**
**Pass 2 (backfill only):** same 3 searches, **Off Market**, run only in cities where Pass 1 returned under ~15 records.

Naming: `Bloom — C1 — {City} — {Apartments | Rentals+MHP | Commercial} — {OnMkt | OffMkt}`

> This is not a single-session run. Work priority cities first (below), report counts per search, and stop at **saved search**. Do not add to a marketing list, skip trace, or export without a count review first — PropStream bills per contact at export.

### ⚠️ The two UI traps that zero out these searches
- **Off Market + any MLS Status selected = 0 records, every city.** A property cannot be off market and actively listed. On the Pass 2 off-market runs, MLS Status must be fully cleared.
- **Listing Type silently resets to "Any" or "For Rent" whenever you flip the On/Off Market toggle.** On every Pass 1 search, re-check that Listing Type = **For Sale** after setting On Market, or you will pull rental listings where the "list price" is monthly rent, not a sale price.

---

## SEARCH 1 — APARTMENTS

```
Save as: Bloom — C1 — {City} — Apartments — OnMkt
Property tab: Residential > Multi-Family
Property types: Multi-Family 5+, Apartment house (5+ units), Garden/Court Apt (5+ units), Multi-Family Dwellings (Generic 2+), Residential Income (General)
Owner Type: Individual
Estimated Value: Min 2000000, Max 25000000
Years of Ownership: Min 15
Lead List: High Equity
Pre-Probate: Exclude
Vacant: No
Intra-Family Transfer: Exclude
MLS On/Off Market: On Market
MLS Listing Type: For Sale          <- re-check after flipping the toggle, it resets
MLS Status: Active, Active Under Contract, Coming Soon, Contingent
Leave blank: Last Sale Price, Year Built, Estimated Equity %, Owner Occupied, Include Unknown Sales Dates, MLS Status Date, Days on Market, MLS Listing Amount, MLS Keywords, PropStream Intelligence, Pre-Foreclosure, Lien/Bankruptcy/Divorce
```

**Pending (separate search, per Mitch):** identical, but `MLS Status: Pending` only. Save as `Bloom — C1 — {City} — Apartments — Pending`.
**Pass 2 backfill:** identical, but `MLS On/Off Market: Off Market`, and **clear MLS Listing Type + MLS Status**. Save as `... — Apartments — OffMkt`.

## SEARCH 2 — RENTALS + MOBILE-HOME PARKS

```
Save as: Bloom — C1 — {City} — Rentals+MHP — OnMkt
Property tab: Residential > Multi-Family
Property types: Multi-Family 2-4, Duplex, Triplex, Quadruplex, Mobile Home or Trailer Park
Owner Type: Individual
Estimated Value: Min 2000000, Max 25000000
Years of Ownership: Min 15
Lead List: High Equity
Pre-Probate: Exclude
Vacant: No
Intra-Family Transfer: Exclude
MLS On/Off Market: On Market
MLS Listing Type: For Sale          <- re-check after flipping the toggle, it resets
MLS Status: Active, Active Under Contract, Coming Soon, Contingent
Leave blank: Last Sale Price, Year Built, Estimated Equity %, Owner Occupied, Include Unknown Sales Dates, MLS Status Date, Days on Market, MLS Listing Amount, MLS Keywords, PropStream Intelligence, Pre-Foreclosure, Lien/Bankruptcy/Divorce
```

**Pending (separate search, per Mitch):** identical, but `MLS Status: Pending` only. Save as `Bloom — C1 — {City} — Rentals+MHP — Pending`.
**Pass 2 backfill:** identical, but `MLS On/Off Market: Off Market`, and **clear MLS Listing Type + MLS Status**. Save as `... — Rentals+MHP — OffMkt`.

## SEARCH 3 — COMMERCIAL  🔻 DEFERRED (2026-08-05, not part of the current run — see note at top; kept for diagnostics)

> **⚠️ Property Classification is SINGLE-SELECT (confirmed in the UI, 2026-07-29).** Picking `Commercial` *replaces* `Residential`; it does not add to it. That is why the property types are split across separate searches rather than combined into one.
>
> **⚠️ Office is NOT under the Commercial classification.** PropStream files Office under **`Other`**, in a section titled *Office Property Types*. Because classification is single-select, retail and office **cannot** be captured in the same search. Search 3 is therefore two searches, **summed** into the `Comm` column of the run log:
> - **3a — Commercial classification:** retail + mixed-use. Config below.
> - **3b — Other classification:** office types. Config below.
>
> **⚠️ There is no `(small)` qualifier on any mixed-use type.** An earlier version of this doc said "Mixed-use (small)," which is not buildable. **Do not** add Building Size or Number of Units to compensate — the **$25M Estimated Value ceiling is the size control**, and size fields silently drop records where the data is missing. Corrected 2026-07-29.
>
> *(An earlier version also listed Office among the Commercial types. Also not buildable. Corrected 2026-07-29.)*

### 3a — Commercial

```
Save as: Bloom — C1 — {City} — Commercial — OnMkt
Property tab: Commercial
Property types — exact UI chip names, verified 2026-07-29:
  Neighborhood Shopping Center
  Strip Center/Mall
  Enterprise Zone
  Store/Office (mixed use)
  Commercial/Office/Residential Mixed Use
  Stores & Apartments
  (Office is NOT in this classification — see 3b)
Owner Type: Individual
Estimated Value: LEAVE BLANK      <- see the data-coverage note below. Do NOT set this.
MLS Listing Amount: Min 2000000, Max 25000000     <- the value gate for commercial/office
Years of Ownership: Min 15   (drop to 10 if a city returns near-zero — commercial is thinnest)
Lead List: High Equity
Pre-Probate: Exclude
Vacant: No
Intra-Family Transfer: Exclude
MLS On/Off Market: On Market
MLS Listing Type: For Sale          <- re-check after flipping the toggle, it resets
MLS Status: Active, Active Under Contract, Coming Soon, Contingent
Leave blank: Last Sale Price, Year Built, Estimated Value, Estimated Equity %, Owner Occupied, Include Unknown Sales Dates, MLS Status Date, Days on Market, MLS Keywords, PropStream Intelligence, Pre-Foreclosure, Lien/Bankruptcy/Divorce
```

> **⚠️ Estimated Value does not exist on commercial records (verified 2026-07-29).** PropStream's commercial and office result cards carry no EST. VALUE and no EST. EQUITY row, and map pins read N/A. Applying an Estimated Value floor returns **0 across the board** — not because no properties qualify, but because the field is empty. San Francisco has **205** individually-owned, 15-year-held, high-equity commercial properties that the value filter cannot see. Isolation: removing the ceiling left 0; removing the floor restored the full 205.
>
> **The substitute is `MLS Listing Amount`, and it is better data.** These searches are on-market only, so every record has an asking price. A listing amount is what the seller is actually asking; Estimated Value is a model output. For a campaign premised on an imminent transaction, the asking price is the right gate.
>
> **⚠️ Do NOT substitute Assessed Total Value or Assessed Land Value.** Under California's Prop 13, assessed value tracks purchase price plus ~2%/yr, so a property held 15+ years — the entire ICP — assesses near its 1990s price. A $2M assessed floor would exclude exactly the highest-embedded-gain targets, and CA is 59 of the 228 cities. The low assessed figure is a **basis** proxy, not a value floor. Useful signal, wrong filter.
>
> **Pass 2 (off-market) has no listing amount.** If the off-market backfill ever runs on commercial, there is no working value gate at all — Owner Type, Years Owned and High Equity carry it, and deal size gets qualified by hand after export.

**Pending (separate search, per Mitch):** identical, but `MLS Status: Pending` only. Save as `Bloom — C1 — {City} — Commercial — Pending`.
**Pass 2 backfill:** identical, but `MLS On/Off Market: Off Market`, and **clear MLS Listing Type + MLS Status**. Save as `... — Commercial — OffMkt`.

### 3b — Office (the `Other` classification)

```
Save as: Bloom — C1 — {City} — Office — OnMkt
Property tab: Other  →  section "Office Property Types"
Property types — exact UI chip names, verified 2026-07-29:
  Commercial Office (General)
  Office Bldg (General)
  Office Bldg (multi-story)
  Condominium Offices
  Professional Bldg
  Medical Bldg
  Dental Bldg
  Financial Bldg
  Mixed Use (Commercial/Industrial)
  (plus any remaining types in that section — select the whole Office
   Property Types group; do NOT select other groups under "Other")
```
**Every other filter is identical to 3a.** Same Owner Type, value range, years owned, lead list, exclusions, MLS block, and blanks.

**Pending:** identical, `MLS Status: Pending` only. Save as `... — Office — Pending`.
**Pass 2 backfill:** identical, `Off Market`, clear MLS Listing Type + MLS Status. Save as `... — Office — OffMkt`.

**Reporting:** 3a + 3b are **summed** into the single `Comm` column in the run log. Note the split in that row's Notes so the two are recoverable.

> **Commercial on-market caveat:** commercial listings are thinly covered in MLS feeds (most trade off-MLS through brokers). Expect both 3a and 3b On Market to return near-zero in most cities. That is a data-coverage limit, not a filter error. Commercial is the one segment where the Off Market backfill is likely to be the real list — and the one where LoopNet / Crexi may simply be a better source than PropStream.

> **Parked observation (2026-07-29):** the Office group contains **Medical Bldg** and **Dental Bldg**. Campaign 3 targets dental and medical practice owners who are selling. An owner who holds both the practice and the building is a double-gain prospect and an unusually strong fit. Not in scope for this run — noted so it isn't lost.

> **MHP note:** mobile-home parks sometimes classify under Commercial, not Residential. If Search 2 shows no parks in a city, check Search 3's Commercial tab.

---

## PRIORITY CITIES — client-named, C1-relevant (run first)

```
San Francisco CA, San Jose CA, Denver CO, Boulder CO, Honolulu HI, Manhattan NY, Santa Barbara CA, Newport Beach CA
```

> The luxury enclaves Mitch named (Aspen, Vail, Sagaponack, Atherton, Bel Air, Montecito, Rancho Santa Fe) are **trophy-home markets** → near-zero individually-owned apartment/commercial. They belong to Campaign 4 (trophy), not here. Excluded from this sheet on purpose.

---

## FULL CITY LIST — ~215 cities, all 10 target states (high-tax, ICP-aligned)

### Comma-separated

```
San Francisco CA, San Jose CA, Los Angeles CA, San Diego CA, Oakland CA, Sacramento CA, Long Beach CA, Fresno CA, Anaheim CA, Santa Ana CA, Riverside CA, Bakersfield CA, Stockton CA, Irvine CA, Fremont CA, San Bernardino CA, Modesto CA, Oxnard CA, Huntington Beach CA, Glendale CA, Santa Clarita CA, Garden Grove CA, Oceanside CA, Rancho Cucamonga CA, Ontario CA, Santa Rosa CA, Elk Grove CA, Corona CA, Hayward CA, Sunnyvale CA, Pomona CA, Escondido CA, Torrance CA, Pasadena CA, Orange CA, Fullerton CA, Roseville CA, Concord CA, Thousand Oaks CA, Simi Valley CA, Santa Monica CA, Berkeley CA, Vallejo CA, Costa Mesa CA, Carlsbad CA, Temecula CA, Ventura CA, Richmond CA, Burbank CA, Daly City CA, San Mateo CA, Redwood City CA, Mountain View CA, Palo Alto CA, Walnut Creek CA, Santa Barbara CA, Newport Beach CA, Palm Springs CA, Palm Desert CA, Manhattan NY, Brooklyn NY, Queens NY, Bronx NY, Staten Island NY, Buffalo NY, Rochester NY, Yonkers NY, Syracuse NY, Albany NY, New Rochelle NY, Mount Vernon NY, White Plains NY, Schenectady NY, Utica NY, Troy NY, Niagara Falls NY, Binghamton NY, Hempstead NY, Freeport NY, Long Beach NY, Nassau County NY, Suffolk County NY, Poughkeepsie NY, Great Neck NY, Newark NJ, Jersey City NJ, Paterson NJ, Elizabeth NJ, Edison NJ, Trenton NJ, Camden NJ, Hoboken NJ, Clifton NJ, Passaic NJ, Union City NJ, Bayonne NJ, Atlantic City NJ, East Orange NJ, Woodbridge NJ, Lakewood NJ, Toms River NJ, Cherry Hill NJ, Bloomfield NJ, Vineland NJ, New Brunswick NJ, Perth Amboy NJ, Plainfield NJ, Hackensack NJ, Fort Lee NJ, Kearny NJ, Boston MA, Worcester MA, Springfield MA, Cambridge MA, Lowell MA, Brockton MA, Quincy MA, Lynn MA, New Bedford MA, Fall River MA, Somerville MA, Framingham MA, Newton MA, Lawrence MA, Waltham MA, Haverhill MA, Malden MA, Medford MA, Taunton MA, Chicopee MA, Weymouth MA, Revere MA, Peabody MA, Methuen MA, Barnstable MA, Pittsfield MA, Everett MA, Salem MA, Minneapolis MN, St. Paul MN, Rochester MN, Duluth MN, Bloomington MN, Brooklyn Park MN, Plymouth MN, St. Cloud MN, Woodbury MN, Maple Grove MN, Eagan MN, Eden Prairie MN, Coon Rapids MN, Burnsville MN, Blaine MN, Lakeville MN, Minnetonka MN, Apple Valley MN, Edina MN, St. Louis Park MN, Mankato MN, Moorhead MN, Richfield MN, Roseville MN, Denver CO, Boulder CO, Aurora CO, Colorado Springs CO, Fort Collins CO, Lakewood CO, Thornton CO, Arvada CO, Westminster CO, Pueblo CO, Centennial CO, Greeley CO, Longmont CO, Loveland CO, Broomfield CO, Grand Junction CO, Castle Rock CO, Commerce City CO, Parker CO, Littleton CO, Englewood CO, Wheat Ridge CO, Honolulu HI, Pearl City HI, Hilo HI, Kailua HI, Waipahu HI, Kaneohe HI, Kahului HI, Kihei HI, Mililani HI, Ewa Beach HI, Kapolei HI, Wailuku HI, Lahaina HI, Kailua-Kona HI, Milwaukee WI, Madison WI, Green Bay WI, Kenosha WI, Racine WI, Appleton WI, Waukesha WI, Oshkosh WI, Eau Claire WI, Janesville WI, West Allis WI, La Crosse WI, Sheboygan WI, Wauwatosa WI, Fond du Lac WI, Brookfield WI, New Berlin WI, Wausau WI, Beloit WI, Lake Geneva WI, Washington DC, Burlington VT, South Burlington VT, Rutland VT, Essex VT, Colchester VT, Bennington VT, Brattleboro VT, Montpelier VT, Stowe VT
```

### JSON array

```json
["San Francisco CA","San Jose CA","Los Angeles CA","San Diego CA","Oakland CA","Sacramento CA","Long Beach CA","Fresno CA","Anaheim CA","Santa Ana CA","Riverside CA","Bakersfield CA","Stockton CA","Irvine CA","Fremont CA","San Bernardino CA","Modesto CA","Oxnard CA","Huntington Beach CA","Glendale CA","Santa Clarita CA","Garden Grove CA","Oceanside CA","Rancho Cucamonga CA","Ontario CA","Santa Rosa CA","Elk Grove CA","Corona CA","Hayward CA","Sunnyvale CA","Pomona CA","Escondido CA","Torrance CA","Pasadena CA","Orange CA","Fullerton CA","Roseville CA","Concord CA","Thousand Oaks CA","Simi Valley CA","Santa Monica CA","Berkeley CA","Vallejo CA","Costa Mesa CA","Carlsbad CA","Temecula CA","Ventura CA","Richmond CA","Burbank CA","Daly City CA","San Mateo CA","Redwood City CA","Mountain View CA","Palo Alto CA","Walnut Creek CA","Santa Barbara CA","Newport Beach CA","Palm Springs CA","Palm Desert CA","Manhattan NY","Brooklyn NY","Queens NY","Bronx NY","Staten Island NY","Buffalo NY","Rochester NY","Yonkers NY","Syracuse NY","Albany NY","New Rochelle NY","Mount Vernon NY","White Plains NY","Schenectady NY","Utica NY","Troy NY","Niagara Falls NY","Binghamton NY","Hempstead NY","Freeport NY","Long Beach NY","Nassau County NY","Suffolk County NY","Poughkeepsie NY","Great Neck NY","Newark NJ","Jersey City NJ","Paterson NJ","Elizabeth NJ","Edison NJ","Trenton NJ","Camden NJ","Hoboken NJ","Clifton NJ","Passaic NJ","Union City NJ","Bayonne NJ","Atlantic City NJ","East Orange NJ","Woodbridge NJ","Lakewood NJ","Toms River NJ","Cherry Hill NJ","Bloomfield NJ","Vineland NJ","New Brunswick NJ","Perth Amboy NJ","Plainfield NJ","Hackensack NJ","Fort Lee NJ","Kearny NJ","Boston MA","Worcester MA","Springfield MA","Cambridge MA","Lowell MA","Brockton MA","Quincy MA","Lynn MA","New Bedford MA","Fall River MA","Somerville MA","Framingham MA","Newton MA","Lawrence MA","Waltham MA","Haverhill MA","Malden MA","Medford MA","Taunton MA","Chicopee MA","Weymouth MA","Revere MA","Peabody MA","Methuen MA","Barnstable MA","Pittsfield MA","Everett MA","Salem MA","Minneapolis MN","St. Paul MN","Rochester MN","Duluth MN","Bloomington MN","Brooklyn Park MN","Plymouth MN","St. Cloud MN","Woodbury MN","Maple Grove MN","Eagan MN","Eden Prairie MN","Coon Rapids MN","Burnsville MN","Blaine MN","Lakeville MN","Minnetonka MN","Apple Valley MN","Edina MN","St. Louis Park MN","Mankato MN","Moorhead MN","Richfield MN","Roseville MN","Denver CO","Boulder CO","Aurora CO","Colorado Springs CO","Fort Collins CO","Lakewood CO","Thornton CO","Arvada CO","Westminster CO","Pueblo CO","Centennial CO","Greeley CO","Longmont CO","Loveland CO","Broomfield CO","Grand Junction CO","Castle Rock CO","Commerce City CO","Parker CO","Littleton CO","Englewood CO","Wheat Ridge CO","Honolulu HI","Pearl City HI","Hilo HI","Kailua HI","Waipahu HI","Kaneohe HI","Kahului HI","Kihei HI","Mililani HI","Ewa Beach HI","Kapolei HI","Wailuku HI","Lahaina HI","Kailua-Kona HI","Milwaukee WI","Madison WI","Green Bay WI","Kenosha WI","Racine WI","Appleton WI","Waukesha WI","Oshkosh WI","Eau Claire WI","Janesville WI","West Allis WI","La Crosse WI","Sheboygan WI","Wauwatosa WI","Fond du Lac WI","Brookfield WI","New Berlin WI","Wausau WI","Beloit WI","Lake Geneva WI","Washington DC","Burlington VT","South Burlington VT","Rutland VT","Essex VT","Colchester VT","Bennington VT","Brattleboro VT","Montpelier VT","Stowe VT"]
```

---

## Run notes
- **Priority cities first**, then work down the full list.
- **Stop at saved search.** Report counts per city per search before any export. Billing is per contact.
- **Commercial (Search 3) returns the least** everywhere — more of it is LLC-held (stripped by Owner Type = Individual) and most commercial trades off-MLS. Near-zero in a city is expected, not a broken filter.
- **VT + small metros are thin** on Apartments/Commercial but still add Rentals+MHP contacts.
- **On-market volume is genuinely small.** SF apartments: 509 qualified owners, 6 actively listed. Do not fix this by loosening Owner Type, Pre-Probate, or the value floor. Fix it by running more cities, then by adding the Off Market backfill (Pass 2).
- **Do not loosen to hit a number:** Owner Type = Individual, Pre-Probate = Exclude, and the $2M value floor all protect list quality and stay put.
- **Copy status:** the Campaign 1 sequence is **written** — `Copy/C1 - Property Sellers (Apartment, Rental, MHP, Commercial).md`, client-facing Google Doc *"Bloom Financial Email Sequence - Apartment, Rental, Commercial (final)"*. It presumes an active or contemplated sale, which now matches the on-market list. Revised per Mitch's July 29 notes (1031 distinction added to E1-A).
  - ⚠️ **One mismatch to watch:** E1 **Variant A** opens *"Are you holding off on selling your properties…"* — that reads wrong to someone who just listed. Variants B, C and D are fine on an on-market list. Either hold Variant A for the Pass 2 off-market backfill, or reword its opener.
- **Verify emails** before upload — PropStream contact data is estimated/multi-match; bounce rate is the launch risk.

---

*Campaign 1 build sheet. Last updated 2026-07-29 for Mitch's on-market / pending timing instruction. States = Mitch's high-tax targets (CA, NY, NJ, MA, MN, CO, HI, WI, VT, DC). Trophy enclaves excluded (Campaign 4). Method + rationale per the PropStream Filter Spec (trophy/C4 doc); scope per the ICP List-Building Spec.*
