# RESTFUL APIS
import os 

from binance.cm_futures import CMFutures

cm_futures_client = CMFutures()

# get server time
print(cm_futures_client.time())

cm_futures_client = CMFutures(key=os.getenv("bn_key"), secret=os.getenv("bn_secret"), timeout=15)

# Get account information
print(cm_futures_client.account())

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 59808
}

# response = cm_futures_client.new_order(**params)
# print(response)



if __name__ == "__main__":
    # websocket
    import time
    import logging
    from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
    logger = logging.getLogger(__name__)


    def message_handler(message):
        print(111)
        print(message)

    ws_client = UMFuturesWebsocketClient()
    ws_client.start()

    ws_client.mini_ticker(
        symbol='bnbusdt',
        id=1,
        callback=message_handler,
    )

    # Combine selected streams
    ws_client.instant_subscribe(
        stream=['bnbusdt@bookTicker', 'ethusdt@bookTicker'],
        callback=message_handler,
    )

    time.sleep(10)

    print("closing ws connection")
    ws_client.stop()