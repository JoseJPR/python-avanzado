import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler_console = logging.StreamHandler()
format_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler_console.setFormatter(format_logs)

logger.addHandler(handler_console)

logger.info('Hi from my first handler')