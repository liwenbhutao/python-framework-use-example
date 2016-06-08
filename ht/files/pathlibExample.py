import logging.config
from pathlib import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(module)s:%(lineno)d [%(levelname)s]:%(message)s')
logger = logging.getLogger()


def main():
    logger.info("start")
    p = Path('.')
    files = [x for x in p.iterdir() if x.is_file()]
    for f in files:
        logger.info(f.name)

    for f in list(p.glob('**/*.py')):
        logger.info(f.name)

    logger.info((p / "pathlibExample.py").exists())
    logger.info(PurePath(p, "pathlibExample.py").suffix)
    logger.info(PurePath(p, "pathlibExample.tar.gz").suffixes)
    logger.info(PurePath(p, "pathlibExample.py").match('*.py'))
    logger.info((p.cwd() / "pathlibExample.py").root)


if __name__ == '__main__':
    main()
