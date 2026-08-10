# Mitchell Bloom V3, Concentrated-Stock Holders: List and Method

The single reference for this vertical. Where the contacts came from, why they qualify, how
the list was built, and what it does not establish. Written so someone who was not in the
build can read it end to end.

Build date: 2026-08-05. Executive review 2026-08-10. Document date: 2026-08-10.

> **Renumbering note.** This vertical was `V2` until 2026-08-10 and is now **V3**. `V2` now
> refers to the business-broker list. This document replaces
> `Mitchell Bloom - V2 List Provenance.md` and `Mitchell Bloom - V2 Scoring & Run Log.md`,
> which both carried the same counts and had to be edited in lockstep. They are deleted.
>
> Copy documents use a separate `C` scale and are unaffected. Concentrated-stock copy stays at
> `Copy/C2 - Concentrated-Stock Holders.md`. **The V and C numbers are independent scales in
> this repo and are not meant to match.**

---

## 1. What this list is, and the numbers

Long-tenured employees at 40 companies that put equity in ordinary employees' hands, located
in high state income tax markets plus Seattle. The offer is capital-gains deferral on a
concentrated, low-basis position.

**The one file to load: `Leads/V3 Stock Holders - INSTANTLY UPLOAD.csv`.**

The sequence uses `{{firstName}}` and nothing else, so two separate campaigns with identical
copy would only buy reporting. The `cohort` column gives that inside a single campaign.

### Every count in this build, stated once

| | |
|---|---|
| **Sendable, delivered** | **10,352** |
| Cohort A, long tenure at older public companies | 7,522 |
| Cohort B, pre-IPO and still-private | 2,830 |
| Companies with sendable rows | 38 of 40 |
| Distinct sending domains | 177 |
| Batch 2, catch-all and unknown, separate inboxes | 4,570 |
| Executive rows still held | 23 |
| Executive rows restored on review | 24 of 47 |

**Geography.** CA 7,852 · WA 1,520 · NY 523 · MA 201 · DC 109 · MN 49 · CO 49 · WI 25 ·
NJ 13 · HI 10 · VT 1.

**Tenure.** Median 12.3 years overall. Cohort A runs 10.2 to 45.0, median 14.3. Cohort B runs
5.0 to 18.8, median 6.6.

**Per company.** Cohort A: Apple 3,247 · Microsoft 1,498 · Broadcom 939 · NVIDIA 763 ·
Tesla 365 · Adobe 362 · AMD · Amazon · Netflix · UPS · Costco · Home Depot · Qualcomm · Cisco.
Cohort B: Uber 989 · Airbnb 629 · Pinterest 382 · Snowflake 232 · Databricks 189 ·
MongoDB 109 · Toast · Anduril · Datadog · Rippling · Twilio · DoorDash · Atlassian · Palantir ·
CrowdStrike · Confluent · Cloudflare · SpaceX · Stripe · Samsara · HashiCorp · Ramp · Okta ·
Zoom.

**Integrity, verified on the delivered file.** Merged equals A plus B. Zero duplicate emails.
Zero overlap between cohorts. No held row present. Every row has a first name, one
well-formed email and a valid cohort. Both cohort blocks sorted descending by score.

Every other section refers back to these numbers rather than restating them.

---

## 2. Where the contacts came from

### One source

**Blitz (`api.blitz-api.ai`), a licensed LinkedIn-derived B2B contact database.** Every row
came from it. There is no second source blended in.

- Nothing was scraped. No website was crawled for this list.
- No one signed into any target site to obtain these records.
- Access is a paid Agency-Enterprise seat with `/search/people` and `/enrichment/email`
  enabled.

Blitz was used instead of Apollo for a practical reason: the in-house Apollo seat carried 100
monthly credits expiring in seven days, with the Revenue, Funding and Lookalike filters
locked. That is a demo seat, not a sourcing tool.

Two downstream services touched the data after Blitz:

| Step | Service | What it did |
|---|---|---|
| Email discovery | Blitz `enrich-email` | returned a work email for 16,022 of 26,000 people |
| Email verification | MillionVerifier | classified each address good, risky or bad |

Emails were **not** guessed or pattern-constructed by us. They were returned by the enrichment
endpoint and then independently verified.

**Every address is a corporate domain.** 16,022 of 16,022 found emails sit on a company
domain and zero are personal addresses. About **1.9%** of found emails (300 of 15,889) sit on
a domain that is not the stated employer's, concentrated in SpaceX (29%) and Home Depot (22%),
both small-n.

### The one thing Blitz cannot do

