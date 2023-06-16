# -*- utf-8 -*-

import time

from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
# 获取交易规则和交易对

symbols = ["maskusdt"]



class WBClient():
    def __init__(self) -> None:
        self.ws_client = UMFuturesWebsocketClient()
        self.symbols = self.get_symbols()
        # self.start()
        self.mark_corn = []

    def reconnect(self):
        # 重连,直到连上为止
        while True:
            print(time.time(), 'reconnect')
            self.close()
            try:
                self.ws_client = UMFuturesWebsocketClient()
                self.start()
                break
            except Exception as e:
                print(e)
                self.close()
                time.sleep(3)

    def reset(self):
        self.reconnect()
        
    def start(self):
        self.ws_client.start()

    def close(self):
        self.ws_client.close()

    def get_symbols(self):
        # todo 
        return symbols  

    def sublive_subscribe(self, stream:list, **kwargs):
        self.ws_client.live_subscribe(stream, int(time.time()), self.message_handler, **kwargs)

    def message_handler(self, message):
        if message is not None:
            if message.get("data"):
                message = message.get("data")
            if message.get("e"):
                try:
                    self.register()[message['e']](message)
                except KeyError:
                    self.reconnect()
     

    def register(self ):
        # 根据返回类型, 调用不同处理函数
        return {
            "kline": self.kline_message_handler,
            "markPriceUpdate": self.mark_message_handler,
            "depthUpdate": self.depth_message_handler,
        }

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
            print(message["k"])
           
    
    def mark_message_handler(self, message):
        # 最新标记价格,入库
       
        print(message.get("p"))
        # if len(self.mark_corn) <60:
        #     self.mark_corn.append(message)
        #     return 
        # print("insert mark")
        # B_DB.mark_1s.insert_many(self.mark_corn)
        # self.mark_corn = []

    def depth_message_handler(self, message):
        # 深度信息,入库
        print(message)
     

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
    wb = WBClient()
    wb.start()
    sub_info = wb.sub_mark_price()
    # sub_info.extend(wb.sub_depth())
    # sub_info.extend(wb.sub_mark_price)
    wb.sublive_subscribe(sub_info)
    wb.close()

