# Mitchell Bloom — Execution Plan

**Built 2026-08-05 from the Aug 5 call.** Source: `Mitchell Bloom - Transcript - 2026-08-05.md`.
Supersedes nothing; runs alongside `Mitchell Bloom - Promises Checklist.md` (which covers the July 6 + July 14 commitments).

**Scheduling constraint:** Mitch travels Aug 6 through Aug 10, back **Tuesday Aug 11**. Everything needing his input stalls until then. Front-load the rest.

**Critical path:** disclaimer (#34) gates all sending → broker framing (#30) gates broker copy (#11) → V3 verification (#12-13) is the only campaign with finished list *and* finished copy.

---

## Phase 0 — Today, before he leaves

- [ ] 1. Send the recap email
- [ ] 2. Add the website hold line so he doesn't sign the other vendor while traveling

## Phase 1 — Unblocked, Aug 6-10

### Broker campaign (replaces the dead business-seller vertical)
- [ ] 3. Build the broker list via the `bizbuysell-broker-list-builder` skill
- [ ] 4. Confirm BizBuySell is scrapable (plain fetch returns 403, CoStar is anti-bot)
- [ ] 5. Try browser-harness cloud mode before paying for the Apify actor
- [ ] 6. Run Leg B (IBBA directory), same states, `hasEmail=true`
- [ ] 7. Capture listing-level rows as a child table keyed to `broker_id`
- [ ] 8. Merge, dedupe on name+firm then phone, apply 3-per-firm cap after verification
- [ ] 9. Enrich missing emails: firm domain → Apollo/Blitz → MillionVerifier
- [ ] 10. Review CoStar ToS before scheduling any recurring pull
- [x] 11. ~~Draft the broker sequence~~ — DONE Aug 5, `Copy/C3 - Business Brokers (referral channel).md`. Offer framing at #30 still unconfirmed

### Concentrated stock (V3, mid-pipeline)
*Renumbered from V2 on 2026-08-10. `V2` now means the business-broker list. Task numbers are unchanged.*
- [ ] 12. Push `_data/Mitchell Bloom - V2 Concentrated Stock - VERIFY these emails.csv` through MillionVerifier *(working file keeps its `V2` prefix, it was not renamed)*
- [ ] 13. Run `build_final.py` on FULL report + MAP to produce the Instantly upload
- [ ] 14. Split Batch 2 risky/catch-all to hold
- [ ] 15. Confirm the SEC filing type before building further scraping on it
- [ ] 16. Set the lookback window *(needs Mitch)*
- [ ] 17. Research the newly-public AI and crypto companies Mitch flagged

### Property lists (V1, largely done)
- [ ] 18. Verify the PropStream spec targets mobile home **parks**, not units
- [ ] 19. Check whether commercial owners can be sourced from Redfin / homes.com

### Copy
- [ ] 20. Integrate the call's angle adjustments across existing verticals
- [ ] 21. Make "plan first, sell second" the through line
- [ ] 22. Widen past the DST: CRUTs, opportunity zones, 1031, QSBS stacking
- [ ] 23. Add the charitable-trust objection handler (give 10% or lose 35%)
- [ ] 24. Rework the CTA to "show you how it works," quick-chat offer moves to his reply
- [ ] 25. Read Mitch's Aug 4 email (his stated setup for "plan first, sell second")
- [ ] 26. Pull BizBuySell Insight Report / IBBA Market Pulse for deal-failure data
- [ ] 27. Decide whether C5 business-seller copy is retired or repointed

> #26 is the highest-leverage research item. Deal-failure data converts Mitch from
> deal-killer to deal-saver, which answers the exact broker objection he keeps hitting.

### Website
- [ ] 28. Build the website concept (committed for the weekend)
- [ ] 29. Define LGJ's website scope so he doesn't double-pay the other vendor

## Phase 2 — Blocked on Mitch, resume Aug 11

- [ ] 30. **Broker offer framing** — refer their client, or broker as his own client? *(blocks #11)*
- [ ] 31. **Broker economics** — referral fee, rev share, or nothing? Also an RIA solicitor-rule question
- [ ] 32. **What Value Builder actually is** — named in four docs, described nowhere
- [ ] 33. **Any existing broker relationship** — has one ever referred him a deal?
- [ ] 34. **The disclaimer** — still open since July 14, blocks all sending
- [ ] 35. **Email archive scope** — the Supabase backend promised at no cost on the deposit call
- [ ] 36. **Deal-size threshold** — deposit vs strategy call conflict
- [ ] 37. **ICP gender** — deposit framed women, stockholder path skews male
- [ ] 38. **Playbook attribution** — Karen Peters case study is ECGS, not his

## Phase 3 — Infrastructure and compliance, ongoing

- [ ] 39. Confirm domain warmup status against the ~4 week timeline
- [ ] 40. Set up GoHighLevel and send the signup link (12 months included)
- [ ] 41. Point secondary domains to taxfreeplan.com
- [ ] 42. Give Mitch a send.leadgenjay.com login
- [ ] 43. Stand up the email archive backend once #35 is confirmed
- [ ] 44. Confirm sending runs on Instantly, not Bison
- [ ] 45. Run the pre-launch audit before any campaign turns on

## Phase 4 — Triggered by first replies

- [ ] 46. At the first real reply, run the live walkthrough call Jonathan committed to
- [ ] 47. At 5-10 replies, pause and read what's landing before building lead management
- [ ] 48. Build the post-booking nurture (videos after the booking, never before)
- [ ] 49. Train his daughter on the system if she takes it on
- [ ] 50. Write the $1,500/month maintenance scope *(he asked, nobody committed)*
