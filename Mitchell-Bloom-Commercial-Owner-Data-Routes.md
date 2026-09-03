# Mitchell Bloom Commercial Owner Data Routes

Verified: 2026-09-03

## Recommended free route

Reverse the original pipeline:

```text
official parcel or recorder data with owner name and sale date
→ commercial property and value gates
→ 15-year ownership gate
→ match the property address to an active Crexi sale listing
→ resolve an LLC, LP, or trust to its human signer
→ enrich and verify the signer email
```

This route solves the owner-name problem before contact enrichment. The active listing remains mandatory because the Deferred Sales Trust must be established before closing.

## Route ranking

### 1. Boulder County, Colorado

Status: strongest free bulk route

Official daily refreshed files:

```text
Owner_Address.csv
Sales.csv
```

Join key:

```text
strap
```

Useful fields include owner name, property address, transfer date, deed number, deed type, and price.

Recommended use:

1. Pull commercial parcels.
2. Keep owner names that appear individual, LLC, LP, trust, or closely held.
3. Keep transfers dated 2011-09-03 or earlier.
4. Apply the $2 million property or listing-value gate.
5. Match addresses to active Crexi listings.

### 2. Denver, Colorado

Status: strong direct route

Official anonymous ArcGIS layer:

```text
ODC_PROP_PARCELS_A/FeatureServer/245
```

Useful fields:

```text
OWNER_NAME
SALE_DATE
SALE_PRICE
RECEPTION_NUM
SCHEDNUM
situs address components
```

A live query returned a real owner record without login.

Recommended use:

1. Query commercial parcels by property-use code.
2. Keep recorded sale dates from 2011-09-03 or earlier.
3. Exclude institutional and government owners.
4. Match the address to an active Crexi listing priced at least $2 million.

### 3. Boston area, Massachusetts

Status: strong assessor route

Official MassGIS statewide source:

```text
Massachusetts_Property_Tax_Parcels/FeatureServer/0
```

Useful fields:

```text
SITE_ADDR
OWNER1
LS_DATE
LS_PRICE
FY
TOWN_ID
```

The route covers Boston and nearby Suffolk County municipalities. A live query returned an FY2026 owner and sale-date record.

Caution: `LS_DATE` is an assessor-derived last-sale date and must be labeled as such.

### 4. New York City

Status: strong recorder route, more complex joins

Official ACRIS Socrata datasets:

```text
Real Property Master: bnx9-e6tj
Parties: 636b-3b5g
Legals: 8h5j-fqxa
```

Join key:

```text
document_id
```

Method:

1. Identify deeds in the Real Property Master table.
2. Join Parties to identify the grantee or buyer.
3. Join Legals to map the document to the BBL and property address.
4. Use document date or recorded date for the ownership-duration gate.
5. Match the property to an active sale listing.

Recorder-derived dates are stronger acquisition evidence than assessor last-sale fields.

### 5. Honolulu, Hawaii

Status: owner route only

Official anonymous ArcGIS table:

```text
CadastralTables/FeatureServer/6
```

The `OWNDAT` table exposes the current tax-bill owner and joins to parcel and address data on `tmk`.

Limitation: the tested official tables did not expose a verified acquisition date. Do not use Honolulu for the 15-year gate unless a second source supplies transfer history.

### 6. Hennepin County, Minnesota

Status: technically useful, operational approval needed

Official parcel service:

```text
https://gis.hennepin.us/arcgis/rest/services/HennepinData/LAND_PROPERTY/MapServer/1
```

Useful fields:

```text
OWNER_NM
SALE_DATE
SALE_PRICE
PID
situs address components
```

A live query returned a commercial LLC owner and sale record.

Caution: the site robots file says `Disallow: /`. Do not automate this route at production scale without clarification or an explicitly downloadable or licensed route.

## California result

Los Angeles, San Francisco, and Santa Clara can support parcel matching and acquisition-date research, but the tested free sources do not disclose current private owner names at scale.

California can still produce occasional owner names through:

```text
planning applications
zoning and entitlement filings
city council attachments
environmental review documents
offering memoranda
recorded-document references indexed by search engines
```

This is a manual research route with uncertain yield. It should not be the primary production source.

## Source decision

Recommended order:

```text
Boulder County
Denver
Boston area
New York City
Honolulu only with a second transfer source
Hennepin only after automation permission is clarified
```

## Required gates

Every shipped lead must still have:

```text
active sale evidence
asking or documented transaction value of at least $2 million
ownership duration of at least 15 years
current recorded owner entity
a defensible human check signer
verified work email
suppression pass
copy fit
```

No owner name should be inferred from a broker, property manager, mailing contact, or same-named company.
