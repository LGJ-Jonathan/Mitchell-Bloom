# Mitchell Bloom — Clay Email Enrichment Playbook (Business Brokers)

**Created 2026-08-05. Revised after the IBBA pull.**
**Use `Leads/V2+V3 Brokers - CLAY UPLOAD v2.csv`.** The v1 file is superseded.
Upstream: `Mitchell Bloom - Broker Scrape RUNBOOK.md` · Downstream: MillionVerifier → Instantly

---

## Where the list stands

Master: `Leads/V2+V3 Brokers - MASTER WITH EMAILS.csv`

| | |
|---|---:|
| Total unique people (BizBuySell + IBBA) | **3,004** |
| With email | **898 (30%)** |
| — from **IBBA** (free, 99% fill) | **724** |
| — from Blitz (paid, 26% fill) | 174 |
| Qualified | 1,771 |
| **Qualified with email → sendable now** | **772** |
| With phone | 2,743 |

## The Clay file

`V2+V3 Brokers - CLAY UPLOAD v2.csv` — **999 qualified brokers who still have no email.** Every row already has a phone.

| | Rows |
|---|---:|
| Need enrichment | **999** |
| …with a domain | 393 (39%) |
| …**no domain** (LinkedIn is the only route) | **606 (61%)** |

By state: CA 366 · NY 150 · NJ 93 · CO 91 · MA 71 · SC 53 · OR 43 · CT 30

Columns: `first_name` · `last_name` · `full_name` · `company_name` · `domain` · `city` · `state` · `country` · `linkedin_url` (empty, to fill) · `live_listings` · `sold_listings` · `phone` · `ibba_certified` · `source_directory` · `profile_url`

> The file contains **only** rows needing enrichment. No filtering step required, and no risk of re-paying for the 898 already solved.

> **What IBBA changed:** it removed **204 rows** from the Clay job (1,203 → 999, ~17% less spend) *and* added 395 brand-new brokers who already came with emails. The bigger win was the second one.

> ⚠️ **Note the mix shifted.** v1 was 43% domainless; v2 is **61% domainless**, because IBBA solved a disproportionate share of the easy domain-bearing rows. **The LinkedIn-first path now matters more, not less.**

---

## Why LinkedIn-first

Email finders (Prospeo, Findymail, Datagma) are far more accurate from a LinkedIn URL than from name + company. And **692 rows have no domain at all**, so LinkedIn is their only path to an email.

**Blitz could not do this step.** Its people-search has no person-name filter (only job title / function / level / location / education), so there is no name → LinkedIn lookup in it. Its only route was `domain → company LinkedIn → employee list → name match`, which is why it finished at **26%** and never even attempted the 692 domainless rows. Clay's Find LinkedIn is a genuinely different capability, not a pricier version of the same one.

---

## Build order

| Step | Tool | Rows in | Expected |
|---|---|---:|---:|
| 1 | Clay **Find LinkedIn Profile** (native enrichment) | 999 | ~55-65% → ~580 |
| 2 | **Claygent Prompt B**, step-1 failures only | ~420 | ~35% → ~145 |
| 3 | **Waterfall → Work Email**, LinkedIn as primary input | ~725 | ~65% → ~470 |
| 4 | Waterfall on `domain` only, the 393 with domains | 393 | ~25% → ~100 |
| 5 | **MillionVerifier** | ~530 | ~85% survive |

**Realistic outcome: ~450 new verified emails, on top of the 898 already in hand ≈ 1,350 of 3,004** (or ~1,200 of the 1,771 qualified).

> **Prompt B is now the high-value prompt.** With 61% of rows domainless, Claygent's LinkedIn recovery is doing more work than Prompt A's site-scraping.

**Run step 4 in parallel with 1-3**, not after. The 511 rows with domains can hit the domain waterfall simultaneously; take whichever returns first. Serializing wastes runtime for nothing.

**Gate step 2 so Claygent only touches empty rows:**
```
if LinkedIn URL is empty AND needs_email = "Y"  →  run Claygent
```
Without the gate Clay runs Claygent on all 1,203 and burns credits on rows the cheap native provider already solved.

