# ICP: Mitchell Bloom Commercial Property Sellers

Build target: Pilot first. Do not set a production target until sender capacity is allocated to this campaign and the paid owner resolution step is measured.

## WHO

A reachable individual commercial real estate owner, or the human with legal signing authority behind an LLC, LP, partnership, or trust, who is selling a highly appreciated property and can establish a Deferred Sales Trust before closing.

## TITLES: INCLUDE

Tier 1:

```text
owner
managing member
trustee
general partner
managing partner
principal
```

Tier 2:

```text
founder
co-founder
president
chief executive officer
sole proprietor
```

A title alone is insufficient. The person must be tied to the recorded owner entity and have signing authority.

## TITLES: EXCLUDE

```text
property manager
asset manager without ownership authority
leasing agent
leasing manager
listing broker
realtor
registered agent without a management role
sales representative
marketing role
finance role
human resources role
legal role without ownership authority
```

## FIRMOGRAPHICS

```text
ownership: individual, family, closely held LLC, LP, partnership, or trust
asset: commercial real estate
asking price or documented transaction value: at least $2,000,000
ownership duration: at least 15 years
sale status: actively listed, under contract, contingent, pending, or another documented approaching sale
```

Corporate, institutional, and private equity owners are excluded.

## GEO: TIER 1

```text
San Francisco, CA
San Jose, CA
Los Angeles, CA
Denver, CO
Boulder, CO
Honolulu, HI
Manhattan, NY
Boston, MA
Minneapolis, MN
```

## GEO: TIER 2

No widening is approved for the pilot. Other properties may qualify only when their actual property address is in:

```text
California
New York
New Jersey
Massachusetts
Minnesota
Hawaii
Wisconsin
Vermont
District of Columbia
Colorado
```

## GEO TRAPS

1. Filter on the actual property address and ZIP, not the search market label.
2. A Los Angeles search can contain nearby municipalities such as Culver City, Beverly Hills, Tarzana, and Woodland Hills. These remain in California but may use a different municipal name.
3. Crexi can briefly render global recommendation cards while a location route is loading. A row must be checked against the card address before collection.
4. Placeholder listings such as `Contact Broker For Actual Addresses` do not support a county parcel match and must be removed.
5. Fuzzy county searches can return a same-number property on the wrong street. The parcel match requires house number or range, ZIP, and at least one substantive street token to agree.

## INDUSTRIES

Database industry values are secondary because this campaign is anchored on ownership and a live property sale, not an employer industry.

Applicable property classes include:

```text
multifamily
mobile home park
retail
office
mixed use
medical
industrial
hospitality
self storage
income-producing land
special purpose commercial property
```

## INDUSTRIES: EXCLUDE

```text
new construction without meaningful appreciation
institutional portfolios
private equity portfolios
corporate-owned real estate
residential owner-occupied homes
brokerages when the broker is the proposed recipient
```

The reason is lack of individual seller fit, insufficient appreciation, or lack of signing authority.

## INCLUDE KEYWORDS

```text
for sale
under contract
pending
contingent
closing
commercial property
multifamily
mobile home park
retail
office
mixed use
medical building
industrial
self storage
hospitality
owner user
investment property
```

## EXCLUDE KEYWORDS

No usable sale trigger:

```text
for lease only
lease available
wanted
buyer requirement
off market with no sale evidence
```

Wrong owner profile:

```text
institutional
private equity
REIT
public company
government owned
municipal owned
```

Insufficient tax fit:

```text
new construction
recently acquired
probate
pre-probate
inherited
```

## HARD EXCLUSIONS

1. No active or approaching sale evidence. The trust must exist before final papers are signed.
2. Asking price or documented transaction value below $2 million.
3. Ownership duration below 15 years.
4. Property in TX, TN, WA, NV, or FL.
5. Pre-probate or inherited property because stepped-up basis can remove the gain.
6. New construction or recently acquired property.
7. Corporate, institutional, and private equity ownership.
8. No reachable human with signing authority behind the recorded owner.
9. Listing brokers and realtors as campaign recipients.
10. Any record already present in refreshed email or domain suppression.

Client evidence:

* July 14, 03:10: `The best targets are, for example, people who are selling a apartment complex, commercial property, or a highly appreciated lot.`
* July 14, 03:10: `Preferably, having their asset in contract pending is good.`
* July 14, 03:10: `The deal really shouldn't be less than $2 million.`
* July 14, 11:53: `The best person would be someone who is in contract, you know, they've got a 60 day close.`
* July 14, 13:27: `We're looking for that ma pa.`
* July 14, 17:00: a new build `hasn't had time`, while the fit is `somebody who's owned a property for a long time.`
* Intake USP: `The strategy must be in place before you sign the final papers. Once you close, the window is gone forever.`

## CARVE-OUTS

1. Do not exclude an LLC merely because it is an entity. Closely held LLCs are common and may resolve to a qualified individual signer.
2. Do not exclude nearby municipalities inside an approved state merely because the search market is Los Angeles. Verify the actual address and tax jurisdiction.
3. Do not exclude a property because the listing broker appears prominently. The broker is a join aid, not the recipient.
4. Do not treat every old building as long held. Building age and ownership duration are separate facts.
5. Do not treat every recent filing as a sale. Use the latest reappraisable ownership transfer or base year, not a file correction.

## PRIORITY SIGNAL

Ranked strongest to weakest:

1. Pending or under contract with an identifiable closing window.
2. Active sale listing with an asking price of at least $2 million.
3. At least 15 years since the latest reappraisable ownership transfer.
4. Closely held entity or individual ownership.
5. Publicly verifiable human signer tied to that entity.
6. Verified work email for the signer.

