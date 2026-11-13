"""Load restaurants.json and report data-quality problems."""
import json
from pathlib import Path

REQUIRED = ["code", "URL", "address", "name", "rating", "type_of_food"]

data = json.loads(Path(__file__).with_name("data").joinpath("restaurants.json").read_text(encoding="utf-8"))

for r in data:
    missing = [k for k in REQUIRED if k not in r]
    if missing:
        print(f"#{r['code']}: missing {missing}")
    if not 0 <= r.get("rating", 0) <= 5:
        print(f"#{r['code']}: rating out of 0-5 range ({r['rating']})")
    if "postcode" in r and not isinstance(r["postcode"], str):
        print(f"#{r['code']}: postcode should be a string ({r['postcode']!r})")
print(f"{len(data)} restaurants checked")
