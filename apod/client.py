import requests
from . import config


class APODClient:
    """
    Client that fetchs NASA's Astronomical Picture of the Day.
    It handles requests with automatic session management and error handling.

    """

    def __init__(self, base_url=config.BASE_URL, api_key=config.API_KEY, timeout=config.TIMEOUT):
        """
        Initialize APODClient.

        Args:
        base_url = url of the APOD website
        api_key = your API key gotten from your environment variable "NASA_API_KEY"
        timeout = Request timeout in secs. Default is set to 10

        """

        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout

        """Creating a session"""
        self.session = requests.Session() 

    def _get(self, params):
        """Sends request. 

        Args:
        params = query parameters, such as {"date": "2026-04-16"}

        Returns:
        Parsed JSON response from the API

        Raises:

        """
        
        params = params.copy()
        params["api_key"] = self.api_key

        try:
            response = self.session.get(self.base_url, params=params, timeout=self.timeout)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise Exception("An HTTP Error occurred.") from http_err
        except requests.exceptions.RequestException as err:
            raise Exception("A request exception occurred.") from err
        else:
            return response.json()
        
    # Get today's picture.
    def get_today(self):
        return self._get({})

    # Get picture by date.
    def get_by_date(self, date):
        return self._get({"date": date})

    # Get random.
    def get_random(self, count):
        return self._get({"count": count})
        

