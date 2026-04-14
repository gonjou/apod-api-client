import unittest
from unittest.mock import patch, MagicMock
from apod.client import APODClient

class TestAPODClient(unittest.TestCase):

    def setUp(self):
        self.client = APODClient()

    @patch('apod.client.requests.Session.get')
    def test_get_today(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "title": "The Long Wispy Tail of Comet R3 (PanSTARRS)",
            "date": "2026-04-14",
            "url": "https://apod.nasa.gov/apod/image/2604/CometR3_Hamdi_960.jpg",
            "explanation": "Short explanation."
            }
        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = self.client.get_today()

        self.assertIsInstance(result, dict)
        self.assertEqual(result["date"], "2026-04-14")
        self.assertIn("title", result)