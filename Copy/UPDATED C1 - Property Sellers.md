# UPDATED C1 - Property Sellers (Apartment / Rental / Mobile-Home Park)

> **Approved set, 2026-08-11.** Three E1 variants selected from ten. Full variant library and rationale live in `C1 - Property Sellers (Apartment, Rental, MHP, Commercial).md`.
> **Commercial dropped from this segment (2026-08-05):** individually-owned commercial sellers were not sourceable cold via PropStream (LLC-held, off-MLS, no value field), so the built list is apartments + rentals/MHP only. Commercial is deferred to Phase 2 (LoopNet / Crexi). The copy itself is asset-agnostic ("your property") and still works for any commercial owner who does appear.

**Campaign type:** Individually-owned apartment buildings, rental properties, and mobile-home parks. Off-market outbound primary; the small on-market hot list runs the same sequence.
**Client:** Mitchell Bloom / Bloom Financial · **Sequencer:** Instantly
**Cadence:** one thread throughout. E1 (day 0) → E2 (day 3, reply) → E3 (day 7, reply). All three carry the E1 subject line. **3 steps, no 4th email.**
**A/B split:** 3 E1 variants / 2 E2 / 2 E3.

**List:** `Leads/V1 COMBINED - INSTANTLY UPLOAD +STATENAME.csv`, 3,838 rows.
**Merge fields:** `{{firstName}}` 100% · `{{propertyStateName}}` 100% · `{{propertyCity}}` 100%.
⚠️ The `+STATENAME` file must be the one uploaded to Instantly. The original `V1 COMBINED (Leg A + Leg B) - INSTANTLY UPLOAD.csv` has only the two-letter state code and `{{propertyStateName}}` will render blank.

**Personalization rule:** city and state only. No street address, no property value, no gain estimate. Skip-traced emails do not always belong to the named owner, so anything parcel-level risks landing wrong and reads as surveillance to this reader.

**The document:** every E1 offers something Mitch sends. That artifact is his existing playbook PDF. No email names it, so the PDF can be exactly what it is.

**Compliance:** "defer," never "avoid." General and educational, hedged, non-promissory, the reader's CPA stays in the decision.
**Banned (per call):** Rob Lowe · audit statistics · indemnification · pricing · "secret method."

**Spam check (mailmeteor local port):** all three E1 bodies, E2-B, E3-A and all subject lines score **Great (0 hits)**. E3-B is Great (1) from the word `leave` in "I'll leave you be." E2-A is the one exception at Poor, on `sales` and `opportunity`, the literal product names. Full emails including the mandatory footer score Poor because the word "unsubscribe" alone is an automatic Poor in that tool. Verified: no compliant footer scores better. Scoring artifact, not a deliverability problem.

**Open items:**
1. **Disclaimer verbiage.** Nothing sends without it.
2. **Confirm the postal address** in the footer is current.
3. **Confirm the playbook PDF** is the right version to send cold. It may have been written for warm prospects.
4. **Three claims need Mitch's sign-off**, not ours to make:
   - E1-2's *"Noticed you might be interested in selling"* asserts intent. The list filter is 15+ years of ownership, not a selling signal.
   - E1-3's *"most owners I talk to in {{propertyCity}}"* implies a local client base in every city on the list.
   - *"Close to a third of the gain"* carries all three emails and swings by state, bracket and depreciation recapture.

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

### E1-1 — the qualifier
Subjects: `still own in {{propertyStateName}}?` · `before you sell in {{propertyStateName}}` · `{{firstName}}, quick question on your property`
```
Hi {{firstName}},

Quick question, do you still own property in {{propertyStateName}}?

Asking because when one of these sells, close to a third of the gain goes to
taxes that year, and most owners don't realize there are several ways to defer
it instead. Every one of them has to be set up before you sign.

I've put together the options and the timing on each. No charge to read it,
and your CPA goes through it with you.

Want me to send it over?

Mitchell
```
*Opens with a question the reader can answer in one word. A "no" is not a loss: it identifies someone who has already sold, which is the only segment the rest of this sequence cannot serve.*

### E1-2 — plan first, sell second
Subjects: `thinking about selling?` · `{{firstName}}, before you list it` · `plan first, sell second` · `worth knowing before you sign`
```
Hi {{firstName}},

Noticed you might be interested in selling your property in
{{propertyStateName}}.

Most people focus on the closing and handle the tax after. That's backwards,
and it's where sellers give up the most, because by then there's nothing left
to set up.

What I recommend is simple. Plan first, sell second. More of it stays in your
family instead of going to taxes.

Happy to walk you and your CPA through it. I've put it together. Want me to
send it over?

Mitchell
```
*Carries Mitch's Aug 5 through-line verbatim and his point that tax planning is where sellers leave the most on the table. See open item 4: the opening line asserts intent we have no data for.*

### E1-3 — the part most people handle late
Subjects: `{{firstName}}, the part most people handle late` · `where the most gets left behind` · `worth knowing before you sign`
```
Hi {{firstName}},

Reaching out because most owners I talk to in {{propertyCity | your area}}
plan the closing and handle the tax after. It's backwards, and it's usually
where the most gets left behind, because by then there's nothing anyone can
set up.

Doing it the other way round is most of what I help with.

I've put together the options and when each one has to be in place. No charge
to read it, and your CPA can go through it with you.

Want me to send it?

Mitchell
```
*The only variant where Mitch says plainly what he does. "Doing it the other way round is most of what I help with" replaced the slogan, which read as a tagline rather than a person. See open item 4 on the opening line.*

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
