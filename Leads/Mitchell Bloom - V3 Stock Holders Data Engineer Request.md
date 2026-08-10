# Mitchell Bloom — C2 List Request (Apollo)

**Campaign:** C2, concentrated-stock holders. Employees sitting on large, low-basis
positions in their employer's stock.
**Sequencer:** Instantly · **Merge field needed:** `{{firstName}}` only.

---

## ⚠️ READ THIS FIRST — do NOT filter by job title or seniority

This is the one campaign where title filtering destroys the list.

The targeting signal is **tenure, not seniority**. Equity is a tenure story. A long-tenured
rank-and-file employee who got shares at a low strike price has a far bigger capital-gains
problem than a recently-hired executive.

From the client's ICP doc:
> *"Seniority: broad — do NOT restrict to execs; rank-and-file hold the biggest surprise
> gains (equity is a tenure story, not a seniority story)."*

From the July 14 strategy call, the client describing his own best-fit prospect:
> **Mitch [25:46]:** *"The SpaceX employee who was the cafeteria lady who's now a millionaire."*
> **Jay [25:56]:** *"I feel like that person is going to be a lot more receptive to the help."*

**So: no title filter, no seniority filter, no department filter. Everyone at these companies
who meets the tenure and location criteria.**

---

## Filters

| Field | Value |
|---|---|
| **Company** | the 40 domains below |
| **Years in Current Company** | **5+** — this is the whole ICP. Split output at 10+ if possible (see tiers) |
| **Person location** | the metro list below |
| **Email status** | Verified |
| **Job title / seniority / department** | **leave completely unset** |

### Tiers, if `Years in Current Company` can be split

| Tier | Tenure | Why |
|---|---|---|
| **Tier 1 — send first** | **10+ years** | Joined before the big run-ups. Genuinely low basis, biggest embedded gain. |
| **Tier 2 — backfill** | **5–10 years** | Real but smaller gains. Use if Tier 1 runs dry. |

If the tool can't split, just send 5+ with the tenure value included as a column and we'll
split it on our end.

### Person location

```
SF Bay Area (San Francisco, Oakland, Berkeley, San Mateo, Redwood City, Palo Alto,
Mountain View, Sunnyvale, Santa Clara, San Jose, Cupertino, Menlo Park, Fremont),
Los Angeles, Santa Monica, Pasadena, Irvine, San Diego, Sacramento,
Seattle, Bellevue, Redmond, Kirkland,
New York, Brooklyn, Jersey City, Hoboken, Newark,
Boston, Cambridge, Waltham,
Denver, Boulder, Broomfield,
Minneapolis, Saint Paul,
Madison, Milwaukee, Washington DC, Honolulu
```

**Allowed states for the final file:** CA, NY, NJ, MA, MN, HI, WI, VT, DC, CO, **WA**.

> WA is included deliberately. Seattle is named in the client's reviewed ICP spec even
> though Washington has no state income tax, because employee equity concentrates in tech
> hubs. Please do not drop it.
>
> Please **post-filter on state**. Several of these city names are ambiguous in the US and
> pull the wrong state otherwise: *Washington* → WA towns instead of DC, *Bloomington* → IN,
> *Burlington* → NC/VT, *Newark* → DE, *Glendale* → AZ. We measured this leakage on our own
> pull and it is real.

---

## Companies (40 domains)

```
amazon.com, microsoft.com, apple.com, cisco.com, tesla.com, nvidia.com, ups.com,
adobe.com, uber.com, qualcomm.com, netflix.com, costco.com, doordash.com,
homedepot.com, airbnb.com, broadcom.com, spacex.com, stripe.com, amd.com,
databricks.com, snowflake.com, datadoghq.com, atlassian.com, pinterest.com,
palantir.com, anduril.com, rippling.com, zoom.us, toasttab.com, okta.com,
crowdstrike.com, mongodb.com, twilio.com, samsara.com, ramp.com, cloudflare.com,
confluent.io, discord.com, hashicorp.com, gitlab.com
```

### Why these 40, and what was deliberately excluded

Three groups, all of which put large low-basis equity in ordinary employees' hands:

- **Recent IPOs (2015–2021)** with broad employee option grants — Uber, Airbnb, DoorDash,
  Snowflake, Palantir, Datadog, CrowdStrike, Atlassian and similar.
- **Still-private companies that run employee tender offers** — SpaceX, Stripe, Databricks,
  Anduril, Rippling, Ramp, Discord. SpaceX is the client's headline example and has *not*
  IPO'd; its staff get liquidity through periodic tender offers instead.
- **Older public companies with long-tenured rank-and-file holders** — NVIDIA, UPS, Apple,
  Microsoft, Amazon, Costco, Home Depot, Broadcom, AMD, Netflix, Tesla, Adobe, Qualcomm,
  Cisco. The client's lead archetype is a **30-year UPS employee** who got stock at issuance;
  UPS IPO'd in 1999, so a "recent IPO" filter would have missed him entirely.

**Excluded on purpose — please don't add them back:** Rivian, Lyft, Roblox, Unity, Affirm,
Robinhood, Coinbase, Block. These traded well below their IPO prices for extended periods,
so many employees hold losses rather than gains. The client's offer is capital-gains
deferral. Someone underwater has no problem to solve and is not a prospect.

---

## Output format

One CSV, these columns:

```
first_name, last_name, company_name, job_title, years_in_current_company,
tier (10plus | 5to10), linkedin_url, email, city, state
```

`job_title` is wanted **as data for personalization**, not as a filter. Include it, don't
select on it.

## Volume expectation

We ran the same universe through Blitz for comparison. Addressable population in these
metros is roughly **386,000**, of which about **23%** clear 5 years and about **6%** clear
10 years. So expect very roughly **20,000–25,000 at 10+ years** and **~65,000 more** in the
5–10 band. If Apollo returns wildly different numbers, worth flagging before export so we
can reconcile.

## Questions to

Shara — this is for the Bloom account, Campaign 2. Copy is already written and
approved internally; the list is the only blocker.
