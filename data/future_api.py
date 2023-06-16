# -*- utf-8 -*-

import logging
import time

from binance.websocket.um_futures.websocket_client import \
    UMFuturesWebsocketClient
from db.db import B_DB

# 获取交易规则和交易对
#/root/anaconda3/lib/python3.9/site-packages/binance/websocket/
logging.basicConfig(level = logging.INFO,format = '%(asctime)s -%(filename)s- line:%(lineno)d - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


symbols = ['btcusdt', 'ethusdt',"bnbusdt", "fitusdt"]

# symbols = ["bnbusdt"]


class WBClient():
    def __init__(self) -> None:
        self.ws_client = UMFuturesWebsocketClient()
        #self.ws_client = UMFuturesWebsocketClient(stream_url="wss://dstream.binance122.com")
        self.symbols = self.get_symbols()
        
        self.mark_corn = []
        self.depth_corn = []
        self.dead = False
      
       
        
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

    def get_symbols(self):
        # todo 
        return symbols  

    def sublive_subscribe(self, stream:list, **kwargs):
        self.ws_client.live_subscribe(stream, int(time.time()), self.message_handler, **kwargs)

    def message_handler(self, message):
      
        logger.debug(message)
        if message is not None:
            if message.get("data"):
                message = message.get("data")
            if message.get("e"):
                try:
                    self.register()[message['e']](message)
                except KeyError:
                    logger.error("keyErr")
                    self.dead = True
                    self.close()

    def register(self ):
        # 根据返回类型, 调用不同处理函数
        return {
            "kline": self.kline_message_handler,
            "markPriceUpdate": self.mark_message_handler,
            "depthUpdate": self.depth_message_handler,
        }

    # def get_dead(self):
    #     return self.dead
    def sub_kline(self):
        # 订阅kline
        return ["{}@kline_{}".format(symbol.lower(), "1m") for symbol in self.symbols]

    def sub_mark_price(self,speed=1):
        #  订阅最新标记价格
        return ["{}@markPrice@{}s".format(symbol.lower(), speed) for symbol in self.symbols]
    
    # def sub_all_mark_price(self,speed=1):
    #     #  订阅最新标记价格
    #     return ["{}@markPrice@{}s".format(symbol.lower(), speed) for symbol in self.symbols]

    def sub_depth(self,level=10,speed=500):
        #  订阅有限档深度
        return ["{}@depth{}@{}ms".format(symbol.lower(), level, speed) for symbol in self.symbols]

    def kline_message_handler(self, message):
        # k线完结,入库
        if message["k"]["x"]:
            B_DB.kline_1m.insert_one(message["k"])
    
    def mark_message_handler(self, message):
        # 最新标记价格,入库
        self.mark_corn.append(message)
        if len(self.mark_corn) <60:
            return 
        logger.info("insert mark message")
        B_DB.mark_1s.insert_many(self.mark_corn)
        self.mark_corn = []

    def depth_message_handler(self, message):
        # 深度信息,入库
        self.depth_corn.append(message)
        if len(self.depth_corn) < 60:
            return 
        
        B_DB.depth_500ms.insert_many(self.depth_corn)
        self.depth_corn = []

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
