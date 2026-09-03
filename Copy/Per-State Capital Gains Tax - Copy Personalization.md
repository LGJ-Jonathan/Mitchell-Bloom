# Per-State Capital Gains Tax — Copy Personalization Spec

Reference for the dynamic tax-figure personalization Mitch requested (Sept 2 email): insert the actual combined capital-gains tax rate for each recipient's state, so the copy reads as researched. This doc has everything needed to build it and update the copy.

**Status:** spec / draft. Not yet applied to the live Instantly sequences. Phone number and the exact hedge wording are still pending Mitch's confirmation (see Open Decisions).

---

## 1. How it works

Each lead already carries its state in the `{{personalization}}` field (verified from the live lists). We add one custom field per lead, `{{gainsRate}}`, filled from the state → rate table below. The copy then reads:

> "at closing in {{personalization}}, you could owe as much as {{gainsRate}} in combined capital gains tax, plus depreciation recapture."

Renders as: *"at closing in California, you could owe as much as 37.1% in combined capital gains tax, plus depreciation recapture."*

---

## 2. The formula

Mitch's formula, which reproduces both of his examples exactly (CA 37.1%, CO 28.2%):

```
Combined rate = Federal LTCG (20%) + NIIT / "Medicare surtax" (3.8%) + State top rate
              = 23.8% base + state top rate
```

Depreciation recapture is handled separately as text (see Section 4) because it is not a per-state constant.

---

## 3. Per-state rate table

Base = 23.8% (federal 20% + NIIT 3.8%). "Combined" = base + state top rate.

### States in the lists

| State | In campaign | State top rate | **Combined (recommended)** | Wrinkle / precise alternative |
|---|---|---|---|---|
| CA | C1, C2 | 13.3% | **37.1%** | clean — matches Mitch |
| NY | C1, C2 | 10.9% | **34.7%** | clean |
| NJ | C1, C2 | 10.75% | **34.6%** | clean |
| DC | C1, C2 | 10.75% | **34.6%** | clean |
| MN | C1, C2 | 9.85% | **33.7%** | +1% NII surtax over $1M → ~34.7% |
| MA | C1, C2 | 5.0% (LTCG) | **28.8%** | +4% millionaire surtax over $1M very likely on these deals → **32.8%** |
| CO | C1, C2 | 4.4% | **28.2%** | clean — matches Mitch |
| HI | C1, C2 | 7.25% (LTCG cap) | **31.1%** | HI caps LTCG at 7.25% (ordinary top is 11%) |
| WI | C1, C2 | 7.65% | **31.5%** | 30% LTCG exclusion → effective ~29.2% |
| WA | C2 only | 7% (excise) | **30.8%** | excise applies only to gain over ~$270k; below that, just 23.8%. Stock only — no recapture |
| VT | C2 only | 8.75% | **32.6%** | 40% LTCG exclusion possible; only 1 lead |

**Recommendation:** use the "Combined (recommended)" column — the simple top-bracket figure. It matches the two numbers Mitch already wrote (CA, CO), keeps the whole set consistent, and every value is a defensible "as high as" ceiling. Refine the wrinkle states (MA, HI, WI, WA, VT, MN) only if Mitch wants precision over consistency.

### Machine-usable mapping

For writing `gainsRate` onto each lead (recommended values):

```json
{
  "CA": "37.1%",
  "NY": "34.7%",
  "NJ": "34.6%",
  "DC": "34.6%",
  "MN": "33.7%",
  "MA": "28.8%",
  "CO": "28.2%",
  "HI": "31.1%",
  "WI": "31.5%",
  "WA": "30.8%",
  "VT": "32.6%"
}
```

State distribution in the live lists (for volume context):
- **C1 (3,838):** CA 1,648 · NY 1,494 · MA 304 · CO 114 · DC 113 · NJ 109 · HI 31 · MN 21 · WI 4
- **C2 (7,499):** CA 5,568 · WA 1,318 · NY 291 · MA 148 · DC 79 · MN 34 · CO 24 · WI 20 · HI 10 · NJ 6 · VT 1

---

## 4. Depreciation recapture (real estate / C1 only)

Cannot be a per-state number. It is up to **25% federal** on the depreciation the owner has already claimed — a figure specific to each property that we do not have. So it stays as **text, never a percentage**:

> "…plus depreciation recapture on any depreciation you've taken over the years."

C2 (stock) has no depreciation recapture — drop that clause entirely for stock copy.

---

## 5. Compliance / hedge rules

Every number is a **top-bracket ceiling**. A seller below the top bracket owes less, and precise figures from a Registered Investment Advisor edge toward tax advice. So:

