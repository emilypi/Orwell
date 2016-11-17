import logging
from logging.config import fileConfig


class Logger:

    def __init__(self):
        try:
            fileConfig('orwell/resources/logging_config.ini')
            self.logger = logging.getLogger('orwell')
            self.logger.info('Instantiating Logger...')

        except FileError as e:
            raise e("Improper logging configuration!")

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def debug(self, msg):
        self.logger.debug(msg)

