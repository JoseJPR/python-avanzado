import logging

logging.basicConfig(level=logging.DEBUG, filename='example.log')

logging.debug('Example log debug')
logging.info('Example log info')
logging.warning('Example log warning')
logging.error('Example log error')
logging.critical('Example log critical')