import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_folder = "new"
log_file = "running_log.log"
os.makedirs(log_folder,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers = [logging.FileHandler(log_file)]

)

logger = logging.getLogger("newlog")

def add_number(a,b):
    out = a+b
    logger.info("Successfully executed the function")
    return out

num=add_number(8,9)
print(num)
logger.info("Code executed")