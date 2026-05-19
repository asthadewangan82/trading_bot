import argparse
from bot.orders import OrderService
from bot.validators import validate_order, validate_side
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        # ✅ Validation
        validate_side(args.side)
        validate_order(args.type, args.price)

        service = OrderService()

        # ✅ Print Request
        print("\n=== ORDER REQUEST ===")
        print(vars(args))

        # ✅ Place Order
        if args.type.upper() == "MARKET":
            response = service.place_market_order(
                args.symbol, args.side, args.quantity
            )
        else:
            response = service.place_limit_order(
                args.symbol, args.side, args.quantity, args.price
            )

        # ✅ FULL RESPONSE (important fix)
        print("\n=== FULL RESPONSE ===")
        print(response)

        # ✅ Clean Output
        print("\n=== ORDER RESPONSE ===")
        print({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice") or response.get("price")
        })

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()