Drop any record without signals 1 or 2, 3, 5, and 6.

## REQUIRED FIELDS

```text
source
source_url
listing_id
listing_status
asking_price
property_name
property_address
property_city
property_state
property_zip
property_type
sale_evidence
sale_evidence_date
county
parcel_id
latest_reappraisable_transfer_date
ownership_years
recorded_owner_entity
owner_entity_source_url
signer_first_name
signer_last_name
signer_title
signer_evidence_url
company_domain
work_email
email_verification_status
email_verification_date
suppression_status
copy_segment
qa_status
```

A row without every applicable field does not ship.

## QUALIFICATION PROMPT

```text
# CONTEXT
You are qualifying a commercial property seller for Bloom Tax & Estate Group's Deferred Sales Trust campaign. The structure must be established before closing.

# OBJECTIVE
Confirm that this is an active, high-value sale of a long-held commercial property in an approved state and identify the human with signing authority behind the recorded owner.

# INSTRUCTIONS
1. Verify the property address and ZIP from the listing.
2. Verify that the listing is active, pending, contingent, or under contract.
3. Verify an asking price or documented transaction value of at least $2,000,000.
4. Verify the latest reappraisable ownership transfer. Require at least 15 years of ownership.
5. Identify the recorded owner entity from an authoritative ownership source.
6. Resolve that entity to a current owner, managing member, trustee, general partner, managing partner, principal, founder, president, or CEO.
7. Reject property managers, leasing agents, brokers, realtors, registered agents without management authority, institutions, private equity firms, and corporations.
8. If any required fact cannot be confirmed, return NOT_FOUND. Do not infer.

# OUTPUT
Return JSON with camelCase fields:
{
  "qualificationStatus": "QUALIFIED | DISQUALIFIED | NOT_FOUND",
  "propertyAddress": "",
  "saleStatus": "",
  "askingPrice": null,
  "latestTransferDate": "",
  "ownershipYears": null,
  "recordedOwnerEntity": "",
  "signerName": "",
  "signerTitle": "",
  "evidenceUrls": [],
  "reason": ""
}
```

## DEDUPE

1. Normalize and deduplicate listing URL and Crexi listing ID.
2. Deduplicate by parcel ID before owner research.
3. Deduplicate by normalized recorded owner entity before contact enrichment.
4. Deduplicate by person and work email before verification.
5. Suppress at both email and domain level against all existing Mitchell Bloom campaigns and positive replies.
6. Refresh suppression immediately before a production export.

Suppression status on 2026-09-03:

* Positive interested replies returned 0 records.
* Existing campaign lead files were not available in the server repository.
* Direct Instantly lead export returned HTTP 403 with the available workspace credential.
* Production suppression is therefore incomplete and no row may ship yet.

## MEASURED FUNNEL

Pilot date: 2026-09-03

```text
Crexi active Los Angeles listings at $2M or more collected: 100
Unique Crexi listing IDs: 100
Listings with an exact county parcel match: 68
Exact parcel match rate: 68%
Listings with no exact parcel match: 31
Listings without a usable street address: 1
Unique matched parcel IDs: 68
Matched parcels held at least 15 years: 19
15-year pass rate among exact parcel matches: 27.9%
15-year pass rate from raw listings: 19%
Matched parcels acquired less than 15 years ago: 49
Current recorded owner names available from the free county portal: 0
Recorded owner entity resolution rate from the approved free route: 0%
Human signer resolution rate: 0%
Email fill rate: not measured because no owner entity passed into enrichment
MillionVerifier OK rate: not measured
Final sendable rows: 0
Paid spend: $0
```

The free listing route works. The free Los Angeles County route supplies parcel IDs, property characteristics, assessment base year, and transfer history, but it does not publish the current private owner name. It cannot support entity-to-human resolution by itself.

## WHERE THE VOLUME IS

Ranked next options:

1. Use a licensed ownership source only on the 19 properties that passed the 15-year gate, then measure recorded owner entity fill.
2. Resolve returned entities through Secretary of State filings and public professional evidence.
3. Enrich and verify email only after a human signer is confirmed.
4. If the 19-row owner test performs adequately, repeat the listing and county-history pipeline on additional Crexi pages and approved markets.
5. Test LoopNet only through a permitted access path. Direct HTTP returned 403 and the browser route failed to provide a stable collection surface during this pilot.
6. Do not use PropStream or alter its commercial filters without explicit approval.

## CAPACITY

Measured on 2026-09-03:

```text
active Instantly mailboxes: 50
mailbox daily limit: 30
email capacity per day: 1,500
sequence length used for planning: 3 emails
new lead capacity per day: 500
one 20-day sending month: 10,000 leads
 two 20-day sending months: 20,000 leads
existing draft campaign leads: 13,115
existing draft inventory at full capacity: 26.23 sending days
```

A production list target remains pending until Jonathan allocates sending capacity between the three existing draft campaigns and this commercial seller segment.

## COPY CHECK

* C1 E1 variants B and C fit an active commercial seller better than variants A and D.
* `Are you holding off on selling your properties` conflicts with an active listing signal.
* `Thinking about selling` is weaker than the known active listing context.
* Toilets, trash, tenants, and maintenance language should be limited to property types where it is credible.
* Failed 1031 and depreciation recapture language can fit commercial sellers, subject to property type and transaction context.
* No copy may imply that an inspection occurred.
* No em dashes may appear in campaign copy.
