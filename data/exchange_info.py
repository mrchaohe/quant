from .login import UM as um


def get_exchange_info():
    """获取交易规则对"""
    # todo 待解析,制作usdt合约
    return um.exchange_info()


def get_peek_data(sym, interval="1d", limit=5):
    """
    获取指定sym峰值，平均值
    :param sym:
    :return:
    """
    res = um.klines(symbol=sym, interval=interval, limit=limit)

