#!/usr/bin/env python3
"""Folkline UI Search — Search utility classes and components by keyword"""
import csv
import sys
import os
import json
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_DIR / "data"

def load_csv(filename):
    rows = []
    filepath = DATA_DIR / filename
    if not filepath.exists():
        return rows
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def search(rows, query, fields=None):
    q = query.lower()
    results = []
    for row in rows:
        score = 0
        searchable = {k.lower(): str(v).lower() for k, v in row.items()}
        if fields:
            searchable = {k: searchable.get(k.lower(), "") for k in fields}
        for val in searchable.values():
            if q in val:
                score += 1
            if val == q:
                score += 5
            if val.startswith(q):
                score += 3
        if score > 0:
            results.append((score, row))
    results.sort(key=lambda x: -x[0])
    return [r[1] for r in results]

def main():
    if len(sys.argv) < 2:
        print("Usage: python search.py <query> [--type utilities|components|tokens|all]")
        print("       python search.py --types")
        print("       python search.py --stats")
        return

    if sys.argv[1] == "--types":
        print("Available types: utilities, components, tokens")
        return

    if sys.argv[1] == "--stats":
        print(json.dumps({
            "utilities": len(load_csv("utilities.csv")),
            "components": len(load_csv("components.csv")),
            "tokens": len(load_csv("design-tokens.csv")),
        }, indent=2))
        return

    query = sys.argv[1]
    filter_type = "all"
    if "--type" in sys.argv:
        idx = sys.argv.index("--type")
        if idx + 1 < len(sys.argv):
            filter_type = sys.argv[idx + 1]

    datasets = {
        "utilities": ("utilities.csv", ["class", "type", "description", "example"]),
        "components": ("components.csv", ["component", "selector", "description"]),
        "tokens": ("design-tokens.csv", ["token", "value", "description"]),
    }

    results = {}
    for name, (filename, fields) in datasets.items():
        if filter_type != "all" and filter_type != name:
            continue
        rows = load_csv(filename)
        found = search(rows, query, fields)
        if found:
            results[name] = found

    output = {"query": query, "type": filter_type, "results": results}
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
