from bot.client import BinanceFuturesClient
import logging

logger = logging.getLogger(__name__)

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(f"Placing MARKET order: {symbol} {side} {quantity}")
            
            response = self.client.place_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Response: {response}")
            return response

        except Exception as e:
            logger.error(f"Market order failed: {e}")
            raise


    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")
            
            response = self.client.place_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"Response: {response}")
            return response

        except Exception as e:
            logger.error(f"Limit order failed: {e}")
            raise