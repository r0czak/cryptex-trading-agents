import requests
from utils.config import  BASE_URL

def get(endpoint, api_key, params=None):
    """Make a GET request to the given endpoint."""
    url = f"{BASE_URL}/{endpoint}"
    headers = {"X-API-Key": api_key}
    return requests.get(url, params=params, headers=headers)

def post(endpoint, api_key, data=None, json=None):
    """Make a POST request to the given endpoint."""
    url = f"{BASE_URL}/{endpoint}"
    headers = {"X-API-Key": api_key}
    return requests.post(url, data=data, json=json, headers=headers) 