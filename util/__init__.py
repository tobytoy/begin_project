from . import logger
from . import tool
import configparser

cf = configparser.ConfigParser()
cf.read("./util/config/config.ini")

logger.log_init(root_path = cf.get("root", "main_root_logger"))

