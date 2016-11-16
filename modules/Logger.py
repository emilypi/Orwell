from logging.config import fileConfig
import logging


class Logger:

    def __init__(self):
        fileConfig('resources/logging_config.ini')
        self.logger = logging.getLogger('orwell')
        self.logger.info('Instantiating Logger...')

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def debug(self, msg):
        self.logger.debug(msg)