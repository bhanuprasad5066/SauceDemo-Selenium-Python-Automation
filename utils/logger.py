import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        file_handler = RotatingFileHandler(
            os.path.join(LOG_DIR, "automation.log"),
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger