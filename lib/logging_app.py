import logging
from logging.handlers import RotatingFileHandler


def log_handler():
    handler = RotatingFileHandler(
        'logging_app.log',
        maxBytes = 10_000_000, 
        backupCount = 5
    )

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[handler],
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

