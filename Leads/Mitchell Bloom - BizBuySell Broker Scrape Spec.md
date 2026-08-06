# Mitchell Bloom — BizBuySell Business-Broker Scrape Spec

**Created 2026-08-05, from the Aug 5 call.** Replaces the direct business-seller marketplace play as Campaign 3.

**Why this exists.** On the Aug 5 call we told Mitch the direct business-seller play is blocked: marketplace listings are deliberately anonymized ("10-person plumbing business in Wisconsin"), no company name, no owner, usually NDA-gated. Mitch's answer, verbatim: *"You see all the brokers on the right side? Maybe we do a campaign where we reach out to the business brokers."* Jonathan: *"That is a lot more doable."* Mitch has cold-called these brokers himself and says **they all pick up the phone** — the channel is responsive, the direct-seller list is not.

**Target size:** ~8,800 business brokers nationwide is **Mitch's number, unverified**. See the verified counts below.

---

## 0. ✅ VERIFIED 2026-08-05 (real browser probe, not estimates)

Probed the live site with `browser-harness` driving real Chrome. The earlier HTTP 403 was **server-side fetch only** — a real browser loads the directory normally, no captcha, no challenge page.

### Actual broker counts, the 10 target markets

| State | Brokers | | State | Brokers |
|---|---:|---|---|---:|
| California | **926** | | Wisconsin | 79 |
| New York | **446** | | District of Columbia | 48 |
| New Jersey | **262** | | Hawaii | 28 |
| Colorado | **248** | | Vermont | 18 |
| Massachusetts | **197** | | | |
| Minnesota | 83 | | **RAW TOTAL** | **2,335** |

> ⚠️ **2,335 is raw, before dedupe.** The site's own wording is *"brokers found serving this area"* — it returns brokers who **serve** the market, not brokers headquartered in it. Confirmed: Tim Whipple of Sunbelt, **Phoenix AZ**, appears on the California page. So (a) the same broker appears under multiple states and must be deduped on `brokerId`, and (b) a share of these sit physically outside the high-tax map. DC's 48 is almost certainly mostly MD/VA firms. **Expect meaningfully fewer than 2,335 unique people.**

### Mechanics, confirmed
- **Pagination:** `/business-brokers/{state}/{page}/` — verified, page 2 of California returns *"Showing 31-60 of 926."* **30 brokers per page.** California = 31 pages; all 10 states ≈ **80 page loads**.
- **No JSON API.** The page is Angular **server-side rendered**, so the broker data ships inside the HTML. Parse the DOM; there is no cleaner endpoint to hit.
- **Broker card link:** `a[href*="/business-broker/"]`, 30 per page.
- **Profile URL confirmed:** `/business-broker/{person-slug}/{firm-slug}/{brokerId}/`

### Contact fields, confirmed on a live profile
| Field | On BizBuySell? |
|---|---|
| Phone | ✅ **Yes** — in the DOM as `tel:` even though the UI shows a "Show Phone Number" button |
| Firm website | ✅ Yes — external link (e.g. `sunbeltnetwork.com`) |
| Name, firm, city/state, bio, certifications, For Sale / Sold tabs | ✅ Yes |
| **Email** | ❌ **No.** Zero `mailto:` links, zero email strings anywhere in the page text |

**So the enrichment step is mandatory and confirmed, not assumed.** The firm website is the useful output: it gives us the domain to run Apollo/Blitz against.

---

## 1. Source

### Primary — BizBuySell broker directory

| Level | URL pattern | Use |
|---|---|---|
| Root | `bizbuysell.com/business-brokers/` | entry, state index |
| State | `bizbuysell.com/business-brokers/california/` | **main seed layer** |
| County | `bizbuysell.com/business-brokers/california/santa-clara-county/` | drill-down where a state page truncates |
| City | `bizbuysell.com/business-brokers/california/los-angeles/` | drill-down for dense metros |
| Paged index | `bizbuysell.com/business-brokers/directory/21/` | numeric pagination |
| Broker profile | `bizbuysell.com/business-broker/{firm-slug}/{firm-slug}/{brokerId}/` | the record we want |
| Contact form | `bizbuysell.com/brokerdirectory/Profile/ContactBroker.aspx?BrokerProfileID={id}` | ⚠️ see email note below |

