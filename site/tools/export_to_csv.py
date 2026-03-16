import json, csv
from pathlib import Path

data_path = Path("data/jobs.json")
out_path = Path("data/jobs_exposure.csv")

data = json.loads(data_path.read_text(encoding="utf-8"))

fields = [
    "title","slug","category","pay","jobs",
    "outlook","outlook_desc","education",
    "exposure","url"
]

with out_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
