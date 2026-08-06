# SEC merger triggers — Campaign 2 timing signal

## Why this exists

`Leads/Mitchell Bloom - ICP List-Building Spec.md` line 36 marks timing, Mitch's stated highest
value target, as ❌ impossible for Campaign 2. `Copy/Vertical 2` line 3 says it plainly: *"No public
selling signal exists in bulk for this ICP."* Campaign 2 therefore runs as a master bucket, with
tenure at a post-IPO employer as the only proxy for "this person holds appreciated stock."

That is not quite right. When a public company is acquired, every employee's vested equity converts
to cash at close, whether they want it or not. The SEC publishes that months in advance in the
merger proxy (DEFM14A). The filing never names the employees, but it names the **company**, and
Blitz turns a company name into employees with emails.

So the SEC is not a lead source here. It is a **trigger list of companies** that feeds the people
search we already run.

Everything here uses free EDGAR. No API key, no subscription. sec-api.io was evaluated and skipped:
it sells parsing convenience, not data we cannot reach.

## Run it

```bash
python3 fetch_triggers.py        # EDGAR indexes -> triggers-live.csv
python3 classify_deals.py        # -> triggers-classified.csv  (10-20 min)
```

Then feed `role == "target"` rows to Blitz. Never the acquirers.

**Cadence: monthly.** About 20 new merger proxies land per month. Re-running is cheap because the
quarterly indexes are cached in `~/.cache/bloom-sec-triggers/` (kept out of the repo, ~30MB each).

Set `EDGAR_UA` if the contact address should change. EDGAR blocks requests without a User-Agent
naming a real person and a reachable email, and caps everyone at 10 requests/second.

## What each stage does

**`fetch_triggers.py`** reads EDGAR's quarterly `form.idx` files, pulls every DEFM14A, dedupes to
the newest filing per company, and drops SPACs and banks (no meaningful employee equity base).

It then decides which deals are still open. When a merger completes, the target gets delisted
(Form 25) and deregistered (Form 15). If neither appears after the proxy date, the deal is still
pending. That is a free, reliable substitute for reading closing dates out of 250 documents.

**`classify_deals.py`** solves the one real trap. A DEFM14A can be filed by *either* side. The
company being acquired files one to approve the sale. The acquirer files one to approve issuing
shares to pay for it. **Only the target's employees get cashed out.** Sending to an acquirer's
staff is wasted spend on people with no liquidity event.

It streams each filing (5-20MB, never written to disk), strips markup, and counts two phrase sets.
Targets discuss the treatment of their own equity awards and shares "converted into the right to
receive." Acquirers discuss a "share issuance proposal." Separation is clean in practice: on the
six-company verification set, targets scored 0 acquirer hits while acquirers scored 65 to 99.

It also captures a `close_hint` sentence, the filing's own language about when the deal is expected
to complete. Read it. A deal closing in three weeks is too late, since the structure has to be in
place before close.

## Verification

Re-run any time the regex sets change:

```bash
python3 classify_deals.py --only "Crinetics,LiveRamp,Simulations Plus,DOMINION,DEVON,AVALONBAY"
```

Expected: Crinetics, LiveRamp and Simulations Plus come back `target`; Dominion Energy, Devon
Energy and AvalonBay come back `acquirer`. Anything less than 6/6 means the phrase sets need work
before spending enrichment credits.

## Handing off to Blitz

Use the skill at `~/.claude/skills/blitz-api/`. Do not hand-roll HTTP.

```bash
set -a; source <path>/.env; set +a
node ~/.claude/skills/blitz-api/blitz.mjs key-info      # ALWAYS check credits first
```

Then resolve each target company to its LinkedIn URL and pull employees. `enrich-company-list.mjs`
may do the whole company-name-to-email chain in one step; try it on 3 companies before writing
anything custom.

Two rules carried over from the spec:

- **Leave seniority broad** (spec line 78). Equity is a tenure story, not a seniority story, and
  rank-and-file hold the biggest surprise gains. Do not pass `--job-level`.
- **Filter people by state, never companies** (spec line 39: CA NY NJ MA MN HI WI VT DC CO). A
  Delaware-incorporated, Austin-headquartered company still employs hundreds of people in the Bay
  Area. Filtering companies by state would gut the list for nothing.

## Known limits

- **Timing is coarse.** "Still pending" is not the same as "closing in 60 days." Read `close_hint`
  before sending, and drop anything closing inside a month.
- **Company size conflicts with the guarantee.** Spec open item 1 notes his agreement reportedly
  requires companies under 50 employees. Acquired public companies are far larger. Unresolved, and
  this pipeline does not fix it. A conversation for Jay.
- **Work-email deliverability is untested** for this client. These are corporate inboxes at large
  companies, not the B2C-leaning addresses Campaign 1 reaches. Watch the first send.
- **Copy needs a timing variant.** `Copy/Vertical 2` line 3's premise is now wrong, and E2-B already
  carries the right line ("this only works if it is set up before you sign"). Small delta, but it
  needs Mitch's sign-off. Three emails maximum, no fourth.
