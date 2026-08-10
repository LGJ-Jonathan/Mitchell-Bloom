# C3 - Business Brokers (referral channel)  *(Campaign 3)*

**Campaign type:** Business brokers, M&A advisors and business intermediaries with live deal flow on BizBuySell. **Referral / channel play, not a direct-seller list.** The broker brings the seller.
**Client:** Mitchell Bloom / Bloom Financial · **Sequencer:** Instantly · **Merge fields:** `{{firstName}}` required · `{{companyName}}` and `{{liveListings}}` optional (see note)
**Cadence:** E1 (day 0) → E2 (day 3, reply on thread) → E3 (day 7, new thread) · **A/B:** 3/2/2
**List:** `Leads/V2 Brokers - QUALIFIED.csv` (+ high-tax expansion, pending map approval)

**Angle (source = Aug 5 call, Mitch verbatim):** ***"Plan first, sell second."*** He asked us to note it on the call. This is NOT the seller pitch reworded. A broker does not care about their own client's tax bill as a favor, they care about deals closing. So the lead is: **tax is what stalls your closings, and I fix it before it stalls them.**

**The four levers (all from the call):**
1. **Deal-saver.** Sellers who get blindsided by a 30 to 45% hit walk away at the table. Handled early, the deal closes.
2. **Value Builder.** Mitch's program to build business value *before* a sale.
3. **The broker's own tax exposure.** Top producers have real income-tax problems of their own.
4. **Network positioning.** The broker gets to be the one who brings a capital-gains answer to the table.

**The two objections Mitch named, pre-empted in the copy:**
- *"That's up to the tax person. We don't even talk about taxes."* → E2 addresses directly.
- *"I don't want to kill my deal."* → E1 flips it: this is what saves deals, not what kills them.

