import requests
from . import config


class APODClient:
    # Initialize url, api_key and timeout instance variables.
    def __init__(self, base_url=config.BASE_URL, api_key=config.API_KEY, timeout=config.TIMEOUT):

        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout

        self.session = requests.Session() # Creating a session.

    # Send request.
    def _get(self, params):
        
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
        

