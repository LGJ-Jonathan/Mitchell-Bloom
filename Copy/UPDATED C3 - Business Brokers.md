# UPDATED C3 - Business Brokers (referral channel)

> **Approved set, 2026-08-11.** Three E1 variants selected from twelve. Full variant library and rationale live in `C3 - Business Brokers (referral channel).md`.

**Campaign type:** Business brokers, M&A advisors and business intermediaries with live deal flow. Referral and channel play, not a direct-seller list. The broker brings the seller.
**Client:** Mitchell Bloom / Bloom Financial · **Sequencer:** Instantly
**Cadence:** one thread throughout. E1 (day 0) → E2 (day 3, reply) → E3 (day 7, reply). All three carry the E1 subject line. **3 steps, no 4th email.**
**A/B split:** 3 E1 variants / 2 E2 / 2 E3.

**List:** `Leads/V2 Brokers - INSTANTLY UPLOAD.csv`, 2,260 rows.
**Merge field:** `{{firstName}}` only, 100%.

**No geographic merge fields, by decision.** The list carries city at 90% and state at 99%, but a merge tag that renders blank for one broker in ten is worse than none. "Your market" and "your area" are written as plain words instead, which read identically to a reader and cannot break.

**The document:** every E1 offers something Mitch sends. That artifact is his existing playbook PDF. No email names it, so the PDF can be exactly what it is.

**Compliance:** "defer," never "avoid." No promissory claims, no guaranteed tax outcome. Every benefit is stated as something that happens to the broker's client, with a line making clear Mitch stays out of the broker's side.
**Banned (per call):** Rob Lowe · audit statistics · indemnification · pricing · "secret method" · the "70% fail" stat (unverified).

**Spam check (mailmeteor local port):** all three E1 bodies, E2-B, E3-A and all subject lines score **Great (0 hits)**. E3-B is Great (1) from the word `leave` in "I'll leave you be." E2-A is the one exception at Poor, on `sales` and `opportunity`, the literal product names. Full emails including the mandatory footer score Poor because the word "unsubscribe" alone is an automatic Poor in that tool. Verified: no compliant footer scores better. Scoring artifact, not a deliverability problem.

> ## ⚠️ BLOCKER: offer framing is still unconfirmed
> All three E1s assume **the broker refers their selling client.** Mitch raised four angles on the Aug 5 call and never picked one:
> 1. Their client keeps more, so the deal closes instead of stalling
> 2. **Value Builder**, his program to raise business value before a sale (described nowhere in the repo)
> 3. The **broker's own** income-tax exposure as a top producer, which is a different offer with a different buyer
> 4. Network positioning, Mitch as the capital-gains partner in their book
>
> Angles 1 and 4 are one offer and are what this copy is built on. Angles 2 and 3 are separate offers and are not in this sequence. **If the intent is broker-as-tax-client, all three E1s need rewriting.** Get the answer before sending this copy for review, or he may reject good copy over a question he never answered.
>
> Also unresolved: **how the broker gets paid.** Brokers are commission operators, and a channel offer with no economics asks them to work free for a stranger. If there is a referral fee, RIA solicitor rules govern how it can be described in cold email. That is a compliance question before it is a copy question.

**Other open items:**
1. **Disclaimer verbiage.** Nothing sends without it.
2. **Confirm the postal address** in the footer is current.
3. **Confirm the playbook PDF** is the right version to send cold.
4. **Proof gap.** Kelly & David is a $7.6M multifamily real estate result and does not belong in a broker email. A business-sale case study would be far stronger here. No proof is currently used in this sequence.
5. E1-3's *"most brokers I talk to in your area overlook it"* implies a local broker network. His claim to make, not ours.
6. E1-2's *"close to a third of the gain"* needs his sign-off as a number he'll put in writing.

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

### E1-1 — plan first, sell second
Subjects: `{{firstName}}, on the sellers you're working with` · `the conversation that happens too late` · `worth raising early`
```
Hi {{firstName}},

Wanted to ask how you handle the tax conversation with your sellers.

Most of them plan the exit and handle the tax after. That's backwards, and
it's where they give up the most, because by then there's nothing left to set
up.

What I recommend is simple. Plan first, sell second. I can be the one who
walks them through it, alongside their CPA.

Interested?

Mitchell
```
*Carries Mitch's Aug 5 through-line verbatim. Opens by asking about the broker's own process rather than pitching, which is what keeps it from reading as a vendor email.*

### E1-2 — what they're actually netting
Subjects: `do deals in your market stall at the end?` · `{{firstName}}, on what they're actually netting` · `what usually holds it up`
```
Hi {{firstName}},

Do deals in your market ever stall at the end over what the seller is actually
netting?

That's usually the tax. Close to a third of the gain, due the year they sell.
Handled before signing, there are several ways to defer it, and closings that
would have dragged tend to go through.

I do that part. Nothing for your seller to pay, their own CPA looks at it, and
I stay out of your side of it.

I've put it together. Want me to send it over?

Mitchell
```
*The deal-saver frame, and the direct answer to the objection Mitch named on July 14: "the broker typically will not want to engage, they don't want their deal to bust." This makes tax the thing that busts deals and Mitch the thing that prevents it.*

### E1-3 — the deadline nobody mentions
Subjects: `one thing worth knowing` · `{{firstName}}, the part sellers miss` · `what their CPA mentions a week late` · `the deadline nobody mentions`
```
Hi {{firstName}},

Wanted to run this by you because most brokers I talk to in your area overlook
it, and it turns out to be genuinely useful.

Any strategy that defers a seller's tax has to be set up before they sign. Not
after. Once the papers go through there's nothing anyone can do, and plenty of
sellers hear that from their CPA a week after closing.

I've put together a few of the options and the deadline on each. Worth having
on hand for the next one.

Want me to email it to you?

Mitchell
```
*Value-first and the lowest-friction variant in the set. Useful to the broker even if they never reply, and "worth having on hand for the next one" makes the document the ask rather than a meeting. See open item 5 on the opening line.*

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

*Sources: Aug 5 call transcript, July 14 strategy call, BizBuySell Broker Scrape Spec, intake. Nothing fabricated. Offer framing, broker economics, proof, disclaimer and postal address all pending Mitch.*
