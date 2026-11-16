# timetable.csv column dictionary

| Column | Meaning | Example |
|---|---|---|
| batch | Programme-Section-Year. Exact match only. | CSE-A-Y2 |
| day | Three-letter weekday, Mon-Sat | Mon |
| start / end | 24-hour HH:MM. A 2-hour lab has end = start + 2h | 09:00 / 11:00 |
| course_code | Unique per course | CS201 |
| course_name | Human-readable name | Data Structures |
| room | Room or lab id | LH-101 |
| faculty | Instructor | Dr. Rao |

Known batches: CSE-A-Y2, CSE-B-Y2, ECE-A-Y2. Anything else is unknown.