- Always hedge: **"as high as {{gainsRate}}"**, **"up to"**, or **"could owe."** Never "you will owe {{gainsRate}}."
- Keep the existing full disclaimer footer on every email (does not provide legal/tax advice, general/educational, consult your own CPA…).
- "Defer / mitigate / minimize," never "avoid" or "eliminate."

---

## 6. "Set up" word ban (Mitch, Sept 2)

Remove "set up" / "set it up" everywhere. Replacements: **create / form / build / coordinate / structure / engineer / compose / manufacture.** Recommended swaps in the current live copy:

| Where | Current | Replace with |
|---|---|---|
| C1 E1-A | "Every one of them has to be **set up** before you sign." | "…has to be **built** before you sign." |
| C1 E1-B | "there's nothing left to **set up**." | "there's nothing left to **structure**." |
| C1 E1-C | "there's nothing anyone can **set up**." | "there's nothing anyone can **build**." |
| C2 E1-A | "each has to be **set up** beforehand, not after." | "each has to be **built** beforehand, not after." |
| C2 E1-B | "Each one has to be **set up** before you sell." | "Each one has to be **structured** before you sell." |
| Shared E3-B | "or even to **set it up**" | "or even to **build it**" |

(No "set up" in the shared E2 variants or E3-A.)

---

## 7. Revised Campaign 1 — Email 1 (with variable + Mitch's rewrites)

Incorporates the `{{gainsRate}}` variable, Mitch's Version A/B/C rewrites, the "set up" ban, the hedge, and no em dashes. `[State]` = `{{personalization}}`.

### Version A
Subject: [First Name], quick question on your property  /  [First Name], a question before you sell

```
Hi [First Name],

Are you planning on selling investment property in [State]?

Asking because at closing you could owe as much as [gainsRate] in combined
capital gains tax, on top of depreciation recapture on any depreciation
you've taken over the years.

Most owners don't realize there are several ways to mitigate, minimize, and
defer what's owed, but the plan has to be built before the sale closes.

I can walk you through the options and the timing.

Open to a quick 15-minute call?
```

### Version B
Subject: [First Name], thinking about selling?  /  [First Name], worth knowing

```
Hi [First Name],

Noticed you might be interested in selling your property in [State].

Most sellers focus on the closing and plan to handle the tax after the sale,
as much as [gainsRate] plus depreciation recapture. By then it's too late,
and that's where people leave the most money on the table, because they
didn't build a strategic plan in advance.

What I recommend is simple. Plan first, sell second. That way, most of it
stays in your pocket instead of going to the government.

Happy to show you how it works, or to spend 15 minutes to see if you qualify.

Open to a quick call?
```

### Version C
Subject: still own in [State]?  /  [First Name], quick thought

```
Hi [First Name],

Most sellers come to us after they've sold, thinking we can help with the tax
consequences after the deal closes. That's backwards, and it's where sellers
leave the most money on the table.

How you structure your sale determines your after-tax proceeds by hundreds of
thousands of dollars, and can mean unnecessary losses of seven figures or more.

That's where my team comes in.

I can walk you through the options if you'd like.

Open to a quick 15-minute call?
```

Emails 2 and 3 are the shared follow-ups (apply the Section 6 "set up" swap in E3-B; otherwise unchanged).

**Campaign 2 (stock):** apply the same treatment — the `{{gainsRate}}` figure (no recapture clause), the "as high as" hedge, and the "set up" swaps. Copy blocks to follow once C1 is locked.

**Campaign 3 (brokers):** on hold per Mitch — do not revise or launch now.

---

## 8. Implementation steps

1. Add a `gainsRate` custom field to each lead in C1 (and C2 if extended), filled from the Section 3 mapping keyed off the lead's state (`personalization`).
2. Update the C1 sequence with the Section 7 copy, using the `{{gainsRate}}` variable.
3. Add a fallback so it never renders blank if a state is missing: `{{gainsRate|a significant amount}}`.
4. Preview in Instantly to confirm the figure renders per state before enabling.

---

## 9. Open decisions (need Mitch)

- **Simple vs. precise** for the wrinkle states (MA, HI, WI, WA, VT, MN). Recommended: simple (Section 3).
- **"40%+" wording.** Mitch's draft B said "40%+"; our true ceiling is ~37% (CA) before recapture. Using `{{gainsRate}}` is more accurate; confirm he's okay replacing "40%+" with the real per-state figure.
- **Phone number.** His Sept 2 note says "Phone number is 888-233-1993," but the mailbox signatures were just changed to the toll-free 800-929-5665. Confirm which number goes where before any signature change.
