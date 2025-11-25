# tests/test_rules.py
import unittest
from src.rules import study_suggestion

class TestStudySuggestion(unittest.TestCase):
    def test_short_low(self):
        self.assertEqual(study_suggestion("short","low"), "Do 1 review question")

    def test_long_high(self):
        self.assertIn("tiny CLI feature", study_suggestion("long","high"))

    def test_default_missing_input(self):
        self.assertIn("Pick a small", study_suggestion("", "high"))

    def test_case_insensitive(self):
        self.assertEqual(study_suggestion("SHORT", "HIGH"),
                         "Watch a 5-min concept video")

if __name__ == "__main__":
    unittest.main()
