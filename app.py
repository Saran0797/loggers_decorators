import logging
from main import Employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("log.app")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)


def add(x, y):
    logger.warning(x + y)


def sub(x, y):
    logger.warning(x - y)


def multi(x, y):
    logger.warning(x * y)


def div(x, y):
    try:
        logger.error(x / y)
    except Exception as e:
        logger.error(e)


div(5, 5)
