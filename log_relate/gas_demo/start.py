from logging import getLogger, Logger
from logging import Logger, getLogger, StreamHandler, FileHandler, Formatter
from logging import DEBUG, INFO, WARN, ERROR, CRITICAL
from typing import Dict, List

from logging.handlers import RotatingFileHandler
from os.path import join

log_path = ''

observer_logger_format: str = r'[Sub] %(asctime)s [defence: %(name)s] [device: %(processName)s] - %(levelname)s : "%(message)s"'
"""str: 布防报警器通用日志格式"""
logger: Logger = getLogger('observer')
"""Logger: 报警器日志"""

logger_format = r'[%(levelname)s] %(asctime)s - %(name)s - %(message)s'
time_format = '%m-%d %H:%M:%S'


def add_stream_handle(loggers: List[Logger], level=DEBUG):
    if loggers:
        format_content = getattr(loggers[0], 'format_content', logger_format)

        stream = StreamHandler()
        stream.setFormatter(Formatter(format_content, time_format))
        stream.setLevel(level)

        for logger in loggers:
            logger.addHandler(stream)


def add_file_handler(loggers: List[Logger], level=DEBUG, file_name: str = 'default.log', mode='a'):
    if loggers:
        format_content = getattr(loggers[0], 'format_content', logger_format)

        handle = RotatingFileHandler(filename=file_name, maxBytes=100 * 1024 * 1024, backupCount=1, mode=mode,
                                     encoding='utf8')
        handle.setFormatter(Formatter(format_content, time_format))
        handle.setLevel(level)

        for logger in loggers:
            logger.addHandler(handle)


def rebuild_observer_logger(logger: Logger, defence_code: int, logger_level: int = 20):
    # remove exist handles:
    for handle in logger.handlers:
        logger.removeHandler(handle)
    # add new handle.
    add_stream_handle([logger], level=logger_level)
    add_file_handler([logger], file_name=join(log_path, 'observer.log'), level=logger_level)

    add_file_handler([logger], file_name=join(log_path, 'observer', str(defence_code) + '.log'),
                     level=10)


def build_logger(logger_name: str, format_content=logger_format, level=DEBUG):
    logger = getLogger(logger_name)
    logger.setLevel(level)

    logger.format_content = format_content
    return logger


class Ob(object):
    def __init__(self):
        self.defence_code = 126
        self.logger_level = 20
        self.logger = build_logger(str(self.defence_code), observer_logger_format, level=10)
        rebuild_observer_logger(self.logger, self.defence_code, self.logger_level)


if __name__ == '__main__':
    print(123)