Waterfall stack for step 3: `Prospeo → Findymail → Datagma → Hunter → Apollo → Dropcontact`. Clay charges only for the first hit.

---

## ⚠️ Do not use Claygent as the primary email finder

It costs multiple credits per row, runs slowly, and **it will hallucinate plausible emails** when it cannot find one. Left unconstrained it sees `jerry@hscbrokers.com` on a page and confidently invents `rick@hscbrokers.com` for a different broker at the same firm. Those bounce and burn Mitch's sending domain.

Every prompt below therefore carries an explicit **"never construct an email from a pattern"** rule and a hard `NOT_FOUND` escape. Keep them.

**Validate everything, including Claygent output.** Anything an LLM returns is a hypothesis until MillionVerifier confirms it.

---

## Claygent Prompt A — personal email from the firm's site
*Run on: rows with a domain that the waterfall missed.*

```
Visit {{domain}} and find the direct email address for {{first_name}} {{last_name}},
who works at {{company_name}} as a business broker.

Check the homepage, /contact, /about, /team, /our-team, /agents, and any staff
or agent profile page.

Return ONLY the email address that belongs to {{first_name}} {{last_name}}
personally.

Rules:
- Do NOT return generic addresses (info@, contact@, admin@, sales@, hello@,
  office@). Those are not what I want.
- Do NOT guess, infer, or construct an email from a pattern you observed.
  Only return an address you actually saw written on the page.
- If you cannot find a personal email for this specific person, return exactly:
  NOT_FOUND

Output format: the raw email address only, or NOT_FOUND. No explanation.
```

## Claygent Prompt B — recover the missing LinkedIn
*Run on: step-1 failures. These are the hard cases, so the disambiguation is strict.*

```
Find the LinkedIn profile URL for {{first_name}} {{last_name}}, a business
broker at {{company_name}} in {{city}}, {{state}}.

Their BizBuySell profile is {{bizbuysell_profile}}. Read it first to confirm
their firm and market before searching.

The match must satisfy ALL of:
- the person's name matches
- their current or recent employer matches {{company_name}}
- their location is consistent with {{city}}, {{state}}

If the name matches but the company does not, that is the WRONG person.
Return NOT_FOUND rather than a close guess.

Do not return company pages, only a personal linkedin.com/in/ URL.

Output: the URL only, or NOT_FOUND.
```

> The "read their BizBuySell profile first" line grounds Claygent in real data before it searches. It measurably cuts wrong-person matches on common names, which is exactly what failed in the Blitz run (e.g. "Tony Clark", "Amy Kinser").

## Claygent Prompt C — role-email fallback
*Run on: last resort only, after A and B.*

```
Visit {{domain}} and find the single best contact email for the business
{{company_name}}.

Prefer, in this order: an email for {{first_name}} {{last_name}}, then a
general office address (info@, contact@).

Also answer: how many brokers or agents work at this firm? Answer with a
number, or UNKNOWN.

Rules:
- Only return an email you actually saw on the site. Never construct one.
- If no email appears anywhere, return NOT_FOUND.

Output as JSON: {"email": "...", "team_size": "..."}
```

### Why `team_size` is in Prompt C

**Measured 2026-08-05:** 13 of 20 broker firm sites (65%) publish an email, but **0 of 20 were personal** — all `info@`, `admin@`, `contact@`, `nfs@`.

So role emails are only worth sending to when the firm is tiny:
- **1-2 people → `info@` IS the broker.** Send.
- **30-agent franchise office → gatekeeper.** Drop.

Route role emails into a **separate, tagged segment**. Do not blend them into the main personalized sequence, the copy assumes a named individual.

---

## Handoff

Final verified list → `propstream-export-to-instantly` shape → Instantly.
Copy: `Copy/C3 - Business Brokers (referral channel).md`.
Merge fields the copy expects: `{{firstName}}` (required), `{{liveListings}}` (optional, needs a fallback configured).
