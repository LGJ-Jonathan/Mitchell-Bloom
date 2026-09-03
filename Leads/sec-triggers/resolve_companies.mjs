#!/usr/bin/env node
/**
 * Stage 3a — turn EDGAR company names into Blitz/LinkedIn accounts.
 *
 * EDGAR names are filing-registry names, not brand names: "ELECTRONIC ARTS INC.",
 * "Core Scientific, Inc./tx", "Barinthus Biotherapeutics plc.". Blitz matches on
 * the brand, so the legal suffixes have to come off before searching.
 *
 * Every match is written out with the employee count and HQ so a human can spot a
 * wrong match before any people get pulled. A wrong account here poisons everything
 * downstream, so this stage is deliberately reviewable.
 *
 *   node resolve_companies.mjs [--role=target] [--limit=N]
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createClient, readCSVObjects, toCSV } from
  "../../../../../.claude/skills/blitz-api/blitz-client.mjs";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const IN = path.join(HERE, "triggers-classified.csv");
const OUT = path.join(HERE, "triggers-companies.csv");

const arg = (k, d) => (process.argv.find(a => a.startsWith(`--${k}=`)) || `=${d}`).split("=")[1];
const ROLE = arg("role", "target");
const LIMIT = Number(arg("limit", 0));

// Legal-entity noise. Order matters: strip the trailing state code first
// ("/tx", "/DE") because it sits outside the suffix.
const clean = (n) => n
  .replace(/\/[a-z]{2}\/?$/i, "")
  .replace(/[,.]?\s*\b(inc|corp|corporation|co|company|holdings?|group|ltd|limited|plc|lp|llc|nv|sa|ag)\b\.?/gi, "")
  .replace(/\s*&\s*co\.?$/i, "")
  .replace(/[,.]+$/, "")
  .trim();

const blitz = createClient();

// EDGAR reports the registrant. Blitz reports the LinkedIn page, whose employee
// count is the population we can actually reach. Both are worth keeping.
const rows = readCSVObjects(IN).objects.filter(r => r.role === ROLE);
const work = LIMIT ? rows.slice(0, LIMIT) : rows;

console.log(`Resolving ${work.length} ${ROLE} companies to LinkedIn accounts...\n`);

const out = [];
for (const [i, r] of work.entries()) {
  const q = clean(r.company);
  let match = null, candidates = 0;
  try {
    const resp = await blitz.search.companies({ company: { name: { include: [q] } } });
    const items = resp?.results ?? [];
    candidates = items.length;
    // Prefer the largest headcount: the parent account, not a regional subsidiary
    // or a same-name consultancy.
    match = items.sort((a, b) =>
      (b.employees_on_linkedin ?? 0) - (a.employees_on_linkedin ?? 0))[0] || null;
  } catch (e) {
    console.log(`  [${i + 1}/${work.length}] ERROR ${q}: ${e.message}`);
  }

  out.push({
    edgar_name: r.company,
    query: q,
    filed: r.filed,
    confidence: r.confidence,
    close_hint: (r.close_hint || "").slice(0, 180),
    matched_name: match?.name || "",
    company_linkedin_url: match?.linkedin_url || "",
    website: match?.website || "",
    industry: match?.industry || "",
    employees_on_linkedin: match?.employees_on_linkedin ?? "",
    hq_city: match?.hq?.city || "",
    hq_country: match?.hq?.country_code || "",
    candidates,
  });

  const m = match ? `${match.name} (${match.employees_on_linkedin ?? "?"} emp)` : "NO MATCH";
  console.log(`  [${i + 1}/${work.length}] ${q.padEnd(34).slice(0, 34)} -> ${m}`);
}

fs.writeFileSync(OUT, toCSV(out));
const hit = out.filter(r => r.company_linkedin_url).length;
const reach = out.reduce((s, r) => s + (Number(r.employees_on_linkedin) || 0), 0);
console.log(`\n  resolved   : ${hit}/${out.length}`);
console.log(`  total reach: ${reach.toLocaleString()} employees on LinkedIn`);
console.log(`\n  -> ${OUT}`);