### Secondary — IBBA member directory (cross-source, cheap)
International Business Brokers Association, ~2,800 certified brokers (CBI / M&AMI / Master CBI). Worth running as **Leg B** because it exposes a **public email field** that BizBuySell does not, and it filters by state natively. Overlaps heavily with BizBuySell — dedupe on name + firm.

---

## 2. ⚠️ The email reality (correct Mitch on this) — **verified**

Mitch said on the call: *"They all have their email address, you know, you can look them all up."* That is true of the broker's **firm website**, not of BizBuySell. Checked a live profile directly: **no `mailto:` links, no email strings in the page at all.** What BizBuySell does give us is **name, firm, phone (`tel:` in the DOM) and the firm's website** — and the website is what makes enrichment work. So the pipeline is:

**BizBuySell profile → firm domain → Apollo / Blitz person lookup (name + domain) → verified email → MillionVerifier.**

IBBA (Leg B) returns real emails directly with a `hasEmail` filter, which is why it runs alongside. Do not promise Mitch a one-step scrape-to-inbox on BizBuySell alone.

---

## 3. Tooling

**Primary: `browser-harness` in cloud mode.** A real browser loads these pages fine (verified), and the whole California directory is ~31 page loads. This does not need a paid actor.

- **Probe / structure work:** local Chrome via `browser-harness`. Cheap, immediate, a handful of page views. Already used to produce section 0.
- **The bulk run:** `browser-harness auth login` → `start_remote_daemon(name)` → Browser Use Cloud. Proxies, stealth, headless, free tier covers 3 concurrent browsers. **This is the mode that satisfies the ban-risk rule** — not Shara's browser, not her IP, never signed in. Stop the daemon when done (`stop_remote_daemon(name)`) or it bills.
- ~80 page loads total across the 10 states, plus one profile load per broker we keep. Throttle it; there is no reason to go fast.

**Fallback only (do not buy unless the above fails):**

| Actor | What it does | Cost |
|---|---|---|
| `memo23/apify-bizbuysell-cheerio` | Broker directories in `startUrls`; outputs name, phone, company, expertise, active + sold listings, licenses, socials, certifications; has an `enrichEmails` option | $26/mo rental + usage |
| `jungle_synthesizer/business-broker-directory-scraper` | **IBBA** directory (a genuinely different source, not a BizBuySell substitute), 26 fields **including email**, `state` / `certification` / `hasEmail` filters | ~$0.10/run + $0.001/record (full 2,800 ≈ $2.90) |

> The IBBA actor is still worth running as **Leg B** regardless — it is a separate directory that exposes real emails, so it both cross-checks the BizBuySell pull and reduces how much Apollo/Blitz enrichment we have to pay for. At ~$2.90 for the full pull that is not a real cost decision.

**Ban risk.** The **403 is server-side fetch only** — real Chrome loads the directory with no captcha and no challenge. That does not make bulk scraping from Shara's IP acceptable: keep volume on cloud browsers, stay signed out, throttle. Review CoStar ToS before scheduling anything recurring.

---

## 4. Fields to capture

### Per broker (the lead record)
`broker_id` · `first_name` · `last_name` · `title` · `firm_name` · `firm_website` · `profile_url` · `phone` · `email` (enriched) · `city` · `state` · `zip` · `service_areas` · `industries_served` · `certifications` (CBI / M&AMI / Master CBI) · `license_number` · `years_in_business` · `active_listing_count` · `sold_listing_count` · `bio` · `linkedin_url` · `photo_url`

### Per active listing under that broker (the personalization payload)
`listing_id` · `listing_url` · `headline` · `industry` · `city` · `state` · `asking_price` · `cash_flow` · `revenue` · `ebitda` · `status` (active / under contract / sold) · `date_listed`

> **Why the listing rows matter.** The personalization Jonathan pitched on the call is listing-level: *"Dara, I saw your listing on BizBuySell for 1.4, about the two retail locations."* Without the listing join there is no first line. Keep listings as a child table keyed to `broker_id`, then flatten the single highest-asking-price active listing onto the broker row for the Instantly upload.

