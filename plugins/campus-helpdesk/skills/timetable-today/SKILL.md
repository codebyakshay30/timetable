---
name: timetable-today
description: Show today's classes for a batch. Run as /campus-helpdesk:timetable-today <batch> <day>.
disable-model-invocation: true
---

Show the timetable for the batch and day in `$ARGUMENTS` (format: `<batch> <day>`, e.g. `CSE-A-Y2 Mon`).

1. Run `python3 "${CLAUDE_SKILL_DIR}/../timetable-helper/scripts/query_timetable.py" --batch <batch> --day <day>`.
2. Print the result as a small table. If the script prints `NO_MATCH`, say exactly that no classes were found. Never invent a class.
