"""Pure data logic (no MCP imports) so it can be unit-tested with the stdlib only."""
import csv
import json
import re
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
VALID_DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
STUDENT_ID_RE = re.compile(r"^S\d{4}$")


def _timetable() -> list[dict]:
    with (DATA / "timetable.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def timetable_for(batch: str, day: str) -> list[dict]:
    day = day.strip()[:3].capitalize()
    if day not in VALID_DAYS:
        raise ValueError(f"day must be one of {', '.join(VALID_DAYS)}; got {day!r}")
    rows = _timetable()
    known = sorted({r["batch"] for r in rows})
    if batch not in known:
        raise ValueError(f"unknown batch {batch!r}; known batches: {', '.join(known)}")
    return [r for r in rows if r["batch"] == batch and r["day"] == day]


def fee_status(student_id: str) -> dict:
    if not STUDENT_ID_RE.match(student_id):
        raise ValueError("student_id must look like S1001 (letter S + 4 digits)")
    records = json.loads((DATA / "fees.json").read_text(encoding="utf-8"))
    if student_id not in records:
        raise ValueError(f"no record for student_id {student_id!r}")
    r = records[student_id]
    return {"student_id": student_id, "total": r["total"], "paid": r["paid"],
            "balance": r["total"] - r["paid"], "due_date": r["due_date"],
            "status": "PAID" if r["paid"] >= r["total"] else "PENDING"}


def hostel_rules() -> str:
    return (DATA / "hostel_rules.md").read_text(encoding="utf-8")
