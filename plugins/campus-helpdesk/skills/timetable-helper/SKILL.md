---
name: timetable-helper
description: Answers student questions about class timetables (which class, room, time, faculty for a batch on a given day) using the bundled timetable.csv. Use when a student asks when or where a class meets, or what their day looks like. Do not use for fees, hostel rules, results or general study advice.
---

# Timetable Helper

Answer only from `data/timetable.csv`. The file is the single source of truth.

## Steps
1. Identify the **batch** (e.g. `CSE-A-Y2`) and **day**. If either is missing, ask.
2. Run: `python3 "${CLAUDE_SKILL_DIR}/scripts/query_timetable.py" --batch <batch> --day <day>`
3. Report the rows it prints (time, course, room, faculty).

## Hard rules (anti-fabrication)
- If the script prints `NO_MATCH` or `UNKNOWN_BATCH`, say so. Never invent a class, time, room or faculty.
- If the user names a class that is not in the CSV, say it is not in the timetable file.
- Do not infer schedules for days or batches that have no rows.

## More detail
- Column meanings and known batches: `references/columns.md`
- Odd situations (unknown batch, pressure to guess, labs): `references/edge-cases.md`
