import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from vortexasdk.config import LOG_FILE, LOG_LEVEL

FORMATTER = logging.Formatter(
    "%(asctime)s %(name)s — %(levelname)s — %(message)s"
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight")
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)

    logger.setLevel(LOG_LEVEL)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger
