import unittest
from unittest.mock import Mock, patch
from apod.main import _validate_date, _validate_count, _process_arguments
from apod.client import APODClient

class TestMainValidation(unittest.TestCase):

    def test_validate_date_yyyymmdd_validation(self):
        with self.assertRaises(ValueError):
            _validate_date("June 16, 1995")
    
    def test_validate_date_rejects_old_dates(self):
        with self.assertRaises(ValueError):
            _validate_date("1800-06-16")

    def test_validate_date_rejects_future_dates(self):
        with self.assertRaises(ValueError):
            _validate_date("3000-06-19")

    def test_validate_date_accepts_valid_date(self):
        result = _validate_date("2026-04-16")
        self.assertEqual(result, "2026-04-16")

    def test_validate_count_rejects_non_integers(self):
        with self.assertRaises(ValueError):
            _validate_count("lol")

    def test_validate_count_rejects_count_under_0(self):
        with self.assertRaises(ValueError):
            _validate_count("-1")

    def test_validate_count_rejects_count_over_10(self):
        with self.assertRaises(ValueError):
            _validate_count("15")

    def test_validate_count_accepts_valid_count(self):
        result = _validate_count("5")
        self.assertEqual(result, 5)

    def test_process_arguments_rejects_over_3_args(self):
        with self.assertRaises(ValueError):
            client = APODClient()
            _process_arguments(client, ["apod.main", "get_by_date", "2000-08-08", "another_argument"])

    def test_process_rejects_2_args(self):
        with self.assertRaises(ValueError):
            client = APODClient()
            _process_arguments(client, [ "apod.main", "get_random"])
    
    def test_process_accepts_valid_arguments(self):
        client = Mock(spec=APODClient)
        client.get_by_date.return_value = {
            "title": "Test Example",
            "date": "2000-08-08"
        }

        result = _process_arguments(client, ["apod.main", "get_by_date", "2000-08-08"])

        client.get_by_date.assert_called_once_with("2000-08-08")
        self.assertIsInstance(result, str)

    

