import unittest
from apod.formatter import format_apod, format_single_apod

class TestFormatter(unittest.TestCase):

    def test_format_single_apod(self):
        data = {
            "title": "Test Example",
            "date": "2026-04-18",
            "url": "example url",
            "explanation": "Image explanation"
        }

        result = format_single_apod(data)

        self.assertIsInstance(result, str)
        self.assertIn("Test Example", result)
        self.assertIn("2026-04-18", result)
        self.assertIn("example url", result)
        self.assertIn("Image explanation", result)

    def test_format_apod(self):
        data = [
            {"title": "Image 1", "date": "1995-06-16", "url": "some url", "explanation": "example explanation"},
            {"title": "Image 2", "date": "2026-03-04", "url": "very nice url", "explanation": "second example explanation"}
        ]

        result = format_apod(data)

        self.assertIsInstance(result, str)
        self.assertIn("Image 1", result)
        self.assertIn("Image 2", result)
        self.assertIn("---", result)