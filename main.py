from binance.spot import Spot

from binance.um_futures import UMFutures

if __name__ == "__main__":

    # client = Spot(key='J9ACx1qqQgwbpZkwSYeB9vT0s1k7NC2939vzXNbpIm5Cfq6vB4Cr0aQpXyqNOltF',
    #                        secret='JFvz23HL4ZMCWFjUAIgbpNHwEKdmblNPr1mnNyWNoQeUvoI4xBCwrqw9zieSSExA')
    # print(client.account())
    # client.system_status()
    # client.depth("ANCUSDT")
    # client.new_order_test()
    fu1 = UMFutures()

    print(fu1.time())
    print(fu1.exchange_info())

    # fu2= CMFutures(key='J9ACx1qqQgwbpZkwSYeB9vT0s1k7NC2939vzXNbpIm5Cfq6vB4Cr0aQpXyqNOltF',
    #                        secret='JFvz23HL4ZMCWFjUAIgbpNHwEKdmblNPr1mnNyWNoQeUvoI4xBCwrqw9zieSSExA')
    fu1.klines()