**Blitz has no tenure filter.** Its complete people filter set is job_title, job_function,
job_level, min_connections, location, education. Tenure is the entire targeting signal for
this ICP.

It works anyway because the data is in the response even though it cannot be filtered on. Each
person carries `experiences[]`, and the current role has `job_start_date`. The stock
`flattenPerson()` in `blitz-client.mjs` drops that field, so a custom flattener derives
`tenure_years` and assigns a tier. Cost of the workaround: pull the entire population and
discard roughly 77% locally rather than filtering server-side. Acceptable only because credits
are unlimited.

Queries used `search-people` with `company.linkedin_url[]` rather than `employee-finder`,
which caps at 10k per company against NVIDIA's roughly 41,500. Amazon, Microsoft and Apple
each exceed the 50k per-query cap and were split into five metro-group queries, which is why
the run is 52 jobs across 40 companies.

Two traps that would have corrupted the list, both handled: **Blitz has no US state filter**,
and several target city names are ambiguous (Washington pulls WA towns instead of DC,
Bloomington pulls IN and IL, Burlington pulls NC, Newark pulls DE, Glendale pulls AZ), so a
post-filter on `state_code` was mandatory and measured real leakage of KY, TX, IN and KS rows.
And the runner is resumable, so **deduplication on `linkedin_url`** was required; an early
partial run produced 160 duplicates.

Measured throughput ceiling was roughly 2,700 rows per minute, identical at concurrency 8 and
20, indicating a server-side cap near 45 rows per second. One client instance only, because
the 5 requests-per-second gate lives on the client.

### The 40 companies

**Named directly on the July 14 strategy call:** SpaceX, NVIDIA, Uber, UPS, Yahoo.

Mitch's framing at [18:50] was a person who worked at UPS "for 30 years, and they got the UPS
stock when it was issued, and they have millions of gains on their UPS stock," then "whether
it's a Yahoo or Uber or SpaceX." Jay at [21:00] added NVIDIA and the logic that these are
"companies that gave stock options to thousands of people." Jonathan at [21:21] asked whether
we could build from "companies that have recently IPO'd over the last 5, 10 years," and Jay's
answer added the qualifier that matters: "IPO'd **and** gave stock options to a large number
of employees."

**The remaining 35 are our extension of that logic, not client instructions.** The extension
is written down in `Mitchell Bloom - V3 Stock Holders Data Engineer Request.md` and was built to the rule
Jay stated: broad employee equity, not merely a large or well-known employer.

**Yahoo was named on the call and is deliberately absent.** Yahoo no longer exists as an
employer to match against: the operating business was sold to Verizon in 2017, the remainder
was renamed Altaba, and Altaba completed its dissolution in 2019. There is no current Yahoo
employer record for a tenure filter to run against. This was a decision, but it was never
written down until this document.

### The three groups

All 40 describe the same underlying situation: ordinary employees holding a large low-basis
position in their employer.

**Group 1. Recent IPOs, 2015 to 2021, with broad employee option grants.** Uber, Airbnb,
DoorDash, Snowflake, Palantir, Datadog, CrowdStrike, Atlassian, Pinterest, MongoDB, Toast,
Twilio, Okta, Zoom, Samsara, Cloudflare, Confluent, HashiCorp, GitLab. The liquidity event has
happened, and staff hired before it hold shares struck at pre-IPO prices.

**Group 2. Still-private companies that run employee tender offers.** SpaceX, Stripe,
Databricks, Anduril, Rippling, Ramp, Discord. These have not IPO'd, so an "IPO'd in the last 5
to 10 years" filter would have missed them entirely. SpaceX is the client's own headline
example and sits in this group, not the first one.

**Group 3. Older public companies with long-tenured rank-and-file holders.** Apple, Microsoft,
Amazon, NVIDIA, Broadcom, Tesla, Adobe, AMD, Netflix, Qualcomm, Cisco, UPS, Costco, Home
Depot. This group exists because of the UPS archetype. UPS went public in 1999, so any
recent-IPO filter would have deleted the exact person Mitch described.

Groups map to the `cohort` column as: **cohort A** is group 3, **cohort B** is groups 1 and 2.

**Discord and GitLab produced zero sendable rows.** Both are in the 40 and both survived
scoring, but every verified address landed in the catch-all batch 2 file (Discord 32,
GitLab 19). That is why 38 companies appear in the delivered file rather than 40.

---

## 3. Why they qualify: the three criteria

There are exactly three. Nothing else was used to qualify a person.

### Criterion 1: five or more years at the company

