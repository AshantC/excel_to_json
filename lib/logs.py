import logging
from logging.handlers import RotatingFileHandler


def log_handler():
    handler = RotatingFileHandler(
        'logs.log',
        maxBytes = 5 * 1024 * 1024, 
        backupCount = 5
    )

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[handler],
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

