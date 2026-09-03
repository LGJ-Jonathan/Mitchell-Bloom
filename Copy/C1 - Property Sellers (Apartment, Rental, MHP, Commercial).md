# C1 - Property Sellers (Apartment / Rental / Mobile-Home Park)  *(Campaign 1, launch priority)*

> **Rewritten 2026-08-05** from the Aug 5 call. Previous version is in git history.
> Client-facing doc: *Bloom Financial - Property Sellers: Five Cold Sequences* (Drive).
> **Commercial dropped from this segment (2026-08-05):** not sourceable cold via PropStream (LLC-held, off-MLS, no value field). Built list = apartments + rentals/MHP. Commercial deferred to Phase 2 (LoopNet / Crexi). Copy is asset-agnostic and still fits any commercial owner in-list. *(Filename keeps "Commercial" to avoid breaking cross-references; scope is what changed.)*

**Campaign type:** Master bucket — individually-owned apartment buildings, rental properties, and mobile-home parks. **OFF-MARKET (outbound) primary**; the small on-market "hot list" runs on this **same** sequence.
**Client:** Mitchell Bloom / Bloom Financial · **Sequencer:** Instantly
**Merge fields:** `{{firstName}}` (all) · `{{propertyCity}}` (V1, V3 only) — **both 100% filled** across all 3,838 rows of `V1 COMBINED`
**Cadence:** E1 (day 0) → E2 (day 3, reply on same thread) → E3 (day 7, new thread) · **A/B:** 4/2/2 · **3 steps, no 4th email.**
**7 E1 variants written, 4 slots.** First-round picks: **E1-A** (what the tax takes) · **E1-F** (the ten percent question) · **E1-G** (after closing) · **E1-D** (the deadline). One mechanism explainer, one argument, one that reaches an audience nobody else reaches, one value-first. Four different bets rather than four wordings of one.

**Angle:** owners hold because of the tax waiting at closing. Mitch's Aug 5 through-line, verbatim and requested in writing: ***"Plan first, sell second."*** Also *"plan first, retire second."*

**🔄 Aug 5 changes folded in:**
- **Not just the DST.** Mitch: *"it's not just the deferred sales trust. I don't want to just pitch one thing."* Every E1 now signals plurality; E2-A names four structures.
- **Timing window** (must be set up before signing) now carries all five E1s, not just one.
- **Buyers already approaching** (E1-E) — Jonathan's line, Mitch: *"Exactly, exactly."* Generalised from "private equity" so it runs on the whole list.
- **Where sellers give up the most** (E1-D) — from *"tax planning is where most sellers leave the most money on the table."*
- **No months of attorney meetings** (E3-B) — from *"you're not even going to get your appointment with the attorney for two months out."*

**Deliberately excluded, both by Shara's call:**
- The *"you still pay the tax, it's just timing"* honesty beat. Correct message, wrong moment — it qualifies rather than intrigues. **Belongs in post-booking nurture.**
- State-vs-federal tax percentage split. Concrete figures read as promissory under RIA ad review.

**Personalization rule:** city and state only. **No street address, no property value, no gain estimate.** Skip-traced emails do not always belong to the named owner (sample row pairs `jovanna.venegas@gmail.com` with owner "Oscar Aarts"), so anything parcel-level risks landing wrong and reads as surveillance to a high-net-worth reader.

**Plain English, jargon-free** in E1 (Mitch's rule): no "1031" (→ "the property you plan to roll into"), no "depreciation recapture," no named code sections. **E2-A is the one exception** — it names four structures with a plain-English gloss each, because "several ways" is too vague to be useful by day 3. *This reverses the July 14 rule and needs Mitch's knowing sign-off.*

**Compliance:** "defer," never "avoid." General/educational, hedged, non-promissory; the reader's CPA stays in the decision. Footer carries **"This is an advertisement."** + Mitch's own disclaimer (`[Disclaimer to be added by Bloom]`).
**Banned (per call):** Rob Lowe · audit statistics · indemnification · pricing · "secret method."

**Spam check (mailmeteor local port):** all E1 bodies and all 20 subject lines score **Great (0 hits)**. E2-A scores Poor purely from `sales` and `opportunity`, which are the literal product names. Every full email is capped at Poor by the mandatory footer (`Financial`, `unsubscribe`, `off`) — a scoring artifact, not a deliverability problem.

**Open items:** disclaimer verbiage · **the summary one-pager** (offered in E1-A, E1-D, E1-F and both E2s — it must exist before launch) · confirm "several / four / six" as one number · confirm E1-G's *"a common way people end up stuck"* is his assertion to make.

---

> **How Email 1 works (for the client):** each contact receives just one of the variants below, not all of them. The system rotates the versions automatically. As replies come in, we keep the ones that earn the most interested replies and drop the rest, then keep refining until we land on the strongest message based on what the audience responds to.

**Footer, every email:**
```
Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.
[Disclaimer to be added by Bloom]
```

---

## E1 — Day 0 (new thread)

### E1-A — what the tax takes
Subjects: `what most owners find out too late` · `{{firstName}}, before you sell` · `plan first, sell second` · `why owners wait`
```
Hi {{firstName}},

When you sell, close to a third of the gain goes to taxes that year. Most
owners around {{propertyCity | your area}} don't realize there are several
ways to defer it instead.

They work about the same way. At closing, a few lines in the paperwork send
the proceeds into a structure rather than straight to you. You draw from it
over time, and the tax spreads out instead of landing in one year.

The one catch is it has to be set up before you sign.

Want me to send over the options?

Mitchell
```

### E1-B — plan first, sell second *(his own variant, evolved)*
Subjects: `planning to sell?` · `plan first, retire second` · `where sellers give up the most` · `worth knowing before you sell`
```
Hi {{firstName}},

Wanted to ask if you're thinking about selling any of the properties you've
owned for years.

Most people focus on the closing and handle the tax after. That's
backwards, and it's where sellers give up the most, because by then
there's nothing left to set up.

What I recommend is simple. Plan first, sell second. More of it stays in
your family instead of going to taxes.

Happy to walk you and your CPA through it. Interested?

Mitchell
```

### E1-C — the buyers coming to you
Subjects: `the buyers coming to you` · `{{firstName}}, on the buyers reaching out` · `before you accept` · `a question about {{propertyCity}}`
```
Hi {{firstName}},

After holding a property in {{propertyCity | your area}} for a long time,
you've probably had buyers come to you directly. Maybe more than a few.

Most owners don't find out what the tax takes until after they've accepted.
By then it's done.

A good part of it can be deferred, in more than one way, but it has to be
in place before you sign.

Want me to show you how it works?

Mitchell
```
*Assumes long tenure rather than asking. Safe: the PropStream filter is Years of Ownership 15+.*

### E1-D — the deadline nobody mentions
Subjects: `one thing worth knowing` · `{{firstName}}, the part people miss` · `what your CPA mentions a week late` · `the deadline nobody mentions`
```
Hi {{firstName}},

Wanted to run this by you. Could be useful whether or not we ever talk.

Any strategy that defers the tax when you sell has to be set up before you
sign. Not after. Once the papers go through there's nothing anyone can do,
and plenty of owners hear that from their CPA a week after closing.

I've summarized a few of the options and the deadline on each.

Want me to email it to you?

Mitchell
```
*Least sales-shaped variant in the set. "Whether or not we ever talk" removes the transaction frame, and it is the only one that works on someone not yet selling.*

### E1-E — when the timing slips
Subjects: `what if it doesn't close in time` · `{{firstName}}, a question on your timing` · `the part that goes wrong` · `worth having a backup`
```
Hi {{firstName}},

Something worth having on your radar.

When most owners sell, the plan is to roll into another property. If that
second closing slips even a little, the whole thing fails and the entire
tax bill lands that year. It's a common way people end up stuck.

You can put a backup in place beforehand, so a slipped timeline doesn't
take the gain with it. It just has to exist before you sign.

Want me to send you how that's set up?

Mitchell
```
*The Kelly & David scenario taught as a warning rather than deployed as a testimonial.*

### E1-F — the ten percent question *(added 2026-08-05)*
Subjects: `the ten percent question` · `{{firstName}}, on the charitable piece` · `would you rather hand over a third` · `the option people dismiss too quickly`
```
Hi {{firstName}},

One of the better options for a property held this long is a charitable
remainder trust. Most people hear the word charitable and tune out.

Worth hearing the rest. You're parting with around ten percent to a cause
you pick, against closer to a third going to taxes. The remainder stays
invested and pays you back over the years.

It has to be set up before you sign.

Want me to show you the comparison?

Mitchell
```
*Recovers the CRUT by name plus Mitch's own objection handler, near verbatim from the Aug 5 call: "you only have to give away 10%, would you rather lose 35%?" That line was homeless after E3-C was cut. Works as an opener because it argues rather than informs, and "most people hear the word charitable and tune out" names the reader's reaction before they have it.*

### E1-G — the one you can still do after closing *(added 2026-08-05)*
Subjects: `the one you can still do after closing` · `{{firstName}}, if you already sold` · `the exception to the deadline` · `what's left if you've closed`
```
Hi {{firstName}},

Most of these have to be set up before you sign. Opportunity zones are the
exception.

You have a window after the closing to move the gain into one, and the tax
waits while it stays invested. If you've already closed on something this
year, it's what's left.

Not right for everyone, but worth knowing it exists.

Want me to send over how it works?

Mitchell
```
*⚠️ **The only variant in any campaign that reaches a seller who has already closed.** Every other email in the sequence is built on "before you sign, or never," which makes all of them useless to that reader. On a list filtered to 15+ years of ownership, some share have recently transacted and we currently have nothing to say to them.*
*Accuracy: the post-closing window for a qualified opportunity fund is real but the rules have been amended more than once. **Mitch to confirm** before send. Deliberately does not state a day count.*

---

## E2 — Day 3 (reply on same thread, keeps E1 subject)

### E2-A — the four structures, each in one line
```
Hi {{firstName}}, floating this back up.

Four of these work for property, and they're simpler than the names sound.

A deferred sales trust pays you out over time. A Delaware Statutory Trust
swaps you into a share of a larger property, so the rent keeps coming
without you managing it. A charitable remainder trust pays you out and
sends the remainder to a cause you pick. Opportunity zones let you
reinvest the gain instead of paying at closing.

Want me to send it over?

Mitchell
```
*The DST line lands directly on the ICP's stated pain ("done with toilets, trash, tenants"). Only email in the sequence that names structures.*

### E2-B — legitimacy, in plain words
```
Hi {{firstName}},

None of this was invented yesterday. These have been in the tax code for
decades, and it isn't a loophole.

The point of it is simple. Instead of a third going to taxes the year you
sell, the whole amount stays invested and you pay as you draw from it.

Want me to send you the summary?

Mitchell
```

---

## E3 — Day 7 (new thread) · final email
Subjects: `one more thing` · `{{firstName}}, quick note` · `one last thought`

### E3-A — working alongside their CPA
```
Hi {{firstName}},

To be clear, I'm not looking to replace anyone on your team.

Most CPAs don't do tax mitigation. It isn't a knock on yours, it just isn't
what they work on day to day, so this rarely comes up.

I work with your CPA, not around them. They look at everything and they
stay in charge.

Happy to send it over so you can pass it along. Want me to?

Mitchell
```
*CTA deliberately does NOT ask to contact their CPA. That is too heavy an ask from someone who has been ignored twice; the reader stays in control.*

### E3-B — no charge, no months of meetings
```
Hi {{firstName}},

Last note from me, then I'll leave you be.

There's no charge to look at this, or to set it up. Most of the work happens
on my end. Your attorney and CPA still look at everything, it just doesn't
turn into months of meetings on your calendar.

You decide once you've both seen exactly how it works.

Want me to send it?

Mitchell
```

---

## Cut, and why

- **The WSJ / Business Insider credibility variant.** Press mention as a cold opener was the most promotional beat in the set. Removed from E1 entirely; there is now no third-party proof anywhere in this sequence. Deliberate, not an oversight.
- **The charitable-objection variant** (ten percent to a cause vs a third to taxes). Removed from E3. E2-A still mentions a charitable remainder trust, so a reader who catches it has no answer to "why would I give anything away" — **handle in the reply script.**

*Sources: Aug 5 call transcript, July 14 strategy call, intake avatar, DST Playbook + Playbook Insights. Nothing fabricated. Postal address and disclaimer pending Mitch.*
