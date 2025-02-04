from utils.request_utils import get

def get_current_vwap():
    """Fetch the current VWAP data."""
    return get("api/v2/vwap/current")

def get_vwap_history(params=None):
    """
    Fetch historical VWAP data. Accepts optional query parameters.
    
    params: dict of filters if needed.
    """
    return get("api/v2/vwap/history", params=params) 