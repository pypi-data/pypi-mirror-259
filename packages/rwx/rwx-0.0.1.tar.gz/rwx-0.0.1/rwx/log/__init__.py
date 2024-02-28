import logging
import sys


def get_logger(name: str) -> logging.Logger:
    formatter = logging.Formatter(
        "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s"
    )

    # file_handler = logging.FileHandler('log.txt')
    # file_handler.setFormatter(formatter)
    # file_handler.setLevel(logging.INFO)

    out_handler = logging.StreamHandler(stream=sys.stdout)
    out_handler.setFormatter(formatter)
    out_handler.setLevel(logging.INFO)

    logger = logging.getLogger(name)
    # logger.addHandler(file_handler)
    logger.addHandler(out_handler)
    logger.setLevel(logging.INFO)
    return logger
