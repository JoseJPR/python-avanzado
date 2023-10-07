import logging

# If use __name__ show the py file with errors
# logger = logging.getLogger('my_custom_logger')
logger = logging.getLogger(__name__)

print(logger)

logger.warning('Example warning log')