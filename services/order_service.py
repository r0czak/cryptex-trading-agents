from utils.request_utils import post, get

def place_order(order_data):
    """
    Place an order (buy or sell) using the backend API.
    
    order_data: dict e.g., {"type": "buy"|"sell", "symbol": "BTC-USD", "amount": 1, "price": 50000}
    """
    return post("api/v2/orderbook/place", json=order_data)

def get_sell_orders():
    """Retrieve current sell orders."""
    return get("api/v2/orderbook/sells")

def get_buy_orders():
    """Retrieve current buy orders."""
    return get("api/v2/orderbook/buys") 