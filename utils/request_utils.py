import requests
from utils.config import API_KEY, BASE_URL

def get(endpoint, params=None):
    """Make a GET request to the given endpoint."""
    url = f"{BASE_URL}/{endpoint}"
    headers = {"X-API-Key": API_KEY}
    return requests.get(url, params=params, headers=headers)

def post(endpoint, data=None, json=None):
    """Make a POST request to the given endpoint."""
    url = f"{BASE_URL}/{endpoint}"
    headers = {"X-API-Key": API_KEY}
    return requests.post(url, data=data, json=json, headers=headers) 