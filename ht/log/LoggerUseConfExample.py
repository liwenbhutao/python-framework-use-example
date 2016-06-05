import logging.config

logging.config.fileConfig('log.conf')

# create logger
logger = logging.getLogger()

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
