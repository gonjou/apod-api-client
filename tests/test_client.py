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

    @patch('apod.client.requests.Session.get')
    def test_get_by_date(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "title": "The Path of Artemis II",
            "date": "2026-04-06",
            "url": "https://apod.nasa.gov/apod/image/2604/moonGamera_velHighRes_3-3-2026c_artemisII_wind_1080p30_2.mp4",
            "explanation": "Artemis II is primarily a test mission designed to make a future Artemis missions."
        }

        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = self.client.get_by_date("2026-04-06")

        self.assertEqual(result["date"], "2026-04-06")
        self.assertIsInstance(result, dict)

    @patch('apod.client.requests.Session.get')
    def test_get_random(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"title": "Neutron Star Earth", "date": "1995-06-16"},
            {"title": "Pillars of Creation", "date": "2022-10-20"},
        ]

        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = self.client.get_random(2)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        