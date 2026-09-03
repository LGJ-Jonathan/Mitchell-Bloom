# UPDATED C2 - Concentrated-Stock Holders

> **Approved set, 2026-08-11.** Three E1 variants selected from ten. Full variant library and rationale live in `C2 - Concentrated-Stock Holders.md`.

**Campaign type:** Employees and former employees holding large low-basis positions in their employer's stock. No public selling signal exists in bulk for this ICP, so the targeting signal is long tenure at the employer.
**Client:** Mitchell Bloom / Bloom Financial · **Sequencer:** Instantly
**Cadence:** one thread throughout. E1 (day 0) → E2 (day 3, reply) → E3 (day 7, reply). All three carry the E1 subject line. **3 steps, no 4th email.**
**A/B split:** 3 E1 variants / 2 E2 / 2 E3.

**List:** `Leads/V3 Stock Holders - INSTANTLY UPLOAD.csv`, 7,499 rows.
**Merge fields:** `{{firstName}}` 100% · `{{company}}` 100%.
⚠️ **List swap required.** Two of the three E1 variants use `{{company}}`. That field exists only on the file above. The file the previous C2 doc named, `_data/Mitchell Bloom - V2 Concentrated Stock - VERIFY these emails.csv`, has only email and name, and those two emails will not render on it.

**What the company field actually contains:** 37 distinct employers. Apple 3,244 · Microsoft 1,495 · NVIDIA 759 · Airbnb 629 · Tesla 364 · Adobe 361, then a tail. `yearsAtCompany` is also 100% filled, median 13.2 years, minimum 5, which is what supports "you've been at {{company}} a while."

**No geographic personalization.** The list carries city and state, but a stock position has no location and inferring one from an employer's headquarters would be a guess.

**The document:** every E1 offers something Mitch sends. That artifact is his existing playbook PDF. No email names it, so the PDF can be exactly what it is.

**Compliance:** "defer," never "avoid." General and educational, hedged, non-promissory, the reader's own CPA stays in the decision.
**Banned (per call):** Rob Lowe · audit statistics · indemnification · pricing · "secret method" · the "70% fail" stat (unverified).

**Spam check (mailmeteor local port):** all three E1 bodies, E2-B, E3-A and all subject lines score **Great (0 hits)**. E3-B is Great (1) from the word `leave` in "I'll leave you be." E2-A is the one exception at Poor, on `sales` and `opportunity`, the literal product names. Full emails including the mandatory footer score Poor because the word "unsubscribe" alone is an automatic Poor in that tool. Verified: no compliant footer scores better. Scoring artifact, not a deliverability problem.

**Open items:**
1. **Disclaimer verbiage.** Nothing sends without it.
2. **Confirm the postal address** in the footer is current.
3. **Confirm the playbook PDF** is the right version to send cold.
4. **Swap the list** to the file named above, or E1-2 and E1-3 send with a blank merge field.
5. **Does Mitch advise on QSBS at all.** E1-3 names an exemption we have never established he works on.
6. *"Close to a third of the gain"* carries E1-1 and needs his sign-off as a number he'll put in writing.

---

> **How Email 1 works (for the client):** each contact receives just one of the three variants below, not all of them. The system rotates the versions automatically. As replies come in, we keep the ones that earn the most interested replies and drop the rest, then keep refining until we land on the strongest message based on what the audience responds to.

**Footer, every email:**
```
Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.
[Disclaimer to be added by Bloom]
```

---

## E1 — Day 0 (new thread)

### E1-1 — in case it applies
Subjects: `in case it applies` · `{{firstName}}, quick one` · `a third, in one year` · `before you sell, not after`
```
Hi {{firstName}},

Quick one, in case it applies to you. If you're sitting on stock with a large
gain in it, close to a third of that can go to taxes the year you sell.

There are several ways to defer it, but each has to be set up beforehand, not
after.

I've put together the options and the timing on each. No charge to read it,
and your own CPA goes through it with you.

Want me to send it over?

Mitchell
```
*Opens conditionally on purpose. This list is inferred from tenure, so we do not actually know anyone holds anything. The conditional is honest about that and self-qualifies: anyone who replies is confirming they hold something.*

