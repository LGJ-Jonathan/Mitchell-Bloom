# C3 - Business Brokers (referral channel)  *(Campaign 3)*

> **Rewritten 2026-08-05** from the Aug 5 call, adapted from the C1 structure. Previous version is in git history.
> Client-facing doc: *Bloom Financial - Business Brokers: Five Cold Sequences* (Drive).

**Campaign type:** Business brokers, M&A advisors and business intermediaries with live deal flow on BizBuySell. **Referral / channel play, not a direct-seller list.** The broker brings the seller.
**Client:** Mitchell Bloom / Bloom Financial · **Sequencer:** Instantly · **Merge field:** `{{firstName}}` only
**Cadence:** E1 (day 0) → E2 (day 3, reply on thread) → E3 (day 7, new thread) · **A/B:** 4/2/2 · **3 steps, no 4th email.**
**8 E1 variants written, 4 slots.** First-round picks: **E1-G** (for the ones you already closed) · **E1-F** (the objection your seller will raise) · **E1-E** (someone in your corner) · **E1-C** (the seller who walks). Two that hand the broker something useful, one that concedes their objection, one that reframes tax as a deal-saver.
**List:** `Leads/V2+V3 Brokers - MASTER WITH EMAILS.csv` — 3,004 unique people, 772 qualified with email and sendable now, 999 pending Clay enrichment.

> ## ⚠️ THE BLOCKER: offer framing is unconfirmed
> Everything below assumes **the broker refers their selling client**. Mitch raised four different angles on the Aug 5 call and never picked one:
> 1. Their client keeps more, so the deal closes instead of stalling
> 2. **Value Builder** — his program to raise business value *before* a sale (described nowhere in the repo)
> 3. The **broker's own** income-tax exposure as a top producer — *a different offer with a different buyer*
> 4. Network positioning — Mitch as the capital-gains partner in their book
>
> Angles 1 and 4 are one offer and are what this copy is written on. Angles 2 and 3 are separate offers and are **not** in this sequence.
> **If the intent is broker-as-tax-client, all five E1s need rewriting.**
>
> Also unresolved: **how the broker gets paid.** Brokers are commission operators; a channel offer with no economics asks them to work free for a stranger. And if there is a referral fee, RIA solicitor rules govern how it can be described in cold email. That is a compliance question before it is a copy question.

**Angle:** Mitch's Aug 5 through-line, verbatim: ***"Plan first, sell second."*** This is NOT the seller pitch reworded. A broker does not care about their client's tax bill as a favor — they care about closings. So the lead is: **tax is what stalls your closings, and I handle it before it does.**

**The two objections Mitch named, pre-empted:**
- *"That's up to the tax person. We don't even talk about taxes."* → E1-E addresses it head-on and concedes the point before reframing.
- *"I don't want to kill my deal."* → E1-A and E1-C flip it: this is what saves closings, not what threatens them.

**Where this diverges from C1 (and why):**
- **The reader is not the seller.** Every benefit is stated as something that happens to *their client*, with a line making clear Mitch stays out of the broker's side.
- **E1-C replaces C1's rollover-trap variant** with the seller who goes quiet late once they see their net. Same structural job (name a specific failure mode) for a different audience.
- **E1-E replaces C1's "deadline" framing** with partner positioning, the angle that dodges the "I don't touch taxes" reflex entirely.

**Deliberately excluded, both by Shara's call:** the *"you still pay the tax"* honesty beat (belongs in post-booking nurture) and any state-vs-federal percentage split.

**Plain English** in E1. **E2-A is the one exception** — names three structures with a one-line gloss each. *Reverses the July 14 jargon rule; needs Mitch's knowing sign-off.*

**Banned (per call):** Rob Lowe · audit statistics · indemnification · pricing · "secret method." **"Defer," never "avoid."** No promissory claims, no guaranteed tax outcome.

**CAN-SPAM:** footer carries physical address (rule 4), clear opt-out (rule 5), ad-identification line (rule 3). Honest subjects including E3 (rule 2).

**Spam check (mailmeteor local port):** all E1 and E3 bodies score **Great (0 hits)** after rewriting around `deal`, `price`, `terms` and `problem`, all of which are on the wordlist and all of which are native broker vocabulary. E2-A scores Poor from `sales` and `opportunity` — literal product names. The mandatory footer caps every full email at Poor regardless.

