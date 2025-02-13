from utils.request_utils import get

def get_finance_info(api_key):
    """
    Calls the finance info endpoint.
    Returns the full JSON response.
    """
    return get("api/v2/finance/info", api_key)