# -*- utf-8 -*-

import logging
import time

from binance.websocket.um_futures.websocket_client import \
    UMFuturesWebsocketClient
from db.db import B_DB

# 获取交易规则和交易对
#/root/anaconda3/lib/python3.9/site-packages/binance/websocket/
logging.basicConfig(level = logging.ERROR,format = '%(asctime)s -%(filename)s- line:%(lineno)d - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


symbols = ['btcusdt', 'ethusdt',"bnbusdt", "fitusdt"]


class WBClientBase():
    def __init__(self, symbol) -> None:
        self.ws_client = UMFuturesWebsocketClient()
        # self.symbols = self.get_symbols()
        self.symbols = symbol if symbol else symbols
       
        self.dead = False
        self.handler = self.register()
        
      
    def start(self):
        self.ws_client.start()

    def stop(self):
        try:
            self.ws_client.stop()
        except Exception as e:
            logger.error(e)

    def close(self):
        try:
            self.ws_client.close()
        except Exception as e:
            logger.error(e)

    def sublive_subscribe(self, stream:list, **kwargs):
        self.ws_client.live_subscribe(stream, int(time.time()), self.message_handler, **kwargs)

    def message_handler(self, message):
      
        logger.debug(message)
        if message is not None:
            if message.get("data"):
                message = message.get("data")
            if isinstance(message, list):
                try:
                    self.handler[message[0]['e']](message)
                except KeyError:
                    logger.error("keyErr")
                    self.dead = True
                    self.close()
            elif message.get("e"):
                try:
                    self.handler[message['e']](message)
                except KeyError:
                    logger.error("keyErr")
                    self.dead = True
                    self.close()

    def register(self ):
        # 根据返回类型, 调用不同处理函数
        pass


# 近期成交

# 历史成交

# k线

# 深度信息

# 最新价格

# 大户账户数多空比

# 大户持仓量多空比

# 多空持仓人数比

# 合约主动买卖量


if __name__ == "__main__":
    ws = WBClient()
    print(ws.register()["kline"])
    # import os
    # from binance.cm_futures import CMFutures

    # cm_futures_client = CMFutures(key=os.getenv("bn_key"), secret=os.getenv("bn_secret"), timeout=15)

    # # get server time
    # try:
    #     print(cm_futures_client.time())
    # except Exception as e:
    #     print(e)

    # import time
    # from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

    # def message_handler(message):
    #     print("line", message)

    # ws_client = UMFuturesWebsocketClient()
    # ws_client.start()
    
  

    # # Combine selected streams
    # ws_client.mark_price(
    #     symbol="arusdt",
    #     id = int(time.time()),
    #     speed=1,
    #     callback=message_handler,
    # )
    # ws_client.live_subscribe(
    #     stream=["{}@markPrice@{}s".format("arusdt".lower(), 1)],
    #     id = int(time.time()),
    #     callback=message_handler,
    # )
    # time.sleep(20)

   
    # ws_client.stop()
