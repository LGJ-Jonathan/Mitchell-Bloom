# Mitchell Bloom — V4 Stock Holder Company Evidence

**Snapshot date:** 2026-09-03  
**Purpose:** Auditable company-level universe for the V4 concentrated-stock-holder rebuild.

## Interpretation

The table qualifies companies, not individual holdings. A company appears because it is recent-public with plausible pre-IPO employee equity, still private with employee tender/secondary activity, or older-public with exceptional measured appreciation. Each person still must pass the current-employment, 5-year tenure, geography, officer, employee-level basis/multiple, modeled-$1M-gain, and verified-work-email gates.

For public names, returns are computed from split-adjusted Yahoo Finance daily closes. “Five year” means the first available close when the ticker has less than five years of public history. Current and employee-level prices were captured from:

`https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?range=max&interval=1d&events=history&includeAdjustedClose=true`

## Universe

| Company | Cohort | Ticker | 3y | 5y / since first available | Evidence rule |
|---|---|---:|---:|---:|---|
| Palantir Technologies | recent_public | PLTR | +1100.1% | +583.6% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| Robinhood | recent_public | HOOD | +1052.7% | +196.0% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| AppLovin | recent_public | APP | +637.1% | +323.5% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| Rocket Lab | recent_public | RKLB | +877.2% | +340.1% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| CrowdStrike | recent_public | CRWD | +419.8% | +218.8% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| Cloudflare | recent_public | NET | +335.6% | +116.7% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| Datadog | recent_public | DDOG | +119.1% | +56.4% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| Uber | recent_public | UBER | +63.2% | +85.5% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| Snowflake | recent_public | SNOW | +123.7% | +14.1% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| DoorDash | recent_public | DASH | +165.3% | +12.6% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| Airbnb | recent_public | ABNB | +30.2% | +12.3% | Yahoo split-adjusted daily close; employee basis uses start-date close or first-public-close floor. |
| MongoDB | recent_public | MDB | -2.5% | -21.5% | Yahoo split-adjusted daily close; only qualifying pre-IPO or 2x employee-level rows survive. |
| Coinbase | recent_public | COIN | +148.7% | -27.8% | Yahoo split-adjusted daily close; only qualifying pre-IPO or 2x employee-level rows survive. |
| Samsara | recent_public | IOT | +21.7% | +56.9% | Yahoo split-adjusted daily close; only qualifying pre-IPO or 2x employee-level rows survive. |
| Vertiv | recent_public | VRT | +589.5% | +863.3% | Yahoo split-adjusted daily close; legacy-tenure successor-company carveout. |
| Reddit | recent_public | RDDT | +209.3% | +209.3% | Yahoo split-adjusted daily close. |
| Hims & Hers | recent_public | HIMS | +303.8% | +223.5% | Yahoo split-adjusted daily close. |
| Astera Labs | recent_public | ALAB | +355.9% | +355.9% | Yahoo split-adjusted daily close. |
| Rubrik | recent_public | RBRK | +149.0% | +149.0% | Yahoo split-adjusted daily close. |
| Arm | recent_public | ARM | +281.5% | +281.5% | Yahoo split-adjusted daily close; legacy-tenure successor-company carveout. |
| CoreWeave | recent_public | CRWV | +111.4% | +111.4% | Yahoo split-adjusted daily close. |
| NVIDIA | repriced_public | NVDA | +371.5% | +911.4% | Passed measured appreciation screen. |
| Broadcom | repriced_public | AVGO | +324.6% | +690.0% | Passed measured appreciation screen. |
| AMD | repriced_public | AMD | +311.8% | +317.9% | Passed measured appreciation screen. |
| Arista Networks | repriced_public | ANET | +287.8% | +752.1% | Passed measured appreciation screen. |
| Vistra | repriced_public | VST | +357.3% | +739.8% | Passed measured appreciation screen; successor-company tenure allowed. |
| Constellation Energy | repriced_public | CEG | +174.0% | +605.0% | Passed measured appreciation screen; successor-company tenure allowed. |
| Palo Alto Networks | repriced_public | PANW | +170.9% | +330.5% | Passed measured appreciation screen. |
| Supermicro | repriced_public | SMCI | +35.1% | +931.3% | Passed five-year appreciation screen. |
| Axon | repriced_public | AXON | +153.6% | +194.6% | Passed three-year appreciation screen. |
| Cheniere Energy | repriced_public | LNG | +80.2% | +240.3% | Passed five-year appreciation screen. |
| Micron Technology | repriced_public | MU | +1278.4% | +1234.3% | Passed measured appreciation screen. |
| Marvell Technology | repriced_public | MRVL | +264.1% | +247.4% | Passed measured appreciation screen. |
| KLA | repriced_public | KLAC | +245.5% | +431.2% | Passed measured appreciation screen. |
| Lam Research | repriced_public | LRCX | +329.0% | +419.7% | Passed measured appreciation screen. |
| Applied Materials | repriced_public | AMAT | +190.5% | +232.9% | Passed measured appreciation screen. |
| GE Aerospace | repriced_public | GE | +276.3% | +430.8% | Passed measured appreciation screen; successor-company tenure allowed. |
| Dell Technologies | repriced_public | DELL | +695.6% | +1068.2% | Passed measured appreciation screen; successor-company tenure allowed. |
| Eli Lilly | repriced_public | LLY | +112.1% | +376.2% | Passed five-year appreciation screen. |
| SpaceX | private_tender | — | — | — | Client-specified employee tender cohort; recurring tender evidence: [Bloomberg syndication](https://finance.yahoo.com/news/spacex-weighs-tender-offer-roughly-233517767.html). |
| Stripe | private_tender | — | — | — | Client-specified employee secondary cohort; 2026 employee share-sale reporting: [Reuters](https://www.reuters.com/business/stripe-valuation-jumps-159-billion-latest-employee-share-sale-2026-02-24/). |
| Databricks | private_tender | — | — | — | Client-specified employee-liquidity cohort; event terms must be refreshed before trigger-specific messaging. |
| Anduril Industries | private_tender | — | — | — | Client-specified employee-liquidity cohort; event terms must be refreshed before trigger-specific messaging. |
| Rippling | private_tender | — | — | — | Client-specified employee-liquidity cohort; event terms must be refreshed before trigger-specific messaging. |
| Ramp | private_tender | — | — | — | Client-specified employee-liquidity cohort; event terms must be refreshed before trigger-specific messaging. |
| OpenAI | private_tender | — | — | — | Client-specified employee-liquidity cohort; event terms must be refreshed before trigger-specific messaging. |
| Anthropic | private_tender | — | — | — | Reported planned employee tender at a $350B valuation: [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-04/anthropic-plans-employee-tender-offer-at-350-billion-valuation). |

## Important limits

- Public returns are auditable company-level facts; the employee's personal award price and holdings are not public.
- A first-public-close floor is conservative for pre-IPO option holders but is not a 409A strike.
- Private-company valuation multiples are lower-confidence research proxies. Do not place the values or an alleged tender deadline into copy without refreshing primary or reputable reporting.
- Cohort inclusion does not guarantee a person clears the modeled $1M exposure threshold; that is applied downstream.
