#!/usr/bin/env python3
"""
Stage 2 — split acquirers from targets, and pull a closing-date hint.

A DEFM14A can be filed by either side of a deal. The company being acquired files
one to ask holders to approve the sale. The acquirer files one to ask holders to
approve issuing shares to pay for it. Only the target's employees get cashed out,
so acquirers are noise and must be dropped before any enrichment spend.

Filings run 5-20MB. Nothing is written to disk; each document is streamed, stripped
of markup, scanned, and discarded.

Usage:
    python3 classify_deals.py
    python3 classify_deals.py --only "Crinetics,LiveRamp,Dominion"   # spot-check
    python3 classify_deals.py --limit 10
"""

import argparse
import csv
import gzip
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

USER_AGENT = os.environ.get("EDGAR_UA", "Shara Ramirez shara@leadgenjay.com")
HERE = os.path.dirname(os.path.abspath(__file__))
IN_CSV = os.path.join(HERE, "triggers-live.csv")
OUT_CSV = os.path.join(HERE, "triggers-classified.csv")

TAGS = re.compile(rb"<[^>]{0,4000}>")
WS = re.compile(rb"[\s\xa0]+")

# The target's proxy is about its own holders being cashed out and its own
# employees' equity being converted. An acquirer's proxy never discusses the
# treatment of its own equity awards, because nothing happens to them.
TARGET_SIGNALS = [
    rb"treatment of (?:company|the company.s) (?:equity awards|stock options|restricted stock)",
    rb"converted into the right to receive",
    rb"each share of company common stock",
    rb"merger sub will (?:be merged|merge) with and into",
]

# The acquirer's ask is permission to issue shares as deal currency.
ACQUIRER_SIGNALS = [
    rb"share issuance proposal",
    rb"stock issuance proposal",
    rb"approval of the issuance of (?:shares|our common stock)",
    rb"issuance of shares of (?:our |parent )?common stock in connection with the merger",
]

CLOSE_HINT = re.compile(
    rb"[^.]{0,160}expect(?:ed|s)?\s+to\s+(?:be\s+)?(?:close|complete|consummate)[^.]{0,160}\.",
    re.I,
)


def get(url, timeout=180):
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip"}
    )
    resp = urllib.request.urlopen(req, timeout=timeout)
    if resp.headers.get("Content-Encoding") == "gzip":
        return gzip.GzipFile(fileobj=io.BytesIO(resp.read()))
    return resp


def primary_document(cik, accession):
    """Resolve the main proxy document, avoiding the full submission blob.

    The .txt full submission bundles every exhibit plus base64-encoded graphics
    and can exceed 100MB. The primary .htm is a fraction of that.
    """
    acc = accession.replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}"
    try:
        with get(f"{base}/index.json", timeout=60) as fh:
            items = json.load(fh)["directory"]["item"]
    except Exception:
        return None
    htm = [i for i in items if i["name"].lower().endswith((".htm", ".html"))]
    if not htm:
        return None
    # The primary document is reliably the largest HTML file in the folder.
    biggest = max(htm, key=lambda i: int(i.get("size") or 0))
    return f"{base}/{biggest['name']}"


def scan(url):
    """Stream, strip markup, and count signal hits. Returns (t_hits, a_hits, hint)."""
    t_hits = a_hits = 0
    hint = b""
    tail = b""
    try:
        with get(url) as fh:
            while True:
                chunk = fh.read(1 << 20)  # 1MB
                if not chunk:
                    break
                # Overlap the previous tail so a phrase split across the chunk
                # boundary is still matched.
                buf = tail + chunk
                tail = buf[-4096:]
                text = WS.sub(b" ", TAGS.sub(b" ", buf)).lower()
                for p in TARGET_SIGNALS:
                    t_hits += len(re.findall(p, text))
                for p in ACQUIRER_SIGNALS:
                    a_hits += len(re.findall(p, text))
                if not hint:
                    m = CLOSE_HINT.search(text)
                    if m:
                        hint = m.group(0)
    except Exception as e:
        return None, None, f"ERROR {e}"
    return t_hits, a_hits, hint.decode("utf-8", "ignore").strip()


def decide(t, a):
    """Acquirer language is rarer and more specific, so it wins when present."""
    if t is None:
        return "unknown", "fetch failed"
    if a >= 2 and a > t:
        return "acquirer", "high" if a >= 5 else "medium"
    if t >= 3:
        return "target", "high" if t >= 8 else "medium"
    if t > a:
        return "target", "low"
    return "unknown", "low"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated substrings of company names")
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    rows = list(csv.DictReader(open(IN_CSV)))
    if args.only:
        needles = [s.strip().lower() for s in args.only.split(",")]
        rows = [r for r in rows if any(n in r["company"].lower() for n in needles)]
    if args.limit:
        rows = rows[: args.limit]

    print(f"Classifying {len(rows)} filings...\n")
    out = []
    for i, r in enumerate(rows, 1):
        acc = os.path.basename(r["url"]).replace(".txt", "")
        doc = primary_document(r["cik"], acc) or r["url"]
        t, a, hint = scan(doc)
        role, conf = decide(t, a)
        out.append({**r, "role": role, "confidence": conf,
                    "target_hits": t, "acquirer_hits": a, "close_hint": hint, "doc": doc})
        flag = {"target": "✓", "acquirer": "✗", "unknown": "?"}[role]
        print(f"  [{i}/{len(rows)}] {flag} {role:9s} t={t} a={a}  {r['company'][:45]}")
        sys.stdout.flush()
        time.sleep(0.3)  # well under EDGAR's 10 req/sec cap

    with open(OUT_CSV, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "filed", "company", "cik", "role", "confidence",
            "target_hits", "acquirer_hits", "close_hint", "url", "doc"])
        w.writeheader()
        w.writerows(out)

    n = lambda k: sum(1 for r in out if r["role"] == k)
    print(f"\n  targets  : {n('target')}   <- feed these to Blitz")
    print(f"  acquirers: {n('acquirer')}   <- excluded, employees do not liquidate")
    print(f"  unknown  : {n('unknown')}   <- needs a human look")
    print(f"\n  -> {OUT_CSV}")


if __name__ == "__main__":
    main()
