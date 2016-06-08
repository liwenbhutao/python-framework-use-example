import logging.config

from path import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(module)s:%(lineno)d [%(levelname)s]:%(message)s')
logger = logging.getLogger()


def main():
    logger.info("start")
    d = Path('/home/guido/bin')
    for f in d.files('*.py'):
        f.chmod(0o755)


if __name__ == '__main__':
    main()
