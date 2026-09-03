#!/usr/bin/env node
/**
 * Stage 3b — pull a people sample from the resolved merger-target companies.
 *
 * Purpose is measurement, not volume. It answers the three numbers that decide
 * whether Campaign 2 is worth launching:
 *   1. how many employees per company sit in Mitch's 10 states
 *   2. what share of those return a deliverable work email
 *   3. what the titles actually look like (is this rank-and-file or a VP flood)
 *
 * Two things worth knowing about the Blitz side:
 *  - Blitz has NO US-state filter. State is a post-filter on `state_code`, so the
 *    raw pull is nationwide and gets cut afterward. The in-state share below is
 *    therefore a real measured rate, not an assumption.
 *  - Seniority is deliberately unfiltered (spec line 78). Equity is a tenure
 *    story, not a title story, so no --job-level is passed.
 *
 *   node sample_people.mjs [--target=100] [--per-company=40]
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createClient, readCSVObjects, toCSV, flattenPerson, pickItems } from
  "../../../../../.claude/skills/blitz-api/blitz-client.mjs";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const IN = path.join(HERE, "triggers-companies.csv");
const OUT = path.join(HERE, "sample-people.csv");

const arg = (k, d) => Number((process.argv.find(a => a.startsWith(`--${k}=`)) || `=${d}`).split("=")[1]);
const TARGET = arg("target", 100);
const PER_CO = arg("per-company", 40);

// Spec line 39. Filtered on the PERSON, never the company: an Austin-headquartered
// company still employs hundreds of people in the Bay Area.
const STATES = new Set(["CA", "NY", "NJ", "MA", "MN", "HI", "WI", "VT", "DC", "CO"]);

// Name-matched to the wrong entity during resolution. Verified by hand against
// headcount and HQ; each is a real company that simply is not the registrant.
const WRONG_MATCH = new Set([
  "Silicon Cert Laboratories",              // not Silicon Laboratories
  "Tiptree Patisserie Ltd",                 // a bakery, not Tiptree Inc
  "Procap Financial Services Private Limited", // India, not ProCap Financial
  "Equitable Advisors",                     // subsidiary, not Equitable Holdings
  "Axalta Coating Systems U.S. Inc",        // 52-person sub, not the 13k parent
]);

// Below this the LinkedIn account is a shell or a stub page, not a workforce.
const MIN_EMPLOYEES = 100;

const blitz = createClient();

const all = readCSVObjects(IN).objects;
const usable = all.filter(r =>
  r.company_linkedin_url &&
  !WRONG_MATCH.has(r.matched_name) &&
  Number(r.employees_on_linkedin) >= MIN_EMPLOYEES);

console.log(`Companies resolved      : ${all.length}`);
console.log(`  dropped, wrong match  : ${all.filter(r => WRONG_MATCH.has(r.matched_name)).length}`);
console.log(`  dropped, too small    : ${all.filter(r => r.company_linkedin_url &&
  !WRONG_MATCH.has(r.matched_name) && Number(r.employees_on_linkedin) < MIN_EMPLOYEES).length}`);
console.log(`  usable                : ${usable.length}\n`);

// Largest first: the biggest employee bases carry the sample and are the ones
// most likely to have a real RSU population.
usable.sort((a, b) => Number(b.employees_on_linkedin) - Number(a.employees_on_linkedin));

const rows = [];
const perCompany = [];

for (const c of usable) {
  if (rows.length >= TARGET) break;
  let raw = 0, inState = 0;
  try {
    for await (const p of blitz.iterate.people(
      {
        company: { linkedin_url: [c.company_linkedin_url] },
        people: { location: { country_code: ["US"] } },
      },
      { maxItems: PER_CO }
    )) {
      raw++;
      const row = flattenPerson(p, {
        trigger_company: c.matched_name,
        edgar_name: c.edgar_name,
        proxy_filed: c.filed,
        close_hint: c.close_hint,
      });
      if (!STATES.has(row.state_code)) continue;
      inState++;
      rows.push(row);
      if (rows.length >= TARGET) break;
    }
  } catch (e) {
    console.log(`  ${c.matched_name}: ERROR ${e.message}`);
    continue;
  }
  perCompany.push({ company: c.matched_name, raw, inState });
  console.log(`  ${c.matched_name.padEnd(38).slice(0, 38)} ${String(raw).padStart(3)} pulled  ${String(inState).padStart(3)} in-state`);
}

const rawTotal = perCompany.reduce((s, r) => s + r.raw, 0);
console.log(`\n  pulled nationwide : ${rawTotal}`);
console.log(`  in target states  : ${rows.length}  (${(100 * rows.length / Math.max(1, rawTotal)).toFixed(0)}%)`);

// ---- email enrichment ------------------------------------------------------
console.log(`\nEnriching ${rows.length} profiles for work email...`);
let found = 0;
const POOL = 5;
let cursor = 0;
await Promise.all(Array.from({ length: POOL }, async () => {
  while (cursor < rows.length) {
    const r = rows[cursor++];
    try {
      const resp = await blitz.enrichment.email(r.linkedin_url);
      const e = resp?.email || resp?.data?.email ||
        (Array.isArray(resp?.all_emails) ? resp.all_emails[0] : "") || "";
      r.email = typeof e === "string" ? e : (e?.email || "");
      if (r.email) found++;
    } catch { /* a miss is a normal outcome, not an error */ }
  }
}));

fs.writeFileSync(OUT, toCSV(rows));
console.log(`  emails found      : ${found}/${rows.length}  (${(100 * found / Math.max(1, rows.length)).toFixed(0)}%)`);
console.log(`\n  -> ${OUT}`);
