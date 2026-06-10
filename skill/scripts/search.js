#!/usr/bin/env node
/**
 * Folkline UI Search — Search utilities and components by keyword
 */
const fs = require("fs");
const path = require("path");

const DATA_DIR = path.join(__dirname, "..", "data");

function loadCSV(filename) {
  const filepath = path.join(DATA_DIR, filename);
  if (!fs.existsSync(filepath)) return [];
  const text = fs.readFileSync(filepath, "utf-8").trim();
  const lines = text.split("\n");
  const headers = lines[0].split(",").map((h) => h.trim());
  return lines.slice(1).map((line) => {
    const vals = line.split(",").map((v) => v.trim().replace(/^"(.*)"$/, "$1"));
    const obj = {};
    headers.forEach((h, i) => (obj[h] = vals[i] || ""));
    return obj;
  });
}

function search(rows, query, fields) {
  const q = query.toLowerCase();
  const scored = rows.map((row) => {
    let score = 0;
    for (const [key, val] of Object.entries(row)) {
      const v = String(val).toLowerCase();
      if (fields && !fields.includes(key)) continue;
      if (v.includes(q)) score += 1;
      if (v === q) score += 5;
      if (v.startsWith(q)) score += 3;
    }
    return { score, row };
  });
  return scored
    .filter((s) => s.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((s) => s.row);
}

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log("Usage: node search.js <query> [--type utilities|components|tokens|all]");
  console.log("       node search.js --types");
  console.log("       node search.js --stats");
  process.exit(0);
}

if (args[0] === "--types") {
  console.log("Available types: utilities, components, tokens");
  process.exit(0);
}

if (args[0] === "--stats") {
  console.log(
    JSON.stringify(
      {
        utilities: loadCSV("utilities.csv").length,
        components: loadCSV("components.csv").length,
        tokens: loadCSV("design-tokens.csv").length,
      },
      null,
      2
    )
  );
  process.exit(0);
}

const query = args[0];
const typeIdx = args.indexOf("--type");
const filterType = typeIdx !== -1 && args[typeIdx + 1] ? args[typeIdx + 1] : "all";

const datasets = {
  utilities: { file: "utilities.csv", fields: ["class", "type", "description", "example"] },
  components: { file: "components.csv", fields: ["component", "selector", "description"] },
  tokens: { file: "design-tokens.csv", fields: ["token", "value", "description"] },
};

const results = {};
for (const [name, { file, fields }] of Object.entries(datasets)) {
  if (filterType !== "all" && filterType !== name) continue;
  const found = search(loadCSV(file), query, fields);
  if (found.length) results[name] = found;
}

console.log(JSON.stringify({ query, type: filterType, results }, null, 2));
