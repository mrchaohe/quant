import logging
import time

from data.future_api import WBClient

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    while True:
       
        wb = WBClient()

        wb.start()
        
        sub_info = wb.sub_kline()
        sub_info.extend(wb.sub_mark_price())
        sub_info.extend(wb.sub_depth())
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
