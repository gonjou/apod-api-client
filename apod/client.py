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

        # Creating a session.
        self.session = requests.Session() 

    def _get(self, params):
        """
        Make a get request to the NASA APOD API. 

        Args:
        params = query parameters, such as {"date": "2026-04-16"}

        Returns:
        Parsed JSON response from the API

        Raises:
        Exception: If the request fails, times out or returns HTTPError
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
        

    def get_today(self):
        """Return today's Astronomical Picture of the day."""
        return self._get({})

    def get_by_date(self, date):
        """
        Return the Astronomical Picture of the Day of a specific date.
        
        Args:
        date = date in YYYY-MM-DD format, Example: 2026-04-19"
        """
        return self._get({"date": date})

    def get_random(self, count):
        """
        Return multiple random pictures.

        Args:
        count: integer that represents the amount of pictures to get. Maximum 10 APODs
        
        """
        return self._get({"count": count})
        