**Why.** Equity value is a function of when you were granted it. Someone hired five or more
years ago received grants at a materially lower strike or share price than someone hired last
year, at every one of these 40 companies. Tenure is the only field available anywhere in the
data that tracks basis.

**How.** Derived locally from `job_start_date`, then everyone under five years discarded. Of
359,169 raw rows: 25,828 at 10+ years, 64,760 at 5 to 10 years, and **82,535 with unknown
tenure, all excluded**. The 82,535 are excluded rather than assumed: measured on 18,000 live
rows, 76% of unknown-tenure records have no job title either, meaning `experiences[]` is empty
and the profile carries no employment history at all. They cannot be qualified on the one
criterion that matters, cannot have employment confirmed, and cannot be personalised. The
recoverable subset is the roughly 24% that have a title but no start date.

### Criterion 2: a high state income tax market, plus Seattle

The criterion in full, and this is the phrasing to use when describing the list to anyone:

> **High state income tax markets, plus Seattle, included deliberately despite Washington
> having no state income tax, because employee equity concentrates in tech hubs.**

**Why.** The pitch is the size of the combined tax bill on a sale. Mitch's own arithmetic on
the call was 20% federal capital gains plus 3.8% net investment income tax plus 13.3%
California, which is where "they're losing a third of their gains just to tax" comes from. The
state layer is what makes the number large enough to be worth a conversation.

**How.** Eleven jurisdictions: CA 13.3% · HI 11.0% · NY 10.9% · NJ 10.75% · DC 10.75% ·
MN 9.85% · MA 9.0% · VT 8.75% · WI 7.65% · CO 4.4% · **WA 0.0%**.

#### The Washington rows do not fit the client's own framing

**1,520 rows, 14.7% of the file, are in Washington, which has no state income tax.** Seattle
is named in the client's reviewed ICP spec, so those rows are there on purpose and the scoring
downweights WA rather than dropping it. But they qualify on equity concentration, not tax
exposure, and the consequence needs stating plainly:

**A Washington prospect faces roughly 23.8% federal on a long-term gain (20% capital gains
plus 3.8% net investment income tax) and nothing at the state layer. Mitch's "losing a third
of their gains just to tax" is a California number. It is not true of these 1,520 people.**

On the same gain a California prospect faces roughly 37.1% and a Washington prospect roughly
23.8%. That is a materially weaker version of the same pitch, and the deferral argument for a
Washington holder rests on the federal layer alone. Anyone describing this list to Mitch, or
writing copy against it, needs that distinction. Treating the whole file as a single high-tax
audience overstates the pitch for one row in seven.

### Criterion 3: no seniority filter

**Why.** Equity is a tenure story, not a seniority story, and the more senior prospect is the
less receptive one. Mitch's archetype at [25:46] is "the SpaceX employee who was the cafeteria
lady who's now a millionaire." Jay's reply at [25:56] is the operative reasoning: "that person
is going to be a lot more receptive to the help." Someone at the top of one of these companies
very likely already has a family office and this advice.

**How.** Job title was pulled as a data column for personalisation and context and was never
used as a selection filter. **VP, SVP and EVP level are kept**, 129 rows across both cohorts.
A twenty-year Apple VP holding RSUs fits the thesis exactly.

The one qualification on this criterion is the executive hold-out, in section 4.

---

## 4. What was excluded

### The eight companies excluded on purpose

**Rivian, Lyft, Roblox, Unity, Affirm, Robinhood, Coinbase, Block.**

Each traded well below its IPO price for extended periods, so employees who received equity
around or after those IPOs hold **losses, not gains**. The client's offer is capital-gains
deferral. Someone underwater has no capital-gains problem to solve and is not a prospect.
Including them would have inflated the count while lowering quality.

Applied at the job-manifest stage, before the pull, then verified after the fact: all eight
return zero rows in both the raw pull and the scored file.

Two accuracy notes:

- The original run log listed **nine**, adding **Notion**. Notion has never had an IPO, so the
  below-IPO-price rationale cannot apply to it. Notion is genuinely absent from the universe,
  but the stated reason does not fit it. The defensible count is **eight**.
- This is a judgment about a share price over a stretch of time, not a per-person test. Some
  employees at these eight certainly do hold gains, for instance anyone hired years before the
  IPO. We accepted losing them rather than mailing a gains-deferral offer to a population
  skewed toward losses.

### The 2,651 rows removed by data-quality filters

From a scored pool of 90,588.

**Impossible tenure, 92 rows.** Rows claiming longer tenure than the company has existed.
Uber 19 · Amazon 14 · DoorDash 11 · Tesla 8 · Costco 7 · Anduril 7 · Airbnb 5 · SpaceX 4 ·
NVIDIA 3, plus eleven companies at one or two each.

