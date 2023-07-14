# -*- utf-8 -*-

import logging
import time

from binance.websocket.um_futures.websocket_client import \
    UMFuturesWebsocketClient
from db.db import B_DB
from future_api_base import WBClientBase
# 获取交易规则和交易对
#/root/anaconda3/lib/python3.9/site-packages/binance/websocket/
logging.basicConfig(level = logging.INFO,format = '%(asctime)s -%(filename)s- line:%(lineno)d - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


symbols = ['btcusdt', 'ethusdt',"bnbusdt", "fitusdt"]

# symbols = ["bnbusdt"]


class WBClient(WBClientBase):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.mark_corn = []
        self.depth_corn = []
        self.kline_corn = []
        self.ticker_corn = []
        self.order_corn = []

    def register(self):
        # 根据返回类型, 调用不同处理函数
        return {
            "kline": self.kline_message_handler,
            "24hrTicker": self.all_ticker_handler,
            "depthUpdate": self.depth_message_handler,
            "bookTicker": self.all_book_ticker_handler,  
        }

    # 整体订阅
    # def all_mark_price(self):
    #     # 全市场mini ticker，最新成交价
    #     return ["!miniTicker@arr"]
    
    def all_book_ticker(self):
        # 全市场最优挂单
        return ["!bookTicker"]
    
    def all_ticker(self):
        # 全市场完成交易ticker
        return ["!ticker@arr"]
    
        
    def all_mark_price(self):
        # 全市场最新标记价格
        return ["!markPrice@arr@1s"]
    
    
    def all_force_order(self):
        # 全市场强平订单
        return ["!forceOrder@arr"]

    # 按symbol订阅
    # def sub_mark_price(self,speed=1):
    #     #  订阅最新标记价格
    #     return ["{}@markPrice@{}s".format(symbol.lower(), speed) for symbol in self.symbols]
    
    def sub_kline(self):
        # 订阅kline
        return ["{}@kline_{}".format(symbol.lower(), "1m") for symbol in self.symbols]
    
    
    def sub_depth(self,level=10,speed=500):
        #  订阅有限档深度
        return ["{}@depth{}@{}ms".format(symbol.lower(), level, speed) for symbol in self.symbols]

    
    # def all_marker_handler(self, message):
    #     self.mark_corn.append(message)
    #     if len(self.mark_corn) <20:
    #         return 
    #     logger.info("insert mark message")
    #     B_DB.all_marker_1s.insert_many(self.mark_corn)
    #     self.mark_corn = []
        
    def all_mark_handler(self, message):
        # 最新标记
        self.mark_corn.append(message)
        if len(self.mark_corn) <20:
            return 
        logger.info("insert mark message")
        B_DB.all_mark_1s.insert_many(self.mark_corn)
        self.mark_corn = []

    def all_ticker_handler(self, message):
        # 24小时完整ticker
        self.ticker_corn.append(message)
        if len(self.ticker_corn) <20:
            return 
        logger.info("insert ticker message")
        B_DB.all_ticker_1s.insert_many(self.ticker_corn)
        self.ticker_corn = []
        
    def all_book_ticker_handler(self, message):
        # 最优单
        self.order_corn.append(message)
        if len(self.order_corn) <20:
            return 
        logger.info("insert order message")
        B_DB.all_order_24h.insert_many(self.order_corn)
        self.order_corn = []


    def kline_message_handler(self, message):
        # k线入库
        self.kline_corn.append(message["k"])
        if len(self.kline_corn) <500:
            return 
        logger.info("insert kline message")
        B_DB.kline_1m.insert_many(self.kline_corn)
        self.kline_corn = []
        
    def depth_message_handler(self, message):
        # 深度信息,入库
        self.depth_corn.append(message)
        if len(self.depth_corn) < 500:
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
