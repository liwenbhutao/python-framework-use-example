import configparser
import io
import logging.config


def main():
    formatterStr = '%(asctime)s %(module)s:%(lineno)d [%(levelname)s]:%(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=formatterStr)
    logger = logging.getLogger()

    config = configparser.RawConfigParser()

    config.add_section('Section1')
    config.set('Section1', 'an_int', '15')
    config.set('Section1', 'a_bool', 'true')
    config.set('Section1', 'a_float', '3.1415')
    config.set('Section1', 'baz', 'fun')
    config.set('Section1', 'bar', 'Python')
    config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

    with io.open('example.cfg', 'w') as configfile:
        config.write(configfile)

    config1 = configparser.RawConfigParser()
    config1.read('example.cfg')

    logger.info("config1{")
    a_float = config1.getfloat('Section1', 'a_float')
    an_int = config1.getint('Section1', 'an_int')
    logger.info(a_float + an_int)

    if config1.getboolean('Section1', 'a_bool'):
        logger.info(config1.get('Section1', 'foo'))

    logger.info("}")

    logger.info("config2{")
    config2 = configparser.ConfigParser()
    config2.read('example.cfg')

    logger.info(config2.get('Section1', 'foo', 0))
    logger.info(config2.get('Section1', 'foo', 1))

    logger.info(config2.get('Section1', 'foo', 0, {'bar': 'Documentation',
                                                   'baz': 'evil'}))
    logger.info("}")
    logger.info("config3{")
    config3 = configparser.SafeConfigParser({'bar': 'Life', 'baz': 'hard'})
    config3.read('example.cfg')

    logger.info(config3.get('Section1', 'foo'))
    config3.remove_option('Section1', 'bar')
    config3.remove_option('Section1', 'baz')
    logger.info(config3.get('Section1', 'foo'))
    logger.info("}")

    logger.info("config4{")
    sample_config = """
    [mysqld]
    user = mysql
    pid-file = /var/run/mysqld/mysqld.pid
    skip-external-locking
    old_passwords = 1
    skip-bdb
    skip-innodb
    """
    config4 = configparser.RawConfigParser(allow_no_value=True)
    config4.readfp(io.BytesIO(sample_config))

    # Settings with values are treated as before:
    config4.get("mysqld", "user")

    # Settings without values provide None:
    config4.get("mysqld", "skip-bdb")

    # Settings which aren't specified still raise an error:
    config4.get("mysqld", "does-not-exist")
    logger.info("}")


if __name__ == '__main__':
    main()