Dropped rather than clamped. Clamping "Uber, 45 years" down to Uber's actual age would relabel
that person a founding-year Uber employee, which is also false. The start date is garbage, so
everything derived from it is garbage. These were 0.4% of the selection but **12 of the top 12
rows** and 58 of the top 500, because the score rewards tenure. The 45-year cap catches 1901
typos; it does not catch "Uber, 45 years".

**Gig and host titles, 2,559 rows.** Applied at **Uber, DoorDash, Airbnb and Lyft only**.
These people list the platform as their employer on LinkedIn but hold no equity in it, so the
concentrated-position premise does not apply. DoorDash 1,180 of 1,738 (67.9%) · Uber 1,009 of
2,574 (39.2%) · Airbnb 370 of 1,427 (25.9%).

Patterns matched: driver, delivery, delivery partner, dasher, deliverer, doordasher, door dash
(anchored), courier, rideshare, host, independent contractor, owner operator, shopper, captain,
creator, uber partner, private contractor, vacation rental owner, property manager, business
owner, photographer, chauffeur, contractor, partner (anchored), plus non-Latin driver titles
and blank or punctuation-only titles.

Two patterns are deliberately anchored:

- **`partner`** matches only titles that are *only* the word Partner. An unanchored
  `\bpartners?\b` dropped 46 salaried staff (HR Business Partner, Compensation Partner,
  Enterprise Partner Manager), who are exactly the RSU-holding employees this list is for.
- **`door dash`** matches only titles that are *only* those two words, because it is also the
  company name and an unanchored pattern would delete "Software Engineer, DoorDash".

**UPS drivers were deliberately kept.** This filter does not touch UPS. Long-tenure UPS
employees are W-2 staff holding real UPS stock and are the closest match in the file to Mitch's
stated archetype.

### Smaller removals further down the funnel

Duplicate email 101 · unusable first name 32 (initials only, "N", "H.", "G") · hard invalid on
verification 916 · true role inbox 4 (`cs@`, `ap@` twice, `it@`). Every dropped row is written
to `_data/V2_DROPPED.csv` with a per-row reason. Nothing was discarded silently.

### The executive hold-out and its two-pass review

Founder, C-suite and standalone "President" titles were pulled out rather than sent. **This is
a receptivity cut, not a qualification one.** Jay's point at [25:28] is that an ordinary
employee is far more receptive than someone at the top, and a founder with a family office
already has this advice.

Nine rows were caught by the very first pass and returned immediately, because their titles
only *reference* an executive rather than being one: "Executive Assistant to Chief Executive
Officer", "Principal Engineer, Office of the CTO", "Senior Executive Assistant to the CEO &
Co-founder". Those are ordinary employees holding RSUs. That left 47 held.

**On 2026-08-10 all 47 were reviewed individually and 24 were restored.** The original hold was
a **title pattern match**, which was always going to catch self-reported nonsense alongside
genuine principals. It was replaced with a verification test:

> Hold a row only if the person is verifiably the actual named officer or founder of that
> specific company. Everything else restores.

That inverts the default deliberately, because the errors are not symmetric. A wrong restore
costs one contact out of 10,352. A wrong hold loses a genuine long-tenured prospect, which is
the entire population this list exists to find.

**Restored, 24.** First pass, eleven: three staff the "assistant to" filter missed (Kelly Ikler
"Ea to CEO", Eugene Choi "Field CTO Office", Dj Banks "Sr Executive Business Partner"), and
eight junk titles claiming a seat held by someone else (Ron Johnson, Aja West and Annabel
Jones, all Microsoft "CEO", actual Satya Nadella · Hassan Khan, Apple "CEO", actual Tim Cook ·
Ocean Trump, Microsoft "CFO", actual Amy Hood · Adam, Adobe "CEO", actual Shantanu Narayen ·
Georgia, Microsoft "President", actual Brad Smith · Hajia Tahir, Microsoft "Vice CEO", not a
role that exists).

Second pass, thirteen more: Jason Demas (Broadcom "Board Member") · Kai Leonard (Microsoft
"CTO", actual Kevin Scott) · Friedrich Thomas (Microsoft "Founder and CEO") · Kevin Pipal
(Apple "Founder Owner") · Damion Valentine (NVIDIA "Founder") · Jacques Goupil (Microsoft
"Board Member") · Anthony Clay (Microsoft, cofounder of a different company) · Fernando Ruiz
(Microsoft, food-service certifications read as an executive title) · Evelyn Rodriguez (Uber
"CEO") · Vinay Srihari (Snowflake "Field CTO") · Meiya Chen (Airbnb "Regional CTO") · Chris
Hoofnagle (Palantir advisory panel) · Indira Henard (Uber Safety Advisory Board).

