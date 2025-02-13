from utils.request_utils import get

def get_current_vwap(api_key, crypto_symbol="BTC", fiat_symbol="USD", interval="ONE_MINUTE"):
    """
    Fetch the current VWAP data using provided parameters.
    
    Parameters:
      crypto_symbol (str): e.g. "BTC"
      fiat_symbol (str): e.g. "USD"
      interval (str): Time interval, e.g. "1m", "5m", "15m", etc.
      
    Returns:
      Response object from the backend.
    """
    params = {
        "cryptoSymbol": crypto_symbol,
        "fiatSymbol": fiat_symbol,
        "interval": interval
    }
    return get("api/v2/vwap/current", api_key, params=params)

def get_vwap_history(api_key, crypto_symbol="BTC", fiat_symbol="USD", start_date=None, end_date=None, interval="ONE_MINUTE", page=0, size=10):
    """
    Fetch historical VWAP data within a given time range.
    
    Parameters:
      crypto_symbol (str): e.g. "BTC"
      fiat_symbol (str): e.g. "USD"
      start_date (datetime or str): Start date/time (ISO formatted if string).
      end_date (datetime or str): End date/time (ISO formatted if string).
      interval (str): Time interval, e.g. "1m", "5m", "15m", etc.
      page (int): Page number for pagination (0-indexed).
      size (int): Number of items per page.
      
    Returns:
      Response object from the backend.
    """
    # If start_date and end_date are datetime objects, convert to ISO format.
    if start_date is not None and hasattr(start_date, "isoformat"):
        start_date = start_date.isoformat()
    if end_date is not None and hasattr(end_date, "isoformat"):
        end_date = end_date.isoformat()
    
    params = {
        "cryptoSymbol": crypto_symbol,
        "fiatSymbol": fiat_symbol,
        "startDate": start_date,
        "endDate": end_date,
        "interval": interval,
        "page": page,
        "size": size
    }
    return get("api/v2/vwap/history", api_key, params=params) 