from binance.api import API


class UMFutures(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://fapi.binance.com"
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from binance.um_futures.market import ping        
    from binance.um_futures.market import time
    from binance.um_futures.market import exchange_info              # 获取交易对信息
    from binance.um_futures.market import depth                      # 深度信息 
    from binance.um_futures.market import trades                     #近期成交 
    from binance.um_futures.market import historical_trades          #查询历史成交(MARKET_DATA) 
    from binance.um_futures.market import agg_trades                 #近期成交(归集)
    from binance.um_futures.market import klines                     # K线数据 
    from binance.um_futures.market import continuous_klines          #连续合约K线数据 
    from binance.um_futures.market import index_price_klines          #价格指数K线数据 
    from binance.um_futures.market import mark_price_klines           #标记价格K线数据
    from binance.um_futures.market import mark_price          #最新标记价格和资金费率
    from binance.um_futures.market import funding_rate          #查询资金费率历史 
    from binance.um_futures.market import ticker_24hr_price_change          # 24hr价格变动情况 
    from binance.um_futures.market import ticker_price          #最新价格 
    from binance.um_futures.market import book_ticker          #当前最优挂单 
    from binance.um_futures.market import open_interest          #获取未平仓合约数
    from binance.um_futures.market import open_interest_hist          #合约持仓量
    from binance.um_futures.market import top_long_short_position_ratio          #大户账户数多空比 
    from binance.um_futures.market import long_short_account_ratio          #大户持仓量多空比
    from binance.um_futures.market import top_long_short_account_ratio          #多空持仓人数比
    from binance.um_futures.market import taker_long_short_ratio          #合约主动买卖量 
    from binance.um_futures.market import blvt_kline          #杠杆代币历史净值K线 
    from binance.um_futures.market import index_info          #综合指数交易对信息 
    from binance.um_futures.market import asset_Index          #多资产模式资产汇率指数 

    # ACCOUNT(including orders and trades)
    from binance.um_futures.account import change_position_mode          #更改持仓模式(TRADE) 
    from binance.um_futures.account import get_position_mode          #查询持仓模式(USER_DATA) 
    from binance.um_futures.account import change_multi_asset_mode          #更改联合保证金模式(TRADE) 
    from binance.um_futures.account import get_multi_asset_mode          #查询联合保证金模式(USER_DATA) 
    from binance.um_futures.account import new_order          #下单 (TRADE) 
    from binance.um_futures.account import new_order_test          #测试下单接口 (TRADE) 
    from binance.um_futures.account import new_batch_order          #批量下单 (TRADE)
    from binance.um_futures.account import query_order          #查询订单 (USER_DATA)
    from binance.um_futures.account import cancel_order          #撤销订单 (TRADE) 
    from binance.um_futures.account import cancel_open_orders          #撤销全部订单 (TRADE) 
    from binance.um_futures.account import cancel_batch_order          #批量撤销订单 (TRADE) 
    from binance.um_futures.account import countdown_cancel_order          #倒计时撤销所有订单 (TRADE) 
    from binance.um_futures.account import get_open_orders          #查询当前挂单 (USER_DATA)
    from binance.um_futures.account import get_orders          #查看当前全部挂单 (USER_DATA)
    from binance.um_futures.account import get_all_orders          #查询所有订单(包括历史订单) (USER_DATA) 
    from binance.um_futures.account import balance          #账户余额V2 (USER_DATA) 
    from binance.um_futures.account import account          #账户信息V2 (USER_DATA) 
    from binance.um_futures.account import change_leverage          #调整开仓杠杆 (TRADE) 
    from binance.um_futures.account import change_margin_type          #变换逐全仓模式 (TRADE)
    from binance.um_futures.account import modify_isolated_position_margin          #调整逐仓保证金 (TRADE) 
    from binance.um_futures.account import get_position_margin_history          #逐仓保证金变动历史 (TRADE)
    from binance.um_futures.account import get_position_risk          #用户持仓风险V2 (USER_DATA)
    from binance.um_futures.account import get_account_trades          #账户成交历史 (USER_DATA)
    from binance.um_futures.account import get_income_history          #获取账户损益资金流水 (USER_DATA) 
    from binance.um_futures.account import leverage_brackets          #杠杆分层标准 (USER_DATA) 
    from binance.um_futures.account import adl_quantile          #持仓ADL队列估算 (USER_DATA
    from binance.um_futures.account import force_orders          #用户强平单历史 (USER_DATA) 
    from binance.um_futures.account import api_trading_status          #合约交易量化规则指标 (USER_DATA) 
    from binance.um_futures.account import commission_rate          #用户手续费率 (USER_DATA) 
    from binance.um_futures.account import download_transactions_asyn          #获取合约资金流水下载Id (USER_DATA) 
    from binance.um_futures.account import aysnc_download_info          #通过下载Id获取合约资金流水下载链接 (USER_DATA) 

    # STREAMS
    from binance.um_futures.data_stream import new_listen_key          #  生成listen key
    from binance.um_futures.data_stream import renew_listen_key          # 延长listen key
    from binance.um_futures.data_stream import close_listen_key          # 关闭listen key
