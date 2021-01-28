import logging
import os
import sys

root = logging.getLogger()
level = logging.getLevelName(os.environ.get("LOG_LEVEL", "INFO"))
root.setLevel(level)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    "%m-%d %H:%M:%S",
)
handler.setFormatter(formatter)
root.addHandler(handler)
Logger = logging.getLogger(__name__)