**Jason Demas is the case that justifies the rule change.** Held on a "Board Member" pattern
match, he is not a Broadcom director. He is VP, Broadband Video Group, and has been at Broadcom
since October 1996. Roughly 29 years of tenure at the company behind 939 cohort A rows, and the
original filter would have dropped him silently.

**Snowflake "Field CTO" restores as a class.** Field CTO is a real enterprise-software job, a
customer-facing senior technical role that companies staff several of. It is not the company's
CTO, and it is the same class as the "Field CTO Office" row restored in the first pass. Both
are exactly the long-tenured senior individual contributors this list exists for.

**Held, 23, each verified as the actual holder of the office named.** Founders and CEOs:
Chesky (Airbnb) · Khosrowshahi (Uber) · Yuan (Zoom) · McKinnon (Okta) · Collison (Stripe) ·
Kreps (Confluent) · Xin (Databricks) · Dageville (Snowflake) · Tan (Broadcom) · Gates
(Microsoft) · Luckey (Anduril) · Pomel (Datadog) · Lee (Ramp). Officers: Podbere (CrowdStrike
CFO since Sept 2015) · Glazer (Palantir CFO since 2020) · Conte (Databricks CFO since Oct
2019) · Gomez (Toast President and CFO) · Krishnamurthy (Uber SVP and CPO) · Ceremony (Uber VP
and CAO) · Bull (MongoDB CAO) · DiPhillips (Airbnb CIO, July 2020 to Dec 2025) · Martinet
(Adobe CCO). Director: Kimbal Musk (Tesla).

Three soft edges in the held set, flagged rather than buried:

- **Kimbal Musk is a director**, not an officer or founder, so he does not literally meet the
  stated rule. He is verifiably on Tesla's board and holding him matches the intent.
- **Stacy Martinet is the closest call in the file.** She verifiably is Adobe's Chief
  Communications Officer, so the rule holds her, but her title is also Vice President and this
  build otherwise keeps every VP. Restoring her would be defensible.
- **Lucius DiPhillips left Airbnb in December 2025** and became Adobe's CIO in January 2026, so
  his row's employer is out of date.

**Two restores are weak prospects even though the rule releases them.** Chris Hoofnagle is a
Berkeley law professor on Palantir's external privacy advisory panel and Indira Henard sits on
Uber's external Safety Advisory Board. Neither is an employee, so neither is likely to hold
employer equity. They restore because the rule is about offices held, not prospect quality, and
two contacts is not worth a special case.

The held file was deleted as superseded along with the A, B and sample files. See section 9.

---

## 5. What we did not verify, and the hard ceiling

Everything above describes what was done. This describes what was assumed.

**Broad employee equity programs were never independently confirmed.** The claim that these 40
companies put meaningful equity in ordinary employees' hands rests on general market knowledge
and on Jay's stated rule, not on any grant-level source. No cap table, S-1 equity-plan section,
Form S-8 registration or company grant policy was pulled or read for any of the 40. It is a
reasonable belief about well-known technology employers. It is not a verified fact per company,
and certainly not per person.

**Tender offers were never confirmed.** Group 2 rests entirely on the premise that SpaceX,
Stripe, Databricks, Anduril, Rippling, Ramp and Discord run periodic employee tender offers. No
tender-offer program was verified for any of them, and no dates, frequency, participation terms
or eligibility rules were checked. The whole of cohort B's private-company share rests on an
unverified premise about liquidity access.

**Stock appreciation was never measured, and no price data is in this build.** Nothing in the
scoring distinguishes a 2015 NVIDIA hire from a 2015 Cisco hire. They score identically. Their
positions are not remotely alike. Tenure and cohort are proxies for low basis, not measurements
of it. See section 7 for the gain factor that was built and deliberately not applied.

**Employment itself is as of the data snapshot.** Job titles and employers are self-reported
LinkedIn text and some are junk ("Stockholder", "Soulseeker", a "Chief Executive Officer" at
Microsoft who is not). We did not confirm any individual still works where their profile says
they work. The Lucius DiPhillips case in section 4 is a documented instance of exactly this.

**Catch-all addresses are unproven, not verified.** The catch-all rows in batch 2 sit on
domains that accept all mail at the SMTP layer, so verification cannot confirm or deny them.
Some share will bounce. That is the reason for separate inboxes.

