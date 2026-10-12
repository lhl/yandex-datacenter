#!/usr/bin/env python3
"""Check the source ledger and observations for obvious schema errors."""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sources = json.loads((root / "data/sources.json").read_text())
assert sources and all(item.get("id") and item.get("url") for item in sources)
ids = {item["id"] for item in sources}
with (root / "data/observations.csv").open(newline="") as handle:
    rows = list(csv.DictReader(handle))
assert rows and all(row["source_id"] in ids for row in rows)
assert len({item["id"] for item in sources}) == len(sources)
print(f"OK: {len(sources)} sources, {len(rows)} observations")