### E1-2 — too much in one place
Subjects: `too much in one place` · `{{firstName}}, on the concentration` · `the reason people hold too long` · `worth having a way out`
```
Hi {{firstName}},

Taking into account the company you work at, wanted to run this by you.

Plenty of people at {{company}} end up with far more in one position than
they'd choose to, and the reason they hold is the tax waiting on the other
side. So the position gets bigger and it gets harder to unwind.

There are a few ways to move out of it and spread the proceeds across other
investments, with the tax spread out rather than landing at once. Each one has
to be set up before you sell.

Want me to send you how they work?

Mitchell
```
*The liquidity and diversification lever, flagged in Playbook Insights as the strongest untapped angle for this ICP: defer the gain and let the proceeds spread across other asset classes. Written in the plural throughout so nothing reads as a single-product pitch.*

### E1-3 — QSBS
Subjects: `your shares may already qualify` · `{{firstName}}, on when you got the stock` · `the exemption most holders miss` · `worth checking before you sell`
```
Hi {{firstName}},

Noticed you've been at {{company}} a while.

If any of your shares came from an earlier stage company, before this one or
alongside it, part of that gain may already qualify for an exemption. Most
holders don't hear about it, and it can sometimes be multiplied across family
members.

Worth checking before you sell, because it can't be fixed afterward.

Want me to send over how it works?

Mitchell
```
*"Multiplied across family members" carries the QSBS stacking concept without jargon Mitch would have to explain.*
*⚠️ **"Before this one or alongside it" is load-bearing.** Naming the employer and then referring to an early stage company contradicts itself when the employer is Apple or Microsoft, which together are 63% of this list. Nobody at Apple holds QSBS stock from Apple. That phrase acknowledges the current employer is not the early stage company and points at whatever the reader held before. Do not cut it.*
*⚠️ Heavily hedged on purpose. QSBS qualification is strict: C-corp original-issuance stock, five-year hold, size limits at issuance. "May already qualify" is doing deliberate work. See open item 5.*

---

## E2 — Day 3 (reply on the E1 thread, keeps the E1 subject)

> **Steps 2 and 3 are shared across C1, C2 and C3.** Identical text in all three campaigns. Written to work whether the reader is the one selling or the one representing a seller, so nothing says "you sell" or "your client."

### E2-A — the structures, each in one line
```
Hi {{firstName}}, floating this back up.

There are a few of these and they're simpler than the names sound.

A deferred sales trust pays out over time. A charitable remainder trust does
the same and sends the remainder to a chosen cause. Opportunity zones let the
gain be reinvested instead of taxed at closing.

Which one fits depends on what the proceeds are meant to do afterward.

Want me to send it over?

Mitchell
```
*Only email in the sequence that names structures. Reverses the July 14 plain-English rule and needs Mitch's knowing sign-off.*
*The Delaware Statutory Trust was dropped when this was generalised. It is real estate only, and it was the line that landed hardest on C1's "done with toilets, trash and tenants" pain. That reach is the price of one shared follow-up.*

### E2-B — legitimacy, in plain words
```
Hi {{firstName}},

None of this was invented yesterday. These have been in the tax code for
decades, and it isn't a loophole.

The point is simple. Instead of a third going to taxes in the year it
sells, the whole amount stays invested and the tax comes out as it's drawn.

Want me to send it over?

Mitchell
```

---

## E3 — Day 7 (reply on the same thread) · final email

No subject line of its own. E3 closes the loop opened by E1 and E2, and "last note from me" only means anything with those two sitting underneath it.

### E3-A — not replacing anyone
```
Hi {{firstName}},

To be clear, I'm not looking to replace anyone.

Most CPAs don't do tax mitigation. It isn't a knock on them, it just isn't
what they work on day to day, so it rarely comes up.

I work alongside whoever's already involved, and they look at everything.

Happy to send it over. Want me to?

Mitchell
```
*"Whoever's already involved" is what makes this one work for all three campaigns. It reads as the reader's own CPA in C1 and C2, and as the seller's CPA in C3, without naming either.*

### E3-B — no charge, no drag
```
Hi {{firstName}},

Last note from me, then I'll leave you be.

There's no charge to look at this, or to set it up. Most of the work happens
on my end, and it doesn't drag a timeline out.

Nothing gets decided until the attorney and CPA have both seen exactly how it
works.

Want me to send it?

Mitchell
```
*"Doesn't drag a timeline out" replaces C1's "months of meetings on your calendar" and C3's "doesn't add weeks to a timeline." Covers both fears in one clause.*

---

*Sources: Aug 5 call transcript, July 14 strategy call, intake avatar, DST Playbook and Playbook Insights. Nothing fabricated. Postal address and disclaimer pending Mitch.*