**Deliverability into these inboxes is untested for this client.** Every delivered row is a
work address at a large enterprise with mature filtering. The V1 apartments list was
personal-domain heavy and is not a read on this. Watch the first 200 sends rather than assuming
V1's numbers transfer.

### The hard ceiling

**We cannot see any individual's stock holdings. Neither can any purchasable data source, and
this is a structural limit rather than a gap in this build.**

Individual securities holdings are private. The only people whose company-stock positions are
publicly reported are corporate officers, directors and beneficial owners above 10%, who file
Forms 3, 4 and 5 with the SEC. That is a few dozen people per company, and it is precisely the
population this campaign deliberately excludes on receptivity grounds. For every ordinary
employee on this list there is no public record of what they hold, when they were granted it,
what they paid, whether they have already sold, or whether they still work there.

The qualification chain terminates here, and it should be stated in the form it actually takes:

> This person has worked five or more years at a company that we believe grants equity broadly,
> and they live somewhere the tax on a gain would be high.

That is a proxy. It is not proof of a holding, of a gain, or of an intent to sell.

**No row in this file is confirmed to hold stock.** Some share sold years ago, never received a
meaningful grant, joined through an acquisition on different terms, or hold a position too
small to be worth a conversation. We cannot identify which ones, and no vendor can sell us that
answer.

What the list is: a defensible, well-filtered population where the base rate of the target
situation is far higher than in any general audience. What it is not: a list of people known to
have a capital-gains problem.

**No timing signal.** Cohorts A and B identify people who probably hold a gain, with no
indication of when they might sell. The M&A trigger layer, which would have supplied a dated
compulsory liquidity event, was scoped and gated but never built. It was the plan's argued
first send. Source files are `Leads/V3 Stock Holders - Merger Triggers *.csv` and `Leads/sec-triggers/`.

**Cohort B is exhausted.** All 6,713 bucket-A rows and 1,731 bucket-B rows in the clean pool
were selected. Cohort B cannot grow without expanding the company universe beyond the current
40, which the plan deferred.

---

## 6. The full funnel

| Stage | Rows | Note |
|---|---|---|
| Raw Blitz pull | 359,169 | 40 companies, LinkedIn-derived |
| Tier 1, 10+ years tenure | 25,828 | |
| Tier 2, 5 to 10 years tenure | 64,760 | |
| **Scored, 5+ years, both tiers** | **90,588** | Tier 3 (82,535 unknown tenure) excluded, not qualifiable |
| Dropped, impossible tenure | -92 | start date predates the company |
| Dropped, gig or host title | -2,559 | Uber, DoorDash, Airbnb, Lyft only |
| **Clean pool** | **87,937** | |
| Selected for enrichment | 26,000 | state-allocated, ranked within state |
| Enriched via Blitz `enrich-email` | 26,000 | |
| Emails found | 16,022 | **61.6% fill** |
| Dropped, duplicate email | -101 | |
| Dropped, unusable first name | -32 | initials only |
| **Uploaded to MillionVerifier** | **15,889** | |
| Returned good | 10,379 | **65.3% pass rate** |
| Returned risky, catch-all | 4,187 | 26.4%, batch 2 |
| Returned risky, unknown | 407 | 2.6%, batch 2 |
| Returned bad, invalid | 916 | **5.8% hard invalid** |
| Dropped, true role inbox | -4 | `cs@`, `ap@` x2, `it@` |
| Verified sendable | 10,375 | |
| Held, founder / C-suite / president | -47 | not deleted at the time |
| **Sendable, as built 2026-08-05** | **10,328** | |
| Restored from the hold-out, 2026-08-10 | +24 | 16 to cohort A, 8 to cohort B |
| **Sendable, current** | **10,352** | see section 1 |

### Enrichment and verification detail

- **Fill rate 61.6%** (16,022 of 26,000). A stratified 500-row pre-test measured 60.0%, so the
  projection held.
- **Fill varies sharply by cohort**: bucket A 68.8%, bucket C 60.7%, bucket B 43.7%.
- **Verification pass rate 65.3%** (10,379 good of 15,889 uploaded).
- Throughput roughly 200 rows per minute against a 5 requests-per-second ceiling.

**Only 5.8% were hard invalid.** The large middle band is catch-all: domains that accept all
mail at the SMTP layer, so the address is unproven rather than known-dead. Corporate domains at
this scale are frequently configured that way, which is why the band is much larger here than
V1's 596 catch-alls on a personal-domain list.

