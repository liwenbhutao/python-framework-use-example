import logging
from time import sleep

from concurrent import futures


def loiter(n):
    logging.getLogger().info('%sloiter(%s): doing nothing for {}s...', n, n)
    sleep(n)
    logging.getLogger().info('%sloiter(%s): done.', n, n)
    return n * 10


def main():
    formatterStr = '%(asctime)s %(module)s:%(lineno)d [%(levelname)s]:%(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=formatterStr)
    logging.getLogger().info('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    logging.getLogger().info('results:%s', results)
    logging.getLogger().info('Waiting for individual results:')
    for i, result in enumerate(results):
        logging.getLogger().info('result %s: %s', i, result)


if __name__ == '__main__':
    main()
