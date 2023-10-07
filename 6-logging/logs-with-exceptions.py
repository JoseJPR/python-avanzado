import logging

logging.basicConfig(level=logging.DEBUG)

try:
    div = 2 / 0
except Exception as e:
    logging.exception(e)