Batch 2 holds 4,163 catch-all and 407 unknown after the role and executive cuts, splits cohort
A 2,123 and cohort B 2,447, and carries a `campaign` column so it can be routed straight into
the matching sequence. **Send it on separate inboxes** so a higher bounce rate cannot damage
the domains carrying the primary send.

**There is exactly one email per person, so there is no second slot.** The PropStream flow
verifies up to three addresses each, which is why roughly 50% of addresses verify but about 75%
of owners end up with a good one. Here the per-address pass rate **is** the per-person pass
rate.

**The fill-rate test sample was every 44th row of the selection**, not the top 500. Profile
completeness correlates with tenure, so testing the top of a tenure-ranked list would have
biased the estimate high, and that estimate is what the selection size rested on.

**The selection was raised from 22,000 to 26,000** after the fill test came in. At 60% fill,
22,000 yields 13,200 emails, which clears 10,000 only if verification lands at 76% or better.
It landed at 65.3%. The increase is the reason this build hit its target.

---

## 7. Scoring method

Three factors, all present in the pull. Every row scores 0 to 100, total weight 1.0.

| Factor | Weight | Definition |
|---|---|---|
| State tax | 0.40 | `rate / 13.3`. CA 13.3 · HI 11.0 · NY 10.9 · NJ 10.75 · DC 10.75 · MN 9.85 · MA 9.0 · VT 8.75 · WI 7.65 · CO 4.4 · **WA 0.0** |
| Tenure | 0.40 | `(min(years, 45) - 5) / 40`. Rescaled to the live range: the file starts at 5 years, so 5y maps to 0.0 |
| Cohort | 0.20 | bucket A (IPO 2015-2021) 1.0 · bucket B (still private, tender offers) 1.0 · bucket C (older public) 0.0 |

**The 45-year cap fired on 100 rows.** It exists to neutralise start dates typed as 1901. Max
tenure before the cap was 124.70 years, after it 45.00.

**Tenure was rescaled during the build.** Dividing by 45 on a file whose median tenure is 7.6
years compressed 95% of rows into a 0.11 to 0.44 band, giving tenure roughly 13 points of range
against state's 40 and making the ICP's core signal nearly inert.

### Selection: allocated across states, not a flat top-N

A flat top-26,000 by score would have selected **100% California**, because CA scores a perfect
1.0 on state tax and holds 46,216 clean rows against the cutoff. That would have silently
converted the approved "downweight WA, do not drop it" decision into a drop, and zeroed out New
York, Minnesota, Wisconsin and Hawaii, which Mitch named on the call.

Instead each state receives an allocation weighted by volume and tax rate, then rows are ranked
**within** each state:

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

### The missing fourth factor

The approved plan specified a gain-multiple factor built from daily closes. **It is not in this
batch.** Stooq sits behind a JavaScript proof-of-work challenge and its robots.txt is
`User-agent: * / Disallow: /`. Yahoo's chart endpoint returns 429 and also disallows all
agents. Neither was worked around.

A Tiingo-based replacement was built and validated afterwards: `_data/prices.mjs`, 33 tickers
cached, **33 of 50 free-tier symbols used this month, so the cache is precious**. The gate
passed decisively: NVDA from 2015-01-01 returns 439.2x against Cisco's 6.2x, and the NVDA 2015
adjusted close of $0.4825 confirms the 4:1 and 10:1 splits are applied.

**It is not applied to this batch and did not influence a single contact in these files.** The
agreed design scores it on **bucket C only**, in the 0.20 weight slot the cohort bump occupies
for buckets A and B, so total weight stays 1.0. It is deliberately not applied to A and B
because for pre-IPO hires the multiple is not merely incomplete, it is inverted: a 2016 Airbnb
hire measured from the 2020 IPO close computes to roughly flat while their real gain is
enormous.

**One unresolved bug.** The floor rule for rows predating a price series gives each row its
company's best-ever multiple, which saturates the 100x cap. Result: all of the top 50 are
`floored` rows, and the best genuinely measured row sits at rank 135. Suggested fix, not applied
or approved: use the company's **median** computed multiple instead of the max.

**Confluent's price series ends 2026-03-17 and HashiCorp's ends 2025-02-27** because both were
acquired. Those are deal prices, not stale data. This affects only the gain file.

---

## 8. Judgment calls

Every item is a decision made during the build rather than a fact established by it.

1. **35 of the 40 companies** are our extension of the call's logic, not client instructions.
2. **Yahoo was dropped** on the reasoning that Altaba dissolved in 2019 and leaves no current
   employer to match against. Sound, but reconstructed for this document rather than recorded
   at the time.
