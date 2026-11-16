#!/usr/bin/env python3
"""Look up classes in data/timetable.csv. Prints rows, or NO_MATCH / UNKNOWN_BATCH.
Usage: query_timetable.py --batch CSE-A-Y2 --day Mon
"""
import argparse
import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "timetable.csv"
DAYS = {"mon", "tue", "wed", "thu", "fri", "sat"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    ap.add_argument("--day", required=True)
    a = ap.parse_args()

    day = a.day.strip()[:3].capitalize()
    if day.lower() not in DAYS:
        print(f"INVALID_DAY: {a.day!r}")
        return 2
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    batches = {r["batch"] for r in rows}
    if a.batch not in batches:
        print(f"UNKNOWN_BATCH: {a.batch!r}. Known batches: {', '.join(sorted(batches))}")
        return 1
    hits = [r for r in rows if r["batch"] == a.batch and r["day"] == day]
    if not hits:
        print("NO_MATCH")
        return 0
    for r in sorted(hits, key=lambda r: r["start"]):
        print(f'{r["start"]}-{r["end"]} | {r["course_code"]} {r["course_name"]} | {r["room"]} | {r["faculty"]}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
