import os

BASE_URL = "https://api.nasa.gov/planetary/apod"

API_KEY = os.getenv("NASA_API_KEY")

TIMEOUT = 10

DEFAULT_COUNT = 1