3. **The eight exclusions** rest on share-price history over a period, not on per-person basis.
   Some employees at those eight do hold gains.
4. **The five-year tenure cutoff** is a round number chosen as a proxy. Nothing measured
   establishes that five years is where a position becomes worth deferring.
5. **82,535 unknown-tenure rows were excluded rather than sampled.** A recoverable subset,
   roughly 24%, has a title but no start date.
6. **Washington is in a high-tax-state list at 0%.** Kept on equity concentration. Those 1,520
   rows face 23.8% federal only, so the client's "losing a third to tax" framing does not
   describe them.
7. **The executive hold is a receptivity judgment, and it was half reversed.** 47 held on a
   title pattern match, 24 restored once every row was checked against the actual holder of the
   office it claimed, 23 still held and all verified. The two soft edges are Kimbal Musk, a
   director rather than an officer or founder, and Stacy Martinet, who holds a real Adobe office
   but is also VP-level, which this build otherwise keeps. Holding anyone at all remains a
   receptivity bet, not a qualification judgment.
8. **Gig-title filtering was applied at four companies only.** Comparable noise at the other 36
   was not searched for.
9. **The selection was raised from 22,000 to 26,000** mid-build after the fill-rate test came in
   below what the target required. That is the reason this build hit 10,000.
10. **The gain-multiple factor was built, validated, and deliberately not applied.** For pre-IPO
    hires the multiple is not merely incomplete but inverted.
11. **Two restored rows are not employees at all.** Hoofnagle and Henard sit on external
    advisory bodies. The rule released them and we accepted that rather than writing a special
    case.

---

## 9. Files, credentials, and what is blocked

### Deliverables

| File | Rows | Where |
|---|---|---|
| `V3 Stock Holders - INSTANTLY UPLOAD.csv` | 10,352 | `Leads/` |
| `V3 Stock Holders - BATCH 2 (risky, hold).csv` | 4,570 | `_data/` |

**`Leads/` holds only `V3 Stock Holders - INSTANTLY UPLOAD.csv` for this vertical.** Batch 2 has
moved to `_data/`. The split cohort files (`(A) long-tenure`, `(B) pre-IPO`), the executive
`HELD` file and the earlier sample file **were deleted as superseded**. The merged file carries
the `cohort` column, so the splits added nothing but a chance to diverge, which is the same
reason this document exists.

Merger-trigger source files, for the layer that was never built:
`Leads/V3 Stock Holders - Merger Triggers DEFM14A.csv`, `Leads/V3 Stock Holders - Merger Triggers LIVE.csv`, and `Leads/sec-triggers/`.

### Working files, `_data/`, gitignored and local only

| Script | Does |
|---|---|
| `run_jobs2.mjs` | concurrent, streaming, resumable puller with tenure derivation |
| `build_tiers.mjs` | dedupe, state enforcement, tier split, drop reporting |
| `score_icp.mjs` | three-factor score, filters, state-allocated selection |
| `blitz_to_verify.py` | Blitz output to MillionVerifier upload format |
| `build_campaigns.py` | verified report to campaign files, merged file, batch 2, held file |
| `prices.mjs` | Tiingo daily closes, 33 tickers cached |
| `score_icp_gain.mjs` | four-factor proposal, bucket C only, NOT used in this batch |
| `company_founded.json` | founding years for the impossible-tenure filter |

Data: `V2_SCORED_all.csv`, `V2_DROPPED.csv` (per-row drop reasons), `V2_SELECTED_26000.csv`,
`V2_ENRICHED_26000.csv`, the VERIFY and MAP pair, `V2_SCORED_all_GAIN.csv`, `prices/`.

> **These `_data/` working files still carry the `V2_` prefix.** They were not renamed because
> the build scripts reference them by name. The prefix is historical and means concentrated
> stock, not brokers.

Credentials live in `_data/.tiingo.env` (mode 600) and the blitz-api skill's own `.env`.
Neither is committed.

### Repo hygiene

Public remote, `https://github.com/LGJ-Jonathan/Mitchell-Bloom.git`. Visibility is decided and
staying public. **Verified: no contact data has ever been committed on any ref.** History is
markdown only. `.gitignore` covers `_data/`, `*.csv`, `*.xlsx`, `*.xls`, `*.json`, `*.tsv`,
`*.parquet`, so lead files cannot be committed regardless of export format.

### Blocked on Mitch, blocks the send and not the list

- Disclaimer verbiage for the `[DISCLAIMER PLACEHOLDER]` in every email
- Ad-review sign-off on the WSJ / Business Insider line in E1-C
- Confirm the CAN-SPAM footer postal address
