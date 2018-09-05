# -*- encoding: utf-8 -*-
"""
    LOGGER Class
    ~~~~~~~~~~~~
    returns a logger instance based on __init__
"""

import logging


class Logger(object):
    def __init__(self,
                 name=__name__,
                 level=logging.DEBUG,
                 file_handler=__name__):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter(
            fmt='%(levelname)s:[%(asctime)s]=>%(name)s:%(message)s',
            datefmt="%Y-%m-%d-%H:%M:%S"
        )

        file_handler = logging.FileHandler(file_handler)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)


if __name__ == '__main__':
    log = Logger()
    log.debug('debugging demo')
    log.info('info demo')
    log.warning('warning demo')
    log.error('error demo')
    log.critical('critical demo')
    log.exception('exception demo')