---

## 5. Filters

**Geography (fixed, do not expand):** CA · NY · NJ · MA · MN · HI · WI · VT · DC, plus **CO** (Vail / Aspen / Cherry Hills, Mitch's home turf). Avoid no-income-tax states (TX / TN / WA / NV / FL) — the whole pitch leans on the state plus the IRS.

**Inclusion:**
- `active_listing_count ≥ 1` — live deal flow, and it is what makes the email personalizable
- **Tier 1:** at least one active listing with `asking_price ≥ $2M` (matches the deal-size floor and the ~$1M capital-gains exposure minimum)
- **Tier 2:** active listings but all under $2M — keep, lower priority, generic angle instead of listing-specific
- Certifications are a quality signal, not a gate — do not restrict to CBI holders on Leg A

**Exclusion:**
- **Franchise-resale-only brokers** — franchise resales rarely produce a seller capital-gains event at target size
- Brokers with zero active and zero sold listings (dead or abandoned profiles)
- Duplicate people across BizBuySell and IBBA — dedupe on `last_name` + `firm_name`, then on phone

**Firm cap:** max **3 brokers per firm**. Large brokerages list a dozen agents at one office; blasting all of them from one domain reads as spam and burns the firm.

**Industry lean (soft sort, not a filter):** the fast-selling verticals already agreed — healthcare practices, medical clinics and aesthetics, veterinary, construction, laboratories, manufacturing, logistics, aerospace/defense, HVAC/plumbing/electrical, industrial waste.

---

## 6. Run order

1. Seed Leg A with the 10 state URLs, paging `/business-brokers/{state}/{page}/` to exhaustion (~80 pages, 30 brokers each)
2. **Dedupe on `brokerId` immediately** — the directory is serving-area based, so brokers repeat across states
3. Drop brokers whose profile city/state falls outside the 10-market map (the Phoenix-on-the-California-page case)
4. Scrape the surviving profiles + their For Sale / Sold tabs for listings
5. Run Leg B (IBBA) filtered to the same 10 states, `hasEmail = true`
6. Merge Leg A + Leg B, dedupe on name + firm, then on phone
7. Enrich missing emails: firm domain (captured from the profile) → Apollo / Blitz by name + domain
8. MillionVerifier, keep valid only
9. Apply the 3-per-firm cap **after** verification (so a dropped email does not waste a slot)
10. Flatten the top active listing onto each broker row, split Tier 1 / Tier 2, export for Instantly

---

## 7. Copy direction (sequence not yet written)

This is a **channel/referral** message, not a seller message. Do not reuse the business-seller sequence.

**Mitch's requested angle, verbatim on the call:** *"Plan first, sell second."* He asked us to note it. Also: *"Plan first, retire second."*

**What we offer the broker:**
1. Their client keeps more, so the deal is likelier to actually close instead of stalling on the tax bill
2. **Value Builder** — Mitch's program to build business value *before* the sale
3. The broker's **own** tax problem: top producers have real income-tax exposure
4. Positioning Mitch as an outside partner in their network, so the broker can say they handle capital-gains deferral

**Objections to pre-empt (Mitch named both):**
- *"That's up to the tax person / we don't even talk about taxes."*
- *"I don't want to kill my deal."* → frame as deal-saver, not deal-killer. Sellers who get blindsided by a 30-45% hit walk away from closings.

**Personalization line:** their specific active BizBuySell listing (price + what it is), from the child table above.

**Compliance unchanged:** disclaimer on every email, **"defer" never "avoid,"** no promissory claims, no audit references, no pricing. Sequence stops at E3.

---

## 8. Open items

1. **Copy not written.** This campaign has a list path and no sequence yet. That is the build blocker.
2. **CoStar ToS** on recurring broker-directory pulls — review before scheduling.
3. **CPAs as a second channel.** Mitch raised it on the same call (*"maybe we approach CPAs at some point"*) for the same reason: they avoid tax-mitigation strategies. Not committed, not scoped.
4. Whether the parked direct business-seller marketplace play ever comes back, or whether brokers permanently own this slot.