**Trust builders:** specialization (the one thing he does) · media (WSJ, MarketWatch, Business Insider, US News) · transparency (sends the mechanism in writing so the broker and their client's CPA can vet it) · the client's own CPA stays in the decision.

**Banned (per call):** Rob Lowe · audit statistics · indemnification · pricing · "secret method." **"Defer," never "avoid."** No promissory claims, no guaranteed tax outcome.

**CAN-SPAM:** footer carries physical address (rule 4), clear opt-out (rule 5), ad-identification line (rule 3). Honest subjects including E3 (rule 2).

> ⚠️ **Open items before send:**
> 1. **Proof gap.** Kelly & David is a $7.6M *multifamily real estate* result. For a business-broker audience a *business sale* case study is far stronger. **Ask Mitch for one.** Until then E2 uses the real-estate example accurately labelled, or drops proof entirely (variant B).
> 2. `{{liveListings}}` requires the variable plus a fallback configured in Instantly. **Validate before launch** or use the variants that do not reference it.
> 3. Media-mention line needs Mitch's ad-review sign-off.
> 4. Confirm postal address.

---

## Subject lines (rotate across E1)
1. `the thing that kills your closings`
2. `plan first, sell second`
3. `your sellers and the tax bill`

## E3 subject lines (new thread)
1. `one more idea`
2. `{{firstName}}, quick thought`

---

## E1 — day 0 (new thread)

### E1-A — deal-saver lead (no merge risk)
```
{{RANDOM | Hi | Hey | Hello}} {{firstName}},

How many of your deals stall once the seller finds out what they keep
after taxes?

In a high tax state it can be close to half the gain, and most owners do
not run the numbers until they are already at the table. Helping them
defer that legally, before the sale closes, is the one thing I do.

To be clear, this is not something that slows a deal down. It is set up
ahead of closing, and it usually takes the biggest objection off the
table before it comes up.

{{RANDOM | Would it be okay if I sent over how it works, so you can look it over? | Mind if I send you the mechanism so you can judge it yourself? | Want me to send how it works so you can see if it fits your sellers?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

### E1-B — "plan first, sell second"
```
{{RANDOM | Hi | Hey | Hello}} {{firstName}},

Plan first, sell second.

Most of the owners you list do it the other way around. They agree on a
number, get to closing, and only then find out what the tax takes. That
is the point where deals get renegotiated or die.

I work with sellers before that happens so the tax is handled ahead of
the sale rather than discovered at the end of it. Their CPA reviews the
whole thing.

{{RANDOM | Would it be okay if I sent over how it works? | Mind if I send the mechanism over so you can look at it? | Want me to send it across so you can vet it?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

### E1-C — listing-count personalization *(requires `{{liveListings}}` + fallback)*
```
{{RANDOM | Hi | Hey | Hello}} {{firstName}},

I saw you have {{liveListings}} businesses listed right now.

Quick question. On the ones that close, do the owners know what they keep
after taxes before they agree to a number, or do they find out at the end?

In a high tax state it can be close to half the gain. Helping owners defer
that legally, before the sale closes, is the one thing I do. It has to be
set up ahead of closing, which is why I am reaching out to you and not to
them.

{{RANDOM | Would it be okay if I sent over how it works? | Mind if I send the mechanism so you can judge it? | Want me to send how it works so you can see if it fits?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

---

---

## 🟠 NO-TAX-STATE SEGMENT — E1-D and E2-C
*Run these **instead of** E1-A/B/C and E2-A/B for brokers in **FL, TX, WA, TN, NV, NH, WY, SD, AK**.*

**Why this exists.** The IBBA national pull added **1,299 emails in no-income-tax states** (Florida alone is 959). Every other E1 variant opens on a line like *"in a high tax state it can be close to half the gain."* To a Florida broker that is simply false, and it is the first thing they read. Sending state-tax copy into a no-tax state reads as a mail-merge that did not check where they are.

**The angle that still works:** **federal capital gains is 20% plus the 3.8% NIIT = 23.8%, everywhere.** On a $3M gain that is roughly $714,000 regardless of state. Depreciation recapture on any real estate in the deal is a further 25%. Smaller than California, still enough to blow up a closing.

> Segment on the `state` column. Never let a `{{liveListings}}` or high-tax line reach this segment.

### E1-D — federal-only, no state-tax claim
```
{{RANDOM | Hi | Hey | Hello}} {{firstName}},

How many of your deals stall once the seller works out what they actually
keep at closing?

No state income tax where you are, but federal capital gains still runs
about 23.8% once you include the investment income surtax, and any real
estate in the deal gets hit again on depreciation recapture. On a few
million in gain that is real money, and most owners have not run the
number until they are already at the table.

Helping owners defer that legally, before the sale closes, is the one
thing I do. It gets set up ahead of closing, so it tends to take the
objection off the table instead of creating one.

{{RANDOM | Would it be okay if I sent over how it works, so you can look it over? | Mind if I send the mechanism so you can judge it yourself? | Want me to send how it works so you can see if it fits your sellers?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

### E2-C — reply on thread, federal-only version of the CPA objection
```
{{RANDOM | Hi | Hey}} {{firstName}},

The usual answer here is that taxes are the seller's CPA's problem, not
the broker's.

Fair. The catch is timing. Once the sale closes almost nothing can be
done, and most CPAs are generalists who do not set these structures up.
So the seller finds out too late, and it is your closing that absorbs it.

I am not asking you to advise anyone on tax. I am offering to be the
person you hand that question to when it comes up, so it stops being
something that stalls your deals.

{{RANDOM | Worth a short conversation? | Open to a quick call on it? | Want me to send how it works first?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

**E3-A (Value Builder) and E3-B (the broker's own tax) work unchanged in this segment** — neither mentions state tax.

---

## E2 — day 3 (reply on the E1 thread, no subject)

### E2-A — kills the "that's the CPA's job" objection
```
{{RANDOM | Hi | Hey}} {{firstName}},

The usual answer I get here is that taxes are the seller's CPA's problem,
not the broker's.

Fair. The catch is timing. Once the sale closes, almost nothing can be
done, and most CPAs are generalists who do not set these structures up.
So the seller finds out too late, and it is your closing that absorbs it.

I am not asking you to advise anyone on tax. I am offering to be the
person you hand that question to when it comes up, so it stops being
something that stalls your deals.

{{RANDOM | Worth a short conversation? | Open to a quick call on it? | Want me to send how it works first?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

### E2-B — proof + partner framing
```
{{RANDOM | Hi | Hey}} {{firstName}},

Following up on the note above.

A recent example, from the real estate side of what I do. A couple sold a
$7.6M property, a 1031 exchange fell through, and they were facing the
full bill. We deferred roughly $1.1M of the capital gains legally, set up
before the sale closed. Their own CPA reviewed it.

Same structure applies to a business sale. I have been featured on this in
the Wall Street Journal and Business Insider.

Most brokers I work with just keep me in the background as the person they
bring in when tax comes up.

{{RANDOM | Would that be useful to have? | Want me to send how it works? | Worth a quick call?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

---

## E3 — day 7 (new thread)

### E3-A — Value Builder angle
```
{{RANDOM | Hi | Hey}} {{firstName}},

Different thought than my last note.

Alongside the tax work I run a program that helps owners build the value
of the business before they take it to market. For a broker that tends to
mean a cleaner business, a better multiple, and a seller who is actually
ready when the offers come in.

If that is useful for the ones who are close but not quite sellable yet,
I am happy to explain how it works.

{{RANDOM | Worth a look? | Want me to send the details? | Should I send it over?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

### E3-B — the broker's own tax exposure
```
{{RANDOM | Hi | Hey}} {{firstName}},

Last note from me, and this one is not about your sellers.

Brokers who have a strong year tend to have a real tax problem of their
own, and most of the planning options only work if they are set up before
the income lands rather than after.

That is the same work I do for sellers, just pointed at you instead.

{{RANDOM | Worth a short call? | Want me to send how it works? | Open to a quick conversation?}}

{{RANDOM | Best | Talk soon | Warm regards}},

Mitchell Bloom
Bloom Financial

Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.

[DISCLAIMER PLACEHOLDER]
```

---

*Sequence stops at E3. No fourth or breakup email.*
