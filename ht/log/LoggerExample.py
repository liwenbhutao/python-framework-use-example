import logging.config

ch = logging.StreamHandler()
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

formatterStr = '%(asctime)s %(module)s:%(lineno)d [%(levelname)s]:%(message)s'
formatter = logging.Formatter(formatterStr)
fh.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG,
                    format=formatterStr)
logging.getLogger().addHandler(fh)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