**Open items:**
1. **Offer framing** (see blocker above) — gates everything.
2. **Broker economics** — referral fee, revenue share, or nothing.
3. **Proof gap.** Kelly & David is a $7.6M *multifamily real estate* result. A business-sale case study would be far stronger here. **Ask Mitch for one.** No proof is currently used in this sequence.
4. **What Value Builder actually is.** Named in four repo docs, described in none.
5. **E1-C's claim** that sellers go quiet late once they see their net reflects the Aug 5 call but is not a documented figure. The BizBuySell Insight Report or IBBA Market Pulse may substantiate it — worth pulling.
6. Disclaimer verbiage · the summary one-pager · confirm postal address.

---

**Footer, every email:**
```
Bloom Financial, 390 Interlocken Crescent, Suite 350, Broomfield, CO 80021
This is an advertisement.
Reply "unsubscribe" and I'll take you off my list.
[Disclaimer to be added by Bloom]
```

---

## E1 — Day 0 (new thread)

### E1-A — what your seller loses
Subjects: `what your sellers lose at closing` · `{{firstName}}, a question on your listings` · `the part that stalls deals` · `before your seller signs`
```
Hi {{firstName}},

When one of your sellers closes, close to a third of the gain can go to
taxes that year. Most of them don't find that out until it's too late to
do anything about it.

There are several ways to defer it, and they have to be set up before the
papers are signed.

I handle that side so you don't have to. Your seller keeps more and nothing
stalls at the finish line.

Want me to send over how it works?

Mitchell
```

### E1-B — plan first, sell second
Subjects: `plan first, sell second` · `{{firstName}}, on the sellers you're working with` · `the conversation that happens too late` · `worth raising early`
```
Hi {{firstName}},

Wanted to ask how you handle the tax conversation with your sellers.

Most of them plan the exit and handle the tax after. That's backwards, and
it's where they give up the most, because by then there's nothing left to
set up.

What I recommend is simple. Plan first, sell second. I can be the one who
walks them through it, alongside their CPA.

Interested?

Mitchell
```

### E1-C — the seller who walks
Subjects: `the deals that fall apart late` · `{{firstName}}, on sellers getting cold feet` · `what stops a sale at the end` · `the number that scares sellers`
```
Hi {{firstName}},

You've probably had a seller go quiet late once they saw what they'd
actually walk away with.

That number is usually what stalls them. When a seller realizes a third of
the gain is going to taxes, what they agreed to stops looking like what
they wanted.

There are several ways to change that number, and every one has to be in
place before signing.

Want me to show you how it works?

Mitchell
```
*The deal-saver frame. Directly answers "I don't want to kill my deal" by making tax the thing that kills deals and Mitch the thing that prevents it.*

### E1-D — the deadline nobody mentions
Subjects: `one thing worth knowing` · `{{firstName}}, the part sellers miss` · `what their CPA mentions a week late` · `the deadline nobody mentions`
```
Hi {{firstName}},

Wanted to run this by you. Could be useful whether or not we ever work
together.

Any strategy that defers a seller's tax has to be set up before they sign.
Not after. Once the papers go through there's nothing anyone can do, and
plenty of sellers hear that from their CPA a week after closing.

I've summarized a few of the options and the deadline on each. Worth having
on hand for the next one.

Want me to email it to you?

Mitchell
```
*Value-first. Useful to the broker even if they never reply, and "worth having on hand for the next one" makes the document the ask rather than a meeting.*

### E1-E — someone in your corner
Subjects: `a name for your back pocket` · `{{firstName}}, worth knowing someone` · `the piece brokers don't handle` · `for the next seller who asks`
```
Hi {{firstName}},

Something worth having on your radar.

Brokers tell me they don't touch taxes, and I understand why. It isn't your
job and you don't want to slow anything down.

But sellers ask anyway, and having someone to hand that question to is
easier than not having one. I work alongside their CPA and I stay clear of
your side of it entirely.

Want me to send you the overview so you have it?

Mitchell
```
*Concedes the objection in Mitch's own words before reframing. Lowest-friction variant in the set — the ask is a document, not a relationship.*

