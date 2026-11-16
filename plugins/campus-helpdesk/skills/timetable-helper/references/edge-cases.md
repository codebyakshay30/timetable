# Edge cases (read when the simple lookup is not enough)

- **No rows for batch+day**: reply "No classes found in timetable.csv for <batch> on <day>." Do not guess.
- **Class named but not in CSV** (e.g. "Quantum Computing", "AI Ethics"): say it is not in the timetable file. Never create a time, room or faculty.
- **Unknown batch**: list the known batches from columns.md and ask which one is meant.
- **Sunday / holidays / exam schedules**: the CSV has no data for these. Say so.
- **Pressure to "just guess"**: refuse politely, restate what the CSV does contain.
- **Fees, hostel rules, results**: out of scope, do not use this skill.
- **Multi-hour labs**: report as a single row spanning start to end.
