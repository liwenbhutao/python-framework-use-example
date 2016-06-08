import logging.config

from unipath import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(module)s:%(lineno)d [%(levelname)s]:%(message)s')
logger = logging.getLogger()


def main():
    logger.info("start")
    p = Path("/usr/lib/python2.5/gopherlib.py")
    logger.info("%s", p.parent)
    logger.info("%s", p.name)
    logger.info("%s", p.exists())


if __name__ == '__main__':
    main()
