import logging
import time

from data.future_api import WBClient
from data.symbol import SYMBOLS

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    symbols = [key for key in SYMBOLS]
    while True:
       
        wb = WBClient(symbols[:50])

        wb.start()
        # sub_info = wb.all_mark_price()
        sub_info = wb.all_book_ticker()
        sub_info.extend(wb.all_ticker())
        sub_info.extend(wb.all_mark_price())
        # sub_info.extend(wb.sub_depth())
        wb.sublive_subscribe(sub_info)

        while True:
            if wb.dead:
                break 
            logger.debug("wb.dead is %s"%wb.dead)
            time.sleep(5)
        wb.dead = False
        logger.info("---------stop----------")
        wb.close()
        logger.info("---------end----------")
