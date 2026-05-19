def validate_order(order_type, price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT orders require --price")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")