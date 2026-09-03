# Mitchell Bloom Commercial Property Pilot Report

Date: 2026-09-03

## Decision

The approved free source route does not support production list building.

Crexi produced 100 active Los Angeles commercial sale listings at $2 million or more. The Los Angeles County Assessor portal matched 68 listings to unique parcels and showed that 19 had been held for at least 15 years. The portal did not publish a current private owner name for any matched parcel, so recorded owner entity resolution was 0% and the pipeline could not proceed to human signer or email enrichment.

No paid enrichment, skip tracing, or PropStream work was performed.

## Pilot scope

```text
market: Los Angeles, California
listing source: Crexi
listing status: active sale
minimum displayed price: $2,000,000
undisclosed price listings: excluded
raw pilot rows: 100
collection pages: first 100 unique listing IDs from three rendered result pages
county source: Los Angeles County Assessor Portal
spend: $0
```

## Source access assessment

### Crexi

Result: viable for browser-based listing discovery.

The rendered search interface exposed listing ID, source URL, status, displayed asking price, property label, and property address. One hundred unique listing IDs were collected after setting the Los Angeles market, active sale status, minimum price, and hidden undisclosed-price filter.

Direct HTTP collection returned Cloudflare responses and was not used to bypass controls. Collection stayed in the normal rendered browser interface.

### LoopNet

Result: not viable through the available free access path.

Direct HTTP returned HTTP 403. The available browser route did not provide a stable listing collection surface. No anti-bot bypass was attempted. LoopNet contributed zero pilot rows and incurred no spend.

### Los Angeles County Assessor Portal

Result: viable for parcel and ownership-duration evidence, not current owner names.

Available public endpoints provided:

```text
address search
10-digit AIN parcel identifier
property use
active parcel status
assessment base year
ownership transfer history
reappraisable transfer dates
```

The public portal did not expose the current private owner name. The county ArcGIS layer containing `OwnerFullName` was confirmed to be a public-owned-parcels layer and did not cover private commercial parcels. It cannot be used as a substitute.

## Matching method

1. Query the county address endpoint with the listing address.
2. Require the returned parcel to match the listing ZIP.
3. Require the returned situs house number to equal the listing number or fall within the displayed address range.
4. Require at least one substantive street token to match after removing direction and common street suffix tokens.
5. Reject placeholder addresses such as `Contact Broker For Actual Addresses`.
6. Fetch parcel detail and ownership history only after the strict address match.
7. Use the latest reappraisable ownership transfer or current base year to calculate the 15-year gate.

A looser first-result match initially produced false positives. Those results were discarded and the full pilot was rerun with the strict matching rules above.

## Measured funnel

```text
Crexi listings collected: 100
Unique Crexi listing IDs: 100
Listings satisfying active and $2M source filters: 100
Exact county parcel matches: 68
Parcel match rate: 68%
No exact county match: 31
No usable street address: 1
Unique matched parcel IDs: 68
Matched parcels held at least 15 years: 19
15-year pass among exact matches: 19 / 68 = 27.9%
15-year pass from raw listings: 19 / 100 = 19%
Matched parcels acquired less than 15 years ago: 49
Current private owner names supplied by county route: 0
Recorded owner entities resolved: 0
Entity resolution rate: 0 / 100 = 0%
Human check signers resolved: 0
Signer resolution rate: 0%
Rows submitted for email enrichment: 0
Email fill rate: not measurable
Rows submitted to MillionVerifier: 0
Final sendable leads: 0
```

## Why the route stopped

The listing and duration stages worked, but the free county source does not identify the current private owner. Without a recorded owner entity, searching for a person risks attaching a broker, property manager, same-named business, or unrelated owner. That fails the central ICP requirement.

Following the skill's cheapest-first rule, the pipeline stopped before contact or email enrichment.

## Sending capacity

Live mailbox data on 2026-09-03:

```text
active mailboxes: 50
mailbox daily limit: 30
email capacity per day: 1,500
planning sequence length: 3 emails
new lead capacity per day: 500
one 20-day sending month: 10,000 leads
two 20-day sending months: 20,000 leads
```

Existing draft Instantly campaigns contain 13,115 leads and have sent 0 emails. At full measured capacity, that inventory represents 26.23 sending days. A new production target should not be selected until sending capacity is allocated between the existing drafts and the commercial segment.

## Suppression status

```text
positive interested replies returned: 0
existing local campaign CSVs available on this server: 0
direct Instantly lead export result: HTTP 403
refreshed complete suppression master: blocked
```

No production record can ship until the existing 13,115 campaign leads can be exported or the source CSVs are provided from the Mac repository.

## Recommended paid test

Do not scale the listing collection yet.

Run one small owner-data test against only the 19 properties that passed the 15-year gate:

1. Retrieve the recorded owner name or entity from a licensed ownership or deed source.
2. Measure owner entity fill on the 19 known qualifying parcels.
3. Resolve each returned entity to a valid human signer using public filings and professional evidence.
4. Deduplicate owner entities and humans.
5. Only then run email enrichment and MillionVerifier.
6. Report entity fill, signer fill, email fill, verifier OK rate, and cost per sendable lead.

PropStream remains blocked without explicit approval. If it is considered for address-level ownership lookup rather than commercial searching, that is a new test and requires approval first.

## Deliverable status

```text
ICP spec: created
100-row pilot: completed
measured entity resolution rate: completed
measured email fill rate: not measurable because entity resolution yielded zero
production CSV: not created
suppression master: blocked by unavailable source files and Instantly HTTP 403
```

A zero-row file is not being labeled final or upload-ready.
