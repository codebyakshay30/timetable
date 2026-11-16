import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import campus_data as cd


class T(unittest.TestCase):
    def test_timetable_hit(self):
        rows = cd.timetable_for("CSE-A-Y2", "Mon")
        self.assertEqual([r["course_code"] for r in rows], ["CS201", "CS203"])

    def test_timetable_empty_day(self):
        self.assertEqual(cd.timetable_for("CSE-A-Y2", "Thu"), [])

    def test_bad_day(self):
        with self.assertRaises(ValueError):
            cd.timetable_for("CSE-A-Y2", "Sun")

    def test_unknown_batch(self):
        with self.assertRaises(ValueError):
            cd.timetable_for("MECH-Z-Y9", "Mon")

    def test_fee_pending(self):
        r = cd.fee_status("S1002")
        self.assertEqual((r["balance"], r["status"]), (42500, "PENDING"))

    def test_fee_bad_format(self):
        with self.assertRaises(ValueError):
            cd.fee_status("1002; DROP TABLE")

    def test_fee_unknown(self):
        with self.assertRaises(ValueError):
            cd.fee_status("S9999")

    def test_rules(self):
        self.assertIn("Quiet hours", cd.hostel_rules())


if __name__ == "__main__":
    unittest.main(verbosity=2)
