
import sys 
import os

# 将当前连接放到python搜索路径
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from db.db import B_DB



def get_symbols():
    cur = B_DB.symbols.find(
        {}, 
        {
            "_id": 0,
            "symbols": {
                "symbol": 1,
                "status": 1,
                "filters": 1,
                "orderTypes": 1, 
                "timeInForce": 1, 
                "liquidationFee": 1, 
                "marketTakeBound": 1,
            }
        }
        
    )
    sym = dict()
    for ret in cur:
        for x in ret["symbols"]:
            if x["symbol"].endswith("USDT"):
                sym[x["symbol"]] = x
        break
    cur.close()
    return sym

SYMBOLS = get_symbols()
if __name__ == "__main__":
    
    pass
    print(SYMBOLS)
