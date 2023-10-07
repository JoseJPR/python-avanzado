import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

logging.debug('Example log debug')
logging.info('Example log info')
logging.warning('Example log warning')
logging.error('Example log error')
logging.critical('Example log critical')