### E1-F — the objection your seller will raise *(added 2026-08-05)*
Subjects: `the objection your seller will raise` · `{{firstName}}, on the charitable piece` · `the ten percent question` · `what to say when they tune out`
```
Hi {{firstName}},

When a seller hears the words charitable remainder trust, most of them tune
out. Understandable.

The math is worth a minute though. They part with around ten percent to a
cause they pick, against closer to a third going to taxes. The rest stays
invested and pays them back over the years.

You don't have to explain any of that. I do.

Want me to show you the comparison?

Mitchell
```
*Recovers the CRUT and Mitch's 10%/35% handler, translated for a reader who is not the one with the tax problem. The broker-specific turn is "You don't have to explain any of that. I do." A broker's real objection is being handed something they'd have to learn and defend mid-deal, so taking the explaining off their plate is the actual product here.*

### E1-G — for the ones you already closed *(added 2026-08-05)*
Subjects: `for the ones you already closed` · `{{firstName}}, on your past sellers` · `the exception to the deadline` · `a reason to reach back out`
```
Hi {{firstName}},

Most of this has to be handled before a seller signs. Opportunity zones are
the exception.

There's a window after closing to move the gain into one, which means a
seller you closed earlier this year may still have a move available.

Worth knowing for the ones already done, not just the ones in front of you.

Want me to send over how it works?

Mitchell
```
*⭐ **Probably the strongest variant in this campaign.** Every other broker email competes for attention against a live pipeline. This one hands the broker a reason to call a past client with good news, which is a relationship win they get to own, and brokers live on repeat business and referrals from closed sellers. It also works on a broker whose current pipeline is thin, which nothing else here does.*
*Accuracy: post-closing window is real but the rules have been amended more than once. **Mitch to confirm.***

### E1-H — QSBS *(added 2026-08-05)*
Subjects: `if your seller holds C corp stock` · `{{firstName}}, worth checking early` · `the exemption most sellers miss` · `before the next one signs`
```
Hi {{firstName}},

If a seller is selling stock in a C corporation they started or joined
early, part of the gain may already qualify for an exemption.

Most sellers have never been told, and fewer know it can sometimes be
multiplied across family members. It depends on when they got the shares
and what the company looked like then.

It can't be fixed afterward, so it's worth checking early.

Want me to send over how it works?

Mitchell
```
*⚠️ **Narrow reach.** QSBS applies to a minority of business-broker deals: it needs C-corp original-issuance stock, a five-year hold and size limits at issuance, and most small-business sales are asset sales or pass-through entities. Worth testing anyway because when it applies the number is large enough that the broker remembers who told them, but rank it behind E1-F and E1-G.*
*Same confirmation needed as C2: **does Mitch advise on QSBS at all.***

---

## E2 — Day 3 (reply on same thread, keeps E1 subject)

### E2-A — the structures, each in one line
```
Hi {{firstName}}, floating this back up.

There are a few of these, and they're simpler than the names sound.

A deferred sales trust pays the seller out over time. A charitable remainder
trust pays them out and sends the remainder to a cause they pick.
Opportunity zones let them reinvest the gain instead of paying at closing.
Which one fits depends on what they want afterward.

None of it touches your side of it.

Want me to send it over?

Mitchell
```

### E2-B — legitimacy, plus the closing argument
```
Hi {{firstName}},

None of this was invented yesterday. These have been in the tax code for
decades, and it isn't a loophole.

The point of it is simple. Instead of a third going to taxes the year they
sell, the whole amount stays invested and they pay as they draw from it. A
seller who sees that number early is a seller who closes.

Want me to send you the summary?

Mitchell
```

---

## E3 — Day 7 (new thread) · final email
Subjects: `one more thing` · `{{firstName}}, quick note` · `one last thought`

### E3-A — staying out of their lane
```
Hi {{firstName}},

To be clear, I'm not looking to come between you and your client.

I work alongside their CPA and stay clear of the transaction itself. The
seller's own attorney and accountant look at everything first.

You'd be handing over a question you don't want anyway.

Happy to send it over so you have it. Want me to?

Mitchell
```

### E3-B — no charge, no timeline drag
```
Hi {{firstName}},

Last note from me, then I'll leave you be.

There's no charge to look at this, or for a seller to set it up. Most of the
work happens on my end, and it doesn't add weeks to a timeline.

If it's ever useful, you'll know where to find me.

Want me to send it?

Mitchell
```
*"Doesn't add weeks to a timeline" is the broker-specific version of C1's "no months of attorney meetings." Timeline drag is the broker's real fear, not cost.*

---

*Sources: Aug 5 call transcript, BizBuySell Broker Scrape Spec, intake. Nothing fabricated. Offer framing, broker economics, proof, disclaimer and postal address all pending Mitch.*
