#!/usr/bin/env python3
"""
Stage 1 — pull merger-proxy trigger companies from free EDGAR.

A DEFM14A is the proxy statement for a merger. When a public company is acquired,
every employee's vested equity converts to cash at close. That is a forced taxable
event on a known date, which is the timing signal Campaign 2 otherwise lacks.

This reads EDGAR's quarterly form indexes (no API key, no cost), keeps the deals
that have not closed yet, and writes them out for Stage 2 to classify.

Usage:
    python3 fetch_triggers.py                  # trailing 5 quarters
    python3 fetch_triggers.py --quarters 8     # go back further
"""

import argparse
import csv
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import date

# EDGAR requires a User-Agent naming a real person and a reachable email.
# Requests without one get 403'd.
USER_AGENT = os.environ.get("EDGAR_UA", "Shara Ramirez shara@leadgenjay.com")

CACHE_DIR = os.path.expanduser("~/.cache/bloom-sec-triggers")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

IDX_URL = "https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{q}/form.idx"

# form.idx is fixed-width-ish: form type, company, CIK, date, path, all space-padded.
ROW = re.compile(r"^(\S+(?:\s\S+)?)\s{2,}(.+?)\s{2,}(\d+)\s+(\d{4}-\d{2}-\d{2})\s+(\S+)")

# Shell companies. A SPAC has a handful of employees and no equity base worth
# reaching, so it is pure noise in a list about employee stock.
SPAC = re.compile(r"(acquisition corp|acquisition co\b|merger corp|equity partners|"
                  r"brigade|capital corp\b)", re.I)

# Bank and thrift mergers are frequent and small, and their employees rarely hold
# meaningful equity. Dropped to keep the list dense.
BANK = re.compile(r"(bancorp|bancshares|bankshares|\bbank\b|savings|financial corp)", re.I)

# When a merger completes, the target is delisted (Form 25) and deregistered
# (Form 15). The absence of either after the proxy is a free, reliable proxy for
# "this deal is still open."
CLOSE_FORMS = ("25-NSE", "25 ", "15-12B", "15-12G")


def trailing_quarters(n):
    """Most recent n quarters as (year, quarter), newest first."""
    today = date.today()
    y, q = today.year, (today.month - 1) // 3 + 1
    out = []
    for _ in range(n):
        out.append((y, q))
        q -= 1
        if q == 0:
            q, y = 4, y - 1
    return out


def fetch_index(year, quarter):
    """Download one quarterly index, caching outside the repo (~30MB each)."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, f"form-{year}-QTR{quarter}.idx")

    # The current quarter keeps growing, so never serve it from a stale cache.
    current = (year, quarter) == trailing_quarters(1)[0]
    if os.path.exists(path) and not current:
        return path

    url = IDX_URL.format(year=year, q=quarter)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp, open(path, "wb") as fh:
            fh.write(resp.read())
    except urllib.error.HTTPError as e:
        # Future or not-yet-published quarters 403/404. Not fatal.
        print(f"  skip {year} QTR{quarter}: HTTP {e.code}", file=sys.stderr)
        return None
    time.sleep(0.2)  # EDGAR caps at 10 req/sec; stay far under it
    return path


def parse(paths):
    """Return (proxy rows, {cik: [close dates]}) from the indexes."""
    proxies, closings = [], defaultdict(list)
    for p in paths:
        with open(p, encoding="latin-1") as fh:
            for line in fh:
                if line.startswith("DEFM14A"):
                    m = ROW.match(line)
                    if m:
                        proxies.append({
                            "filed": m.group(4),
                            "company": m.group(2).strip(),
                            "cik": m.group(3),
                            "url": "https://www.sec.gov/Archives/" + m.group(5),
                        })
                elif line.startswith(CLOSE_FORMS):
                    m = ROW.match(line)
                    if m:
                        closings[m.group(3)].append(m.group(4))
    return proxies, closings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quarters", type=int, default=5)
    args = ap.parse_args()

    print(f"Fetching {args.quarters} quarters of EDGAR indexes...")
    paths = [p for p in (fetch_index(y, q) for y, q in trailing_quarters(args.quarters)) if p]
    proxies, closings = parse(paths)

    # Keep only the newest proxy per company. Deals get amended and refiled.
    proxies.sort(key=lambda r: r["filed"], reverse=True)
    seen, uniq = set(), []
    for r in proxies:
        if r["cik"] not in seen:
            seen.add(r["cik"])
            uniq.append(r)

    core, dropped = [], []
    for r in uniq:
        if SPAC.search(r["company"]) or BANK.search(r["company"]):
            dropped.append(r)
        else:
            core.append(r)

    live, closed = [], []
    for r in core:
        after = [d for d in closings.get(r["cik"], []) if d > r["filed"]]
        if after:
            r["closed_on"] = min(after)
            closed.append(r)
        else:
            r["closed_on"] = ""
            live.append(r)

    def write(name, rows, fields):
        path = os.path.join(OUT_DIR, name)
        with open(path, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        return path

    write("triggers-live.csv", live, ["filed", "company", "cik", "url"])
    write("triggers-closed.csv", closed, ["filed", "company", "cik", "url", "closed_on"])

    print(f"\n  DEFM14A filings      : {len(proxies)}")
    print(f"  unique companies     : {len(uniq)}")
    print(f"  SPACs + banks dropped: {len(dropped)}")
    print(f"  deals already closed : {len(closed)}")
    print(f"  STILL PENDING        : {len(live)}  -> triggers-live.csv")
    print("\nNewest 10 pending:")
    for r in live[:10]:
        print(f"  {r['filed']}  {r['company']}")


if __name__ == "__main__":
    main()
