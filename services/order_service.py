from utils.request_utils import post, get

def place_order(order_data, api_key):
    """
    Place an order (buy or sell) using the backend API.
    
    order_data: dict e.g., {"type": "buy"|"sell", "symbol": "BTC-USD", "amount": 1, "price": 50000}
    """
    return post("api/v2/orderbook/place", api_key, json=order_data)

def get_sell_orders_foreign(api_key, params=None):
    """Retrieve current sell orders."""
    return get("api/v2/orderbook/sells/foreign", api_key, params)

def get_buy_orders_foreign(api_key, params=None):
    """Retrieve current buy orders."""
    return get("api/v2/orderbook/buys/foreign", api_key, params)

def get_sell_orders(api_key, params=None):
    """Retrieve current sell orders."""
    return get("api/v2/orderbook/sells", api_key, params)

def get_buy_orders(api_key, params=None):
    """Retrieve current buy orders."""
    return get("api/v2/orderbook/buys", api_key, params) 